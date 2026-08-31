from Nodo import Nodo


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





# RECORRIDOS DEL ÁRBOL




    def InOrden(self):
        """Recorre el árbol en orden simétrico (inorden) e imprime sus valores."""
        self._inorden_recursivo(self.raiz)

    def _inorden_recursivo(self, nodo):
        """Recorre el subárbol en inorden e imprime sus valores.

        Args:
            nodo: Nodo raíz del subárbol a recorrer.
        """
        if nodo is None:
            return
        self._inorden_recursivo(nodo.izquierdo)
        print(nodo.valor)
        self._inorden_recursivo(nodo.derecho)

    def PostOrden(self):
        """Recorre el árbol en postorden e imprime sus valores."""
        self._postorden_recursivo(self.raiz)

    def _postorden_recursivo(self, nodo):
        """Recorre el subárbol en postorden e imprime sus valores.

        Args:
            nodo: Nodo raíz del subárbol a recorrer.
        """
        if nodo is None:
            return
        self._postorden_recursivo(nodo.izquierdo)
        self._postorden_recursivo(nodo.derecho)
        print(nodo.valor)

    def PreOrden(self):
        """Recorre el árbol en preorden e imprime sus valores."""
        self._preorden_recursivo(self.raiz)

    def _preorden_recursivo(self, nodo):
        """Recorre el subárbol en preorden e imprime sus valores.

        Args:
            nodo: Nodo raíz del subárbol a recorrer.
        """
        if nodo is None:
            return
        print(nodo.valor)
        self._preorden_recursivo(nodo.izquierdo)
        self._preorden_recursivo(nodo.derecho)











    @property
    def raiz(self):
        """Nodo raíz del árbol.

        Returns:
            Nodo or None: Referencia al nodo raíz del árbol.
        """
        return self._raiz

    @raiz.setter
    def raiz(self, raiz):
        """Establece el nodo raíz del árbol.

        Args:
            raiz: Nueva referencia al nodo raíz.
        """
        self._raiz = raiz
