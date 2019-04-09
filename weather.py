import requests


class Weather():

    def __int__(self):
        self.location = None

    def set_location(self, location):
        self.location = location

    def download_weather_data(self):
        #TODO validate location
        apikey = 'ffdc73fba9bede8bb4da20f33d4843df'
        api_openweather = 'http://api.openweathermap.org/data/2.5/forecast?q=%s&cnt=3&appid=%s' % (self.location, apikey)

        response = requests.get(api_openweather)
        response.raise_for_status()

        return response.json()

    def get_forecast_data(self):
        w = self.download_weather_data()
        w = w['list']
        current = w[0]['weather'][0]['description']
        tomorrow = w[1]['weather'][0]['description']
        dayafter = w[2]['weather'][0]['description']

        return self.location, current, tomorrow, dayafter
