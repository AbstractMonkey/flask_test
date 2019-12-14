from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/weather')
def weather():
    return "It's shitty outside"

if __name__ == '__main__':
    app.run(debug=True)
    

