from PyQt6.QtWidgets import *
from gui import *

class Logic(QMainWindow, Ui_MainWindow):
    nums_in_box = ['-']
    math_function = ''
    nums_for_calculation = []
    area_or_volume = 0
    divide_by_zero = False
    divide_determiner = False

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
        self.radio_area.clicked.connect(lambda: self.area())
        self.radio_volume.clicked.connect(lambda: self.volume())
        self.radio_square_cube.clicked.connect(lambda: self.square_cube())
        self.radio_rectangle_cuboid.clicked.connect(lambda: self.rectangle_cuboid())
        self.radio_circle_sphere.clicked.connect(lambda: self.circle_sphere())
        self.radio_triangle_pyramid.clicked.connect(lambda: self.triangle_pyramid())
        self.radio_equilateral_cone.clicked.connect(lambda: self.equilateral_cone())
        self.radio_hypotenuse_cylinder.clicked.connect(lambda: self.hypotenuse_cylinder())
        self.pushButton_submit.clicked.connect(lambda: self.submit())
        self.button_clear.clicked.connect(lambda: self.clear())
        self.button_del.clicked.connect(lambda: self.delete())
        self.button_decimal.clicked.connect(lambda: self.decimal())
        self.button_negative.clicked.connect(lambda: self.negative())

# -----------------------------------------------------------------------------
# Checks
    def length_check(self):
        if len(Logic.nums_in_box) <= 26:
            return True
        else:
            return False

    def box_empty_check(self):
        #if (Logic.nums_in_box[0] == '-') or (Logic.nums_in_box[0] == 0 and Logic.math_function >= 1) or (Logic.nums_in_box[0] == 1 and Logic.math_function >= 1):
        if Logic.nums_in_box[0] == '-':
            return True
        else:
            return False

    def area_or_volume_check(self):
        if self.radio_square_cube.isChecked():
            self.square_cube()
        elif self.radio_rectangle_cuboid.isChecked():
            self.rectangle_cuboid()
        elif self.radio_circle_sphere.isChecked():
            self.circle_sphere()
        elif self.radio_triangle_pyramid.isChecked():
            self.triangle_pyramid()
        elif self.radio_equilateral_cone.isChecked():
            self.equilateral_cone()
        elif self.radio_hypotenuse_cylinder.isChecked():
            self.hypotenuse_cylinder()

