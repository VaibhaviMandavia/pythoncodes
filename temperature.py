# import requests module
import requests

city = input("Enter city name : ")
req = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=ee5f36eb9dcd8f0933a4535132a5a46a&units=metric')
data = req.json()
print("temperature of "+city+" is ",data["main"]["temp"])



# ee5f36eb9dcd8f0933a4535132a5a46a