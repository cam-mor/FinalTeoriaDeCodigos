from itertools import product


def inverso_modular(a, p):
    a = a % p
    if a == 0:
        raise ValueError("no hay inverso para 0")
    t, nuevo_t = 0, 1
    r, nuevo_r = p, a
    while nuevo_r != 0:
        q = r // nuevo_r
        t, nuevo_t = nuevo_t, t - q * nuevo_t
        r, nuevo_r = nuevo_r, r - q * nuevo_r
    if r != 1:
        raise ValueError("elemento no invertible")
    if t < 0:
        t += p
    return t


def transponer_matriz(matriz):
    return [list(fila) for fila in zip(*matriz)]


def multiplicar_matrices(matriz_a, matriz_b, p):
    filas = len(matriz_a)
    columnas = len(matriz_b[0])
    intermedia = len(matriz_b)
    salida = [[0 for _ in range(columnas)] for _ in range(filas)]
    for i in range(filas):
        for k in range(intermedia):
            if matriz_a[i][k] == 0:
                continue
            for j in range(columnas):
                salida[i][j] = (salida[i][j] + matriz_a[i][k] * matriz_b[k][j]) % p
    return salida


def multiplicar_matriz_vector(matriz, vector, p):
    return [
        sum((matriz[i][j] * vector[j]) for j in range(len(vector))) % p
        for i in range(len(matriz))
    ]


def forma_escalonada_reducida(matriz, p):
    copia = [fila[:] for fila in matriz]
    filas = len(copia)
    columnas = len(copia[0])
    columnas_pivote = []
    fila_actual = 0
    for col in range(columnas):
        if fila_actual >= filas:
            break
        fila_pivote = None
        for i in range(fila_actual, filas):
            if copia[i][col] % p != 0:
                fila_pivote = i
                break
        if fila_pivote is None:
            continue
        if fila_pivote != fila_actual:
            copia[fila_actual], copia[fila_pivote] = copia[fila_pivote], copia[fila_actual]
        inv = inverso_modular(copia[fila_actual][col], p)
        copia[fila_actual] = [(val * inv) % p for val in copia[fila_actual]]
        for i in range(filas):
            if i != fila_actual and copia[i][col] % p != 0:
                factor = copia[i][col] % p
                copia[i] = [(copia[i][j] - factor * copia[fila_actual][j]) % p for j in range(columnas)]
        columnas_pivote.append(col)
        fila_actual += 1
    return copia, columnas_pivote


def base_nucleo(matriz, p):
    rref_mat, columnas_pivote = forma_escalonada_reducida(matriz, p)
    filas = len(rref_mat)
    columnas = len(rref_mat[0])
    columnas_libres = [c for c in range(columnas) if c not in columnas_pivote]
    base = []
    for libre in columnas_libres:
        vec = [0] * columnas
        vec[libre] = 1
        for r, col_pivote in enumerate(columnas_pivote):
            if r < filas:
                vec[col_pivote] = (-rref_mat[r][libre]) % p
        base.append(vec)
    return base


def forma_estandar(matriz, p):
    copia = [fila[:] for fila in matriz]
    filas = len(copia)
    columnas = len(copia[0])
    permutacion = list(range(columnas))
    fila_actual = 0
    col_actual = 0
    while fila_actual < filas and col_actual < columnas:
        fila_pivote = None
        col_pivote = None
        for j in range(col_actual, columnas):
            for i in range(fila_actual, filas):
                if copia[i][j] % p != 0:
                    fila_pivote = i
                    col_pivote = j
                    break
            if col_pivote is not None:
                break
        if col_pivote is None:
            break
        if col_pivote != col_actual:
            for i in range(filas):
                copia[i][col_actual], copia[i][col_pivote] = copia[i][col_pivote], copia[i][col_actual]
            permutacion[col_actual], permutacion[col_pivote] = permutacion[col_pivote], permutacion[col_actual]
        if fila_pivote != fila_actual:
            copia[fila_actual], copia[fila_pivote] = copia[fila_pivote], copia[fila_actual]
        inv = inverso_modular(copia[fila_actual][col_actual], p)
        copia[fila_actual] = [(val * inv) % p for val in copia[fila_actual]]
        for i in range(filas):
            if i != fila_actual and copia[i][col_actual] % p != 0:
                factor = copia[i][col_actual] % p
                copia[i] = [(copia[i][j] - factor * copia[fila_actual][j]) % p for j in range(columnas)]
        fila_actual += 1
        col_actual += 1
    return copia, permutacion


def aplicar_permutacion_columnas(matriz, permutacion):
    return [[fila[i] for i in permutacion] for fila in matriz]


def eliminar_columna(matriz, indice_columna):
    return [fila[:indice_columna] + fila[indice_columna + 1 :] for fila in matriz]


def agregar_columna_paridad(matriz, p):
    salida = []
    for fila in matriz:
        paridad = sum(fila) % p
        salida.append(fila + [paridad])
    return salida


def generar_palabras_codigo(generador, p):
    k = len(generador)
    n = len(generador[0])
    palabras = []
    for mensaje in product(range(p), repeat=k):
        palabra = [0] * n
        for i in range(k):
            if mensaje[i] == 0:
                continue
            for j in range(n):
                palabra[j] = (palabra[j] + mensaje[i] * generador[i][j]) % p
        palabras.append(palabra)
    return palabras


def peso_vector(vector, p):
    if p != 2:
        raise ValueError("peso solo definido para p=2 en este helper")
    return sum(1 for v in vector if v % 2 != 0)
