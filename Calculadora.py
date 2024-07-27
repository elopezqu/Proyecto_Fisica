import sys
import random
import numpy as np
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QLineEdit, QPushButton, QLabel, QHBoxLayout, QSizePolicy, QMessageBox
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt

class CalculadoraMonteCarlo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Calculadora de Integrales')
        self.resize(500, 450)
        
        layout = QVBoxLayout()
        
        titulo_label = QLabel("Calculadora de Integrales")
        titulo_label.setAlignment(Qt.AlignCenter)
        titulo_label.setStyleSheet("font-size: 24px; font-weight: bold;")
        titulo_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        layout.addWidget(titulo_label)

        principal = QHBoxLayout()
        integration_layout = QHBoxLayout()
        integration_layout2 = QVBoxLayout()

        self.limite_inferior_input = QLineEdit()
        self.limite_inferior_input.setPlaceholderText("Lí. infe.")
        self.limite_inferior_input.setFixedWidth(100)
        self.limite_inferior_input.setFont(QFont("Arial", 14))
        self.limite_inferior_input.setAlignment(Qt.AlignCenter) 
        integration_layout2.addWidget(self.limite_inferior_input)
        
        integral_label = QLabel("∫")
        integral_label.setStyleSheet("font-size: 120px;")
        integration_layout.addWidget(integral_label)
        
        caja_funcion = QHBoxLayout()
        self.resultado_display = QLineEdit()
        self.resultado_display.setFont(QFont("Arial", 20))
        self.resultado_display.setPlaceholderText("f(x)")
        self.resultado_display.setAlignment(Qt.AlignCenter)
        caja_funcion.addWidget(self.resultado_display)
        integration_layout2.addLayout(caja_funcion)

        dx_label = QLabel("dx")
        dx_label.setStyleSheet("font-size: 14px; font-weight: bold;")
        dx_label.setMargin(10)
        dx_label.setSizePolicy(10, 0)
        caja_funcion.addWidget(dx_label)
        integration_layout2.addLayout(caja_funcion)
        
        self.limite_superior_input = QLineEdit()
        self.limite_superior_input.setPlaceholderText("Lí. supe.")
        self.limite_superior_input.setFont(QFont("Arial", 14))
        self.limite_superior_input.setFixedWidth(100)
        self.limite_superior_input.setAlignment(Qt.AlignCenter) 
        integration_layout2.addWidget(self.limite_superior_input)
        
        integration_layout.setContentsMargins(1, 1, 1, 25)
        principal.addLayout(integration_layout)
        principal.addLayout(integration_layout2)
        layout.addLayout(principal)
        
        grid_layout = QGridLayout()
        
        botones = [
            ('sin', 0, 0), ('cos', 0, 1), ('tan', 0, 2), ('e', 0, 3),
            ('√', 1, 0), ('^', 1, 1), ('log', 1, 2), ('ln', 1, 3),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('π', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('÷', 4, 3),
            ('(', 5, 0), ('0', 5, 1), (')', 5, 2), ('×', 5, 3),
            ('X', 6, 0), ('Calcular', 6, 1), ('Borrar', 6, 2), ('+', 6, 3)
        ]
        
        for btn_text, row, col, rowspan, colspan in [(b[0], b[1], b[2], 1, 1) if len(b) == 3 else b for b in botones]:
            button = QPushButton(btn_text)
            button.clicked.connect(self.on_click)
            grid_layout.addWidget(button, row, col, rowspan, colspan)
        
        layout.addLayout(grid_layout)
        self.setLayout(layout)
    
    def on_click(self):
        sender = self.sender()
        text = sender.text()
        
        if text == 'Borrar':
            self.resultado_display.clear()
            self.limite_inferior_input.clear()
            self.limite_superior_input.clear()
        elif text == 'Calcular':
            self.interpretar()
        else:
            self.resultado_display.setText(self.resultado_display.text() + text)
    
    def interpretar(self):
        if not self.limite_inferior_input.text() or not self.limite_superior_input.text() or not self.resultado_display.text():
            self.mostrar_mensaje_error("Falta ingresar valores")
            return
        
        try:

            # Aqui la parte que convierte
            expr = self.resultado_display.text()
            print(expr)

            limite_inferior = float(self.limite_inferior_input.text())
            limite_superior = float(self.limite_superior_input.text())
            
            print(limite_inferior)
            print(limite_superior)

        except Exception as e:
            self.resultado_display.setText("Error")

    def mostrar_mensaje_error(self, mensaje):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Advertencia")
        msg.setText(mensaje)
        msg.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = CalculadoraMonteCarlo()
    calc.show()
    sys.exit(app.exec_())
