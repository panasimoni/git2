class Writer:
    def __init__(self, fileName):
        self.fileName = fileName
        self.i = open(self,fileName, "w+", "r")

    def write(self, mensaje:str):
        i.write(mensaje)
     
    def read(self):
        i.readlines()

    def close(self):

def main():
    prueba = FileWriter("")