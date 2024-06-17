
import requests
import firebase_admin
from firebase_admin import credentials, firestore
cred = credentials.Certificate("credentials.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
api_key ='2989ec907410272f4fe71e27aa5442f0'
departments = ['Mumbai' , 'Delhi' , 'Chennai', 'Vellore']
for department in departments:
    print(department)
    user_input = department
    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])
    print(f"The weather in {user_input} is: {weather}")
    print(f"The temperature in {user_input} is: {temp}ºF")
    doc_ref = db.collection('department').document(user_input)
    doc_ref.set({
        'city': user_input,
        'weather': weather,
        'temperature': temp
    })
