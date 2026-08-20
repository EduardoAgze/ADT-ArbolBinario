"""
Autor:    Vargas Pantoja Luis Eduardo
Título:   Estructura de un Arbol Binario enfocado en el juego de tres en raya.
Version:  1.0.0
Fecha:    19/08/2026
"""

from Nodo import Nodo


class Arbol:
    """Representa el tablero de tres en raya como 3 mini árboles binarios."""

    def __init__(self):
        """Inicializa el tablero con 3 filas vacías."""
        self._filas = []
        for _ in range(3):
            raiz = Nodo(' ')
            raiz.izquierdo = Nodo(' ')
            raiz.derecho = Nodo(' ')
            self._filas.append(raiz)

    def obtener_nodo(self, fila, columna):
        """Devuelve el nodo en (fila, columna).

        La columna 0 representa la raíz, la columna 1 es el hijo
        izquierdo y la columna 2 es el hijo derecho.

        Args:
            fila: índice de la fila (0 a 2).
            columna: índice de la columna (0 a 2).

        Returns:
            Nodo: el nodo ubicado en (fila, columna).
        """
        raiz = self._filas[fila]
        if columna == 0:
            return raiz
        elif columna == 1:
            return raiz.izquierdo
        else:
            return raiz.derecho

    def obtener_valor(self, fila, columna):
        """Devuelve el valor guardado en (fila, columna).

        Args:
            fila: índice de la fila (0 a 2).
            columna: índice de la columna (0 a 2).

        Returns:
            str: valor almacenado en esa casilla.
        """
        return self.obtener_nodo(fila, columna).valor

    def establecer_valor(self, fila, columna, valor):
        """Coloca un valor en (fila, columna).

        Args:
            fila: índice de la fila (0 a 2).
            columna: índice de la columna (0 a 2).
            valor: valor a colocar en la casilla.
        """
        self.obtener_nodo(fila, columna).valor = valor

    def hay_ganador(self):
        """Revisa filas, columnas y diagonales en busca de un ganador.

        Returns:
            str or None: 'X' u 'O' si hay un ganador, None si no.
        """
        lineas = [
            [(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
            [(0, 0), (1, 0), (2, 0)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],
            [(0, 0), (1, 1), (2, 2)],
            [(0, 2), (1, 1), (2, 0)],
        ]
        for a, b, c in lineas:
            v1 = self.obtener_valor(*a)
            v2 = self.obtener_valor(*b)
            v3 = self.obtener_valor(*c)
            if v1 != ' ' and v1 == v2 == v3:
                return v1
        return None

    def mostrar(self):
        """Imprime el tablero en consola."""
        for fila in range(3):
            valores = [self.obtener_valor(fila, c) for c in range(3)]
            print(' | '.join(valores))


if __name__ == '__main__':
    # Ejemplo de uso
    tablero = Arbol()

    tablero.establecer_valor(0, 1, 'X')
    tablero.establecer_valor(1, 1, 'O')
    tablero.establecer_valor(1, 0, 'X')
    tablero.establecer_valor(2, 2, 'O')
    tablero.establecer_valor(2, 0, 'X')
    tablero.establecer_valor(0, 0, 'O')

    print("Tablero final:")
    tablero.mostrar()

    ganador = tablero.hay_ganador()
    if ganador:
        print(f'\nGana el jugador: {ganador}')
    else:
        print('\nAún no hay ganador.')