import sys
from PyQt5 import QtWidgets

from integracion_lineal.integracion import CalculadoraSimpson
from regrecion_lineal.regresion import CalculadoraRegresion
from union import ListaLigada


class App(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Menú Principal")
        self.setGeometry(100, 100, 300, 200)

        self.btn_integracion = QtWidgets.QPushButton("Integración", self)
        self.btn_integracion.setGeometry(50, 50, 200, 40)

        self.btn_regresion = QtWidgets.QPushButton("Regresión", self)
        self.btn_regresion.setGeometry(50, 110, 200, 40)

        self.btn_integracion.clicked.connect(self.abrir_integracion)
        self.btn_regresion.clicked.connect(self.abrir_regresion)

    def abrir_integracion(self):
        self.win = VentanaIntegracion()
        self.win.show()

    def abrir_regresion(self):
        self.win = VentanaRegresion()
        self.win.show()


class VentanaIntegracion(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Integración")
        self.setGeometry(100, 100, 300, 200)

        self.calc = CalculadoraSimpson()

        self.input_x = QtWidgets.QLineEdit(self)
        self.input_x.setPlaceholderText("x")
        self.input_x.move(50, 30)

        self.input_dof = QtWidgets.QLineEdit(self)
        self.input_dof.setPlaceholderText("dof")
        self.input_dof.move(50, 70)

        self.btn = QtWidgets.QPushButton("Calcular", self)
        self.btn.move(50, 110)

        self.resultado = QtWidgets.QLabel("", self)
        self.resultado.move(50, 150)

        self.btn.clicked.connect(self.calcular)

    def calcular(self):
        try:
            x = float(self.input_x.text())
            dof = float(self.input_dof.text())
            res = self.calc.integrar(x, dof)
            self.resultado.setText(str(res))
        except:
            self.resultado.setText("Error")


class VentanaRegresion(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Regresión")
        self.setGeometry(100, 100, 350, 250)

        self.lista = ListaLigada()

        self.input_x = QtWidgets.QLineEdit(self)
        self.input_x.setPlaceholderText("x")
        self.input_x.move(30, 30)

        self.input_y = QtWidgets.QLineEdit(self)
        self.input_y.setPlaceholderText("y")
        self.input_y.move(150, 30)

        self.btn_add = QtWidgets.QPushButton("Agregar", self)
        self.btn_add.move(30, 70)

        self.btn_calc = QtWidgets.QPushButton("Calcular", self)
        self.btn_calc.move(150, 70)

        self.resultado = QtWidgets.QLabel("", self)
        self.resultado.setGeometry(30, 120, 300, 100)

        self.btn_add.clicked.connect(self.agregar)
        self.btn_calc.clicked.connect(self.calcular)

    def agregar(self):
        try:
            x = float(self.input_x.text())
            y = float(self.input_y.text())
            self.lista.insertar(x, y)
            self.input_x.clear()
            self.input_y.clear()
        except:
            self.resultado.setText("Error en datos")

    def calcular(self):
        calc = CalculadoraRegresion(self.lista)
        res = calc.calcular_parametros()

        if res:
            texto = f"b0: {res['b0']}\nb1: {res['b1']}\nr: {res['r']}"
            self.resultado.setText(texto)
        else:
            self.resultado.setText("Sin datos")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ventana = App()
    ventana.show()
    sys.exit(app.exec_())