from manim import *

class Punto1Intro(Scene):
    def construct(self):
        titulo = Text("Punto 1 - Reed-Solomon", font_size=48)
        campo = MathTex(r"\mathbb{F}_5 = \{0,1,2,3,4\}")
        parametros = MathTex(r"n = 5,\; k = 3")

        bloque = VGroup(titulo, campo, parametros).arrange(DOWN, buff=0.4)
        bloque.move_to(ORIGIN)

        self.play(
            LaggedStart(
                Write(titulo),
                Write(campo),
                Write(parametros),
                lag_ratio=0.2,
            ),
            run_time=3,
        )
        self.wait(1)

class Punto1MatrizGeneradora(Scene):
    def construct(self):
        titulo = Text("Punto 1 - Matriz generadora", font_size=44)
        etiqueta = MathTex(r"G =")
        matriz = MathTex(
            r"\begin{bmatrix}"
            r"1 & 1 & 1 & 1 & 1\\"
            r"0 & 1 & 2 & 3 & 4\\"
            r"0 & 1 & 4 & 4 & 1"
            
            
            
            r"\end{bmatrix}"
        )

        encabezado = VGroup(titulo).to_edge(UP)
        bloque = VGroup(etiqueta, matriz).arrange(RIGHT, buff=0.4)
        bloque.move_to(ORIGIN)

        self.play(Write(encabezado))
        self.play(Write(etiqueta))
        self.play(Write(matriz))
        self.wait(2)


class Punto1MensajePolinomio(Scene):
    def construct(self):
        titulo = Text("Mensaje como polinomio", font_size=44)
        linea = Text("Mensaje de 3 simbolos", font_size=32)
        polinomio = MathTex(r"m(x) = a_0 + a_1 x + a_2 x^2")
        grado = MathTex(r"\deg(m) \le 2")

        encabezado = VGroup(titulo).to_edge(UP)
        bloque = VGroup(linea, polinomio, grado).arrange(DOWN, buff=0.45)
        bloque.move_to(ORIGIN)

        self.play(Write(encabezado))
        self.play(LaggedStart(Write(linea), Write(polinomio), Write(grado), lag_ratio=0.3), run_time=3)
        self.wait(1)


class Punto1PuntosEvaluacion(Scene):
    def construct(self):
        titulo = Text("Puntos de evaluacion", font_size=44)
        puntos = MathTex(r"\{0,1,2,3,4\}")
        nota = Text("Aritmetica modulo 5", font_size=30)

        encabezado = VGroup(titulo).to_edge(UP)
        bloque = VGroup(puntos, nota).arrange(DOWN, buff=0.5)
        bloque.move_to(ORIGIN)

        self.play(Write(encabezado))
        self.play(Write(puntos))
        self.play(Write(nota))
        self.wait(1)


class Punto1Codificacion(Scene):
    def construct(self):
        titulo = Text("Codificacion", font_size=44)
        linea1 = Text("Evaluar m(x) en 5 puntos", font_size=32)
        linea2 = Text("Equivale a multiplicar", font_size=32)
        ecuacion = MathTex(r"c = m G")

        encabezado = VGroup(titulo).to_edge(UP)
        bloque = VGroup(linea1, linea2, ecuacion).arrange(DOWN, buff=0.45)
        bloque.move_to(ORIGIN)

        self.play(Write(encabezado))
        self.play(LaggedStart(Write(linea1), Write(linea2), Write(ecuacion), lag_ratio=0.3), run_time=3)
        self.wait(1)


class Punto1MatrizControl(Scene):
    def construct(self):
        titulo = Text("Matriz de control", font_size=44)
        linea1 = Text("Base del nucleo de G", font_size=32)
        ecuacion = MathTex(r"G H^T = 0")

        encabezado = VGroup(titulo).to_edge(UP)
        bloque = VGroup(linea1, ecuacion).arrange(DOWN, buff=0.5)
        bloque.move_to(ORIGIN)

        self.play(Write(encabezado))
        self.play(LaggedStart(Write(linea1), Write(ecuacion), lag_ratio=0.35), run_time=2.5)
        self.wait(1)


class Punto1TamanoCodigo(Scene):
    def construct(self):
        titulo = Text("Tamaño del codigo", font_size=44)
        ecuacion = MathTex(r"|C| = 5^3 = 125")

        encabezado = VGroup(titulo).to_edge(UP)
        ecuacion.move_to(ORIGIN)

        self.play(Write(encabezado))
        self.play(Write(ecuacion))
        self.wait(1)
