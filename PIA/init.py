import argparse
class args():
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument('-a', '--Accion', type=str,
                        help='Seleccion de la tarea',
                        choices=['op1','op2','op3']
                        )
        self.parser.add_argument('-n', '--nombre', type=str, help = 'Nombre de archivo (opcional)')
        self.args = self.parser.parse_args()
    def x():
        pass
