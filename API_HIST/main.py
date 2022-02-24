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
            NumTag ="Tag_" + str(i)
            ListaDeTags[NumTag] = row[0]
            i=i+1
        ListaDeTags["Tags"]=i
        data=ListaDeTags
        return jsonify(data)

@app.route("/ver-tags/<id_tag>", methods=["GET"])
def imagen(id_tag):
    if request.method == "GET":
        provider = ["prv", "Microsoft.ACE.OLEDB.12.0", "Microsoft.Jet.OLEDB.4.0"]
        constr = "Provider=ihOLEDB.iHistorian.1;User Id=;Password="
        con = adodbapi.connect(constr)
        cursor = con.cursor()
        cursor.execute("SELECT TagName, TimeStamp, Value, Quality FROM ihRawData WHERE TagName = "+ id_tag +" AND samplingmode=RawbyTime AND RowCount=1 AND timestamp>=Now-10s ORDER BY timestamp DESC",)
        results=cursor.fetchall()
        resultado=results[0]
        data={
            "NombreTag": resultado[0],
            "Tiempo": resultado[1].strftime("%d-%m-%Y %H:%M:%S"),
            "Valor": resultado[2],
            "Calidad": resultado[3],
        }
        return jsonify(data)

@app.route("/ver-historico", methods=["GET"])
def ver_historico():
    if request.method == "GET":
        nombre = request.args.get("nombre")
        npuntos = request.args.get("npuntos")
        intervalo= request.args.get("intervalo")
        fechainicio = request.args.get("fechainicio")
        fechafin = request.args.get("fechafin")
        provider = ["prv", "Microsoft.ACE.OLEDB.12.0", "Microsoft.Jet.OLEDB.4.0"]
        constr = "Provider=ihOLEDB.iHistorian.1;User Id=;Password="
        con = adodbapi.connect(constr)
        cursor = con.cursor()
        cursor.execute("SELECT TagName, TimeStamp, Value, Quality FROM ihRawData WHERE TagName = "+ nombre +" AND RowCount="+ npuntos +" AND samplingmode=trend AND intervalmilliseconds="+ intervalo +" AND timestamp>="+ fechainicio +" AND timestamp<="+ fechafin,)
        results=cursor.fetchall()
        data=[]
        i=0
        for row in results:
            resultado=row
            data.append({
                "Numero": i,
                "NombreTag": resultado[0],
                "Tiempo": resultado[1].strftime("%d-%m-%Y %H:%M:%S"),
                "Valor": resultado[2],
                "Calidad": resultado[3],
            })
            i=i+1
        return jsonify(data)

if __name__=="__main__":
  app.run("0.0.0.0", port=5050)