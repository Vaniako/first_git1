from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLineEdit,QHBoxLayout,QVBoxLayout,QPushButton,QLabel
# Create window
window = QWidget()
window.setWindowTitle('Qmemori card')
window.resize(600,500)
# window.move(700,100)
# Create Lable
l_qwestion = QLabel('Введіть запитання:')
l_right_answer = QLabel('Введіть правельну відповідь:')
l_wrong_answer_1 = QLabel('Введіть першу хибну відповідь:')
l_wrong_answer_2 = QLabel('Введіть другу хибну відповідь:')
l_wrong_answer_3 = QLabel('Введіть третю хибну відповідь:')
l_wrong_answer_4 = QLabel('Введіть четверту хибну відповідь:')
l_statistic = QLabel('Статистика:')
l_statistic.setStyleSheet("font-size : 12pt; font-weight : bold; color : brown")
l_qwes = QLabel('')
# Create line Edit
ed_qwestion = QLineEdit('')
ed_right_answer = QLineEdit('')
ed_wrong_answer1 = QLineEdit('')
ed_wrong_answer2 = QLineEdit('')
ed_wrong_answer3 = QLineEdit('')
ed_wrong_answer4 = QLineEdit('')
# Create button
btn_add_qwestion = QPushButton('Додати')
btn_clear = QPushButton('Очистити')
btn_back = QPushButton('Назад')
# Create layout
vl_lable = QVBoxLayout()
vl_edit = QVBoxLayout()
hl_btn = QHBoxLayout()
hl_lay = QHBoxLayout()
vl_main = QVBoxLayout()
# Add to layout
vl_lable.addWidget(l_qwestion)
vl_lable.addWidget(l_right_answer)
vl_lable.addWidget(l_wrong_answer_1)
vl_lable.addWidget(l_wrong_answer_2)
vl_lable.addWidget(l_wrong_answer_3)
vl_lable.addWidget(l_wrong_answer_4)

vl_edit.addWidget(ed_qwestion)
vl_edit.addWidget(ed_right_answer)
vl_edit.addWidget(ed_wrong_answer1)
vl_edit.addWidget(ed_wrong_answer2)
vl_edit.addWidget(ed_wrong_answer3)
vl_edit.addWidget(ed_wrong_answer4)

hl_btn.addWidget(btn_add_qwestion)
hl_btn.addWidget(btn_clear)

hl_lay.addLayout(vl_lable)
hl_lay.addLayout(vl_edit)

vl_main.addLayout(hl_lay)

vl_main.addLayout(hl_btn)

vl_main.addWidget(l_statistic,alignment=Qt.AlignLeft)
vl_main.addWidget(l_qwes,alignment=Qt.AlignLeft)
vl_main.addWidget(btn_back)
# Add to window
window.setLayout(vl_main)