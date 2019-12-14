# Secret key

import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):

    SECRET_KEY = '907359183518935783'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
