import flask from Flask
from flask_test import routes
from flask_test import config

app = Flask(__name__)

# Config class
app.config.from_object(Config)


