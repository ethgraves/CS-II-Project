from PyQt6.QtWidgets import *
from gui import *

class Logic(QMainWindow, Ui_MainWindow):
    nums_in_box = ['-']
    math_function = []
    nums_for_calculation = []
    function_count = 0

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.button_0.clicked.connect(lambda: self.push_0())
        self.button_1.clicked.connect(lambda: self.push_1())
        self.button_2.clicked.connect(lambda: self.push_2())
        self.button_3.clicked.connect(lambda: self.push_3())
        self.button_4.clicked.connect(lambda: self.push_4())
        self.button_5.clicked.connect(lambda: self.push_5())
        self.button_6.clicked.connect(lambda: self.push_6())
        self.button_7.clicked.connect(lambda: self.push_7())
        self.button_8.clicked.connect(lambda: self.push_8())
        self.button_9.clicked.connect(lambda: self.push_9())
        self.button_plus.clicked.connect(lambda: self.plus())
        self.button_subtract.clicked.connect(lambda: self.subtract())
        self.button_multiply.clicked.connect(lambda: self.multiply())
        self.button_divide.clicked.connect(lambda: self.divide())
        self.button_equal.clicked.connect(lambda: self.equal())

# -----------------------------------------------------------------------------
# Checks
    def length_check(self):
        if len(Logic.nums_in_box) <= 26:
            return True
        else:
            return False

    def box_empty_check(self):
        if (Logic.nums_in_box[0] == '-') or (Logic.nums_in_box[0] == 0 and Logic.math_function >= 1) or (Logic.nums_in_box[0] == 1 and Logic.math_function >= 1):
            return True
        else:
            return False

# -----------------------------------------------------------------
# Calculator Buttons
# ------------------
# Numbers
    def push_0(self):
        if self.box_empty_check() == True:
            self.label_calculations.setText('0')
            Logic.nums_in_box[0] = '0'
        else:
            if self.length_check() == True:
                self.label_calculations.setText(f'{''.join(Logic.nums_in_box)}0')
                Logic.nums_in_box.append('0')

    def push_1(self):
        if self.box_empty_check() == True:
            self.label_calculations.setText('1')
            Logic.nums_in_box[0] = '1'
        else:
            if self.length_check() == True:
                self.label_calculations.setText(f'{''.join(Logic.nums_in_box)}1')
                Logic.nums_in_box.append('1')

    def push_2(self):
        if self.box_empty_check() == True:
            self.label_calculations.setText('2')
            Logic.nums_in_box[0] = '2'
        else:
            if self.length_check() == True:
                self.label_calculations.setText(f'{''.join(Logic.nums_in_box)}2')
                Logic.nums_in_box.append('2')

    def push_3(self):
        if self.box_empty_check() == True:
            self.label_calculations.setText('3')
            Logic.nums_in_box[0] = '3'
        else:
            if self.length_check() == True:
                self.label_calculations.setText(f'{''.join(Logic.nums_in_box)}3')
                Logic.nums_in_box.append('3')

    def push_4(self):
        if self.box_empty_check() == True:
            self.label_calculations.setText('4')
            Logic.nums_in_box[0] = '4'
        else:
            if self.length_check() == True:
                self.label_calculations.setText(f'{''.join(Logic.nums_in_box)}4')
                Logic.nums_in_box.append('4')

    def push_5(self):
        if self.box_empty_check() == True:
            self.label_calculations.setText('5')
            Logic.nums_in_box[0] = '5'
        else:
            if self.length_check() == True:
                self.label_calculations.setText(f'{''.join(Logic.nums_in_box)}5')
                Logic.nums_in_box.append('5')

    def push_6(self):
        if self.box_empty_check() == True:
            self.label_calculations.setText('6')
            Logic.nums_in_box[0] = '6'
        else:
            if self.length_check() == True:
                self.label_calculations.setText(f'{''.join(Logic.nums_in_box)}6')
                Logic.nums_in_box.append('6')

    def push_7(self):
        if self.box_empty_check() == True:
            self.label_calculations.setText('7')
            Logic.nums_in_box[0] = '7'
        else:
            if self.length_check() == True:
                self.label_calculations.setText(f'{''.join(Logic.nums_in_box)}7')
                Logic.nums_in_box.append('7')

    def push_8(self):
        if self.box_empty_check() == True:
            self.label_calculations.setText('8')
            Logic.nums_in_box[0] = '8'
        else:
            if self.length_check() == True:
                self.label_calculations.setText(f'{''.join(Logic.nums_in_box)}8')
                Logic.nums_in_box.append('8')

    def push_9(self):
        if self.box_empty_check() == True:
            self.label_calculations.setText('9')
            Logic.nums_in_box[0] = '9'
        else:
            if self.length_check() == True:
                self.label_calculations.setText(f'{''.join(Logic.nums_in_box)}9')
                Logic.nums_in_box.append('9')

# ------------------
# Math Functions
    def plus(self):
        Logic.nums_for_calculation.append(int(''.join(Logic.nums_in_box)))
        Logic.nums_in_box = ['-']
        Logic.math_function = 'plus'
        Logic.function_count += 1

    def subtract(self):
        Logic.nums_for_calculation.append(int(''.join(Logic.nums_in_box)))
        Logic.nums_in_box = ['-']
        Logic.math_function = 'subtract'
        Logic.function_count += 1

    def multiply(self):
        Logic.nums_for_calculation.append(int(''.join(Logic.nums_in_box)))
        Logic.nums_in_box = ['-']
        Logic.math_function = 'multiply'
        Logic.function_count += 1

    def divide(self):
        Logic.nums_for_calculation.append(int(''.join(Logic.nums_in_box)))
        Logic.nums_in_box = ['-']
        Logic.math_function = 'divide'
        Logic.function_count += 1

    def equal(self):
        Logic.function_count = 0
        Logic.nums_for_calculation.append(int(''.join(Logic.nums_in_box)))
        Logic.nums_in_box = ['-']
        if Logic.math_function == 'plus':
            if len(Logic.nums_for_calculation) == 1:
                Logic.nums_for_calculation.append(0)
            self.label_calculations.setText(f'= {sum(Logic.nums_for_calculation)}')
            Logic.nums_for_calculation = []
        elif Logic.math_function == 'subtract':
            if len(Logic.nums_for_calculation) == 1:
                Logic.nums_for_calculation.append(0)
            self.label_calculations.setText(f'= {Logic.nums_for_calculation[0] - Logic.nums_for_calculation[1]}')
            Logic.nums_for_calculation = []
        elif Logic.math_function == 'multiply':
            if len(Logic.nums_for_calculation) == 1:
                Logic.nums_for_calculation.append(1)
            self.label_calculations.setText(f'= {Logic.nums_for_calculation[0] * Logic.nums_for_calculation[1]}')
            Logic.nums_for_calculation = []
        elif Logic.math_function == 'divide':
            if len(Logic.nums_for_calculation) == 1:
                Logic.nums_for_calculation.append(1)
            self.label_calculations.setText(f'= {(Logic.nums_for_calculation[0] / Logic.nums_for_calculation[1]):.2f}')
            Logic.nums_for_calculation = []

# ------------------
# Mode Button
    def mode(self):
        if self.radioButton.setEnabled(False):
            self.radioButton.setEnabled(True)
        else:
            self.radioButton.setEnabled(False)