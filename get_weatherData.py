import requests
from bs4 import BeautifulSoup
import pandas as pd
page = requests.get("https://weather.com/en-IN/weather/tenday/l/bf01d09009561812f3f95abece23d16e123d8c08fd0b8ec7ffc9215c0154913c")
content = page.content
soup = BeautifulSoup(content, "html.parser")
final = []
all = soup.find("div", {"class": "locations-title ten-day-page-title"}).find("h1").text
table = soup.find_all("table", {"class": "twc-table"})
for items in table:
    for i in range(len(items.find_all("tr")) - 1):
        collect = {}
        try:
            collect["day"] = items.find_all("span", {"class": "date-time"})[i].text
            collect["date"] = items.find_all("span", {"class": "day-detail"})[i].text
            collect["desc"] = items.find_all("td", {"class": "description"})[i].text
            collect["temp"] = items.find_all("td", {"class": "temp"})[i].text
            collect["precip"] = items.find_all("td", {"class": "precip"})[i].text
            collect["wind"] = items.find_all("td", {"class": "wind"})[i].text
            collect["humidity"] = items.find_all("td", {"class": "humidity"})[i].text
        except:
            collect["day"] = "None"
            collect["date"] = "None"
            collect["desc"] = "None"
            collect["temp"] = "None"
            collect["precip"] = "None"
            collect["wind"] = "None"
            collect["humidity"] = "None"
        final.append(collect)

df = pd.DataFrame(final)
print(df)
df.to_csv("WeatherData.csv")