# -----------------------------------------------------------------
# Calculator Buttons
# ------------------
# Numbers
    def push_0(self):
        # print(Logic.nums_in_box)
        # print(Logic.nums_for_calculation)
        # print(Logic.math_function)
        # if Logic.math_function == 'divide':
        #     print('test')
        # print(Logic.nums_in_box)
        # print(Logic.nums_for_calculation)
        # print(Logic.math_function)
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
        Logic.math_function = ''
        Logic.nums_for_calculation.append(''.join(Logic.nums_in_box))
        Logic.nums_in_box = ['-']
        if len(Logic.nums_for_calculation) > 1:
            for x in range(0, len(Logic.nums_for_calculation)):
                if Logic.nums_for_calculation[x] == '-':
                    Logic.nums_for_calculation[x] = 0
            Logic.nums_for_calculation = [float(x) for x in Logic.nums_for_calculation]
            Logic.nums_for_calculation[0] = Logic.nums_for_calculation[0] + Logic.nums_for_calculation[1]
            Logic.nums_for_calculation = Logic.nums_for_calculation[:1:]
        Logic.math_function = 'plus'

    def subtract(self):
        Logic.math_function = ''
        Logic.nums_for_calculation.append(''.join(Logic.nums_in_box))
        Logic.nums_in_box = ['-']
        if len(Logic.nums_for_calculation) > 1:
            for x in range(0, len(Logic.nums_for_calculation)):
                if Logic.nums_for_calculation[x] == '-':
                    Logic.nums_for_calculation[x] = 0
            Logic.nums_for_calculation = [float(x) for x in Logic.nums_for_calculation]
            Logic.nums_for_calculation[0] = Logic.nums_for_calculation[0] - Logic.nums_for_calculation[1]
            Logic.nums_for_calculation = Logic.nums_for_calculation[:1:]
        Logic.math_function = 'subtract'

    def multiply(self):
        Logic.math_function = ''
        Logic.nums_for_calculation.append(''.join(Logic.nums_in_box))
        Logic.nums_in_box = ['-']
        if len(Logic.nums_for_calculation) > 1:
            for x in range(0, len(Logic.nums_for_calculation)):
                if Logic.nums_for_calculation[x] == '-':
                    Logic.nums_for_calculation[x] = 1
            Logic.nums_for_calculation = [float(x) for x in Logic.nums_for_calculation]
            Logic.nums_for_calculation[0] = Logic.nums_for_calculation[0] * Logic.nums_for_calculation[1]
            Logic.nums_for_calculation = Logic.nums_for_calculation[:1:]
        Logic.math_function = 'multiply'

    def divide(self):
        Logic.math_function = ''
        Logic.nums_for_calculation.append(''.join(Logic.nums_in_box))
        Logic.nums_in_box = ['-']
        if len(Logic.nums_for_calculation) > 1:
            for x in range(0, len(Logic.nums_for_calculation)):
                if Logic.nums_for_calculation[x] == '-':
                    Logic.nums_for_calculation[x] = 1
            Logic.nums_for_calculation = [float(x) for x in Logic.nums_for_calculation]
            # if Logic.nums_for_calculation[1] == 0:
            #     Logic.divide_by_zero = True
            # else:
            Logic.nums_for_calculation[0] = Logic.nums_for_calculation[0] / Logic.nums_for_calculation[1]
            Logic.nums_for_calculation = Logic.nums_for_calculation[:1:]
            Logic.math_function = 'divide'

    def equal(self):
        if Logic.math_function == 'plus':
            self.plus()
        elif Logic.math_function == 'subtract':
            self.subtract()
        elif Logic.math_function == 'multiply':
            self.multiply()
        elif Logic.math_function == 'divide':
            # FIXME
            # if Logic.divide_by_zero == True:
            #     self.label_calculations.setText(f'69')
            # else:
            self.divide()
        self.label_calculations.setText(f'= {Logic.nums_for_calculation[0]}')

# ------------------
# Addition Buttons

    def clear(self):
        Logic.nums_in_box = ['-']
        Logic.nums_for_calculation = []
        Logic.math_function = ''
        self.label_calculations.setText('')

    def delete(self):
        if Logic.nums_in_box[0] == '-':
            self.clear()
        else:
            Logic.nums_in_box.pop(-1)
            self.label_calculations.setText(f'{''.join(Logic.nums_in_box)}')

    def decimal(self):
        pass

    def negative(self):
        pass

