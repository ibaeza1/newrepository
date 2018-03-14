class Cliente:
    def __init__(self, rut, **kwargs):
        super().__init__(**kwargs)
        self.rut = rut

    def mostrar(self):
        return self.rut

    
class Medidor:
    
    def __init__(self,kwh,**kwargs):
        super().__init__(**kwargs)
        self.kwh = kwh
        
    def mostrar_kwh(self):
        return int(self.kwh)


class Departamento(Medidor, Cliente):
    
    def __init__(self,n,**kwargs):
        super().__init__(**kwargs)
        self.nombre = n
        self.lista = []
                     
    def es_electrodp(self):
        rut = input("Rut:")
        self.rut = rut
        if self.kwh > 4000:
            print('{} es electrodependiente'.format(self.nombre))
            self.lista.append(self.rut)
        else:
            print('{} no es electrodependiente'.format(self.nombre))
        print(self.lista)
    
        
class Edificio(Departamento):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    def ed(self):
        kwh = int(input('Kwh: '))
        self.kwh = kwh
        if self.kwh > 10000:
            return True
        else:
            return False

            
class Casa(Medidor, Cliente):
    
    def __init__(self, direc, num, **kwargs):
        super().__init__(**kwargs)
        self.direc = direc
        self.num = num
        
    def electro_dependiente(self):
        k = int(input('Kwh: '))
        self.kwh = k
        if self.kwh > 5000:
            return True
        else:
            return False

        
class Comuna(Casa, Edificio):
    
    def __init__(self, nombre, **kwargs):
        super().__init__(**kwargs)
        self.nombre = nombre
        self.lista_casas = []
        self.lista_departamentos = []
        
    def agregar_casa(self):
        n = input('Numero de Casa: ')
        self.num = n
        if self.electro_dependiente() == True:
            self.lista_casas.append(self.num)
        else:
            pass
        print(self.lista_casas)
    def agregar_edificio(self):
        c = input('Rut del dueno: ')
        self.rut = c
        if self.ed() == True:
            self.lista_departamentos.append(self.rut)
        else:
            pass
        print(self.lista_departamentos)



comuna = Comuna('Las Condes', direc = 'Manquehue', num = '', rut = '', kwh = '',n = '' )
i = 0
while i <= 4:
    comuna.agregar_casa()
    comuna.agregar_edificio()
    i += 1




    
