#создай приложение для запоминания информации
from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QButtonGroup, QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QRadioButton, QGroupBox
from random import randint
class Question():
    def __init__(self, q, r_ans, w_ans1, w_ans2, w_ans3):
        self.q = q
        self.r_ans = r_ans
        self.w_ans1 = w_ans1
        self.w_ans2 = w_ans2
        self.w_ans3 = w_ans3
spisok = list()
serf = Question('Где живёт мой кот','дома','у бабушки','на улице','в лесу')
spisok.append(serf)
serf = Question('Сколько лет В.В.Путину?','70','60','100','45')
spisok.append(serf)
serf = Question('Какой город является столицкй России?','Москва','Вашинктон','Киев','Минск')
spisok.append(serf)
serf = Question('Где живут пингвины?','Антарктида','Арктика','Мехсика','Атлантида')
spisok.append(serf)
z = 0
app = QApplication([])
window = QWidget()
window.setWindowTitle('Memory Card')
window.resize(500,500)
question = QLabel('Какой национальности не существует?')
box1 = QGroupBox('Варианты ответов')
group = QButtonGroup()
ans1 = QRadioButton('Энцы')
ans2 = QRadioButton('Смурфы')
ans3 = QRadioButton('Чулымцы')
ans4 = QRadioButton('Алеуты')
group.addButton(ans1)
group.addButton(ans2)
group.addButton(ans3)
group.addButton(ans4)
h1 = QHBoxLayout()
h1.addWidget(ans1, alignment = Qt.AlignLeft)
h1.addWidget(ans3, alignment = Qt.AlignLeft)
h2 = QHBoxLayout()
h2.addWidget(ans2, alignment = Qt.AlignLeft)
h2.addWidget(ans4, alignment = Qt.AlignLeft)
v1 = QVBoxLayout()
v1.addLayout(h1)
v1.addLayout(h2)
box1.setLayout(v1)
box2 = QGroupBox('Результат теста')
label1 = QLabel('Правильно/Неправильно')
label2 = QLabel('Правильный ответ')
v3 = QVBoxLayout()
v3.addWidget(label1, alignment = Qt.AlignLeft)
v3.addWidget(label2, alignment = Qt.AlignCenter)
box2.setLayout(v3)
box2.hide()
button = QPushButton('Ответить')
v2 = QVBoxLayout()
v2.addWidget(question, alignment = Qt.AlignVCenter)
v2.addWidget(box1, alignment = Qt.AlignVCenter)
v2.addWidget(box2, alignment = Qt.AlignVCenter)
v2.addWidget(button, alignment = Qt.AlignVCenter)
def show_result():
    box1.hide()
    box2.show()
    button.setText('Следующий вопрос')
    check_answer()
def show_question():
    box1.show()
    box2.hide()
    button.setText('Ответить')
    group.setExclusive(False)
    ans1.setChecked(False)
    ans2.setChecked(False)
    ans3.setChecked(False)
    ans4.setChecked(False)
    group.setExclusive(True)
    global z
    ask(spisok[z])
    if z < len(spisok)-1:
        z += 1
    else:
        z = 0
def start_test():
    if button.text() == 'Ответить':
        show_result()
    else:
        show_question()
def ask(q: Question):
    question.setText(q.q)
    rand = randint(0,3)
    if rand == 0:
        ans1.setText(q.r_ans)
        ans2.setText(q.w_ans1)
        ans3.setText(q.w_ans2)
        ans4.setText(q.w_ans3)
    elif rand == 1:
        ans2.setText(q.r_ans)
        ans1.setText(q.w_ans1)
        ans3.setText(q.w_ans2)
        ans4.setText(q.w_ans3)
    elif rand == 2:
        ans3.setText(q.r_ans)
        ans2.setText(q.w_ans1)
        ans1.setText(q.w_ans2)
        ans4.setText(q.w_ans3)
    elif rand == 3:
        ans4.setText(q.r_ans)
        ans2.setText(q.w_ans1)
        ans3.setText(q.w_ans2)
        ans1.setText(q.w_ans3)
    label2.setText(q.r_ans)
def check_answer():
    if label2.text() == group.checkedButton().text():
        label1.setText('Правильно')
    else:
        label2.setText('Неверно')


button.clicked.connect(start_test)
ask(spisok[z])
z += 1
window.setLayout(v2)
window.show()
app.exec_()
