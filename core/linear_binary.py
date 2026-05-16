from .matrix import (
    agregar_columna_paridad,
    aplicar_permutacion_columnas,
    eliminar_columna,
    forma_escalonada_reducida,
    forma_estandar,
    generar_palabras_codigo,
)


GENERADOR_BASE = [
    [1, 1, 1, 0, 0, 0, 0],
    [1, 0, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 1, 1],
    [0, 1, 0, 1, 0, 1, 0],
]


def construir_lineal_binario():
    p = 2
    generador_estandar, permutacion_estandar = forma_estandar(GENERADOR_BASE, p)
    n = len(generador_estandar[0])
    k = len(generador_estandar)

    auto_dual = False
    if n % 2 == 0 and k == n // 2:
        matriz_gram = _matriz_gram(generador_estandar, p)
        auto_dual = _es_matriz_cero(matriz_gram)

    permutacion_equivalente = [2, 0, 1, 3, 4, 5, 6]
    generador_equivalente = aplicar_permutacion_columnas(generador_estandar, permutacion_equivalente)

    generador_extension = agregar_columna_paridad(generador_estandar, p)

    columna_perforacion = 6
    generador_perforado = eliminar_columna(generador_estandar, columna_perforacion)

    columna_reduccion = 0
    generador_reducido = acortar_codigo(generador_estandar, columna_reduccion)

    return {
        "p": p,
        "generador_base": GENERADOR_BASE,
        "generador_estandar": generador_estandar,
        "permutacion_estandar": permutacion_estandar,
        "auto_dual": auto_dual,
        "generador_equivalente": generador_equivalente,
        "permutacion_equivalente": permutacion_equivalente,
        "generador_extension": generador_extension,
        "columna_perforacion": columna_perforacion,
        "generador_perforado": generador_perforado,
        "columna_reduccion": columna_reduccion,
        "generador_reducido": generador_reducido,
    }


def acortar_codigo(generador, indice_columna):
    p = 2
    palabras_codigo = generar_palabras_codigo(generador, p)
    filtradas = []
    for palabra in palabras_codigo:
        if palabra[indice_columna] == 0:
            filtradas.append(palabra[:indice_columna] + palabra[indice_columna + 1 :])
    if not filtradas:
        return []
    rref_mat, _ = forma_escalonada_reducida(filtradas, p)
    base = [fila for fila in rref_mat if any(v != 0 for v in fila)]
    return base


def _matriz_gram(generador, p):
    filas = len(generador)
    salida = [[0 for _ in range(filas)] for _ in range(filas)]
    for i in range(filas):
        for j in range(filas):
            salida[i][j] = sum(generador[i][t] * generador[j][t] for t in range(len(generador[0]))) % p
    return salida


def _es_matriz_cero(matriz):
    return all(all(v == 0 for v in fila) for fila in matriz)
