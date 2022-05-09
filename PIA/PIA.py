import os
import logging
import argparse
import tareas

def main():
    try:
        os.mkdir('.\\Datos') 
    except:
        pass
    FORMAT = '%(asctime)s %(message)s'
    logging.basicConfig(format=FORMAT, filename='PIA.txt', level=logging.INFO)
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--Accion', type=str,
                            help='Seleccion de la tarea',
                            choices=['op1','op2','op3','op4']
                            )
    parser.add_argument('-n', '--nombre', type=str, default='datos', help = 'Nombre de archivo/dominio (opcional)')
    args = parser.parse_args()
    # Se invocan las clases de las tareas
    
    try:
        if args.Accion == 'op1':
            logging.info("Se opera la Opcion 1")
            t1 = tareas.t1()
            x = [args.nombre]
            t1.ip(x[0])
        elif args.Accion == 'op2':
            logging.info("Se opera la Opcion 2")
            x = [args.nombre]
            t2 = tareas.t2(x[0])
            t2.download_images()
        elif args.Accion == 'op3':
            logging.info("Se opera la Opcion 3")
            x = [args.nombre]
            t3 = tareas.t3()
            t3.mail_search(x[0])
        elif args.Accion == 'op4':
            logging.info("Se opera la Opcion ")
            t4 = tareas.t4()
            t4.server()
        else:
            exit()
    except Exception as e:
        logging.error(e)
                        
if __name__  == '__main__':
    main()
