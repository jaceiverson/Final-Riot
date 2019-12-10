"""
1) MongoDB
2) Hosted on AWS
3) I have heard about MongoDB and it seemed like it would be good for posting API files (json)


"""
import json
import pprint as pprint
import ssl
import pandas as pd
from pymongo import MongoClient
import operator

#function used for sorting stats by their value
def sortByValue(dict):
    ids=sorted(dict.items(),key=operator.itemgetter(1))
    for x in ids:
        print(x[1],x[0])

client = MongoClient("mongodb+srv://jaceiverson:vufspUcCvsFX2yCT@test-ol2kq.mongodb.net/test?retryWrites=true",ssl=True, ssl_cert_reqs=ssl.CERT_NONE)
db = client["Test"]
collection=db["League Champions"]
print(collection)
championList={}
championList=collection.distinct("id")
champDict={}
champwithID={}
allChampList=[]
#gets list of all Champion Stats names
champStats=list(collection.find_one()['stats'].keys())

#makes a dictionary with all stats
for x in range(len(championList)):
    champDict[championList[x]]=collection.distinct("stats")[x]
    allChampList.append({championList[x]:collection.distinct('stats')[x]})
#prints the Dictionary nicely to the screen
#pprint.pprint(champDict)
#sortByValue(champDict)

#writes it to a file
with open('champBaseStats.json','w') as f:
    json.dump(champDict,f,indent=4)

#writes it to the db
collectionName='Champion Base Stats'

if collectionName in db.list_collection_names():
    baseStatTable=db.get_collection(collectionName )
else:
    baseStatTable=db.create_collection(collectionName)

baseStatTable.insert_many(allChampList)


print(baseStatTable.inserted_ids)


"""
#gets Champion ID (Work in progress)


for x in range(len(championList)):
    champwithID[championList[x]]=int(collection.distinct("key")[x])


sortByValue(champwithID)
    
"""

