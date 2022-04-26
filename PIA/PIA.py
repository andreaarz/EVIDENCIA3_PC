import os
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--Accion', type=str,
                        help='Seleccion de la tarea',
                        choices=['op1','op2','op3']
                        )
    parser.add_argument('-n', '--nombre', type=str, help = 'Nombre de archivo (opcional)')
    args = parser.parse_args()
    if args.Accion == 'op1':
        op1()
    elif args.Accion == 'op2':
        op2()
    elif args.Accion == 'op1':
        op3()


def op1:
    pass


    
def op2:
    pass
    

def op3:
    pass


                        
if __name__  == '__main__':
    main()
