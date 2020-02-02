import requests
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get('https://forecast.weather.gov/MapClick.php?lat=39.96199000000007&lon=-83.00274999999993#.XjXtamhKiHt')
soup = BeautifulSoup(page.content, 'html.parser')

week = soup.find(id = 'seven-day-forecast-container')
# print(week)

items = week.find_all(class_='tombstone-container')
# print(items[0])

# print(items[0].find(class_ = 'period-name').text)
# print(items[0].find(class_ = 'short-desc').text)
# print(items[0].find(class_ = 'temp').text)

period_names = [item.find(class_ = 'period-name').text for item in items]
short_description =[item.find(class_ = 'short-desc').text for item in items]
temperature = [item.find(class_ = 'temp').text for item in items]

# print(period_names)
# print(short_description)
# print(temperature)

weather_stuff = pd.DataFrame(
    {
    'period': period_names,
    'short-descriptions': short_description,
    'temperature': temperature,
    }
)

print(weather_stuff)

# weather_stuff.to_csv('weather_scrape.csv')
