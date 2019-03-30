from flask import Flask, render_template
from quickWeather import city, w
app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('homepage.html', city=city, today=w[0]['weather'][0]['main'], today_dscr= w[0]['weather'][0]['description'])