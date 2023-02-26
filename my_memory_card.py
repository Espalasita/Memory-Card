from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton, QPushButton, QGroupBox, QButtonGroup
from time import sleep
from random import shuffle,randint

class Question():
    def __init__(self, q, r, w1, w2, w3):
        self.question = q
        self.right = r
        self.wrong1 = w1
        self.wrong2 = w2
        self.wrong3 = w3
questions_list = []
questions_list.append(Question('Which color does not appear on the American flag?', 'Green', 'Red', 'White', 'Blue'))
questions_list.append(Question('A traditional residence of the Yakut people', 'Urasa', 'Yurt', 'Igloo', 'Hut'))
q1=Question('The national language of Brazil', 'Portuguese', 'Brazilian', 'Spanish', 'Italian')
questions_list.append(q1)
questions_list.append(Question("What is the name of Earth's largest ocean?", 'Pacific', 'Afrika', 'Atlantic Ocean', 'Asia Ocean'))
questions_list.append(Question("When did the Dodo bird go extinct?", '1662', '1945', '1771', '1290'))
questions_list.append(Question("Which Country owns the most Nuclear Warheads?", 'USA', 'China', 'France', 'Russia'))
questions_list.append(Question("Who, in 1903, was the first woman to win a Nobel Prize?", 'Madam Curies', 'Joe Biden', 'Shane Kawl', 'Auntie Kelly'))
questions_list.append(Question("What element does the chemical symbol Au stand for?", 'Gold', 'Helium', 'Tantalum', 'Aluminum'))
questions_list.append(Question("I’m tall when I’m young, and I’m short when I’m old. What am I?", 'A Candle', 'A deformed child', 'A Tree', 'A Sponge'))
questions_list.append(Question("The shooting of whom, in 1914, started World War I?", 'Archduke Franz Ferdinand', 'Charles Martel', 'Adolf Hitler', 'The Bishop of Normandy'))
app = QApplication([])

'''Interface for the Memory Card Application'''
lb_Question = QLabel('Which nationality does not exist') #Question
btn_OK = QPushButton('Answer') #Answer button

radioGroup = QGroupBox('Answer Options')
rbtn_1 = QRadioButton('Enets')
rbtn_2 = QRadioButton('Smurfs')
rbtn_3 = QRadioButton('Chulyms')
rbtn_4 = QRadioButton('Aleuts')
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

choiceGroup = QButtonGroup()
choiceGroup.addButton(rbtn_1)
choiceGroup.addButton(rbtn_2)
choiceGroup.addButton(rbtn_3)
choiceGroup.addButton(rbtn_4)

layout_ans = QHBoxLayout()
layout_ans_left = QVBoxLayout()
layout_ans_left.addWidget(rbtn_1)
layout_ans_left.addWidget(rbtn_2)

layout_ans_right = QVBoxLayout()
layout_ans_right.addWidget(rbtn_3)
layout_ans_right.addWidget(rbtn_4)

layout_ans.addLayout(layout_ans_left)
layout_ans.addLayout(layout_ans_right)
radioGroup.setLayout(layout_ans)
#radioGroup.hide()

labelGroup = QGroupBox('Test Result')
layout_label = QVBoxLayout()
lb_TrueFalse = QLabel('True/False')
lb_answer = QLabel('Correct Answer!')
layout_label.addWidget(lb_TrueFalse)
layout_label.addWidget(lb_answer)
labelGroup.setLayout(layout_label)
labelGroup.hide()

main_layout = QVBoxLayout()
main_layout.addWidget(lb_Question, alignment= Qt.AlignCenter)
main_layout.addWidget(radioGroup)

main_layout.addWidget(labelGroup)
main_layout.addWidget(btn_OK, alignment= Qt.AlignCenter)

def show_result():
    radioGroup.hide()
    labelGroup.show()
    btn_OK.setText('Next Question')

def show_question():
    labelGroup.hide()
    radioGroup.show()
    btn_OK.setText('Answer')
    choiceGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    choiceGroup.setExclusive(True)

def ask(q: Question):
    lb_Question.setText(q.question)
    lb_answer.setText(q.right)
    shuffle(answers)
    answers[0].setText(q.right)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    show_question()

def check_answer():
    if answers[0].isChecked():
        lb_TrueFalse.setText('Correct!')
        window.score += 1
    else:
        lb_TrueFalse.setText('Incorrect!')
    show_result()
    print('Statistics')
    print('Total questions answered:', window.total)
    print('Total questions answered correctly:', window.score)
    print('Rating', (window.score/window.total)*100)

def next_question():
    window.total += 1
    cur_question = randint(0, len(questions_list)-1)
    q = questions_list[cur_question]
    ask(q)

def start_test():
    if btn_OK.text() == 'Answer':
        check_answer()
    else:
        next_question()

window = QWidget()
window.setWindowTitle('Memo Card')
window.resize(400, 200)
window.setLayout(main_layout)

btn_OK.clicked.connect(start_test)
window.score = 0
window.total = 0
next_question()

window.show()
app.exec()