from flask import Flask, render_template, request, redirect, url_for
from weather import Weather

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('homepage.html')


@app.route('/search', methods=['POST', 'GET'])
def search_for_a_city():
    location = request.form # from search bar
    return redirect(url_for('result_page', location=location['location']))


@app.route('/weather/<location>')
def result_page(location):
    w = Weather(location)
    forecast = w.get_forecast_data()
    return render_template('result.html', data=forecast)


if __name__ == '__main__':
    app.run(debug=True)
