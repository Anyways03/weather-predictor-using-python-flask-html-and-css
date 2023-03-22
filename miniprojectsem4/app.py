from flask import Flask, render_template, request
import requests
import json
import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['city']
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=3b188f641cce6a09e30ac80021816755'
       
        r = requests.get(url.format(city)).json()
    
        if r['cod'] != '404':
            weather = {
                'city': city,
                'temperature': r['main']['temp'],
                'description': r['weather'][0]['description'],
                'icon': r['weather'][0]['icon']}
            if(weather['temperature'] > 25):
                prediction="It will be a hot day today!!Drink plenty of water!!"
            elif(weather['temperature'] < 10):
                prediction="Its a cold today!!Wear warm clothes!!"
            else:
                prediction="Its a normal day!!Enjoy!!"
       


            return render_template('weather.html', weather=weather,prediction=prediction,temperature=weather['temperature'])
        else:
            error = 'City not found. Please try again!'
            return render_template('index.html', error=error)
    return render_template('index.html')
import ntplib
from time import ctime





if __name__ == '__main__':
    app.run(debug=True)