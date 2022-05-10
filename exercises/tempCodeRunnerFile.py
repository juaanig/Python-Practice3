class Article():

    def __init__(self,nombre,costo,descuento=0):
        self.nombre = nombre
        self.costo = costo
        self.descuento = descuento
    

    def actualizar_iva(self):
        total = self.costo*0.21
        return total
    
    def calcular_precio(self):
        iva = self.actualizar_iva()
        aux = self.costo + iva
        final = aux - (aux*self.descuento) 
        return round(final,2)

#========== borrar despues =================


#===========================================


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

# Test básico
article = Article("Auto", 1)
assert article.nombre == "Auto"
assert article.calcular_precio() == 1.21

article = Article("Auto", 1, 0.21)
assert article.nombre == "Auto"
assert article.calcular_precio() == 0.96


# Test palabra clave
article = Article(costo=1, nombre="Auto")
assert article.nombre == "Auto"
assert article.calcular_precio() == 1.21

article = Article(costo=1, nombre="Auto", descuento=0.21)
assert article.nombre == "Auto"
assert article.calcular_precio() == 0.96