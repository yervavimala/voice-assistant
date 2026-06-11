import requests

city = input("Enter city name: ")

url = f"https://wttr.in/{city}?format=3"

try:
    response = requests.get(url)
    print("\nWeather Information:")
    print(response.text)
except Exception as e:
    print("Error:", e)