            

#class Medidor:
 #   def __init__(self):

#      self._kwh = None
 #   @property
  #  def kwh(self):
   #     return self._kwh
 #   @kwh.setter
  #  def kwh(self,kwh):
   #     self._kwh = kwh
    #    print(self.kwh)

class Cliente:
    def __init__(self,nombre,rut):
        self.nombre = nombre
        self.rut = rut

    def mostrar(self):
        return self.nombre , self.rut

    
class Medidor:
    
    def __init__(self,kwh):
        self.kwh = kwh
        
    def mostrar_kwh(self):
        return int(self.kwh)
    
        
class Edificio(Departamento):
    
    def __init__(self,direccion,nombre,kwh,medidor):
        super().__init__(kwh)
        self.direccion = direccion
        self.nombre = nombre
        
    def ed(self):
        if self.kwh > 10000:
            print(True)
        else:
            print(False)

            
class Casa:
    
    def __init__(self,direc,num,el):
        self.direc = direc
        self.ed = False
        self.num = num
        self.el = int(el)
        
    def electro_dependiente(self):
        if self.el > 5000:
            return True
        else:
            return False

        
class Comuna(Casa):
    
    def __init__(self,nombre,direc,num,el):
        self.nombre = nombre
        super().__init__(direc,num,el)
        self.lista_casas = []
        
    def agregar_casa(self):
        if self.electro_dependiente() == True:
            self.lista_casas.append(self.direc)
        else:
            pass
        print(self.lista_casas)
    def agregar_edificio(self):
        pass


class Departamento(Medidor,Cliente):
    
    def __init__(self,nombre,kwh):
        super().__init__(kwh)
        self.nombre = nombre
                     
    def es_electrodp(self):   
        if self.kwh > 4000:
            print('{} es electrodependiente'.format(self.nombre))
        else:
            print('{} no es electrodependiente'.format(self.nombre))
            

#perro = Comuna('hola','213','2312',123123)
#perro.agregar_casa()
#med = Edificio('gh','A',a)
i = 0

while i <= 4:
    a = int(input('Kwh:'))
    b = input('direc:')
    perro = Comuna('hola',b,'2312',a)
    perro.agregar_casa()
    i += 1
    
    






    
