class FileWriter:
    def __init__(self, fileName):
        self.filename = fileName
        try:
            self.i = open(self.filename, "r+")
        except Exception:
            self.i = open(self, fileName, "w+")
        print(self.i)

    def write(self, mensaje:str):
      self.i.write(mensaje)
   
    def read(self)->str:
        return self.i.readlines()
    
    def close(self):
        self.i.close()

if __name__ == "__main__":
    def main():
        pruebaW = FileWriter("FileWriter.txt")
        pruebaW.write("hola")
        pruebaW.close()

        pruebar = FileWriter("fileWriter.txt")
        print(pruebar.read())
        pruebar.close()

    main()