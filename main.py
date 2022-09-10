from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from keys import keys

import sys
sys.path.append('classes')
import Libro
from Libro import LIBRO

#Achieving connection with Mongo
client = MongoClient(f"mongodb+srv://scuolaManta:{keys.mongoPWD}@smartlibrarian.evahg90.mongodb.net/?retryWrites=true&w=majority")

#Check for connection
try:
    # The ping command is cheap and does not require auth.
    client.admin.command('ping')
except ConnectionFailure:
    print("<smartLibrarian> Connection failed")
    quit(-1)


#Getting collection libri
db = client.smartLibrarian
libri = db.libri

libroBello = LIBRO("ciao", "Alberto", "divertente", "Giuseppe");

libro_id = libri.insert_one(libroBello.toJson()).inserted_id

print(libro_id)