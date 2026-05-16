from .matrix import base_nucleo, generar_palabras_codigo, peso_vector


def construir_codigo_ciclico():
    p = 2
    n = 7
    coeficientes_g = [1, 1, 0, 1]
    k = n - (len(coeficientes_g) - 1)

    generador = []
    for desplazamiento in range(k):
        fila = [0] * desplazamiento + coeficientes_g + [0] * (n - desplazamiento - len(coeficientes_g))
        generador.append(fila)

    matriz_control = base_nucleo(generador, p)
    coeficientes_h = dividir_polinomios([1, 0, 0, 0, 0, 0, 0, 1], coeficientes_g, p)

    palabras_codigo = generar_palabras_codigo(generador, p)
    no_cero = [w for w in palabras_codigo if any(v != 0 for v in w)]
    distancia_minima = min(peso_vector(w, p) for w in no_cero) if no_cero else 0

    return {
        "p": p,
        "n": n,
        "k": k,
        "coeficientes_g": coeficientes_g,
        "coeficientes_h": coeficientes_h,
        "generador": generador,
        "matriz_control": matriz_control,
        "palabras_codigo": palabras_codigo,
        "distancia_minima": distancia_minima,
    }


def dividir_polinomios(dividendo, divisor, p):
    numerador = dividendo[:]
    denominador = divisor[:]
    while len(numerador) > 0 and numerador[-1] == 0:
        numerador.pop()
    while len(denominador) > 0 and denominador[-1] == 0:
        denominador.pop()
    if not denominador:
        raise ValueError("divisor is zero")
    if len(numerador) < len(denominador):
        return [0]

    resultado = [0] * (len(numerador) - len(denominador) + 1)
    while len(numerador) >= len(denominador):
        desplazamiento = len(numerador) - len(denominador)
        coef_lider = numerador[-1]
        if coef_lider != 0:
            resultado[desplazamiento] = coef_lider
            for i in range(len(denominador)):
                numerador[i + desplazamiento] = (numerador[i + desplazamiento] - coef_lider * denominador[i]) % p
        while len(numerador) > 0 and numerador[-1] == 0:
            numerador.pop()
    return _recortar_polinomio(resultado)


def _recortar_polinomio(polinomio):
    salida = polinomio[:]
    while len(salida) > 1 and salida[-1] == 0:
        salida.pop()
    return salida
