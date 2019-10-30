#!/usr/bin/env python
from config import db
from bson.json_util import dumps
import json

class User(db.Document):
    ''' The data model'''
    handle = db.StringField(required=True)
    def as_dict(self):
        return {'id': json.loads(dumps(getattr(self,'pk')))['$oid'], 'handle': getattr(self, 'handle')}