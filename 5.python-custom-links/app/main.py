from pymongo import MongoClient
from pprint import pprint

MONGO_URL = "mongodb://mongo:27017"
client = MongoClient(MONGO_URL)
db = client.records
col = db.links
col.insert_one(
    {"mywebsite": 
        "joshasgard.github.io"
        })
links = col.find({}) #finds all document in the links collection
for link in links:
    pprint(link)