from bs4 import BeautifulSoup
import requests

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
            country_name = country.text
            country_link = country["href"]
            
            country_list[country_name] = country_link

        # Hold country list for future requests
        self.country_list = country_list

rec = COVID19_Receiver()
print(rec.country_list)