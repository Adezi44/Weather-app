import requests

api_key = 'dd80d597963dfc340dcbf0faf0ed67e9'

user_input=input("Enter City:")

weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&appid={api_key}&units=metric")

if weather_data.json()['cod'] == '404':
    print('No City found')
else:
    weather= weather_data.json()['weather'][0]['main']
    temperature= weather_data.json()['main']['temp']

    print(f'The weather of {user_input} is {weather}')
    print(f'The temperature of {user_input} is {temperature}')