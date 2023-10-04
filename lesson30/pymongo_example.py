from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import bson

uri = "mongodb+srv://Primat:d2z76ctb@cluster0.v1o4bs7.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

weather_db = client.get_database('sample_weatherdata')
data_collection = weather_db.get_collection('data')
#collection_of_batches = data_collection.find_raw_batches()
#for data in collection_of_batches:
#    print(bson.decode_all(data))
#first_result = data_collection.find_one(filter={'position': {'type': 'Point', 'coordinates': [-47.9, 47.6]}})
#print(first_result)
another_value = data_collection.insert_one({'ladies':True,'beautiful':True})
check_if_value_inserted = data_collection.find_one(another_value.inserted_id)
print(check_if_value_inserted)