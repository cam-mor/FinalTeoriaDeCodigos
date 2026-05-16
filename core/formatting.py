def matriz_a_texto(matriz):
    if not matriz:
        return "[]"
    columnas = len(matriz[0])
    anchos = [0] * columnas
    for fila in matriz:
        for j, val in enumerate(fila):
            anchos[j] = max(anchos[j], len(str(val)))
    lineas = []
    for fila in matriz:
        partes = []
        for j, val in enumerate(fila):
            partes.append(str(val).rjust(anchos[j]))
        lineas.append("[" + " ".join(partes) + "]")
    return "\n".join(lineas)


def vector_a_texto(vector):
    return "[" + " ".join(str(v) for v in vector) + "]"


def polinomio_a_texto(coeficientes, var="x"):
    terminos = []
    for potencia, coef in enumerate(coeficientes):
        if coef == 0:
            continue
        if potencia == 0:
            terminos.append(str(coef))
        elif potencia == 1:
            if coef == 1:
                terminos.append(var)
            else:
                terminos.append(f"{coef}{var}")
        else:
            if coef == 1:
                terminos.append(f"{var}^{potencia}")
            else:
                terminos.append(f"{coef}{var}^{potencia}")
    if not terminos:
        return "0"
    return " + ".join(terminos)


def palabras_codigo_a_texto(palabras_codigo, grupo=8):
    lineas = []
    linea = []
    for idx, palabra in enumerate(palabras_codigo, start=1):
        linea.append("".join(str(v) for v in palabra))
        if idx % grupo == 0:
            lineas.append("  ".join(linea))
            linea = []
    if linea:
        lineas.append("  ".join(linea))
    return "\n".join(lineas)
