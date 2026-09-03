"""
Autor:    Vargas Pantoja Luis Eduardo
Título:   Clase ArbolBinario para representar un árbol binario de búsqueda (ABB) incluyendo sus recorridos y métodos de inserción y búsqueda.
Version:  1.0.0
Fecha:    31/08/2026
"""
from model.nodo import Nodo


class ArbolBinario:
    """Representa un árbol binario de búsqueda (ABB).

    Attributes:
        raiz: Referencia al nodo raíz del árbol, o None si está vacío.
    """

    def __init__(self):
        self._raiz = None

    def es_vacio(self):
        return self.raiz is None

    def EsHoja(self):
        if self.raiz is not None:
            return self.raiz.izquierdo is None and self.raiz.derecho is None
        return False

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(valor, self.raiz)

    def _insertar_recursivo(self, valor, nodo):
        if valor < nodo.valor:
            if nodo.izquierdo is None:
                nodo.izquierdo = Nodo(valor)
            else:
                self._insertar_recursivo(valor, nodo.izquierdo)
        else:
            if nodo.derecho is None:
                nodo.derecho = Nodo(valor)
            else:
                self._insertar_recursivo(valor, nodo.derecho)

    def buscar(self, valor):
        return self._buscar_recursivo(valor, self.raiz)

    def _buscar_recursivo(self, valor, nodo):
        if nodo is None:
            return False
        if valor == nodo.valor:
            return True
        elif valor < nodo.valor:
            return self._buscar_recursivo(valor, nodo.izquierdo)
        else:
            return self._buscar_recursivo(valor, nodo.derecho)

    def evaluar(self):
        """Evalúa la expresión representada por el árbol binario.

        Returns:
            float: Resultado de la evaluación de la expresión.
        """
        return self._evaluar_recursivo(self.raiz)

    def _evaluar_recursivo(self, nodo):
        if nodo is None:
            return 0

        # Si es un nodo hoja, devuelve su valor como número.
        if nodo.izquierdo is None and nodo.derecho is None:
            return float(nodo.valor)

        # Evaluar los subárboles izquierdo y derecho.
        izquierda = self._evaluar_recursivo(nodo.izquierdo)
        derecha = self._evaluar_recursivo(nodo.derecho)

        # Aplicar la operación correspondiente según el valor del nodo.
        if nodo.valor == '+':
            return izquierda + derecha
        elif nodo.valor == '-':
            return izquierda - derecha
        elif nodo.valor == '*':
            return izquierda * derecha
        elif nodo.valor == '/':
            if derecha != 0:
                return izquierda / derecha
            else:
                raise ValueError("División por cero no permitida.")
        else:
            raise ValueError(f"Operador desconocido: {nodo.valor}")




    def InOrden(self):
        elementos = []
        self._inorden_recursivo(self.raiz, elementos)
        return " ".join(elementos)

    def _inorden_recursivo(self, nodo, elementos):
        if nodo is not None:
            self._inorden_recursivo(nodo.izquierdo, elementos)
            elementos.append(str(nodo.valor))
            self._inorden_recursivo(nodo.derecho, elementos)

    def PostOrden(self):
        elementos = []
        self._post_orden_recursivo(self.raiz, elementos)
        return " ".join(elementos)

    def _post_orden_recursivo(self, nodo_actual, elementos):
        if nodo_actual is not None:
            self._post_orden_recursivo(nodo_actual.izquierdo, elementos)
            self._post_orden_recursivo(nodo_actual.derecho, elementos)
            elementos.append(str(nodo_actual.valor))

    def PreOrden(self):
        elementos = []
        self._preorden_recursivo(self.raiz, elementos)
        return " ".join(elementos)

    def _preorden_recursivo(self, nodo, elementos):
        if nodo is not None:
            elementos.append(str(nodo.valor))
            self._preorden_recursivo(nodo.izquierdo, elementos)
            self._preorden_recursivo(nodo.derecho, elementos)

    @property
    def raiz(self):
        return self._raiz

    @raiz.setter
    def raiz(self, raiz):
        self._raiz = raiz
