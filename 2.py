from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel,QVBoxLayout,QRadioButton,QHBoxLayout,QMessageBox
from random import randint

def show_lose():
    ms = QMessageBox()
    ms.setText('Пощастить іншим разом!')
    ms.exec_()
def show_win():
    ms = QMessageBox()
    ms.setText('Ви виграли зустріч з творцями каналу!')
    ms.exec_()

app = QApplication([])
win = QWidget()
win.setWindowTitle('Конкурс від Crazy People')
win.resize(400,200)
l_qves = QLabel('Як звали першого ютуб-блогера, який набрав 100000000 підписників')
r_bt_3 =   QRadioButton('SlivkiShow')
r_bt_2 = QRadioButton('Рет і Лінк')
r_bt_1 = QRadioButton('PewDiePie')
r_bt_4 = QRadioButton('TheBrianMaps')
r_bt_5 = QRadioButton('Mister Max')
r_bt_6 = QRadioButton('EeOneGuy')

v_main = QVBoxLayout()
h_1 =QHBoxLayout()
h_2 = QHBoxLayout()
h_3 = QHBoxLayout()
h_4 = QHBoxLayout()

h_3.addWidget(l_qves, alignment= Qt.AlignCenter)
h_1.addWidget(r_bt_1, alignment= Qt.AlignCenter)
h_1.addWidget(r_bt_2, alignment= Qt.AlignCenter)
h_2.addWidget(r_bt_3, alignment= Qt.AlignCenter)
h_2.addWidget(r_bt_4, alignment= Qt.AlignCenter)
h_4.addWidget(r_bt_5, alignment= Qt.AlignCenter)
h_4.addWidget(r_bt_6, alignment= Qt.AlignCenter)

v_main.addLayout(h_3)
v_main.addLayout(h_1)
v_main.addLayout(h_2)
v_main.addLayout(h_4)


r_bt_1.clicked.connect(show_win)
r_bt_3.clicked.connect(show_lose)
r_bt_2.clicked.connect(show_lose)
r_bt_4.clicked.connect(show_lose)
r_bt_5.clicked.connect(show_lose)
r_bt_6.clicked.connect(show_lose)

win.setLayout(v_main) 

win.show()
app.exec_()
