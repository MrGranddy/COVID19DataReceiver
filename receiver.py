from bs4 import BeautifulSoup
import requests
import re
import datetime

enumerate_months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]

class COVID19_Receiver:
    def __init__(self):
        # This is the website which we draw the data from
        self.main_url = "https://www.worldometers.info/coronavirus/"
        
        # Get main page in BeautifulSoup
        html_content = requests.get(self.main_url).text
        soup = BeautifulSoup(html_content, "lxml")

        # Get the table on the main page to extract avaiable countries
        todays_data_table = soup.find("table", {"id": "main_table_countries_today"})
        rows = todays_data_table.find_all("tr", {"class": None})

        # A dict holding avaiable countrties and their links
        country_list = {}

        for row in rows:
            country = row.find("a", {"class": "mt_a"}) # Country name and its link
            if country is None:
                continue
            country_name = country.text.lower()
            country_link = country["href"]
            
            country_list[country_name] = country_link

        # Hold country list for future requests
        self.country_list = country_list

    def get_country_data(self, country):
        if country.lower() in self.country_list:
            # Get country detalils page
            html_content = requests.get(self.main_url + self.country_list[country]).text
            soup = BeautifulSoup(html_content, "lxml")

            # The data is kept in scripts as arrays
            scripts = soup.find_all("script", {"type": "text/javascript"})

            # Get related scripts
            data_scripts = []
            for script in scripts:
                if "data: " in str(script):
                    data_scripts.append(str(script))

            # Extract data from the scripts
            data = []
            for script in data_scripts:
                try:
                    m = re.search(r"data: \[([0-9,]*)\]", script).group(1)
                    data.append( [ int(x) for x in m.strip().split(",") ] )
                except:
                    pass

            # We get the time labels from any of the data scripts
            time_labels = re.search(r'xAxis: {(\s)*categories: \[([0-9A-Za-z\s",]*)\]',
                         data_scripts[2]).group(2)
            time_labels = time_labels.strip().split(",")
            
            # Convert labels into datetime
            datetimes = []
            for label in time_labels:
                raw = label.replace('"', '')
                raw = raw.lower()
                month, day = raw.split()
                datetimes.append( datetime.date(2020, enumerate_months.index(month)+1, int(day)) )

            # Prepare data to return
            data_dict = {}
            data_dict["daily_total_cases"] = data[0]
            data_dict["daily_active_cases"] = data[1]
            data_dict["daily_total_deaths"] = data[2]
            data_dict["daily_new_deaths"] = data[3]
            data_dict["dates"] = datetimes


            return data_dict

        else:
            raise "The country you are looking for does not exist."

    def get_country_list(self):
        return sorted(list(self.country_list.keys()))
