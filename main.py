from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget
from random import choice,shuffle
# Create class
class Qwestion():
    def __init__(self,qwestion,answer,wrong_answer1,wrong_answer2,wrong_answer3):
        self.qwestion = qwestion
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3
        self.isAsking = True
        self.count_ask = 0
        self.corect_ans = 0

    def corect_answer(self):
        self.count_ask += 1
        self.corect_ans += 1
    def asked(self):
        self.corect_ans += 1




app = QApplication([])
import main_window as wind
import menu_window as manu_w
# Set answer
def ans():
    global chose
    chose = choice(qwestions)

    wind.lb_qwes.setText(chose.qwestion)
    wind.lb_rigth_ans.setText(chose.answer)

    shuffle(rbs)
    rbs[0].setText(chose.answer)
    rbs[1].setText(chose.wrong_answer1)
    rbs[2].setText(chose.wrong_answer2)
    rbs[3].setText(chose.wrong_answer3)
# Check Button cleced
def show_result():
    if wind.butn_Ok.text() == 'Відповісти':
        wind.ans_Group.show()
        wind.rb_Group.hide()

        wind.butn_Ok.setText('Наступне запитання')
    else :
        ans()
        wind.butn_Ok.setText('Відповісти')
        wind.rb_Group.show()
        wind.ans_Group.hide()
        
        wind.rb_Button_Group.setExclusive(False)
        for rb in rbs:
            rb.setChecked(False)
        wind.rb_Button_Group.setExclusive(True)
# Check corect answer
def check_result():
    k_down = 3
    for i in rbs:
        if i.isChecked():
            if i.text() == qwestions[0].answer:
                k_down = 1
            else:
                k_down = 0
    if k_down == 1:
        wind.lb_result.setText('Вірно')
    elif k_down == 0:
        wind.lb_result.setText('Не вірно')
def menu():
    manu_w.window.show()
    wind.win.hide()
def back():
    wind.win.show()
    manu_w.window.hide()    
# list qwestions
q1 = Qwestion('мама','mother','m1','m2','m3')

qwestions = [q1]



rbs = [wind.rb_1,wind.rb_2,wind.rb_3,wind.rb_4]

ans()
wind.butn_Ok.clicked.connect(check_result)
wind.butn_Ok.clicked.connect(show_result)
wind.butn_manu.clicked.connect(menu)
manu_w.btn_back.clicked.connect(back)
wind.win.show()
app.exec_()