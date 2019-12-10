import pandas as pd
import pprint as pprint
champions=pd.read_json('championData')

#pprint.pprint(champions)

print(champions['data'])