from PyQt6.QtWidgets import *
from gui import *
import random

class Logic(QMainWindow, Ui_MainWindow):
    guess = [
        ['-', '-', '-', '-', '-']
    ]
    colors = ['-', '-', '-', '-', '-']

    with open('words_to_guess.txt', 'r') as file:
        all_words = file.readlines()
        word_to_guess = all_words[random.randint(0, (len(all_words) - 1))]
        word_to_guess = word_to_guess[0:-1]

        word_to_guess_letters = [*word_to_guess]
        word_to_guess_letters_copy = word_to_guess_letters[:]

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.__box = 0

        # DEBUG for Testing
        self.label_debug.setText(Logic.word_to_guess)

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
        self.pushButton_DELETE.clicked.connect(lambda: self.delete())
        self.pushButton_ENTER.clicked.connect(lambda: self.enter())

# --------------------------------------------------------------------------------------------------------------------------------------------------
    # Getters and Setters
    def get_box(self):
        return self.__box

    def set_box(self, value):
        if value == 1:
            self.__box += value
        elif value == -1:
            self.__box -= 1
        elif value == 0:
            self.__box = value
        else:
            self.__box += value

# --------------------------------------------------------------------------------------------------------------------------------------------------
    # Checks
    def letters_check(self, letter):
        self.set_box(0)
        for c in range(5):
            self.set_box(1)
            if Logic.guess[-1][c] == '-':
                Logic.guess[-1][c] = letter
                return self.get_box()

    def valid_word_check(self, word):
        if '-' in Logic.guess[-1]:
            self.label_valid_or_not.setText('Too short')
            return False
        else:
            with open('valid_words.txt', 'r') as file:
                valid_words = file.read()
                word = ''.join(word)
                word = word.lower()
                if word in valid_words:
                    self.label_valid_or_not.setText('Valid word')
                    return True
                else:
                    self.label_valid_or_not.setText('Not a valid word')
                    return False

    def check_for_win(self, word_letters):
        Logic.guess[-1] = [x.lower() for x in Logic.guess[-1]]
        for a in range(0, 5):
            if Logic.guess[-1][a] == Logic.word_to_guess_letters[a]:
                Logic.colors[a] = 'background-color: rgb(0, 255, 0)'
                Logic.word_to_guess_letters[a] = '-'
        for b in range(0, 5):
            if Logic.guess[-1][b] in Logic.word_to_guess_letters:
                for c in range(0, 5):
                    if Logic.guess[-1][b] == Logic.word_to_guess_letters[c]:
                        Logic.colors[c] = 'background-color: rgb(255, 255, 0)'
                        Logic.word_to_guess_letters[c] = '-'
        for d in range(0 ,5):
            if Logic.word_to_guess_letters[d] != '-':
                Logic.colors[d] = 'background-color: rgb(150, 150, 150)'
        Logic.word_to_guess_letters = Logic.word_to_guess_letters_copy[:]
        print(Logic.word_to_guess_letters)
        print(Logic.colors)

    def coloring(self):
        if len(Logic.guess) == 1:
            self.label_R1_C1.setStyleSheet(Logic.colors[0])
            self.label_R1_C2.setStyleSheet(Logic.colors[1])
            self.label_R1_C3.setStyleSheet(Logic.colors[2])
            self.label_R1_C4.setStyleSheet(Logic.colors[3])
            self.label_R1_C5.setStyleSheet(Logic.colors[4])
        elif len(Logic.guess) == 2:
            self.label_R2_C1.setStyleSheet(Logic.colors[0])
            self.label_R2_C2.setStyleSheet(Logic.colors[1])
            self.label_R2_C3.setStyleSheet(Logic.colors[2])
            self.label_R2_C4.setStyleSheet(Logic.colors[3])
            self.label_R2_C5.setStyleSheet(Logic.colors[4])
        elif len(Logic.guess) == 3:
            self.label_R3_C1.setStyleSheet(Logic.colors[0])
            self.label_R3_C2.setStyleSheet(Logic.colors[1])
            self.label_R3_C3.setStyleSheet(Logic.colors[2])
            self.label_R3_C4.setStyleSheet(Logic.colors[3])
            self.label_R3_C5.setStyleSheet(Logic.colors[4])
        elif len(Logic.guess) == 4:
            self.label_R4_C1.setStyleSheet(Logic.colors[0])
            self.label_R4_C2.setStyleSheet(Logic.colors[1])
            self.label_R4_C3.setStyleSheet(Logic.colors[2])
            self.label_R4_C4.setStyleSheet(Logic.colors[3])
            self.label_R4_C5.setStyleSheet(Logic.colors[4])
        elif len(Logic.guess) == 5:
            self.label_R5_C1.setStyleSheet(Logic.colors[0])
            self.label_R5_C2.setStyleSheet(Logic.colors[1])
            self.label_R5_C3.setStyleSheet(Logic.colors[2])
            self.label_R5_C4.setStyleSheet(Logic.colors[3])
            self.label_R5_C5.setStyleSheet(Logic.colors[4])
        elif len(Logic.guess) == 6:
            self.label_R6_C1.setStyleSheet(Logic.colors[0])
            self.label_R6_C2.setStyleSheet(Logic.colors[1])
            self.label_R6_C3.setStyleSheet(Logic.colors[2])
            self.label_R6_C4.setStyleSheet(Logic.colors[3])
            self.label_R6_C5.setStyleSheet(Logic.colors[4])
        Logic.colors = ['-', '-', '-', '-', '-']

