import os
from pymongo import MongoClient

MONGO_URL = "localhost"
MONGO_USUARIO = ""
MONGO_PASSWORD = ""
MONGO_PUERTO = 27017
cliente_mongo = MongoClient(
    host=MONGO_URL, username=MONGO_USUARIO, password=MONGO_PASSWORD, port=MONGO_PUERTO
)


def insertar_documento_test():
    db = cliente_mongo.prueba
    coleccion_test = db.tags
    res = coleccion_test.insert_one({"NombreTag": "DESKTOP-3PEVOMB.Ramp", "Numero": 1})
    id_insertada = res.inserted_id
    print({"id_insertado": id_insertada})
    

if __name__ == "__main__":
    insertar_documento_test()