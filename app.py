from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/weather')
def weather():
    w = 78
    w -= 10
    if w > 65 and w < 90:
        return "It's nice outside"
    if w > 45 and w < 66:
        return "It's ok outside"
    else:
        return "It's miserable outside"


if __name__ == '__main__':
    app.run(debug=True)
    

