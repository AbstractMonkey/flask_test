from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/weather')
def weather():
    w = 78
    w -= 10
    if w > 65 and w < 90:
        data = {"message": "It's nice outside"}
    elif w > 45 and w < 66:
        data = {"message": "It's ok outside"}
    else:
        data = {"message": "It's miserable outside"}
    return render_template("weather.html", title="WeatherApp", data=data)

if __name__ == '__main__':
    app.run(debug=True)
    

