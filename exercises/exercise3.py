class Article:
    """Re-Escribir el ejercicio anterior utilizando una property en vez de un
    método de instancia."""

    def __init__(self,nombre,costo,descuento=0):
            self.nombre = nombre
            self.costo = costo
            self.descuento = descuento
    
    
    #===============================
    __iva = 0.21
    
    @classmethod
    def actualizar_iva(cls,arg):
        cls.__iva = arg 
    #===============================
    
    #===============================
    @property                       #esta seccion se utiliza para retornar el atributo __precio
    def precio(self):
        pre = round((self.costo -self.descuento)*(1+self.__iva),2)
        return pre
    #===============================
   
    """ 
    Restricciones:
        - Utilizar 3 variables de instancia (se instancian en el constructor)
        - Utilizar 1 property       
        - Utilizar 1 variable de clase (fuera del constructor)
        - Utilizar 1 método de clase (metodo de clase)
        - No utilizar métodos de instancia (metodo que modifica una var del constructor)
        - No utilizar Dataclasses
        - Utilizar Type Hints en todos los métodos y variables
     
        article = Article(nombre="Auto", costo=1)
        print(article.precio)
        article.precio = 2
        print(article.precio)""" 

# NO MODIFICAR - INICIO
# Test parámetro obligatorio
try:
    article = Article()
    assert False, "No se puede instanciar sin nombre ni costo"
except TypeError:
    assert True

try:
    article = Article("Auto")
    assert False, "No se puede instanciar sin costo"
except TypeError:
    assert True

try:
    article = Article(nombre="Auto", costo=1)
    assert True
except TypeError:
    assert False, "El descuento es opcional"

try:
    article = Article(nombre="Auto", costo=1)
    article.precio = 2
    assert False, "No se puede modificar el precio"
except AttributeError:
    assert True
 

# Test básico
article = Article("Auto", 1)
assert article.nombre == "Auto"
assert article.precio == 1.21


article = Article("Auto", 1, 0.21)
assert article.nombre == "Auto"
assert article.precio == 0.96


# Test palabra clave
article = Article(costo=1, nombre="Auto")
assert article.nombre == "Auto"
assert article.precio == 1.21

article = Article(costo=1, nombre="Auto", descuento=0.21)
assert article.nombre == "Auto"
assert article.precio == 0.96


# Test de método de clase
Article.actualizar_iva(0.25)

article = Article(costo=1, nombre="Auto")
assert article.nombre == "Auto"
assert article.precio == 1.25
# NO MODIFICAR - FIN
