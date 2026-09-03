# ADT - Árbol Binario

Implementación de un Árbol Binario de Búsqueda (ABB) como Tipo de Dato
Abstracto, con ejercicios aplicados en consola y una versión web con Flask.

**Materia:** Estructura de Datos II
**Alumno:** Luis Eduardo Vargas Pantoja
**# de Registro:** 225044765

## Estructura del proyecto

| Archivo | Descripción |
|---|---|
| `ejercicios_y_clases/nodo.py` | Clase `Nodo` (valor, hijo izquierdo y derecho) |
| `ejercicios_y_clases/arbolbinario.py` | `ArbolBinario` (ABB): insertar, buscar, recorridos in/pre/post y construcción desde posfija |
| `ejercicios_y_clases/ejercicio_expresiones.py` | Conversión infija→posfija y construcción del árbol de expresiones |
| `ejercicios_y_clases/ejercicio_3enraya.py` | Tres en raya con 3 árboles binarios (uno por fila) |
| `MVC_ejer._expresiones/` | App web con Flask en arquitectura MVC (model, controller, templates y static) para el ejercicio de expresiones |

## Cómo ejecutar

**Ejercicios en consola:**
```bash
python3 ejercicios_y_clases/ejercicio_expresiones.py
python3 ejercicios_y_clases/ejercicio_3enraya.py
```

**App web (Flask):**
```bash
cd MVC_ejer._expresiones
python3 -m venv .venv && .venv/bin/pip install flask   # solo la primera vez
.venv/bin/python app.py                                 # abrir http://127.0.0.1:5000
```
