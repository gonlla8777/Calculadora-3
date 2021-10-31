from PyQt5.QtWidgets import QInputDialog, QMainWindow, QApplication 
from PyQt5 import uic

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("windowscalcu.ui", self)

        
        self.boton_cero.clicked.connect(self.obtener)
        self.boton_uno.clicked.connect(self.obtener1)
        self.boton_dos.clicked.connect(self.obtener2)
        self.boton_tres.clicked.connect(self.obtener3)
        self.boton_cuatro.clicked.connect(self.obtener4)
        self.boton_cinco.clicked.connect(self.obtener5)
        self.boton_seis.clicked.connect(self.obtener6)
        self.boton_siete.clicked.connect(self.obtener7)
        self.boton_ocho.clicked.connect(self.obtener8)
        self.boton_nueve.clicked.connect(self.obtener9)
        self.boton_suma.clicked.connect(self.obtener10)
        self.boton_resta.clicked.connect(self.obtener11)
        self.boton_multiplicar.clicked.connect(self.obtener12)
        self.boton_dividir.clicked.connect(self.obtener13)
        self.boton_porcentaje.clicked.connect(self.obtener14)
        self.boton_potencia.clicked.connect(self.obtener15)
        self.boton_raiz.clicked.connect(self.obtener16)
        self.boton_parentesis_iz.clicked.connect(self.obtener17)
        self.boton_parentesis_de.clicked.connect(self.obtener18)
        self.boton_igual.clicked.connect(self.obtener19)
        self.boton_decimal.clicked.connect(self.obtener20)
        self.boton_borrar_2.clicked.connect(self.obtener21)
        self.boton_borrar_todo.clicked.connect(self.borratodo)


    

    entrada2 = []

    def borratodo(self):
        borra = ""
        self.valor.setText(borra)
        self.valor2.setText(borra)



    def obtener(self):
        entrada2 = self.valor2.text()
        entrada2 += "0"
        entrada = self.valor.text()
        entrada += "0"
        self.valor.setText(entrada)
        self.valor2.setText(entrada2)
       
        
        
    
    def obtener1(self):
        entrada2 = self.valor2.text()
        entrada2 += "1"
        entrada = self.valor.text()
        entrada += "1"
        self.valor.setText(entrada)
        self.valor2.setText(entrada2)
    
    def obtener2(self):
        entrada2 = self.valor2.text()
        entrada2 += "2"
        entrada = self.valor.text()
        entrada += "2"
        self.valor.setText(entrada)
        self.valor2.setText(entrada2)


        


    def obtener3(self):
        entrada2 = self.valor2.text()
        entrada2 += "3"
        entrada = self.valor.text()
        entrada += "3"
        self.valor.setText(entrada)
        self.valor2.setText(entrada2)

    def obtener4(self):
        entrada2 = self.valor2.text()
        entrada2 += "4"
        entrada = self.valor.text()
        entrada += "4"
        self.valor.setText(entrada)
        self.valor2.setText(entrada2)

    def obtener5(self):
        entrada2 = self.valor2.text()
        entrada2 += "5"
        entrada = self.valor.text()
        entrada += "5"
        self.valor.setText(entrada)
        self.valor2.setText(entrada2)

    def obtener6(self):
        entrada2 = self.valor2.text()
        entrada2 += "6"
        entrada = self.valor.text()
        entrada += "6"
        self.valor.setText(entrada)
        self.valor2.setText(entrada2)

    def obtener7(self):
        entrada2 = self.valor2.text()
        entrada2 += "7"
        entrada = self.valor.text()
        entrada += "7"
        self.valor.setText(entrada)
        self.valor2.setText(entrada2)

    def obtener8(self):
        entrada2 = self.valor2.text()
        entrada2 += "8"
        entrada = self.valor.text()
        entrada += "8"
        self.valor.setText(entrada)
        self.valor2.setText(entrada2)

    def obtener9(self):
        entrada2 = self.valor2.text()
        entrada2 += "9"
        entrada = self.valor.text()
        entrada += "9"
        self.valor.setText(entrada)
        self.valor2.setText(entrada2)

    def obtener10(self):
        entrada = self.valor.text()
        entrada += "+"
        self.valor.setText(entrada)
        self.valor2.setText(entrada)
    
    def obtener11(self):
        entrada = self.valor.text()
        entrada += "-"
        self.valor.setText(entrada)
        self.valor2.setText(entrada)

    def obtener12(self):
        entrada2 = self.valor2.text()
        entrada2 += "x"
        entrada = self.valor.text()
        entrada += "*"
        self.valor.setText(entrada)
        self.valor2.setText(entrada2)

    def obtener13(self):
        entrada = self.valor.text()
        entrada += "/"
        self.valor.setText(entrada)
        self.valor2.setText(entrada)

    def obtener14(self):
        entrada = self.valor.text()
        entrada += "%-"
        self.valor.setText(entrada)
        self.valor2.setText(entrada)

    def obtener15(self):
        entrada2 = self.valor2.text()
        entrada2 += "^"
        entrada = self.valor.text()
        entrada += "**"
        self.valor.setText(entrada)
        self.valor2.setText(entrada2)

        #RAIZ

    def obtener16(self):
        
        #self.operador1 ** (self.operador2**(-1)
        entrada = self.valor.text()
        entrada += "**(1/2)"
        self.valor.setText(entrada)
        entrada2 = self.valor2.text()
        entrada2 += "√"
        self.valor2.setText(entrada2)
        
        
            

    def obtener17(self):
        entrada2 = self.valor2.text()
        entrada2 += "("
        entrada = self.valor.text()
        entrada += "("
        self.valor.setText(entrada)
        self.valor2.setText(entrada2)

    def obtener18(self):
        entrada2 = self.valor2.text()
        entrada2 += ")"
        entrada = self.valor.text()
        entrada += ")"
        self.valor.setText(entrada)
        self.valor2.setText(entrada2)

    def obtener19(self):
       
        entrada = self.valor.text()
        try:
                ans = eval(entrada)
                self.valor.setText(str(ans))
        except:
                self.valor.setText("ERROR")
        

    def obtener20(self):
        entrada2 = self.valor2.text()
        entrada2 += "."
        entrada = self.valor.text()
        entrada += "."
        self.valor.setText(entrada)
        self.valor2.setText(entrada2)

    def obtener21(self):
        entrada = self.valor.text()
        self.valor.setText(entrada[:len(entrada)-1])

app = QApplication([])
win = MiVentana()
win.show()
app.exec_()