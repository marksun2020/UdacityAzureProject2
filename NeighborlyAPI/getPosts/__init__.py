import logging
import azure.functions as func
import pymongo
import json
from bson.json_util import dumps


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python getPosts trigger function processed a request.')

    try:
        url = "mongodb://project2instance:aKdpdVle1URXB0q1aZJ4hDCzp6RBjpLuStUcrWDsIwUFeMG7KWOkxy9h9UmzYXdAY4lgP6mbynBLkVrhnBRZng==@project2instance.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@project2instance@"
        client = pymongo.MongoClient(url)
        database = client['project2db']
        collection = database['posts']

        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8', status_code=200)
    except:
        return func.HttpResponse("Bad request.", status_code=400)