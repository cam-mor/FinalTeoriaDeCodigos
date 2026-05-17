from manim import *


GENERADOR_BASE = [
    [1, 1, 1, 0, 0, 0, 0],
    [1, 0, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 1, 1],
    [0, 1, 0, 1, 0, 1, 0],
]

GENERADOR_ESTANDAR = [
    [1, 0, 0, 0, 0, 1, 1],
    [0, 1, 0, 0, 1, 0, 1],
    [0, 0, 1, 0, 1, 1, 0],
    [0, 0, 0, 1, 1, 1, 1],
]

GENERADOR_EQUIVALENTE = [
    [0, 1, 0, 0, 0, 1, 1],
    [0, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 1, 1, 1, 1],
]

GENERADOR_EXTENSION = [
    [1, 0, 0, 0, 0, 1, 1, 1],
    [0, 1, 0, 0, 1, 0, 1, 1],
    [0, 0, 1, 0, 1, 1, 0, 1],
    [0, 0, 0, 1, 1, 1, 1, 0],
]

GENERADOR_PERFORADO = [
    [1, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 1, 0],
    [0, 0, 1, 0, 1, 1],
    [0, 0, 0, 1, 1, 1],
]

GENERADOR_REDUCIDO = [
    [1, 0, 0, 1, 0, 1],
    [0, 1, 0, 1, 1, 0],
    [0, 0, 1, 1, 1, 1],
]


def _build_matrix(data, scale=0.72):
    matriz = Matrix(data)
    matriz.scale(scale)
    return matriz


class Punto2Intro(Scene):
    def construct(self):
        titulo = Text("Punto 2 - Codigo lineal binario", font_size=44)
        linea1 = Text("Matriz generadora original G", font_size=32)
        linea2 = MathTex(r"G \subseteq \mathbb{F}_2^{4 \times 7}")

        g_label = MathTex("G =")
        g_matrix = _build_matrix(GENERADOR_BASE, scale=0.72)
        g_group = VGroup(g_label, g_matrix).arrange(RIGHT, buff=0.4)

        encabezado = VGroup(titulo).to_edge(UP)
        bloque = VGroup(linea1, linea2, g_group).arrange(DOWN, buff=0.5)
        bloque.next_to(encabezado, DOWN, buff=0.6)

        self.play(Write(encabezado))
        self.play(LaggedStart(Write(linea1), Write(linea2), Create(g_group), lag_ratio=0.3), run_time=3)
        self.wait(1)


class Punto2FormaEstandar(Scene):
    def construct(self):
        titulo = Text("Forma estandar", font_size=44)
        linea = Text("Operaciones por filas y permutacion de columnas", font_size=30)
        forma = MathTex(r"[I_k \mid P]")
        perm = Text("Permutacion: (1, 2, 3, 4, 5, 6, 7)", font_size=26)

        g_label = MathTex("G_{std} =")
        g_matrix = _build_matrix(GENERADOR_ESTANDAR, scale=0.72)
        g_group = VGroup(g_label, g_matrix).arrange(RIGHT, buff=0.4)

        encabezado = VGroup(titulo).to_edge(UP)
        bloque = VGroup(linea, forma, g_group, perm).arrange(DOWN, buff=0.45)
        bloque.next_to(encabezado, DOWN, buff=0.5)

        self.play(Write(encabezado))
        self.play(
            LaggedStart(Write(linea), Write(forma), Create(g_group), Write(perm), lag_ratio=0.35),
            run_time=3,
        )
        self.wait(1)


class Punto2AutoDual(Scene):
    def construct(self):
        titulo = Text("Auto-dualidad", font_size=44)
        linea1 = Text("Si n es impar, no puede ser auto-dual", font_size=30)
        linea2 = MathTex(r"n = 7 \Rightarrow \text{no auto-dual}")

        encabezado = VGroup(titulo).to_edge(UP)
        bloque = VGroup(linea1, linea2).arrange(DOWN, buff=0.5)
        bloque.move_to(ORIGIN)

        self.play(Write(encabezado))
        self.play(LaggedStart(Write(linea1), Write(linea2), lag_ratio=0.35), run_time=3)
        self.wait(1)


