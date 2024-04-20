from PyQt6.QtWidgets import *
from gui import *

class Logic(QMainWindow, Ui_MainWindow):
    nums_in_box = ['-']

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.button_0.clicked.connect(lambda : self.push_0())
        self.button_1.clicked.connect(lambda : self.push_1())
        self.button_2.clicked.connect(lambda : self.push_2())


    def length_check(self):
        if len(Logic.nums_in_box) <= 26:
            return True
        else:
            return False

    def box_empty_check(self):
        if Logic.nums_in_box[0] == '-':
            return True
        else:
            return False

    def push_0(self):
        if self.box_empty_check() == True:
            self.label_calculations.setText('0')
            Logic.nums_in_box[0] = '0'
        else:
            if self.length_check() == True:
                self.label_calculations.setText(f'0{''.join(Logic.nums_in_box)}')
                Logic.nums_in_box.append('0')
        print(Logic.nums_in_box)

    def push_1(self):
        if self.box_empty_check() == True:
            self.label_calculations.setText('1')
            Logic.nums_in_box[0] = '1'
        else:
            if self.length_check() == True:
                self.label_calculations.setText(f'1{''.join(Logic.nums_in_box)}')
                Logic.nums_in_box.append('1')
        print(Logic.nums_in_box)

    def push_2(self):
        if self.box_empty_check() == True:
            self.label_calculations.setText('2')
            Logic.nums_in_box[0] = '2'
        else:
            if self.length_check() == True:
                self.label_calculations.setText(f'2{''.join(Logic.nums_in_box)}')
                Logic.nums_in_box.append('2')
        print(Logic.nums_in_box)