# ------------------
# Area and Volume
    '''
    s = side, b = base, h = height, w = width, l = length, r = radius, p = pi
    Areas:
        Square: s * s
        Rectangle: b * h
        Circle: p * r^2
        Triangle: (b * h) / 2
        Equilateral Triangle: (sqrt(3) / 4) * s^2
        Hypotenuse: sqrt(b^2 + h^2)
    Volumes:
        Cube: s^3
        Cuboid: l * b * h
        Sphere: (4 / 3) * p * r^3
        Pyramid: (l * w * h) / 3
        Cone: (1 / 3) * p * r^2 * h
        Cylinder: p * r^2 * h
    '''
    def area(self):
        Logic.area_or_volume = 0
        self.area_or_volume_check()

    def volume(self):
        Logic.area_or_volume = 1
        self.area_or_volume_check()

    def square_cube(self):
        if Logic.area_or_volume == 0:
            self.label_top.setText('Side')
            self.lineEdit_top.setEnabled(True)
            self.label_middle.setText('')
            self.lineEdit_middle.setEnabled(False)
            self.label_bottom.setText('')
            self.lineEdit_bottom.setEnabled(False)
        elif Logic.area_or_volume == 1:
            self.label_top.setText('Side')
            self.lineEdit_top.setEnabled(True)
            self.label_middle.setText('')
            self.lineEdit_middle.setEnabled(False)
            self.label_bottom.setText('')
            self.lineEdit_bottom.setEnabled(False)

    def rectangle_cuboid(self):
        if Logic.area_or_volume == 0:
            self.label_top.setText('Base')
            self.lineEdit_top.setEnabled(True)
            self.label_middle.setText('Height')
            self.lineEdit_middle.setEnabled(True)
            self.label_bottom.setText('')
            self.lineEdit_bottom.setEnabled(False)
        elif Logic.area_or_volume == 1:
            self.label_top.setText('Length')
            self.lineEdit_top.setEnabled(True)
            self.label_middle.setText('Base')
            self.lineEdit_middle.setEnabled(True)
            self.label_bottom.setText('Height')
            self.lineEdit_bottom.setEnabled(True)

    def circle_sphere(self):
        if Logic.area_or_volume == 0:
            self.label_top.setText('Radius')
            self.lineEdit_top.setEnabled(True)
            self.label_middle.setText('')
            self.lineEdit_middle.setEnabled(False)
            self.label_bottom.setText('')
            self.lineEdit_bottom.setEnabled(False)
        elif Logic.area_or_volume == 1:
            self.label_top.setText('Radius')
            self.lineEdit_top.setEnabled(True)
            self.label_middle.setText('')
            self.lineEdit_middle.setEnabled(False)
            self.label_bottom.setText('')
            self.lineEdit_bottom.setEnabled(False)

    def triangle_pyramid(self):
        if Logic.area_or_volume == 0:
            self.label_top.setText('Base')
            self.lineEdit_top.setEnabled(True)
            self.label_middle.setText('Height')
            self.lineEdit_middle.setEnabled(True)
            self.label_bottom.setText('')
            self.lineEdit_bottom.setEnabled(False)
        elif Logic.area_or_volume == 1:
            self.label_top.setText('Length')
            self.lineEdit_top.setEnabled(True)
            self.label_middle.setText('Width')
            self.lineEdit_middle.setEnabled(True)
            self.label_bottom.setText('Height')
            self.lineEdit_bottom.setEnabled(True)

    def equilateral_cone(self):
        if Logic.area_or_volume == 0:
            self.label_top.setText('Side')
            self.lineEdit_top.setEnabled(True)
            self.label_middle.setText('')
            self.lineEdit_middle.setEnabled(False)
            self.label_bottom.setText('')
            self.lineEdit_bottom.setEnabled(False)
        elif Logic.area_or_volume == 1:
            self.label_top.setText('Radius')
            self.lineEdit_top.setEnabled(True)
            self.label_middle.setText('Height')
            self.lineEdit_middle.setEnabled(True)
            self.label_bottom.setText('')
            self.lineEdit_bottom.setEnabled(False)

    def hypotenuse_cylinder(self):
        if Logic.area_or_volume == 0:
            self.label_top.setText('Base')
            self.lineEdit_top.setEnabled(True)
            self.label_middle.setText('Height')
            self.lineEdit_middle.setEnabled(True)
            self.label_bottom.setText('')
            self.lineEdit_bottom.setEnabled(False)
        elif Logic.area_or_volume == 1:
            self.label_top.setText('Radius')
            self.lineEdit_top.setEnabled(True)
            self.label_middle.setText('Height')
            self.lineEdit_middle.setEnabled(True)
            self.label_bottom.setText('')
            self.lineEdit_bottom.setEnabled(False)

    def submit(self):
        #FIXME: Exceptions don't work
        if self.radio_square_cube.isChecked():
            side = self.lineEdit_top.text()
            while True:
                try:
                    side = float(side)
                except:
                    if side == '':
                        self.label_calculations.setText('One or more inputs are blank')
                    else:
                        self.label_calculations.setText('Enter a number for inputs')
                else:
                    break
            self.label_calculations.setText(f'Area = {side ** 2}')
        elif self.radio_rectangle_cuboid.isChecked():
            self.rectangle_cuboid()
        elif self.radio_circle_sphere.isChecked():
            self.circle_sphere()
        elif self.radio_triangle_pyramid.isChecked():
            self.triangle_pyramid()
        elif self.radio_equilateral_cone.isChecked():
            self.equilateral_cone()
        elif self.radio_hypotenuse_cylinder.isChecked():
            self.hypotenuse_cylinder()