# --------------------------------------------------------------------------------------------------------------------------------------------------
    # Functions
    def shifting_box(self, box):
        if len(Logic.guess) == 2 and self.get_box() <= 5:
            self.set_box(5)
        elif len(Logic.guess) == 3 and self.get_box() <= 10:
            self.set_box(10)
        elif len(Logic.guess) == 4 and self.get_box() <= 15:
            self.set_box(15)
        elif len(Logic.guess) == 5 and self.get_box() <= 20:
            self.set_box(20)
        elif len(Logic.guess) == 6 and self.get_box() <= 25:
            self.set_box(25)
        return self.get_box()


    def adding_letter(self, letter, box):
        box = self.shifting_box(box)
        print(Logic.guess)
        print(box)
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
        elif box == 6:
            self.label_R2_C1.setText(letter)
        elif box == 7:
            self.label_R2_C2.setText(letter)
        elif box == 8:
            self.label_R2_C3.setText(letter)
        elif box == 9:
            self.label_R2_C4.setText(letter)
        elif box == 10:
            self.label_R2_C5.setText(letter)
        elif box == 11:
            self.label_R3_C1.setText(letter)
        elif box == 12:
            self.label_R3_C2.setText(letter)
        elif box == 13:
            self.label_R3_C3.setText(letter)
        elif box == 14:
            self.label_R3_C4.setText(letter)
        elif box == 15:
            self.label_R3_C5.setText(letter)
        elif box == 16:
            self.label_R4_C1.setText(letter)
        elif box == 17:
            self.label_R4_C2.setText(letter)
        elif box == 18:
            self.label_R4_C3.setText(letter)
        elif box == 19:
            self.label_R4_C4.setText(letter)
        elif box == 20:
            self.label_R4_C5.setText(letter)
        elif box == 21:
            self.label_R5_C1.setText(letter)
        elif box == 22:
            self.label_R5_C2.setText(letter)
        elif box == 23:
            self.label_R5_C3.setText(letter)
        elif box == 24:
            self.label_R5_C4.setText(letter)
        elif box == 25:
            self.label_R5_C5.setText(letter)
        elif box == 26:
            self.label_R6_C1.setText(letter)
        elif box == 27:
            self.label_R6_C2.setText(letter)
        elif box == 28:
            self.label_R6_C3.setText(letter)
        elif box == 29:
            self.label_R6_C4.setText(letter)
        elif box == 30:
            self.label_R6_C5.setText(letter)

    def delete(self):
        for c in range(4, -1, -1):
            if Logic.guess[-1][c] != '-':
                Logic.guess[-1][c] = '-'
                self.adding_letter('', self.get_box())
                self.set_box(-1)
                break

    def enter(self):
        self.word_letters = Logic.guess[-1]
        if self.valid_word_check(self.word_letters) == True:
            win = self.check_for_win(self.word_letters)
            #TODO: Add events for winning and losing
            if win == False:
                pass
            else:
                pass
            self.coloring()

            Logic.guess.append(['-', '-', '-', '-', '-'])
            self.set_box(5)

# --------------------------------------------------------------------------------------------------------------------------------------------------
    # Home Page
    def guest(self):
        self.stackedWidget.setCurrentIndex(1)

# --------------------------------------------------------------------------------------------------------------------------------------------------
    # Game Page
    def letter_guess(self, letter):
        box = self.letters_check(letter)
        self.adding_letter(letter, box)