#!/usr/bin/env python
import os
import yaml
from flask import Flask
from flask_mongoengine import MongoEngine

app = Flask(__name__)

config_obj = yaml.load(open('config.yaml'), Loader=yaml.Loader)

db_host = os.getenv('MONGODB_URL')

app.config['MONGODB_SETTINGS'] = {
    'host': config_obj['MONGODB_URL'] if db_host is None else db_host,
    }


db = MongoEngine()

db.init_app(app)

