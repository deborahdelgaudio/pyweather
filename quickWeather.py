#! python3
# Prints the weather for a location from command line
import requests, json, sys
'''
# - compute location from command line arguments
if len(sys.argv) < 2:
    print("Usage: quickWeather.py location")
    sys.exit()
'''
#location = ''.join(sys.argv[1:])# add to the string location the args int the list except for the first one
location = 'Milano'
apikey_open_weather = 'ffdc73fba9bede8bb4da20f33d4843df'

# - Download the Json Data of the current weather
url_opeweather = 'http://api.openweathermap.org/data/2.5/forecast?q=%s&cnt=3&appid=%s' %(location, apikey_open_weather)
response = requests.get(url_opeweather)
response.raise_for_status()

# - Load Json into data Python variable.
#weatherData = json.loads(response.text) #.loads() is for string obj!
weatherData = response.json()

# - Print weather description
w = weatherData['list']
city = location
today_weather = w[0]['weather'][0]['main'] + ' ' + w[0]['weather'][0]['description']
tomorrow_weather = w[1]['weather'][0]['main'] + ' ' + w[1]['weather'][0]['description']
day_after_weather = w[2]['weather'][0]['main'] + ' ' + w[2]['weather'][0]['description']

'''
print('Current weather in %s:' % (location) )
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
'''