import socket
import nmap
from bs4 import *
import base 64
import os
import logging
import re
import sha512


class t1:
    def ip():
        # Aqui es donde se va a tomar la ip del usuario
        # para hacer un scn de los puertos
        input('Se tomara la ip local, presione enter para continuar\n')
        hostname = socket.gethostname()
        lip = socket.gethostbyname(hostname)
        print(lip)
        while True:
            print('Que desea hacer?')
            op = int(input('-1.- Scan IP local\n-2.- IP publica\n-Etc.-Salir\n'))
            if op == 1:
                ip_sc(lip)
                print('Proceso terminado con exito')
            elif op == 2:
                print('Por razones de seguridad, no se saca ip publica\n')
                pip = str(input('Inserte su IP publica:\n'))
                ip_sc(pip)
                print('\n\nProceso terminado con exito')
            else:
                print('Saliendo del programa')
                break 


    def pch():
        nm = nmap.PortScanner()
    nm.scan(ip, '22-443')
    datos = ''
    for host in nm.all_hosts():
        datos += ('----------------------------------------------------')
        datos += ('\nHost : %s (%s)' % (host, nm[host].hostname()))
        datos += ('\nEstado : %s' % nm[host].state())
        for protocolo in nm[host].all_protocols():
            datos += ('\n----------')
            datos +=('\nprotocolo : %s' % protocolo)
            lport = sorted(nm[host][protocolo].keys())
            for puerto in lport:
                datos += ('\nPuerto: %s\tEstado: %s' % (puerto, nm[host][protocolo][puerto]['state']))
            print(datos)       
    enc = base64.b64encode(datos)
    return enc


    def encripcion():
    
    pass

    def encri():


    def lectura():
    pass

class t2(url):
    def __init__(self, url):
        self.r = requests.get(url)
        if self.r.status_code != 200:
            logging.error("Pagina no encontrada")
            print("Pagina no encontrada!")
            exit()
        self.soup = BeautifulSoup(r.text, 'html.parser')
        
    def download_images(self, url):
        logging.info("Entra a la función downloads_images" )  
        images = self.soup.findAll('img') 
        try:
            os.mkdir('.\\Datos') 
        except:
            pass
        count = 0
        print(f"{len(images)} Imagenes encontradas!")
        logging.info(f"{len(images)} Imagenes encontradas!")
        logging.info("Iniciando descarga"
        if len(images) != 0: 
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
                    r = requests.get(image_link).content 
                    try:  
                        r = str(r, 'utf-8') 
                    except UnicodeDecodeError: 
                        with open(f"{folder_name}/images{i+1}.jpg", "wb+") as f: 
                            f.write(r) 
                        count += 1
                except: 
                    pass
            if count == len(images):
                logging.info("Todas las imagenes han sido descargadas")
                print("Imagenes Descargadas!") 
            else: 
                print(f"Total {count} Images Downloaded Out of {len(images)}")
                logging.info(f"Total {count} Images Downloaded Out of {len(images)}")


    def descargar_pdfs(self, url):
        logging.info("Entra en la función descargar_pdfs" )
        links = self.soup.find_all('a')   
        i = 0
        for link in links: 
            if ('.pdf' in link.get('href', [])): 
                i += 1
                response = requests.get(link.get('href'))       
                pdf = open("pdf"+str(i)+".pdf", 'wb') 
                pdf.write(response.content) 
                pdf.close() 
                print("File ", i, " Downloaded!") 
        print("Todos los PDF descargados!")
        logging.info("Todos los PDF descargados")


    def find_mails(self, url):
        logging.info("Entra en la función find_emails" )
        logging.info("Busca la pagina: " + url)
        regExMail = r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+"
        new_emails = set(re.findall(regExMail, self.r.text, re.I))
        name = input("Ingresa el nombre del archivo (sin el .txt): ")
        logging.info("El nombre del archivo será: " + name)
        fo = open(name + ".txt", "w")
        logging.info("Abre el archivo: " + name + ".txt")
        for i in new_emails:
            #c += 1
            fo.write(i)
            logging.info("Escribiendo el email... " + i + " en: " + name + ".txt")
            fo.write("\n")
            logging.info("Finalizado")

