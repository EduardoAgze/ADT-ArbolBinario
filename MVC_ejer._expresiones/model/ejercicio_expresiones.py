"""
Autor:    Vargas Pantoja Luis Eduardo
Título:   Expresiones matematicas de infija a posfija y su representación en un árbol binario.
Version:  1.0.0
Fecha:    31/08/2026
"""

from model.arbolbinario import ArbolBinario
from model.nodo import Nodo

class ArbolBinario_Expresiones(ArbolBinario):
    """Representa un árbol binario de expresiones matemáticas.

    Attributes:
        raiz: Referencia al nodo raíz del árbol, o None si está vacío.
    """

    def __init__(self):
        super().__init__()

    def construir_desde_posfija(self, posfija):
        if not posfija:
            self.raiz = None
            return

        pila_nodos = []

        for caracter in posfija:
            nodo = Nodo(caracter)

            if caracter not in "+-*/":
                pila_nodos.append(nodo)
            else:
                nodo._derecho = pila_nodos.pop()
                nodo._izquierdo = pila_nodos.pop()
                pila_nodos.append(nodo)

        self.raiz = pila_nodos.pop()

    def evaluar(self):
        """Evalúa la expresión representada por el árbol binario.

        Returns:
            float: Resultado de la evaluación de la expresión.
        """
        return self._evaluar_recursivo(self.raiz)

    def _evaluar_recursivo(self, nodo):
        """Evalúa la expresión de forma recursiva.

        Args:
            nodo: Nodo actual durante el recorrido del árbol.

        Returns:
            float: Resultado parcial de la evaluación.
        """
        if nodo is None:
            return 0

        # Si es una hoja (número), devolver su valor
        if nodo.izquierdo is None and nodo.derecho is None:
            return float(nodo.valor)

        # Evaluar los subárboles izquierdo y derecho
        izquierda = self._evaluar_recursivo(nodo.izquierdo)
        derecha = self._evaluar_recursivo(nodo.derecho)

        # Aplicar el operador del nodo actual a los resultados de los subárboles
        if nodo.valor == '+':
            return izquierda + derecha
        elif nodo.valor == '-':
            return izquierda - derecha
        elif nodo.valor == '*':
            return izquierda * derecha
        elif nodo.valor == '/':
            return izquierda / derecha


def prioridad(op):
    """Devuelve la jerarquía del operador matemático.
    
    Args:
        op (str): Operador matemático ('+', '-', '*', '/').
    Returns:
        int: Nivel de prioridad (1 para '+' y '-', 2 para '*' y '/')
    
    """
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    return 0


def infija_a_posfija(expresion):
    """Convierte una expresión matemática de notación infija a posfija.

    Args:
        expresion (str): Expresión matemática simple.
    
    Returns:
        list: Lista de caracteres que representa la expresión en notación posfija.

    
    """
    salida = []
    pila_operadores = []
    numero_actual = ""

    for caracter in expresion:
        
        if caracter in "+-*/":
            # Agregar el número acumulado a la salida antes de procesar el operador
            if numero_actual != "":
                salida.append(numero_actual)
                numero_actual = ""

            # Desapilar operadores con prioridad >= al operador actual
            while (  pila_operadores and prioridad(pila_operadores[-1]) >= prioridad(caracter)):
                salida.append(pila_operadores.pop())
            # Apilar el operador actual
            pila_operadores.append(caracter)

        # Procesar dígitos: acumularlos en número_actual
        elif caracter.isdigit():
            numero_actual += caracter

    # Agregar el último número si existe
    if numero_actual != "":
        salida.append(numero_actual)

    # Desapilar todos los operadores restantes hacia la salida
    while pila_operadores:
        salida.append(pila_operadores.pop())

    return salida

