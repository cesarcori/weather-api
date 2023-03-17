import requests

# Change the API key for your own.
API_KEY = "508ea5b6ada26fb9a2cbb16579af96c9"
lat, lon = ["-16.707881", "-70.584655"]

url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = round(data['main']["temp"] - 273.15, 2) # kelvin to celsius
    print("Weather:", weather)
    print("Temperature:", temperature, "celsius")
else:
    print("An error has ocurred")


