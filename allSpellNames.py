import pandas as pd
import pprint
import json
import re
#static file, I don't get this from the web
champion=pd.read_json('championFull.json')

spells={}
#Zyra is the last champion. This makes sure that nothing is added after she is here
tracker='Zyra'
breakit=0
#there are some issues that make it so the names come across strange. I made this to prevent that
possibleIssues=['Wrapper','Human','New','VC','cast']
spellList=['Q','W','E','R']
issues=False
pattern=re.compile(r'\W')
for x in champion['data']:
    if breakit==1:
        break

    spells.update({x['id']: {}})
    qwer=0
    issues=False
    for y in x['spells']:

        name = spellList[qwer]
        desc=y['name']
        for test in possibleIssues:
            if test in y['id']:
                issues=True
        if issues:
            desc=y['name']
        else:
            if x['id'] in y['id']:
                desc=y['id'].replace(x['id'],'')
            if desc == name or desc.lower()in re.sub(pattern,"",y['name']).lower():
                desc=y['name']
            else:
                desc=desc + '/'+y['name']
        qwer+=1

        spells[x['id']].update({name:desc})
    if x['id']==tracker:
        breakit=1

pprint.pprint(spells)

with open('allSpellData.json', "w") as outfile:
    json.dump(spells, outfile, indent=4)

