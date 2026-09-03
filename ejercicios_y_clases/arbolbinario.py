"""
Autor:    Vargas Pantoja Luis Eduardo
Título:   Clase ArbolBinario para representar un árbol binario de búsqueda (ABB) incluyendo sus recorridos y métodos de inserción y búsqueda.
Version:  1.0.0
Fecha:    31/08/2026
"""
from nodo import Nodo


class ArbolBinario:
    """Representa un árbol binario de búsqueda (ABB).

    Attributes:
        raiz: Referencia al nodo raíz del árbol, o None si está vacío.
    """

    def __init__(self):
        """Inicializa un árbol binario de búsqueda vacío."""
        self._raiz = None


    def es_vacio(self):
        """Comprueba si el árbol está vacío.

        Returns:
            bool: True si el árbol no tiene raíz, False en caso contrario.
        """
        return self.raiz is None

    def EsHoja(self):
        """Comprueba si la raíz del árbol es una hoja.

        Returns:
            bool: True si la raíz no tiene hijos, False en caso contrario.
        """
        if self.raiz is not None:
            return self.raiz.izquierdo is None and self.raiz.derecho is None
        return False

    def insertar(self, valor):
        """Inserta un valor en el árbol binario de búsqueda.

        Args:
            valor: Valor que se insertará en el árbol.
        """
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(valor, self.raiz)

    def _insertar_recursivo(self, valor, nodo):
        """Inserta un valor de forma recursiva manteniendo el orden del ABB.

        Args:
            valor: Valor que se insertará.
            nodo: Nodo actual durante el recorrido del árbol.
        """
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
        """Busca un valor en el árbol binario de búsqueda.

        Args:
            valor: Valor que se buscará en el árbol.

        Returns:
            bool: True si el valor existe en el árbol, False en caso contrario.
        """
        return self._buscar_recursivo(valor, self.raiz)

    def _buscar_recursivo(self, valor, nodo):
        """Busca un valor de forma recursiva.
        """
        if nodo is None:
            return False
        if valor == nodo.valor:
            return True
        elif valor < nodo.valor:
            return self._buscar_recursivo(valor, nodo.izquierdo)
        else:
            return self._buscar_recursivo(valor, nodo.derecho)

    def construir_desde_posfija(self, posfija):
        """Construye un árbol binario a partir de una expresión en notación posfija.

        Args:
            posfija (str): Expresión en notación posfija sin espacios.
                          Los operandos pueden ser números o variables (caracteres),
                          y los operadores son: +, -, *, /.

        """
        if not posfija:
            self.raiz = None
            return
        
        pila_nodos = []

        for caracter in posfija:
            nodo = Nodo(caracter)

            # Si es un número (operando)
            if caracter not in "+-*/":
                pila_nodos.append(nodo)
            else:
                # Si es un operador, asigna los dos últimos nodos como sus hijos
                nodo._derecho = pila_nodos.pop()
                nodo._izquierdo = pila_nodos.pop()
                pila_nodos.append(nodo)

        # El último nodo en la pila es la raíz principal
        self.raiz = pila_nodos.pop()




# RECORRIDOS DEL ÁRBOL




    def InOrden(self):
        """Recorre el árbol en orden simétrico (inorden).

        Returns:
            str: Cadena con los valores del árbol separados por espacios.
        """
        elementos = []
        self._inorden_recursivo(self.raiz, elementos)
        return " ".join(elementos)

    def _inorden_recursivo(self, nodo, elementos):
        """Recorre el subárbol en inorden y almacena sus valores.

        Args:
            nodo: Nodo raíz del subárbol a recorrer.
            elementos: Lista donde se almacenan los valores.
        """
        if nodo is not None:
            self._inorden_recursivo(nodo.izquierdo, elementos)
            elementos.append(str(nodo.valor))
            self._inorden_recursivo(nodo.derecho, elementos)



    def PostOrden(self):
        """Recorre el árbol en postorden.

        Returns:
            str: Cadena con los valores del árbol separados por espacios.
        """
        elementos = []
        self._post_orden_recursivo(self.raiz, elementos)
        return " ".join(elementos)

    def _post_orden_recursivo(self, nodo_actual, elementos):
        """Recorre el subárbol en postorden y almacena sus valores.

        Args:
            nodo_actual: Nodo raíz del subárbol a recorrer.
            elementos: Lista donde se almacenan los valores.
        """
        if nodo_actual is not None:
            # 1. Recorrer subárbol izquierdo
            self._post_orden_recursivo(nodo_actual.izquierdo, elementos)
            # 2. Recorrer subárbol derecho
            self._post_orden_recursivo(nodo_actual.derecho, elementos)
            # 3. Visitar raíz
            elementos.append(str(nodo_actual.valor))



    def PreOrden(self):
        """Recorre el árbol en preorden.

        Returns:
            str: Cadena con los valores del árbol separados por espacios.
        """
        elementos = []
        self._preorden_recursivo(self.raiz, elementos)
        return " ".join(elementos)

    def _preorden_recursivo(self, nodo, elementos):
        """Recorre el subárbol en preorden y almacena sus valores.

        Args:
            nodo: Nodo raíz del subárbol a recorrer.
            elementos: Lista donde se almacenan los valores.
        """
        if nodo is not None:
            elementos.append(str(nodo.valor))
            self._preorden_recursivo(nodo.izquierdo, elementos)
            self._preorden_recursivo(nodo.derecho, elementos)











    @property
    def raiz(self):
        """GETTER:
        Obtiene la referencia al nodo raíz del árbol."""
        return self._raiz

    @raiz.setter
    def raiz(self, raiz):
        """SETTER:
        Establece la referencia al nodo raíz del árbol."""
        self._raiz = raiz
