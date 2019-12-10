"""
2) Create the following Routes in your Flask Application (Use the data you persisted in Module 9)

Default Route ("/") - Go to a simple html template page that tells about your data.
GET ("/item") - Will return UP TO 1000 items from your data.
GET ("/item/<id>") - Will return a single item from your data, by ID. If you data does not have a unique identifier then please let me know and I will help you get one added.
DELETE("/item/<id>") - Will delete a single item (again, you will need a unique column name)
POST ("/item") - As opposed to GET, POST will create a new item in your database. The body of the request will contain the item to be added.

I am having hard time with the CSS

Questions for Mckelly:
1)Css not working
2)Interactive HTML
3)

"""

from pymongo import MongoClient
from flask import Flask, g, render_template, abort, request
from bson.json_util import dumps
from bson.objectid import ObjectId
import ssl
import json
import dns
import os
import pprint

# Configure the connection
client = MongoClient("mongodb+srv://jaceiverson:vufspUcCvsFX2yCT@test-ol2kq.mongodb.net/test?retryWrites=true",ssl=True, ssl_cert_reqs=ssl.CERT_NONE)
db=client['Test']
champ=db['League Champions']
championFile={}

#puts all the champions into a dictionary locally
for x in champ.find():
    championFile[str([x['id']][0])]=x

#this works
print(dumps(champ.find({'id':'Aatrox'})))
