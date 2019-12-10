import pandas as pd
import json
from pymongo import MongoClient
import ssl
import requests
import pprint
import dictdiffer


def makeBaseStats(patch):
    champBaseStats = {}

    for x in patch:
        stats = []
        for y in patch22[x]['stats']:
            stats.append(patch[x]['stats'][y])

        champBaseStats[x] = stats

    return champBaseStats


client = MongoClient("mongodb+srv://jaceiverson:vufspUcCvsFX2yCT@test-ol2kq.mongodb.net/test?retryWrites=true",ssl=True, ssl_cert_reqs=ssl.CERT_NONE)
db = client["Test"]

db.get_collection("League Champions")

#checks to see what base stats changed
url21="https://ddragon.leagueoflegends.com/cdn/9.21.1/data/en_US/champion.json"
url22="https://ddragon.leagueoflegends.com/cdn/9.22.1/data/en_US/champion.json"
newChampionData=requests.get(url21)
patch21=newChampionData.json()['data']
newChampionData=requests.get(url22)
patch22=newChampionData.json()['data']

p21Base=makeBaseStats(patch21)
p22Base=makeBaseStats(patch22)

different={}
for x in p22Base:
    values=[]
    if x in patch21:
        for y in range(len(p22Base[x])):
            if p22Base[x][y]!=p21Base[x][y]:
                values.append(y)
        if len(values)==0:
            different[x]={"Different at":None}
        else:
            different[x] = {"Different at": values}
    else:
        different[x] = {"Different at": "new champion"}
pprint.pprint(different)