class Punto2Equivalente(Scene):
    def construct(self):
        titulo = Text("Codigo equivalente", font_size=44)
        linea1 = Text("Aplicamos otra permutacion de columnas", font_size=30)
        linea2 = Text("Se conserva el mismo codigo", font_size=30)
        perm = Text("Permutacion: (3, 1, 2, 4, 5, 6, 7)", font_size=26)

        g_label = MathTex("G_{eq} =")
        g_matrix = _build_matrix(GENERADOR_EQUIVALENTE, scale=0.72)
        g_group = VGroup(g_label, g_matrix).arrange(RIGHT, buff=0.4)

        encabezado = VGroup(titulo).to_edge(UP)
        bloque = VGroup(linea1, linea2, g_group, perm).arrange(DOWN, buff=0.45)
        bloque.next_to(encabezado, DOWN, buff=0.5)

        self.play(Write(encabezado))
        self.play(
            LaggedStart(Write(linea1), Write(linea2), Create(g_group), Write(perm), lag_ratio=0.35),
            run_time=3,
        )
        self.wait(1)


class Punto2Operaciones(Scene):
    def construct(self):
        titulo = Text("Operaciones clasicas", font_size=44)
        encabezado = VGroup(titulo).to_edge(UP)

        linea1 = Text("Extension: agregar bit de paridad global", font_size=28)
        ext_label = MathTex("G_{ext} =")
        ext_matrix = _build_matrix(GENERADOR_EXTENSION, scale=0.6)
        ext_group = VGroup(ext_label, ext_matrix).arrange(RIGHT, buff=0.35)
        ext_block = VGroup(linea1, ext_group).arrange(DOWN, buff=0.4)
        ext_block.next_to(encabezado, DOWN, buff=0.6)

        linea2 = Text("Perforacion: eliminar columna 7", font_size=28)
        perf_label = MathTex("G_{perf} =")
        perf_matrix = _build_matrix(GENERADOR_PERFORADO, scale=0.7)
        perf_group = VGroup(perf_label, perf_matrix).arrange(RIGHT, buff=0.35)
        perf_block = VGroup(linea2, perf_group).arrange(DOWN, buff=0.4)
        perf_block.next_to(encabezado, DOWN, buff=0.6)

        linea3 = Text("Reduccion: fijar columna 1 en 0 y acortar", font_size=28)
        red_label = MathTex("G_{red} =")
        red_matrix = _build_matrix(GENERADOR_REDUCIDO, scale=0.75)
        red_group = VGroup(red_label, red_matrix).arrange(RIGHT, buff=0.35)
        red_block = VGroup(linea3, red_group).arrange(DOWN, buff=0.4)
        red_block.next_to(encabezado, DOWN, buff=0.6)

        self.play(Write(encabezado))
        self.play(FadeIn(ext_block))
        self.wait(1)
        self.play(FadeOut(ext_block))
        self.play(FadeIn(perf_block))
        self.wait(1)
        self.play(FadeOut(perf_block))
        self.play(FadeIn(red_block))
        self.wait(1)
        self.wait(1)


class Punto2Resumen(Scene):
    def construct(self):
        titulo = Text("Resumen", font_size=44)
        linea1 = MathTex(r"\text{Se obtiene } G, G_{std} \text{ y } G_{eq}")
        linea1.scale(0.9)
        linea2 = Text("Extension, perforacion y reduccion", font_size=30)

        encabezado = VGroup(titulo).to_edge(UP)
        bloque = VGroup(linea1, linea2).arrange(DOWN, buff=0.5)
        bloque.move_to(ORIGIN)

        self.play(Write(encabezado))
        self.play(LaggedStart(Write(linea1), Write(linea2), lag_ratio=0.35), run_time=3)
        self.wait(1)
