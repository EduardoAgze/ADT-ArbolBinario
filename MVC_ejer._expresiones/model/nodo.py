"""
Autor:    Vargas Pantoja Luis Eduardo
Título:   Clase Nodo para representar un nodo de un árbol binario incluyendo sus getters y setters.
Version:  1.0.0
Fecha:    31/08/2026
"""
class Nodo:
    """Representa un nodo de un árbol binario.

    Attributes:
        valor: valor almacenado en el nodo.
        izquierdo: referencia al hijo izquierdo del nodo.
        derecho: referencia al hijo derecho del nodo.
    """

    def __init__(self, valor):
        self._valor = valor
        self._izquierdo = None
        self._derecho = None

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, valor):
        self._valor = valor

    @property
    def izquierdo(self):
        return self._izquierdo

    @izquierdo.setter
    def izquierdo(self, izquierdo):
        self._izquierdo = izquierdo

    @property
    def derecho(self):
        return self._derecho

    @derecho.setter
    def derecho(self, derecho):
        self._derecho = derecho
