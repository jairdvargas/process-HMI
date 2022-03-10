import os
from pymongo import MongoClient

MONGO_URL = "mongo"
MONGO_USUARIO = "root"
MONGO_PASSWORD = "example"
MONGO_PUERTO = 27017
cliente_mongo = MongoClient(
    host=MONGO_URL, username=MONGO_USUARIO, password=MONGO_PASSWORD, port=MONGO_PUERTO
)


def insertar_documento_test():
    db = cliente_mongo.historian
    coleccion_test = db.tags
    res = coleccion_test.insert_one({"EGU":"°C","_id":"DESKTOP-3PEVOMB.Test","descripcion":"Test de variable","tag":"DESKTOP-3PEVOMB.Test","valor":69.3,"zona":"zonatest"})
    id_insertada = res.inserted_id
    print({"tag_insertado": id_insertada})
    

#if __name__ == "__main__":
#    insertar_documento_test()