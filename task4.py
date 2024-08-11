import requests

#give API key
WEATHER_API_KEY = 'API_KEY'

def get_weather_data(endpoint, params):
    base_url = "http://api.openweathermap.org/data/2.5/"
    params['appid'] = WEATHER_API_KEY
    response = requests.get(base_url + endpoint, params=params)
    
    # Print the full request URL for debugging
    print(f"Request URL: {response.url}")
    
    if response.status_code == 200:
        return response.json()
    else:
        # Print error details for debugging
        print(f"Error: {response.status_code}, {response.text}")
        return None

def get_current_weather(location):
    params = {'q': location, 'units': 'metric'}
    return get_weather_data('weather', params)

def get_historical_weather(location, date):
    params = {
        'q': location,
        'dt': date,  # Historical data is usually fetched by timestamp
        'units': 'metric'
    }
    return get_weather_data('onecall/timemachine', params)

def get_forecast(location, days):
    params = {'q': location, 'cnt': days, 'units': 'metric'}
    return get_weather_data('forecast/daily', params)

def run_conversation():
    while True:
        # Asking user for the task
        user_input = input("What would you like to do? (current weather, history weather, forecast): ").strip().lower()

        if 'current weather' in user_input:
            location = input("Please provide the location: ")
            weather = get_current_weather(location)
            if weather:
                print(f"The current temperature in {location} is {weather['main']['temp']}°C with {weather['weather'][0]['description']}.")
            else:
                print("Couldn't fetch weather data. Please try again.")

        elif 'history weather' in user_input:
            location = input("Please provide the location: ")
            date = input("Please provide the date (in UNIX timestamp format): ")
            weather = get_historical_weather(location, date)
            if weather:
                print(f"The temperature in {location} on {date} was {weather['current']['temp']}°C with {weather['current']['weather'][0]['description']}.")
            else:
                print("Couldn't fetch historical weather data. Please try again.")

        elif 'forecast' in user_input:
            location = input("Please provide the location: ")
            days = int(input("Please provide the number of days for the forecast: "))
            forecast = get_forecast(location, days)
            if forecast:
                for day in forecast['list']:
                    print(f"Date: {day['dt_txt']} - Temp: {day['main']['temp']}°C - Description: {day['weather'][0]['description']}")
            else:
                print("Couldn't fetch forecast data. Please try again.")

        else:
            print("Invalid option, please choose again.")
        
        continue_prompt = input("Would you like to do another task? (yes/no): ").strip().lower()
        if continue_prompt != 'yes':
            print("Goodbye!")
            break

if __name__ == "__main__":
    run_conversation()
