from PyQt6.QtWidgets import *
from gui import *

class Logic(QMainWindow, Ui_MainWindow):
    guess = [
        ['-', '-', '-', '-', '-']
    ]

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Home Page
        self.pushButton_guest.clicked.connect(lambda: self.guest())

        # Game Page
        self.pushButton_Q.clicked.connect(lambda: self.letter_guess('Q'))
        self.pushButton_W.clicked.connect(lambda: self.letter_guess('W'))
        self.pushButton_E.clicked.connect(lambda: self.letter_guess('E'))
        self.pushButton_R.clicked.connect(lambda: self.letter_guess('R'))
        self.pushButton_T.clicked.connect(lambda: self.letter_guess('T'))
        self.pushButton_Y.clicked.connect(lambda: self.letter_guess('Y'))
        self.pushButton_U.clicked.connect(lambda: self.letter_guess('U'))
        self.pushButton_I.clicked.connect(lambda: self.letter_guess('I'))
        self.pushButton_O.clicked.connect(lambda: self.letter_guess('O'))
        self.pushButton_P.clicked.connect(lambda: self.letter_guess('P'))
        self.pushButton_A.clicked.connect(lambda: self.letter_guess('A'))
        self.pushButton_S.clicked.connect(lambda: self.letter_guess('S'))
        self.pushButton_D.clicked.connect(lambda: self.letter_guess('D'))
        self.pushButton_F.clicked.connect(lambda: self.letter_guess('F'))
        self.pushButton_G.clicked.connect(lambda: self.letter_guess('G'))
        self.pushButton_H.clicked.connect(lambda: self.letter_guess('H'))
        self.pushButton_J.clicked.connect(lambda: self.letter_guess('J'))
        self.pushButton_K.clicked.connect(lambda: self.letter_guess('K'))
        self.pushButton_L.clicked.connect(lambda: self.letter_guess('L'))
        self.pushButton_Z.clicked.connect(lambda: self.letter_guess('Z'))
        self.pushButton_X.clicked.connect(lambda: self.letter_guess('X'))
        self.pushButton_C.clicked.connect(lambda: self.letter_guess('C'))
        self.pushButton_V.clicked.connect(lambda: self.letter_guess('V'))
        self.pushButton_B.clicked.connect(lambda: self.letter_guess('B'))
        self.pushButton_N.clicked.connect(lambda: self.letter_guess('N'))
        self.pushButton_M.clicked.connect(lambda: self.letter_guess('M'))



    # Checks
    def letters_check(self, letter):
        box = 0
        for r in range(len(Logic.guess)):
            for c in range(5):
                box += 1
                if Logic.guess[r][c] == '-':
                    Logic.guess[r][c] = letter
                    return box

    def adding_letter(self, letter, box):
        if box == 1:
            self.label_R1_C1.setText(letter)
        elif box == 2:
            self.label_R1_C2.setText(letter)
        elif box == 3:
            self.label_R1_C3.setText(letter)
        elif box == 4:
            self.label_R1_C4.setText(letter)
        elif box == 5:
            self.label_R1_C5.setText(letter)


    # Home Page
    def guest(self):
        self.stackedWidget.setCurrentIndex(1)


    # Game Page
    def letter_guess(self, letter):
        box = self.letters_check(letter)
        self.adding_letter(letter, box)
