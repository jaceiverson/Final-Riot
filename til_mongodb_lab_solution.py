from pymongo import MongoClient
from pprint import pprint
import json

"""# 1) Make sure to create an account on mlab.com

# 2) Connect to the server
client = MongoClient('mongodb://mis:mis5400@ds027758.mlab.com:27758/mis')

# 3) Connect to mis db
mis_db = client.mis

# 4) Create a new collection
til_collection = mis_db.create_collection('til_collection')"""

# 5) Read the json in (from file) and insert
with open(r'todayilearned.json') as data_file:
    data = json.load(data_file)

# This will read a list (look at the json)
data_list = data['data']['children']

# Insert each entry
for til_entry in data_list:
    til_collection.insert(til_entry['data'])

# 6) Get count
print('Added ',til_collection.count(),'TIL entries')

# 7) Select top 10 rows
for item in til_collection.find({'domain':'en.wikipedia.org'}).limit(10):
    pprint(item)

