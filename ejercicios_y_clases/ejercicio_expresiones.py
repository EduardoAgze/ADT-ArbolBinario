"""
Autor:    Vargas Pantoja Luis Eduardo
Título:   Expresiones matematicas de infija a posfija y su representación en un árbol binario.
Version:  1.0.0
Fecha:    31/08/2026
"""

from arbolbinario import ArbolBinario



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






if __name__ == "__main__":
    expresion = input("Ingrese una expresión matemática (solo números y +-*/): ")

    

    # 1. Convertir de Infija a Posfija
    posfija = infija_a_posfija(expresion)
    print(f"1. Lista Notación Posfija: {posfija}")

    # 2. Crear el Árbol Binario y armar su estructura
    arbol = ArbolBinario()
    arbol.construir_desde_posfija(posfija)

    # 3. Obtener el recorrido en PostOrden
    print(f"2. Recorrido PostOrden del Árbol: {arbol.PostOrden()}")