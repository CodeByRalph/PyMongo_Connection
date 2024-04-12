from fastapi import FastAPI, HTTPException
import certifi
import pprint
from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv, find_dotenv
import os
from urllib.parse import quote_plus

app = FastAPI()

ca = certifi.where()
load_dotenv(find_dotenv())
password = quote_plus(os.environ.get("MONGODB_PWD"))
uri = f"mongodb+srv://rstout:{password}@srodetailing.6dlfnxr.mongodb.net/?retryWrites=true&w=majority&appName=SRODetailing"
# Create a new client and connect to the server
client = MongoClient(uri, tlsCAFile=ca)
printer = pprint.PrettyPrinter()