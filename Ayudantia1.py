print(*[True, False])
#Los argumentos posicionales de usan cuando se requiere un numero indeterminado de argumentos
def using_args(*argumentos):
    print(argumentos)
    for i in argumentos:
        print(i)

#using_args('s',3,5,True)

#**kwargs en Python
a = {'b' : 1, 'c' : 2, 'd' : 3}
#print(a)
#print(type(a))

def using_kwargs(**kwargs):
    print(kwargs)
    print(type(kwargs))


#using_kwargs(**a)

def using_kwargs(c, **kwargs):
    print(c)
    print(kwargs)
    print(b)
    print(d)

#using_kwargs(**a)

def using_kwargs(d, b, c):
    print(b)
    print(c)
    print(d)
          
#Cuando a una funcion le paso nombres con argumentos desempaquetados se imprimen en el orden en el que estan en el diccionario
# __str__ y __repr__ tienen que retornar un string
using_kwargs(**a)

class Ser:
    
    rut = 0

    def __init__(self, nombre, **kwargs):
        self.nombre = nombre
    

class Humano(Ser):
    def __init__(self, ano_nacimiento, **kwargs):
        super().__init__(**kwargs)
        self.ano_nacimiento = ano_nacimiento

    def Saludar(self):
        pass

    def __str__(self):
        pass

class Dios(Ser):

    def __init__(self, poder, **kwargs):
        super().__init__(**kwargs)
        self.poder = poder


class Investigador:
    def __init__(self, area='', **kwargs):
        print("init Investigador con area {} y kwargs:{}".format(area, kwargs))
        super().__init__(**kwargs)
        self.area = area
        self.num_publicaciones = 0
        
class Docente:
    def __init__(self, departamento='', **kwargs):
        print("init Docente con depto {} y kwargs:{}".format(departamento, kwargs))
        super().__init__(**kwargs)
        self.departamento = departamento
        self.num_cursos = 3
        
class Academico(Docente, Investigador):
    def __init__(self, nombre, oficina, **kwargs):
        print("init Academico con nombre {}, oficina {}, kwargs:{}".format(nombre, oficina, kwargs))
        super().__init__(**kwargs)
        self.nombre = nombre
        self.oficina = oficina
        print(self.area)

print(Academico.__mro__)
p1 = Academico("Emilia Donoso", oficina="O5", area="Inteligencia de Máquina", departamento="Ciencia De La Computación")
print("--------")
print(p1.nombre)
print(p1.area)
print(p1.departamento)
























    
