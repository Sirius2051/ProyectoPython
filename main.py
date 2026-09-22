
import requests
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit

app = QApplication([])

window = QWidget()

window.resize(600, 300)
window.setWindowTitle("Conversiones al dia")

# icon = QIcon()
# pixmap = QPixmap()
# pixmap.load("treasure.png")
# icon.addPixmap(pixmap)
# window.setWindowIcon(icon)
window.setStyleSheet(
"""
color: #efefef;
background: #232323;
font-size: 16pt;
font-family: Cascadia Mono;
"""
)

button = QPushButton("Ver precio")
button.setStyleSheet(
"""
background: rgb(45, 90, 212);
border-radius: 18px; 
border: none;
padding: 10px 5px;
"""
)


dolar_label = QLabel("Dolar") 
dolar_label.setStyleSheet(

"""
font-weight: bold;
font-size: 14pt;

"""
)
euros_label = QLabel("Euro") 
euros_label.setStyleSheet(
"""
font-weight: bold;
font-size: 14pt;
"""
)
dolar_values = QLabel("0") 
euros_values = QLabel("0") 

precio = QLineEdit("0")
precio.setStyleSheet(
"""
border-radius: 14px; 
border: 1px solid #353535;
padding: 10px 30px;
"""
)
button2 = QPushButton("Calcular")
button2.setStyleSheet(
"""
background: rgb(170, 45, 90);
border-radius: 14px; 
border: none;
padding: 10px 30px;
"""
)
dolar_precio = QLabel("0") 
euros_precio = QLabel("0") 

main_layout = QVBoxLayout()

text_layout = QHBoxLayout()
values_layout = QHBoxLayout()
precio_layout = QHBoxLayout()
precios_layout = QHBoxLayout()


main_layout.addWidget(button)
text_layout.addWidget(dolar_label, alignment=Qt.AlignCenter)
text_layout.addWidget(euros_label, alignment=Qt.AlignCenter)

main_layout.addLayout(text_layout)

values_layout.addWidget(dolar_values, alignment=Qt.AlignCenter)
values_layout.addWidget(euros_values, alignment=Qt.AlignCenter)
main_layout.addLayout(values_layout)

precio_layout.addWidget(precio)
precio_layout.addWidget(button2)
main_layout.addLayout(precio_layout)

precios_layout.addWidget(dolar_precio, alignment=Qt.AlignCenter)
precios_layout.addWidget(euros_precio, alignment=Qt.AlignCenter)
main_layout.addLayout(precios_layout)



window.setLayout(main_layout)


def getValues():
    url = "https://ve.dolarapi.com/v1/cotizaciones"

    response = requests.get(url)
    data = response.json()

    dolar_values.setText(str(data[0]["promedio"]))
    euros_values.setText(str(data[1]["promedio"]))

def preciosCalc():
    dolar = float(dolar_values.text())
    euros = float(euros_values.text())

    valor = float(precio.text())

    dolarv = valor * dolar
    eurov = valor * euros

    dolar_precio.setText(str(dolarv))
    euros_precio.setText(str(eurov))

button.clicked.connect(getValues)
button2.clicked.connect(preciosCalc)
window.show()

app.exec_()