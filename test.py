from pymongo import MongoClient

client = MongoClient()
store = client['housing']
collection = store['threemonths']

for doc in collection.find():
    print doc