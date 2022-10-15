import json
import requests
from datetime import date, time, datetime

## Read from API
## https://doc.forecast.solar/doku.php?id=api

## Base URL for API calls:
## https://api.forecast.solar/ 

## Example URL = https://api.forecast.solar/estimate/:lat/:lon/:dec/:az/:kwp
api_url = "https://api.forecast.solar/estimate/50.82172/5.72486/25/40/4.4"
response = requests.get( 
                    url= api_url
)
jsonresponse = response.json()

## watts - Watts (power) average for the period
## watt_hours - Watt hours (energy) summarized over the day
## watt_hours_period - Watt hours (energy) for the period
## watt_hours_day - Watt hours (energy) summarized for each day
## To see at what time you can start an heavy power user, we look at watt_hours_period

## What is the Watt Hour of your device. (Hourly)
device_watt_hour = 830             ## Afwasmachine = 832 Wh (gemiddeld)

## What date is it?
today = date.today()

## Get the estimates per hour in Watts, watt_hours and watt_hours_day
day_estimates = jsonresponse['result']
print("*** Forecast in Watts per hour ***")
watt_hours_period = day_estimates['watt_hours_period']
for timestamp,value in watt_hours_period.items():
    if date.today() == datetime.date( datetime.strptime( timestamp, "%Y-%m-%d %H:%M:%S")):
        if device_watt_hour <= value:
            print( timestamp, " Power on device: ", value)




