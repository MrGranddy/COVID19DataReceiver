from receiver import COVID19_Receiver
import numpy as np

rec = COVID19_Receiver()
usa_data = rec.get_country_data("usa")

daily_total_cases_in_usa = usa_data["daily_total_cases"]
print(daily_total_cases_in_usa)
"""
[15, 15, 15, 15, 15, 15, 35, 35, 35, 53, 57, 60, 60, 63, 68, 75, 100, 124,
158, 221, 319, 435, 541, 704, 994, 1301, 1630, 2183, 2770, 3613, 4596, 6346,
9296, 13865, 19497, 24345, 33745, 44056, 55222, 68673, 86061, 104804,
124256, 144321, 165053, 189967, 216622, 246729, 279183, 313379, 338779,
370019, 403521, 435518, 469124, 502876, 532879, 560300, 586941, 617661,
648003, 677570, 709735]
"""
# Each value in the list has its date in the dates list with the same index
dates = usa_data["dates"] # This contains date objects
print(dates[0])
"""
2020-02-15
"""
daily_total_deaths_in_usa = usa_data["daily_total_deaths"]
print(daily_total_deaths_in_usa)
"""
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 6, 9, 11, 12, 15, 19,
22, 26, 30, 38, 41, 48, 57, 69, 87, 110, 150, 206, 255, 301, 414, 556,
781, 1028, 1296, 1697, 2222, 2592, 3150, 4064, 5114, 6088, 7139, 8469,
9636, 10895, 12868, 14811, 16712, 18747, 20577, 22105, 23640, 29825,
32443, 34619, 37154]
"""