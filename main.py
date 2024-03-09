from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout,QPushButton

app = QApplication([])
win = QWidget()

win.setWindowTitle('Перша програма')
win.resize(500,500)
win.move(700,250)

winer = QLabel('s')

len = QVBoxLayout()
len.addWidget(winer, alignment=Qt.AlignCenter)





win.show()
app.exec_()