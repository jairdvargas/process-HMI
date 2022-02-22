#Este es el programa principal
#Elaborado por Jair Vargas

from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os
import sys
import adodbapi


app = Flask(__name__)
# aqui se habilita cors
CORS(app)

@app.route("/ver-tags",  methods=["GET"])
def ver_tags():
    if request.method == "GET":
      
        provider = ["prv", "Microsoft.ACE.OLEDB.12.0", "Microsoft.Jet.OLEDB.4.0"]
        constr = "Provider=ihOLEDB.iHistorian.1;User Id=;Password="
        con = adodbapi.connect(constr)
        cursor = con.cursor()
        cursor.execute("SELECT TagName FROM ihTags",)
        results=cursor.fetchall()
        ListaDeTags = {"Tags": 0}
        i=0
        for row in results:
            #print(row[0])
            NumTag ="Tag_" + str(i)
            ListaDeTags[NumTag] = row[0]
            i=i+1
        ListaDeTags["Tags"]=i
        data=ListaDeTags
        return data

if __name__=="__main__":
  app.run("0.0.0.0", port=5050)