import requests

api_key = '03e0b73b12344958443bb248c4f83796' 

city = input("Enter city name: ")
unit_choice = input("Choose units - C for Celsius, F for Fahrenheit: ").upper()

if unit_choice == 'F':
    units = 'imperial'
    units_label = 'Fahrenheit'
else:
    units = 'metric'
    units_label = 'Celsius'

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units={units}"
response = requests.get(url)
data = response.json()

if 'main' in data:
    print(f"\nWeather in {data['name']}:")
    print(f"Temperature: {data['main']['temp']}° {units_label}")
    print(f"Description: {data['weather'][0]['description'].capitalize()}")
    print(f"Humidity: {data['main']['humidity']}%")
    print(f"Wind Speed: {data['wind']['speed']} m/s")
else:
    print("\nFailed to fetch weather data. Please check the city name or API key.")
