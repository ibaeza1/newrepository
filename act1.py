class Comuna(Casa,Edificio):
    def __init__(self,nombre,lista_edificios ,lista_casas):
        self.nombre = nombre
        self.lista_edificios = lista_edificios
        self.lista_casas = lista_casas
    def agregar_casa(self,casa):
        self.lista_casas.append(casa)
        return self.lista_casas
    def agregar_edificio(self,edificio):
        self.lista_edificios.append(edificio)
        return self.lista_edificios
    def mostrar_lista(self):
        for i in lista_edificios:
            print(i)
        for j in lista_casas:
            print(j)

class Casa:
    def __init__(self,direc,num):
        self.direc = direc
        self.ed = False
        self.num = num
    def electro_dependiente(self,el):
        if el > 5000:
            print('Es electrodependiente')
        else:
            print('No es electrodependiente')
    
class Edificio:
    def __init__(self,direccion,nombre,medidor,lista_deptos):
        self.direccion = direccion
        self.nombre = nombre
        self.medidor = medidor
        self.lista_deptos = lista_deptos
    def ed(self):
        if int(self.medidor) > 10000:
            print(True)
        else:
            print(False)
            
class Medidor:
    def __init__(self):
        self._kwh = None
    @property
    def kwh(self):
        return self._kwh
    @kwh.setter
    def kwh(self,kwh):
        self._kwh = kwh
        
class Departamento(Medidor):
    def __init__(self,nombre,kwh):
        self.nombre = nombre
        self.kwh = kwh
 
    def es_electrodp(self):   
        if self.kwh > 4000:
            print('{} es electrodependiente'.format(self.nombre))
        else:
            print('{} no es electrodependiente'.format(self.nombre))

med = Medidor()
a = int(input('medidor:'))
med.kwh = a
depto = Departamento('A',med.kwh)
depto.es_electrodp()




    
