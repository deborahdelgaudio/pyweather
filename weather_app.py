from flask import Flask, render_template, request, redirect, url_for
from weather import Weather

app = Flask(__name__)
w = Weather()

@app.route('/')
def homepage():
    return render_template('homepage.html')


@app.route('/search', methods=['POST', 'GET'])
def search_for_a_city():
    if request.method == "POST":
        location = request.form
        w.set_location(location['location'])
        return redirect(url_for('.result_page', location=location['location']))
    else:
        return redirect(url_for('.homepage'))


@app.route('/weather/<location>')
def result_page(location):
    return render_template('result.html', data=w.get_forecast_data())


if __name__ == '__main__':
    app.run(debug=True)