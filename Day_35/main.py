import requests

MY_LAT = 51.509865
MY_LON = -0.118092
API_KEY = "0d2290211e38a885ffec8334df03777f"
url = "https://api.openweathermap.org/data/2.5/forecast"

params = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "appid": API_KEY,
}

response = requests.get(url, params=params)
response.raise_for_status()
weather_data = response.json()

print(weather_data)