import requests
import csv

# Change the API key for your own.
API_KEY = "508ea5b6ada26fb9a2cbb16579af96c9"

# Read the file csv 
with open("./coordinates.csv") as file:
    csv_reader = csv.reader(file, delimiter=",")
    locations = [locate for locate in csv_reader]

# Show the options to choose
locations.pop(0)
print("\n*** Weather location ***\n")
for n in range(len(locations)):
    print(n+1, locations[n][2], sep=":")

# User choose one option
index = int(input("\nChoose one location: ")) - 1
lat, lon, loc = float(locations[index][0]), float(locations[index][1]), locations[index][2]

# Read API
url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = round(data['main']["temp"] - 273.15, 2) # kelvin to celsius
    print("\nLocation:", loc)
    print("Weather:", weather)
    print("Temperature:", temperature, "celsius")
else:
    print("\nAn error has ocurred")


