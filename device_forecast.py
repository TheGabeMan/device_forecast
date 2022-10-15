import json
import sys
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
if jsonresponse['result'] == None:
    print( "No results")
    print( "Respone Code : ",  jsonresponse['message']['code'] )
    print( "Respone type : ",  jsonresponse['message']['type'] )
    print( "Respone text : ",  jsonresponse['message']['text'] )
    print( "Retry at : ",  jsonresponse['message']['ratelimit']['retry-at'] )
    sys.exit()
## watts - Watts (power) average for the period
## watt_hours - Watt hours (energy) summarized over the day
## watt_hours_period - Watt hours (energy) for the period
## watt_hours_day - Watt hours (energy) summarized for each day
## To see at what time you can start an heavy power user, we look at watt_hours_period

## What is the Watt Hour of your device. (Hourly)
devices_watt_hour = [ ["dish washer",832] , ["washing machine",1400], ["dryer",2000] ]

## What date is it?
today = date.today()

## Get the estimates per hour in Watts, watt_hours and watt_hours_day
day_estimates = jsonresponse['result']
print("*** Forecast in Watts per hour ***")
watt_hours_period = day_estimates['watt_hours_period']
for timestamp,value in watt_hours_period.items():
    if date.today() == datetime.date( datetime.strptime( timestamp, "%Y-%m-%d %H:%M:%S")):
        ## Cycle through all devices to check their power
        for devwatt in devices_watt_hour:
            if devwatt[1] <= value:
                print( timestamp, " Start your ", devwatt[0], " as the solar power is expected to be ", value, "Wh.")



