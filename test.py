from receiver import COVID19_Receiver

import matplotlib.pyplot as plt
from matplotlib.dates import (DAILY, DateFormatter,
                              rrulewrapper, RRuleLocator, drange)
import numpy as np
import datetime


# tick every 5th easter
rule = rrulewrapper(DAILY, interval=5)
loc = RRuleLocator(rule)
formatter = DateFormatter('%d/%m/%y')

rec = COVID19_Receiver()
data = rec.get_country_data("turkey")

fig, axs = plt.subplots(2,2)

key_title_pairs = [
    ("daily_total_cases", "Daily Total COVID-19 Cases in Turkey"),
    ("daily_active_cases", "Daily Active COVID-19 Cases in Turkey"),
    ("daily_total_deaths", "Daily Total Deaths from COVID-19 in Turkey"),
    ("daily_new_deaths", "Daily New Deaths from COVID-19 in Turkey"),
]

fig.tight_layout(pad=3.0)

for i, (key, title) in enumerate(key_title_pairs):
    x = i // 2
    y = i % 2
    axs[x,y].plot_date(data["dates"], data[key], 'ro', MarkerSize=2)
    axs[x,y].set_title(title)
    axs[x,y].xaxis.set_major_locator(loc)
    axs[x,y].xaxis.set_major_formatter(formatter)
    axs[x,y].xaxis.set_tick_params(rotation=30, labelsize=10)

plt.show()
