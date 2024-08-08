import requests

# Function to convert Kelvin to Celsius
def kelvin_to_celsius(kelvin):
    return kelvin - 273.15


# Set up the API URL with your API key
url = 'Put your API key'

try:
    # Send the GET request to the API
    weather_res = requests.get(url)
    weather_res.raise_for_status()  # Raise an error for bad status codes

    # Parse the JSON response
    weather_data = weather_res.json()

    # Extract and print specific information
    city = weather_data['city']['name']
    forecast_list = weather_data['list']
    print(f"Weather forecast for {city}:")
    for forecast in forecast_list[:5]:  # Print first 5 forecasts
        dt_txt = forecast['dt_txt']
        temp_k = forecast['main']['temp']
        temp_c = kelvin_to_celsius(temp_k)
        description = forecast['weather'][0]['description']
        print(f"{dt_txt}: {temp_c:.2f}°C, {description}")

except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except Exception as err:
    print(f"Other error occurred: {err}")
