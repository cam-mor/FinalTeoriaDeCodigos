from .matrix import base_nucleo, generar_palabras_codigo, multiplicar_matrices, transponer_matriz


def construir_codigo_rs(p=5, n=5, k=3, puntos=None):
    if puntos is None:
        puntos = list(range(n))
    generador = [[pow(a, i, p) for a in puntos] for i in range(k)]
    base_nulo = base_nucleo(generador, p)
    matriz_control = base_nulo
    palabras_codigo = generar_palabras_codigo(generador, p)
    ht = transponer_matriz(matriz_control)
    producto_gh = multiplicar_matrices(generador, ht, p)
    return {
        "p": p,
        "n": n,
        "k": k,
        "puntos": puntos,
        "generador": generador,
        "matriz_control": matriz_control,
        "palabras_codigo": palabras_codigo,
        "producto_gh": producto_gh,
    }


def codificar_mensaje(generador, mensaje, p):
    if len(mensaje) != len(generador):
        raise ValueError("message length mismatch")
    n = len(generador[0])
    palabra = [0] * n
    for i in range(len(mensaje)):
        for j in range(n):
            palabra[j] = (palabra[j] + mensaje[i] * generador[i][j]) % p
    return palabra
