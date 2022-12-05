import dbConfig
import pymongo
import json
from pymongo import MongoClient, InsertOne
from pymongo.server_api import ServerApi


def upload_json(game_number):
    user = dbConfig.user
    password = dbConfig.password
    link = dbConfig.link
    client = pymongo.MongoClient("mongodb+srv://"+user+":"+password+link, server_api=ServerApi('1'))
    db = client.esake
    collection = db.boxscores
    requesting = []

    with open(r"boxscore"+game_number+".json") as f:
        dic = json.load(f)
        requesting.append(InsertOne(dic))

    result = collection.bulk_write(requesting)
    client.close()
