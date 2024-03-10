from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel,QVBoxLayout,QPushButton
from random import randint
def winers():
    a = randint(1,100)
    winer.setText(str(a))
    text.setText('Переможець:')
app = QApplication([])
win = QWidget()
text = QLabel('Натисни щоб дізнатися переможця')
v1 = QVBoxLayout()
buttn = QPushButton('Згенеруіати')
winer = QLabel('?')
win.resize(500,300)
win.setWindowTitle('Визначник переможця')

v1.addWidget(text, alignment =Qt.AlignCenter)
v1.addWidget(winer, alignment=Qt.AlignCenter)
v1.addWidget(buttn, alignment=Qt.AlignCenter)
buttn.clicked.connect(winers)
win.setLayout(v1)


win.show()
app.exec_()