import requests
from bs4 import BeautifulSoup
import pandas as pd
import geocoder
import pymongo
import os
from tqdm import tqdm



###################################################### Fetch address from gov #######################################################
# Fetch data from gov
url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQjf_HNeEZKM-XJX-q5v4cfNrB3kcv4gOT8kFbV9rurfoX_H5Qv9112Pv0PgYNFSzbReyNlQkLrJib3/pubhtml'
resp = requests.get(url).text
soup = BeautifulSoup(resp, 'html.parser')

# parse data from html table to DF
DF = pd.read_html(str(soup.table), encoding='utf-8')[0]
DF.columns = pd.MultiIndex.from_arrays(DF.iloc[0:2].values)
DF = DF.iloc[3:, 1:]
DF = DF.set_index((None, '編號'))


###################################################### Transfer address to LatLng #######################################################
# address to latlng
print(DF)
address_list = DF.iloc[:, -2].to_list()
latlng_list = []
print('address to latlng starts...')
for address in tqdm(address_list):
    geo = geocoder.arcgis(address).json
    latlng_list.append( geo )
DF[('LatLon', 'LatLon')] = latlng_list

# drop na and retrieve only latlng from geo
print(f'len b/f cleaning: {len(DF)}')
to_drop = []
for _, row in DF.iterrows():
    if not row.to_list()[-1]:
        to_drop.append(row.name)
    else:
        DF.loc[row.name, ('LatLon', 'LatLon')] = [row[('LatLon', 'LatLon')]['lat'], row[('LatLon', 'LatLon')]['lng']]
DF.drop(to_drop, axis=0, inplace=True)
print(f'len a/f cleaning: {len(DF)}')

# sum the ppl
DF[('剩餘人次', '剩餘人次')] = DF.iloc[:, 2:13].sum(axis=1)
DF[('剩餘人次', '剩餘人次')] = DF[('剩餘人次', '剩餘人次')].apply(lambda cell: f'{cell:.0f}')


###################################################### Store DF to MongoDB #######################################################
# POST to mongodb
DF.columns = DF.columns.map(str)
client = pymongo.MongoClient( os.environ['MONGODB_URI'] )
db = client['NRICM101-map']
col = db['source']
col.delete_many({})
col.insert_many(DF.to_dict('records'))