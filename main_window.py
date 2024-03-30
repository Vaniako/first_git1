from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QWidget, QLabel,QVBoxLayout,
    QRadioButton,QHBoxLayout,QMessageBox,
    QGroupBox, QButtonGroup,QSpinBox,
    QPushButton
)
# window
win = QWidget()
win.setWindowTitle('Memory Card')
win.resize(600,500)
# Button
butn_manu = QPushButton('Меню')
butn_Sleep = QPushButton('Відпочити')
butn_Ok = QPushButton('Відповісти')
# Spin
sp_Sleep = QSpinBox()
sp_Sleep.setValue(30)
# RadioButton and Groups
rb_Button_Group = QButtonGroup()
rb_Group = QGroupBox('Варіанти відповідей')

rb_1 = QRadioButton('1')
rb_2 = QRadioButton('2')
rb_3 = QRadioButton('3')
rb_4 = QRadioButton('4')

rb_Button_Group.addButton(rb_1)
rb_Button_Group.addButton(rb_2)
rb_Button_Group.addButton(rb_3)
rb_Button_Group.addButton(rb_4)
# Lable
lb_qwes = QLabel('Питання')
# Layout for Group answers
hl__Main_ans = QHBoxLayout()
vl_ans1 = QVBoxLayout()
vl_ans2 = QVBoxLayout()
# Connect radiobatton to vlayout
vl_ans1.addWidget(rb_1)
vl_ans1.addWidget(rb_2)

vl_ans2.addWidget(rb_3)
vl_ans2.addWidget(rb_4)
# Conect Vboxes to Hbox
hl__Main_ans.addLayout(vl_ans1)
hl__Main_ans.addLayout(vl_ans2)
# Connect Main Hlayout to window of Group
rb_Group.setLayout(hl__Main_ans)
# =============================================
# Answer window
ans_Group = QGroupBox('Результат тесту')
lb_result = QLabel('Результат')
lb_rigth_ans = QLabel('Відповідь')

lb_layout = QVBoxLayout()
# Connect lable to layout
lb_layout.addWidget(lb_result, alignment=(Qt.AlignLeft | Qt.AlignTop))
lb_layout.addWidget(lb_rigth_ans, alignment=Qt.AlignCenter,stretch=2)
# Hide windiw and connect layout to window
ans_Group.setLayout(lb_layout)
ans_Group.hide()
# MAIN layouts
MHL_1 = QHBoxLayout()
MHL_2 = QHBoxLayout()
MHL_3 = QHBoxLayout()
MHL_4 = QHBoxLayout()
MVL = QVBoxLayout()

MHL_1.addWidget(butn_manu)
MHL_1.addStretch(1)
MHL_1.addWidget(butn_Sleep)
MHL_1.addWidget(sp_Sleep)
MHL_1.addWidget(QLabel('хвилин'))

MHL_2.addWidget(lb_qwes,alignment=(Qt.AlignHCenter | Qt.AlignVCenter))

MHL_3.addWidget(rb_Group)
MHL_3.addWidget(ans_Group)

MHL_4.addStretch(1)
MHL_4.addWidget(butn_Ok,stretch=2)
MHL_4.addStretch(1)

MVL.addLayout(MHL_1,stretch=1)
MVL.addLayout(MHL_2,stretch=2)
MVL.addLayout(MHL_3,stretch=8)
MVL.addStretch(1)
MVL.addLayout(MHL_4)
MVL.addStretch(1)
MVL.setSpacing(5)
win.setLayout(MVL)

