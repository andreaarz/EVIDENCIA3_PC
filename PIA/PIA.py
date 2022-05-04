import os
import logging
import argparse
import srvinit
import tareas

def main():
    logging.basicConfig(filename='PIA.txt', level=logging.INFO)
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--Accion', type=str,
                            help='Seleccion de la tarea',
                            choices=['op1','op2','op3']
                            )
    parser.add_argument('-n', '--nombre', type=str, help = 'Nombre de archivo (opcional)')
    args = parser.parse_args(
    opcion = tareas.Tareas()
    try:
        if args.Accion == 'op1':
            sv = echoserver.client()
            opcion.ip()
        elif args.Accion == 'op2':
            opcion.wsscp()
        elif args.Accion == 'op1':
            opcion.mailsnd()
    except Exception as e:
        logging.error(e)
                        
if __name__  == '__main__':
    main()
