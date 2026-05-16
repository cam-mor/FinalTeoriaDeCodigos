import tkinter as tk
import webbrowser
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

from core.cyclic import construir_codigo_ciclico
from core.formatting import matriz_a_texto, palabras_codigo_a_texto, polinomio_a_texto, vector_a_texto
from core.linear_binary import construir_lineal_binario
from core.reed_solomon import codificar_mensaje, construir_codigo_rs


class AplicacionTeoriaCodigos(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Teoria de Codigos - Proyecto Final")
        self.geometry("980x640")
        self.minsize(900, 600)
        self._build_ui()
        self.show_punto1()

    def _build_ui(self):
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        sidebar = ttk.Frame(self, padding=10)
        sidebar.grid(row=0, column=0, sticky="ns")

        main = ttk.Frame(self, padding=10)
        main.grid(row=0, column=1, sticky="nsew")
        main.rowconfigure(0, weight=1)
        main.columnconfigure(0, weight=1)

        ttk.Label(sidebar, text="Menu", font=("Segoe UI", 12, "bold")).pack(anchor="w", pady=(0, 8))

        ttk.Button(sidebar, text="Punto 1 - Reed-Solomon", command=self.show_punto1).pack(fill="x", pady=4)
        ttk.Button(sidebar, text="Punto 2 - Lineal binario", command=self.show_punto2).pack(fill="x", pady=4)
        ttk.Button(sidebar, text="Punto 3 - Ciclico", command=self.show_punto3).pack(fill="x", pady=4)
        ttk.Button(sidebar, text="Acerca", command=self.show_ayuda).pack(fill="x", pady=4)
        ttk.Button(sidebar, text="Abrir GitHub", command=self.open_github).pack(fill="x", pady=4)

        self.salida = ScrolledText(main, wrap="word", font=("Consolas", 11))
        self.salida.grid(row=0, column=0, sticky="nsew")
        self.salida.configure(state="disabled")

        menu = tk.Menu(self)
        puntos = tk.Menu(menu, tearoff=0)
        puntos.add_command(label="Punto 1 - Reed-Solomon", command=self.show_punto1)
        puntos.add_command(label="Punto 2 - Lineal binario", command=self.show_punto2)
        puntos.add_command(label="Punto 3 - Ciclico", command=self.show_punto3)
        menu.add_cascade(label="Puntos", menu=puntos)
        ayuda = tk.Menu(menu, tearoff=0)
        ayuda.add_command(label="Acerca", command=self.show_ayuda)
        ayuda.add_command(label="Abrir GitHub", command=self.open_github)
        menu.add_cascade(label="Ayuda", menu=ayuda)
        self.config(menu=menu)

    def _set_text(self, texto):
        self.salida.configure(state="normal")
        self.salida.delete("1.0", tk.END)
        self.salida.insert(tk.END, texto)
        self.salida.configure(state="disabled")

    def show_punto1(self):
        datos = construir_codigo_rs()
        mensaje = [1, 2, 3]
        palabra = codificar_mensaje(datos["generador"], mensaje, datos["p"])
        cuerpo = []
        cuerpo.append("Punto 1 - Reed-Solomon (n=5, k=3) sobre F5\n")
        cuerpo.append("Descripcion de F5: {0,1,2,3,4} con suma y producto modulo 5.\n")
        cuerpo.append("Mensajes como polinomios: m(x)=a0 + a1 x + a2 x^2.\n")
        cuerpo.append("Puntos de evaluacion: " + ", ".join(str(v) for v in datos["puntos"]) + "\n\n")

        cuerpo.append("Matriz generadora (Vandermonde):\n")
        cuerpo.append(matriz_a_texto(datos["generador"]) + "\n\n")

        cuerpo.append("Matriz de control (base del nul-espacio):\n")
        cuerpo.append(matriz_a_texto(datos["matriz_control"]) + "\n\n")

        cuerpo.append("Ejemplo de codificacion:\n")
        cuerpo.append("Mensaje m = " + vector_a_texto(mensaje) + "\n")
        cuerpo.append("Polinomio m(x) = " + polinomio_a_texto(mensaje) + "\n")
        cuerpo.append("Codeword c = m * G = " + vector_a_texto(palabra) + "\n\n")

        cuerpo.append("Validacion computacional:\n")
        cuerpo.append("|C| = {0} (esperado {1})\n".format(len(datos["palabras_codigo"]), datos["p"] ** datos["k"]))
        cuerpo.append("G * H^T =\n")
        cuerpo.append(matriz_a_texto(datos["producto_gh"]) + "\n")

        cuerpo.append("\nAlgoritmo utilizado:\n")
        cuerpo.append("1) Elegir puntos de evaluacion en F5 y formar G tipo Vandermonde.\n")
        cuerpo.append("2) Calcular H como una base del nucleo de G.\n")
        cuerpo.append("3) Generar palabras con m * G para todos los mensajes.\n")
        cuerpo.append("4) Verificar G * H^T = 0 y el tamano del codigo.\n")

        self._set_text("".join(cuerpo))

    def show_punto2(self):
        datos = construir_lineal_binario()
        cuerpo = []
        cuerpo.append("Punto 2 - Codigo lineal binario\n")
        cuerpo.append("Matriz generadora original G:\n")
        cuerpo.append(matriz_a_texto(datos["generador_base"]) + "\n\n")

        cuerpo.append("Matriz generadora en forma estandar:\n")
        cuerpo.append(matriz_a_texto(datos["generador_estandar"]) + "\n")
        perm_std = [i + 1 for i in datos["permutacion_estandar"]]
        cuerpo.append("Permutacion de columnas aplicada (1-based): " + str(perm_std) + "\n\n")

        cuerpo.append("Auto-dual: " + ("Si" if datos["auto_dual"] else "No") + "\n")
        cuerpo.append("Nota: n=7 es impar, por lo tanto no puede ser auto-dual.\n\n")

        cuerpo.append("Codigo equivalente (permuta de columnas):\n")
        cuerpo.append(matriz_a_texto(datos["generador_equivalente"]) + "\n")
        perm_eq = [i + 1 for i in datos["permutacion_equivalente"]]
        cuerpo.append("Permutacion usada (1-based): " + str(perm_eq) + "\n\n")

        cuerpo.append("Codigo de extension (bit de paridad global):\n")
        cuerpo.append(matriz_a_texto(datos["generador_extension"]) + "\n\n")

        cuerpo.append("Codigo de perforacion (se elimina columna {0}):\n".format(datos["columna_perforacion"] + 1))
        cuerpo.append(matriz_a_texto(datos["generador_perforado"]) + "\n\n")

        cuerpo.append("Codigo de reduccion (shortening en columna {0}):\n".format(datos["columna_reduccion"] + 1))
        cuerpo.append(matriz_a_texto(datos["generador_reducido"]) + "\n")

        cuerpo.append("\nAlgoritmo utilizado:\n")
        cuerpo.append("1) Llevar G a forma estandar con permutacion de columnas y operaciones.\n")
        cuerpo.append("2) Evaluar auto-dualidad con la matriz de Gram (solo si n es par).\n")
        cuerpo.append("3) Construir codigo equivalente con una permutacion distinta.\n")
        cuerpo.append("4) Aplicar extension, perforacion y reduccion segun definiciones.\n")

        self._set_text("".join(cuerpo))

    def show_punto3(self):
        datos = construir_codigo_ciclico()
        cuerpo = []
        cuerpo.append("Punto 3 - Codigo binario ciclico (n=7)\n")
        cuerpo.append("Polinomio generador g(x) = " + polinomio_a_texto(datos["coeficientes_g"]) + "\n")
        cuerpo.append("Polinomio de control h(x) = " + polinomio_a_texto(datos["coeficientes_h"]) + "\n\n")

        cuerpo.append(
            "Parametros: n={0}, k={1}, d_min={2}\n\n".format(
                datos["n"], datos["k"], datos["distancia_minima"]
            )
        )

        cuerpo.append("Matriz generadora:\n")
        cuerpo.append(matriz_a_texto(datos["generador"]) + "\n\n")

        cuerpo.append("Matriz de control:\n")
        cuerpo.append(matriz_a_texto(datos["matriz_control"]) + "\n\n")

        cuerpo.append("Algoritmo utilizado:\n")
        cuerpo.append("1) Elegir g(x) que divide x^7 - 1 y construir G por desplazamientos.\n")
        cuerpo.append("2) Calcular H como base del nucleo de G y h(x) = (x^7 - 1)/g(x).\n")
        cuerpo.append("3) Enumerar palabras y calcular la distancia minima por pesos.\n\n")

        cuerpo.append("Listado de codewords:\n")
        cuerpo.append(palabras_codigo_a_texto(datos["palabras_codigo"]) + "\n")

        self._set_text("".join(cuerpo))

    def open_github(self):
        webbrowser.open_new("https://github.com/cam-mor/FinalTeoriaDeCodigos")

    def show_ayuda(self):
        texto = (
            "Proyecto Final - Teoria de Codigos\n\n"
            "Repositorio GitHub:\n"
            "https://github.com/cam-mor/FinalTeoriaDeCodigos\n\n"
            "Use 'Abrir GitHub' en el menu Ayuda o en la barra lateral.\n"
        )
        self._set_text(texto)
