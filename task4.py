import requests

# Replace with your OpenWeatherMap API key
WEATHER_API_KEY = 'adbc5212e8b30c4074d77dc6fa989975'

def get_weather_data(location):
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={WEATHER_API_KEY}&units=metric"
    
    # Make the API request
    response = requests.get(base_url)
    
    # Print the full request URL for debugging
    print(f"Request URL: {response.url}")
    
    if response.status_code == 200:
        return response.json()
    else:
        # Print error details for debugging
        print(f"Error: {response.status_code}, {response.text}")
        return None

def display_weather_info(weather_data, location):
    if weather_data:
        temp = weather_data['main']['temp']
        description = weather_data['weather'][0]['description']
        print(f"The current temperature in {location} is {temp}°C with {description}.")
    else:
        print("Couldn't fetch weather data. Please try again.")

def run_conversation():
    while True:
        location = input("Please provide the location: ").strip()

        # Fetch and display the weather data
        weather_data = get_weather_data(location)
        display_weather_info(weather_data, location)
        
        continue_prompt = input("Would you like to check another location? (yes/no): ").strip().lower()
        if continue_prompt != 'yes':
            print("Goodbye!")
            break

if __name__ == "__main__":
    run_conversation()
