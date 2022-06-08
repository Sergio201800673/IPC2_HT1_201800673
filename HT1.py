class Main:
    def __init__(self) -> None:
        a = True
        Lista = Listas()
        while a:
            Opcion = input("1. Insertar en lista\n2. Seleccionar numero\n3. Salir\n")
            if Opcion == "1":
                info = input("Ingrese valor en la lista: ")
                Lista.insertar(Dato(info))
            elif Opcion == "2":
                Lista.imprimir()
                busqueda = input("Ingrese numero a buscar: ")
                print(Lista.buscar(busqueda))
            elif Opcion == "3":
                a = False
            else:
                print("opcion incorrecta, ingrese nuevamente")

class Listas:
    def __init__(self) -> None:
        self.primero = None
        self.ultimo = None
        self.size = 0

    def insertar(self,dato):
        self.size += 1
        if self.primero == None:
            self.primero = dato
            self.ultimo = dato 
        else: 
            self.ultimo.setSiguiente(dato)
            dato.setAnterior(self.ultimo)
            self.ultimo = dato
    
    def imprimir(self):
        aux = self.primero
        while aux != None:
            print("---" + aux.lexema + "---")
            aux = aux.siguiente

    def buscar(self,buscar):
        aux = self.primero
        while aux != None:
            if aux.lexema == buscar:
                return("anterior " + aux.anterior.lexema + " actual " + aux.lexema + " siguiente " + aux.siguiente.lexema)
            aux = aux.siguiente
        return("No se encontró")

class Dato:
    def __init__(self,lexema) -> None:
        self.lexema = lexema
        self.siguiente = None
        self.anterior = None
    
    def getSiguiente(self):
        return self.siguiente

    def setSiguiente(self,siguiente):
        self.siguiente = siguiente

    def getAnterior(self):
        return self.anterior

    def setAnterior(self,anterior):
        self.anterior = anterior

Main()