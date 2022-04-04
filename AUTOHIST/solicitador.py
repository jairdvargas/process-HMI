#Archivo para poder ir solicitando datos historicos del servidor primario hacia el servidor historian, para actualizar.
#Desde aqui solo realiza la orden, pero no la accion.

import functools
from threading import Thread
import time
import requests


def mifuncion(argumento1, argumento2):
    res=requests.get(argumento1, headers=argumento2)

    print("solicitando datos");

if __name__== '__main__':
    #Esta ip es del contenedor ......
    url='http://api:5051/historico-adb'
    headers={'user-agent': 'my-app/0.0.1'}
    counter = 0
    #Este 1920 es simplemente las veces que va a ejecutar este bucle +1 
    #se podria modificar para que pasado estas veces vuelva a iniciar
    #Ahora solo funciona por un turno de 8 horas
    while counter < 1920:
        req = hilo=Thread(target=functools.partial(mifuncion, url, headers))
        req.start()
        counter+=1
        #el numero dentro de sleep es el tiempo que espera
        time.sleep(30)







hilo.start()
