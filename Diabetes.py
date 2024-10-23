from pymongo import MongoClient
import pandas as pd

def data():
    uri = "mongodb://localhost:27017/"
    client = MongoClient(uri)
    database = client["ML_Project"]
    collection = database["Diabetes"]
    res = collection.find()
    data = []
    for i in res:
        data.append(i)
    return data

def load_data():
    df = pd.DataFrame(data())
    df.drop('_id',axis=1,inplace=True)
    df.dropna(inplace=True)
    return df


