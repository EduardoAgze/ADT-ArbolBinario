class Nodo:
    """Representa un nodo de un árbol binario.

    Attributes:
        valor: valor almacenado en el nodo.
        izquierdo: referencia al hijo izquierdo del nodo.
        derecho: referencia al hijo derecho del nodo.
    """

    def __init__(self, valor):
        """Inicializa un nodo con un valor y sin hijos.

        Args:
            valor: valor que se almacenará en el nodo.
        """
        self._valor = valor
        self._izquierdo = None
        self._derecho = None

    @property
    def valor(self):
        """GETTER:
        Obtiene el valor almacenado en el nodo."""
        return self._valor

    @valor.setter
    def valor(self, valor):
        """SETTER:
        Establece el valor almacenado en el nodo."""
        self._valor = valor

    @property
    def izquierdo(self):
        """GETTER:
        Obtiene la referencia al hijo izquierdo."""
        return self._izquierdo

    @izquierdo.setter
    def izquierdo(self, izquierdo):
        """SETTER:
        Establece la referencia al hijo izquierdo."""
        self._izquierdo = izquierdo

    @property
    def derecho(self):
        """GETTER:
        Obtiene la referencia al hijo derecho."""
        return self._derecho

    @derecho.setter
    def derecho(self, derecho):
        """SETTER:
        Establece la referencia al hijo derecho."""
        self._derecho = derecho



