import socket
import subprocess
from subprocess import call
import nmap
from bs4 import *
import os
import logging
import requests
import re
import srvinit
from pyhunter import PyHunter
import hashlib

def save(nom, datos):
    with open("Datos\\%s.txt"%(nom),'a',encoding='utf-8', errors='ignore') as d:
        d.write(datos)
        d.close()



def hashing():
    sha512 = hashlib.sha512()
    for dirpath,nomdir,archivo in os.walk("."):
        for nom in archivo:
            dire=os.path.join(os.getcwd(),nom)
            try:
                with open(dire, 'rb') as f:
                    while True:
                        data = f.read(BUF_SIZE)
                        if not data:
                            break
                        sha512.update(data)
            except:
                pass
            x = str("SHA512: {0}".format(sha512.hexdigest()))
        
class t1():
    def ip(self, nombre):
        # Aqui es donde se va a tomar la ip del usuario
        # para hacer un scn de los puertos
        logging.info('Se realizo la toma de ip')
        hostname = socket.gethostname()
        lip = socket.gethostbyname(hostname)
        self.pch(nombre, lip)


    def pch(self, nombre, ip):
        logging.info('Se hara el escaneo de puertos')
        nm = nmap.PortScanner()
        # Se indica la ip y los puertos a escanear
        nm.scan(ip, '22-443')
        datos = ''
        for host in nm.all_hosts():
            datos += ('----------------------------------------------------')
            datos += ('\nHost : %s (%s)' % (host, nm[host].hostname()))
            datos += ('\nEstado : %s' % nm[host].state())
            for protocolo in nm[host].all_protocols():
                # Se leeb y almacenan los datos en una variable para enviar
                datos += ('\n----------')
                datos +=('\nprotocolo : %s' % protocolo)
                lport = sorted(nm[host][protocolo].keys())
                for puerto in lport:
                    datos += ('\nPuerto: %s\tEstado: %s' % (puerto, nm[host][protocolo][puerto]['state']))
        logging.info('Escaneo realizado')
        # Se envian los datos a encriptar
        self.enc(nombre, datos)

            
    def enc(self, nombre ,datos):
        logging.info('Se realizo encriptacion de los datos')
        sha512 = hashlib.sha512()
        sha512.update(datos.encode('utf-8'))
        enc = str("SHA512: {0}".format(sha512.hexdigest()))
        save(nombre, enc)
            

class t2():
    def __init__(self, url):
        self.url = url
        self.r = requests.get(self.url)
        if self.r.status_code != 200:
            logging.error("Pagina no encontrada")
            print("Pagina no encontrada!")
            exit()
        self.soup = BeautifulSoup(self.r.text, 'html.parser')
        
    def download_images(self):
        logging.info('Buscando datos de la pagina')
        logging.info("Entra a la función downloads_images" )  
        images = self.soup.findAll('img') 
        count = 0
        print(f"{len(images)} Imagenes encontradas!")
        logging.info(f"{len(images)} Imagenes encontradas!")
        logging.info("Iniciando descarga")
        if (len(images)!=0):
            for i, image in enumerate(images): 
                try: 
                    image_link = image["data-srcset"] 
                except: 
                    try: 
                        image_link = image["data-src"] 
                    except: 
                        try: 
                            image_link = image["data-fallback-src"] 
                        except: 
                            try: 
                                image_link = image["src"] 
                            except: 
                                pass
                try: 
                    self.r = requests.get(image_link).content 
                    try:  
                        self.r = str(self.r, 'utf-8') 
                    except UnicodeDecodeError: 
                        with open(f"Datos/images{i+1}.jpg", "wb+") as f: 
                            f.write(self.r) 
                        count += 1
                except: 
                    pass
            if count == len(images):
                logging.info("Todas las imagenes han sido descargadas")
                print("Imagenes Descargadas!") 
            else: 
                print(f"Total {count} Images Downloaded Out of {len(images)}")
                logging.info(f"Total {count} Images Downloaded Out of {len(images)}")
        self.find_mails()



    def find_mails(self):
        logging.info("Entra en la función find_emails" )
        regExMail = r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+"
        new_emails = self.soup(text = (re.compile(regExMail)))
        logging.info("Datos de correo guardados en archivo: ./Datos/datos.txt" )
        fo = open('datos//datos.txt', "w")
        logging.info("Abre el archivo: datos.txt"  )
        for i in new_emails:
            c += 1
            fo.write(i)
            logging.info("Escribiendo el email... " + i + " en: Datos.txt ")
            fo.write("\n")
            logging.info("Finalizado")


class t3():
    def mail_search(self,dom):
        datos=''
        logging.info('Buscando correos del dominio')
        apikey = 'ec7d46dd6e46c8266cc306665649698ed6ca7635'
        hunter = PyHunter(apikey)
        resultado = hunter.domain_search(company=str(dom), limit=1, emails_type='personal')
        for key, val in resultado.items():
            datos += (str(key)+ ': '+ str(val)+ '\n')
        save('datos', datos)
        ar = os.path.join(os.getcwd(),'pwsh.ps1')
        ar = r'{}'.format(ar)
        subprocess.run(['powershell.exe',ar])
            


class t4():
    def server(self):
        logging.info('inicializacion del servidor socket')
        srvinit.iniciar()
        logging.info('Finalizando el servidor')
