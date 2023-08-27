import pyttsx3
import requests
import json
speech = pyttsx3.init()
city = input("Enter the city: ")
url = f"https://api.weatherapi.com/v1/current.json?key=ad2a1e53b00a4e76865104550232708&q={city}"
r = requests.get(url)
wdict = json.loads(r.text)
t = wdict["current"]["temp_c"]
c = wdict["location"]["country"]
st = wdict["location"]["region"]
ws = wdict["current"]["wind_kph"]
con = wdict["current"]["condition"]["text"]
s1 = f"The current temperature in {city} which is in {c} is {t} degrees celsius."
s2 = f"{city} is in the region {st}."
s3 = f"The wind speed in {city} is {ws} kilometre per hour."
s4 = f"There will be {con} in {city} now."
print(s1)
print(s2)
print(s3)
print(s4)
speech.say(s1)
speech.say(s2)
speech.say(s3)
speech.say(s4)
speech.runAndWait()