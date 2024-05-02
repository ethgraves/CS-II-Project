from PyQt6.QtWidgets import *
from gui import *

class Logic(QMainWindow, Ui_MainWindow):
    guess = [
        ['-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', '-']
    ]

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Home Page
        self.pushButton_guest.clicked.connect(lambda: self.guest())

        # Game Page
        self.pushButton_Q.clicked.connect(lambda: self.letter_guess('Q'))

    # Home Page
    def guest(self):
        self.stackedWidget.setCurrentIndex(1)


    # Game Page
    def letter_guess(self, letter):
        for r in range(len(Logic.guess)):
            for c in range(5):
                if Logic.guess[r][c] == '-':
                    Logic.guess[r][c] = letter
                    self.label_R1_C1.setText(letter)