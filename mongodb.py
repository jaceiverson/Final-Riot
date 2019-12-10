##########################
# MongoDB, using pymongo #
##########################
'''
Free MongoDB Instance at mlab.com
using pymongo from
Installing with pip (pip install pymongo)
Using Robo 3T or Mongo Compass as a GUI to MongoDB Instance can be helpful

http://api.mongodb.org/python/current/tutorial.html

'''

import datetime
import pymongo

# More about "bson" here: http://bsonspec.org/


user='jace%2Eiverson%40aggiemail%2Eusu%2Eedu'
pswd='FwYf1Cs5IV1%23'

client = pymongo.MongoClient(f"mongodb+srv://{user}:{pswd}@test-ol2kq.mongodb.net/test?retryWrites=true&w=majority")
db = client.test


mis_db = client.mis

# Let's create a collection

book_collection = mis_db.book_collection


# Add a new book
books = [{"author": "Bob",
        "text": "Ni, Ni, Ni, Ni... None shall pass, Fall 2017!!!!",
        "tags": ["mongodb", "python", "pymong/o"],
        "date": datetime.datetime.utcnow(),
        "SomeNewField" : "Excellent",
        "Randomly Added Field From a Project Manager": "Some Value"
        },

        {"author": "Jojo",
        "text": "Ni, Ni, Ni, Ni... None shall pass, Summer 2018!!!!",
        "tags": ["mongodb", "python", "pymong/o"],
        "date": datetime.datetime.utcnow(),
        "SomeNewField" : "Excellent",
        "CoverType" :"Hard-Cover"
        }]

book_collection.insert_many(books)

# See existing books
for book in book_collection.find():
    print(book)


# Add another book
book = {"author": "King Arthur",
        "text": "What you ginna do? ",
        "tags": ["mongodb", "python", "pymongo", "rabbit"],
        "date": datetime.datetime.utcnow()}

book_collection.insert(book)

book = book_collection.find_one({'tags': 'rabbit'})

books_cursor = book_collection.find({'tags': 'rabbit'})

# How many results?
books_cursor.count()

# Retrieve based on query
for book in books_cursor:
    print(book)

# Retrieve by ID
from bson.objectid import ObjectId
single_book = book_collection.find_one({'_id':ObjectId('5b1878434720273a0cda4a3f')})

# Update (https://docs.mongodb.com/getting-started/python/update/)
result = book_collection.update_one({'text': 'What you ginna do? '},
                                {
                                    '$set': {
                                        'text' : 'What are you going to do?'
                                    }
                                })


# Note that with MongoDB just calling .update (not update_one or update_many) will replace the full document, the
# only thing that will stay is the _id.
result = book_collection.update_one({'_id': ObjectId('59f0c35d4720271dccb29b73')}
                                ,{  "author": "King Arthur",
                                    "text": "What you ginna do? ",
                                    "date": datetime.datetime.utcnow()
                               })
# So in the update above, all tags have been removed.
result = book_collection.delete_one({'_id': ObjectId('5ab05eb96ff43d0c0821ea25')})

print('Deleted',result.deleted_count,'documents.')

client.close()


###############
# MongoDB Lab #
###############
# SETUP: Go to mlab.com and create a free account and mongo database
# 1) Use the file todayilearned.json from https://www.reddit.com/r/todayilearned.json
# 2) Look at the data and lets decide how to create a list of dictionary objects (posts = data['data']['children'])
# 3) Now add each item to the new collection
# 4) write a query that finds all TIL from domain wikipedia.org
# (https://stackoverflow.com/questions/10320633/mongo-how-to-query-a-nested-json)

# NOTES: Will need to use import json. import pprint helps.
