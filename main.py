from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import*
import sys

def evt_btn_cliced():
    win.setWindowTitle(len.text())

app = QApplication(sys.argv)

win = QDialog()
win.setWindowTitle('LOL')
win.setGeometry(801,200,500,500)

len = QLineEdit('Defolt text',win)
len.move(180,190)

btn = QPushButton('Ubdate Window Title',win)
btn.move(170,240)
btn.resize(150,50)
btn.clicked.connect(evt_btn_cliced)

win.show()
sys.exit(app.exec_())

win.show()
sys.exit(app.exec_())
