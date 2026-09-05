from flask import render_template, request, redirect, url_for, flash
from model.ejercicio_expresiones import infija_a_posfija
from model.ejercicio_expresiones import ArbolBinario_Expresiones


def index():
    """Mostrar la página principal con el formulario de conversión."""
    return render_template("index.html")


def convertir():
    """Convertir una expresión infija y mostrar los resultados."""
    expresion = request.form.get("expresion")

    if not expresion:
        flash("Ingrese una expresión válida.")
        return redirect(url_for("index"))

    # 1. Convertir de Infija a Posfija.
    posfija = infija_a_posfija(expresion)

    # 2. Crear el Árbol Binario y armar su estructura.
    arbol = ArbolBinario_Expresiones()
    arbol.construir_desde_posfija(posfija)

    # 3. Obtener los recorridos del árbol.
    preorden = arbol.PreOrden()
    inorden = arbol.InOrden()
    postorden = arbol.PostOrden()

    # 4. Generar la representación gráfica del árbol en formato SVG.
    grafico_svg = arbol.grafo().pipe(format="svg").decode("utf-8")

    flash("Expresión convertida")

    return render_template("index.html",
                           expresion=expresion,
                           posfija=posfija,
                           preorden=preorden,
                           inorden=inorden,
                           postorden=postorden,
                           grafico_svg=grafico_svg,
                           resultado=arbol.evaluar())