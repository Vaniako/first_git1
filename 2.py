from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel,QVBoxLayout,QPushButton
from random import randint
def winers():
    a = randint(0,9)
    b = randint(0,9)
    if a == b:
        winer.setText(str(a))
        winer2.setText(str(b))
        text.setText('Ви виграли! Зіграйте знову')
    else:
        winer.setText(str(a))
        winer2.setText(str(b))
        text.setText('Ви програли! Зіграйте знову')
app = QApplication([])
win = QWidget()
text = QLabel('Натисни щоби взяти участь')
v1 = QVBoxLayout()
buttn = QPushButton('Випробувати удачу')
winer = QLabel('?')
winer2 = QLabel('?')
win.resize(500,300)
win.setWindowTitle('Лотерея')

v1.addWidget(text, alignment =Qt.AlignCenter)
v1.addWidget(winer, alignment=Qt.AlignCenter)
v1.addWidget(winer2, alignment=Qt.AlignCenter)
v1.addWidget(buttn, alignment=Qt.AlignCenter)
buttn.clicked.connect(winers)
win.setLayout(v1)


win.show()
app.exec_()