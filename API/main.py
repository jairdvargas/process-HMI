# antes de todo se tiene que crear la carpeta .venv y usar el comando
# pipenv install flask

import requests
import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from flask_cors import CORS
import json

# cargar el archivo de variable donde esta la llave del api
#http://localhost:5050/ver-historico?nombre=DESKTOP-3PEVOMB.Sin&npuntos=250&intervalo=1m&fechainicio=Now-2h&fechafin=Now

HISTORIAN_TAGS_URL="http://localhost:5050/ver-tags"
HISTORIAN_TAG_URL="http://localhost:5050/ver-tags/"
HISTORICOS_URL="http://localhost:5050/ver-historico"

app = Flask(__name__)
# aqui se habilita cors
CORS(app)

@app.route("/listar-tags", methods=["GET"])
def listar_tags():
    if request.method == "GET":
        # leer tags del historian
        respuesta = requests.get(url=HISTORIAN_TAGS_URL)
        # la funcion find retorna "cursor" y se tiene que convertir a json con jsonify
        data = respuesta.json()
        return data

@app.route("/listar-tags-sim", methods=["GET"])
def listar_tags_sim():
    if request.method == "GET":
        respuesta = {"Tag_0":"DESKTOP-3PEVOMB.Ramp","Tag_1":"DESKTOP-3PEVOMB.Sin","Tag_2":"DESKTOP-3PEVOMB.Step","Tags":3}
        return jsonify(respuesta)

@app.route("/tag/<id_tag>", methods=["GET"])
def tag(id_tag):
    if request.method == "GET":
        nueva_URL=HISTORIAN_TAG_URL + id_tag
        respuesta = requests.get(url=nueva_URL)
        data = respuesta.json()
        return data

@app.route("/tag-sim/<id_tag>", methods=["GET"])
def tag_sim(id_tag):
    if request.method == "GET":
        respuesta = {"Calidad":"Good NonSpecific","NombreTag":"DESKTOP-3PEVOMB.Ramp","Tiempo":"26-02-2022 09:26:43","Valor":566.6666666666666}
        return jsonify(respuesta)

#http://localhost:5051/historico?nombre=DESKTOP-3PEVOMB.Sin&npuntos=250&intervalo=10m&fechainicio=Now-2h&fechafin=Now
@app.route("/historico", methods=["GET"])
def historico():
    if request.method == "GET":
        nombre = request.args.get("nombre")
        npuntos = request.args.get("npuntos")
        intervalo= request.args.get("intervalo")
        fechainicio = request.args.get("fechainicio")
        fechafin = request.args.get("fechafin")
        params = {
            "nombre": nombre,
            "npuntos": int(npuntos),
            "intervalo": intervalo,
            "fechainicio": fechainicio,
            "fechafin": fechafin
            }
        respuesta = requests.get(url=HISTORICOS_URL, params=params)
        data = respuesta.json()
        return jsonify(data)

@app.route("/historico-sim", methods=["GET"])
def historico_sim():
    if request.method == "GET":
        archivo = open("simulacion.json")
        data = json.load(archivo)
        archivo.close()
        return jsonify(data)


if __name__ == "__main__":
    app.run("0.0.0.0", port=5051)