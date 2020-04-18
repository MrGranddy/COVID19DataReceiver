# COVID19DataReceiver
A simple framework to get daily spread and mortality data of COVID-19

Using the framework is simple, first you import your receiver, 
for now there is only the COVID19 receiver.

Then using the receiver you can do two things:
1. You can get the list of avaiable country names using the method
   "get_country_list"

2. You can get the data of a country using the method
   "get_country_data" this one gets the country name as an argument


The data you will receive is a dictionary with 5 keys:
1. "dates", this contains the date of each index in the upcoming 4 different
    data list as python date objects.
2. "daily_total_cases", contains total number of cases recorded up until the
    according date for the country.
3. "daily_active_cases", contains the number of active cases on
    the according date.
4. "daily_total_deaths", contains the total number of recorded deaths
    up until the according date.
5.  "daily_new_deaths", contains the recorded deaths for the according date

In addition "test.py" in the repo shows a plotting example, also you can
check "example.py" for clarity of usage.
