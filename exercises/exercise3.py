"""Properties"""


class Article:
    """Re-Escribir el ejercicio anterior utilizando una property en vez de un
    método de instancia.

    Restricciones:
        - Utilizar 3 variables de instancia
        - Utilizar 1 property
        - Utilizar 1 variable de clase
        - Utilizar 1 método de clase
        - No utilizar métodos de instancia
        - No utilizar Dataclasses
        - Utilizar Type Hints en todos los métodos y variables
    """
    IVA = 0.21

    @classmethod
    def actualizar_iva(cls, nuevo_iva):
        cls.IVA = nuevo_iva

    def __init__(self, nombre, costo, descuento=0):
        self._nombre = nombre
        self._costo = costo
        self._descuento = descuento
        self._precio = self.calcular_precio()

    def calcular_precio(self) -> float:
        resultado = (self._costo * (self.IVA+1))
        resultado -= (resultado * self._descuento)
        return round(resultado, 2)

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    @property
    def costo(self):
        return self._costo

    @costo.setter
    def costo(self, nuevo_costo):
        self._costo = nuevo_costo

    @property
    def descuento(self):
        return self._descuento

    @descuento.setter
    def descuento(self, nuevo_descuento=0):
        self._descuento = nuevo_descuento

    @property
    def precio(self):
        return self._precio


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
