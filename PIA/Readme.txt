Instrucciones:
-El archivo Pia.py se abre mediante dos argumentos:
ej: python PIA.py -a op1 -n 'Datos'
-Las opciones de -a (Accion) son las siguientes:
1.- op1: Lectura de Local ip, escaneo de puertos y encriptacion de datos (sha512)
2.- op2: Web scrapping(La pagina web se inserta con -n 'www.pagina.com')
3.- op3: Lectura de correos mediante Hunter (el uso del domino es: -n 'Dominio') 
4.- op4: Creacion de socket (Requiere inicializacion del archivo cliee.py para su ejecucion completa)
-Una vez iniciado el uso del programa este hara el proceso indicado de manera independiente

-Use -h/--help para mas ayuda sobre los argumentos


Modulos necesarios para la ejecucion:
os
logging
argparse
socket
subprocess
nmap (externo, requiere instalacion)
bs4 (externo, requiere instalacion)
requests
re
pyhunter (externo, requiere instalacion)
hashlib
