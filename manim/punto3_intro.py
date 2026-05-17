from manim import *


COEF_G = [1, 1, 0, 1]
COEF_H = [1, 1, 1, 0, 1]

GENERADOR = [
	[1, 1, 0, 1, 0, 0, 0],
	[0, 1, 1, 0, 1, 0, 0],
	[0, 0, 1, 1, 0, 1, 0],
	[0, 0, 0, 1, 1, 0, 1],
]

MATRIZ_CONTROL = [
	[1, 0, 1, 1, 1, 0, 0],
	[1, 1, 1, 0, 0, 1, 0],
	[0, 1, 1, 1, 0, 0, 1],
]

CODEWORDS = [
	"0000000",
	"0001101",
	"0011010",
	"0010111",
	"0110100",
	"0111001",
	"0101110",
	"0100011",
	"1101000",
	"1100101",
	"1110010",
	"1111111",
	"1011100",
	"1010001",
	"1000110",
	"1001011",
]


def _build_matrix(data, scale=0.72):
	matriz = Matrix(data)
	matriz.scale(scale)
	return matriz


class Punto3Intro(Scene):
	def construct(self):
		titulo = Text("Punto 3 - Codigo binario ciclico", font_size=44)
		linea1 = MathTex(r"\text{Elegimos } g(x) \text{ que divide } x^{7} - 1", font_size=30)
		gx = MathTex(r"g(x)=1 + x + x^3")
		hx = MathTex(r"h(x)=1 + x + x^2 + x^4")

		encabezado = VGroup(titulo).to_edge(UP)
		bloque = VGroup(linea1, gx, hx).arrange(DOWN, buff=0.45)
		bloque.next_to(encabezado, DOWN, buff=0.6)

		self.play(Write(encabezado))
		self.play(LaggedStart(Write(linea1), Write(gx), Write(hx), lag_ratio=0.35), run_time=3)
		self.wait(1)


class Punto3Parametros(Scene):
	def construct(self):
		titulo = Text("Parametros", font_size=44)
		linea1 = Text("Codigo ciclico binario no trivial", font_size=30)
		params = MathTex(r"n=7,\; k=4,\; d_{min}=3")

		encabezado = VGroup(titulo).to_edge(UP)
		bloque = VGroup(linea1, params).arrange(DOWN, buff=0.5)
		bloque.next_to(encabezado, DOWN, buff=0.6)

		self.play(Write(encabezado))
		self.play(LaggedStart(Write(linea1), Write(params), lag_ratio=0.35), run_time=3)
		self.wait(1)


class Punto3Generador(Scene):
	def construct(self):
		titulo = Text("Matriz generadora", font_size=44)
		linea1 = Text("Desplazamientos ciclicos de g(x)", font_size=30)

		g_label = MathTex("G =")
		g_matrix = _build_matrix(GENERADOR, scale=0.72)
		g_group = VGroup(g_label, g_matrix).arrange(RIGHT, buff=0.4)

		encabezado = VGroup(titulo).to_edge(UP)
		bloque = VGroup(linea1, g_group).arrange(DOWN, buff=0.5)
		bloque.next_to(encabezado, DOWN, buff=0.6)

		self.play(Write(encabezado))
		self.play(LaggedStart(Write(linea1), Create(g_group), lag_ratio=0.35), run_time=3)
		self.wait(1)


class Punto3Control(Scene):
	def construct(self):
		titulo = Text("Matriz de control", font_size=44)
		linea1 = Text("Base del nucleo de G", font_size=30)

		h_label = MathTex("H =")
		h_matrix = _build_matrix(MATRIZ_CONTROL, scale=0.72)
		h_group = VGroup(h_label, h_matrix).arrange(RIGHT, buff=0.4)

		encabezado = VGroup(titulo).to_edge(UP)
		bloque = VGroup(linea1, h_group).arrange(DOWN, buff=0.5)
		bloque.next_to(encabezado, DOWN, buff=0.6)

		self.play(Write(encabezado))
		self.play(LaggedStart(Write(linea1), Create(h_group), lag_ratio=0.35), run_time=3)
		self.wait(1)


class Punto3Codewords(Scene):
	def construct(self):
		titulo = Text("Listado de codewords", font_size=44)
		linea1 = Text("Se enumeran las 2^4 palabras", font_size=30)

		fila1 = Text("  ".join(CODEWORDS[:8]), font="Consolas", font_size=26)
		fila2 = Text("  ".join(CODEWORDS[8:]), font="Consolas", font_size=26)
		lista = VGroup(fila1, fila2).arrange(DOWN, buff=0.35)

		encabezado = VGroup(titulo).to_edge(UP)
		bloque = VGroup(linea1, lista).arrange(DOWN, buff=0.5)
		bloque.next_to(encabezado, DOWN, buff=0.6)

		self.play(Write(encabezado))
		self.play(LaggedStart(Write(linea1), Write(lista), lag_ratio=0.35), run_time=3)
		self.wait(1)


class Punto3Algoritmo(Scene):
	def construct(self):
		titulo = Text("Algoritmo", font_size=44)
		linea1 = Text("1) Elegir g(x) y construir G por desplazamientos", font_size=30)
		linea2 = MathTex(r"\text{2) Calcular H y } h(x) = (x^{7} - 1)/g(x)", font_size=30)
		linea3 = MathTex(r"\text{3) Enumerar palabras y hallar } d_{min}", font_size=30)

		encabezado = VGroup(titulo).to_edge(UP)
		bloque = VGroup(linea1, linea2, linea3).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
		bloque.next_to(encabezado, DOWN, buff=0.6)

		self.play(Write(encabezado))
		self.play(
			LaggedStart(Write(linea1), Write(linea2), Write(linea3), lag_ratio=0.35),
			run_time=4,
		)
		self.wait(1)
