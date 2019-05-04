from flask import Flask, render_template, request, redirect, url_for
from weather import Weather

app = Flask(__name__)
w = Weather()

@app.route('/')
def homepage():
    return render_template('homepage.html')


@app.route('/result', methods=['POST', 'GET'])
def result_page():
    if request.method == "POST":
        location = request.form
        w.set_location(location['location'])
        return render_template('result.html', data=w.get_forecast_data())
    else:
        return redirect(url_for('homepage'))


if __name__ == '__main__':
    app.run(debug=True)