# Forecast when to power on your device
As a big fan of Home Assistant (https://www.home-assistant.io/) I've made some alerts based on how much power my solar panels deliver. For example when my solar panels supply more than 1000W, my desk light flashes and I get an alert telling me I could use my dishwasher using only solar power. But it doesn't tell me in the morning at what time it might be best to turn on the dishwasher. Therefore I created this little python script.

It collects the forecast data from the forecast.solar API (https://forecast.solar/) and based on the Watt per hour value of your device, it shows at which times today your panels will deliver more power than your device uses.

PS: As I'm just starting writing in Python, and making in integration for Home Assistant is still way over my head, I kept it at this little script for now.
