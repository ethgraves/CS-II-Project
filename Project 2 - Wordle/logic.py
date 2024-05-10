from PyQt6.QtWidgets import *
from gui import *
import random

# TODO:
'''
- Add user system
- Add winning/losing functions

'''

class Logic(QMainWindow, Ui_MainWindow):
    guess = [
        ['-', '-', '-', '-', '-']
    ]
    colors = ['-', '-', '-', '-', '-']
    letters = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']

    word_to_guess_determiner = 0
    word_to_guess_letters = []
    word_to_guess_letters_copy = []

    num_guesses = 0

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.__box = 0

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
        self.pushButton_login.clicked.connect(lambda: self.login())
        self.pushButton_playAgain.clicked.connect(lambda: self.play_again())

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

    def word_to_guess(self):
        random.seed = random.randint(0,100000)
        with open('words_to_guess.txt', 'r') as file:
            all_words = file.readlines()
            word_to_guess = all_words[random.randint(0, (len(all_words) - 1))]
            word_to_guess = word_to_guess[0:-1]

            word_to_guess_letters = [*word_to_guess]
            word_to_guess_letters_copy = word_to_guess_letters[:]

        return word_to_guess_letters, word_to_guess_letters_copy

    def get_word_to_guess(self):
        if Logic.word_to_guess_determiner == 0:
            word_to_guess_letters, word_to_guess_letters_copy = self.word_to_guess()
            Logic.word_to_guess_letters = word_to_guess_letters
            Logic.word_to_guess_letters_copy = word_to_guess_letters_copy
            Logic.word_to_guess_determiner = 1
        else:
            word_to_guess_letters = Logic.word_to_guess_letters
            word_to_guess_letters_copy = Logic.word_to_guess_letters_copy

        self.label_debug.setText(''.join(word_to_guess_letters))
        return word_to_guess_letters, word_to_guess_letters_copy



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
            self.label_valid_or_not.setStyleSheet('background-color: rgb(255, 255, 255)')
            return False
        else:
            with open('valid_words.txt', 'r') as file:
                valid_words = file.read()
                word = ''.join(word)
                word = word.lower()
                if word in valid_words:
                    self.label_valid_or_not.setText('')
                    self.label_valid_or_not.setStyleSheet('background-color:')
                    return True
                else:
                    self.label_valid_or_not.setText('Not a valid word')
                    self.label_valid_or_not.setStyleSheet('background-color: rgb(255, 255, 255)')
                    return False

    def check_for_win(self, word_letters):
        print(1)
        print(Logic.word_to_guess_letters)
        Logic.guess[-1] = [x.lower() for x in Logic.guess[-1]]
        for a in range(0, 5):
            print(2)
            if Logic.guess[-1][a] == Logic.word_to_guess_letters[a]:
                print(3)
                Logic.colors[a] = 'background-color: rgb(0, 255, 0)'
                print(4)
                self.coloring_keyboard(Logic.guess[-1][a], 'background-color: rgb(0, 255, 0)')
                Logic.guess[-1][a] = '-'
                Logic.word_to_guess_letters[a] = '~'
        for b in range(0, 5):
            if Logic.guess[-1][b] in Logic.word_to_guess_letters:
                for c in range(0, 5):
                    if Logic.guess[-1][b] == Logic.word_to_guess_letters[c]:
                        Logic.colors[b] = 'background-color: rgb(255, 255, 0)'
                        self.coloring_keyboard(Logic.guess[-1][b], 'background-color: rgb(255, 255, 0)')
                        Logic.guess[-1][b] = '-'
                        Logic.word_to_guess_letters[c] = '~'
        for d in range(0 ,5):
            if Logic.colors[d] == '-':
                Logic.colors[d] = 'background-color: rgb(150, 150, 150)'
                self.coloring_keyboard(Logic.guess[-1][d], 'background-color: rgb(150, 150, 150)')
        Logic.word_to_guess_letters = Logic.word_to_guess_letters_copy[:]

    def coloring_keyboard(self, letter, color):
        if color == 'background-color: rgb(0, 255, 0)':
            if letter == 'q':
                if letter in Logic.letters:
                    self.pushButton_Q.setStyleSheet(color)
                    Logic.letters.remove('q')
            elif letter == 'w':
                if letter in Logic.letters:
                    self.pushButton_W.setStyleSheet(color)
                    Logic.letters.remove('w')
            elif letter == 'e':
                if letter in Logic.letters:
                    self.pushButton_E.setStyleSheet(color)
                    Logic.letters.remove('e')
            elif letter == 'r':
                if letter in Logic.letters:
                    self.pushButton_R.setStyleSheet(color)
                    Logic.letters.remove('r')
            elif letter == 't':
                if letter in Logic.letters:
                    self.pushButton_T.setStyleSheet(color)
                    Logic.letters.remove('t')
            elif letter == 'y':
                if letter in Logic.letters:
                    self.pushButton_Y.setStyleSheet(color)
                    Logic.letters.remove('y')
            elif letter == 'u':
                if letter in Logic.letters:
                    self.pushButton_U.setStyleSheet(color)
                    Logic.letters.remove('u')
            elif letter == 'i':
                if letter in Logic.letters:
                    self.pushButton_I.setStyleSheet(color)
                    Logic.letters.remove('i')
            elif letter == 'o':
                if letter in Logic.letters:
                    self.pushButton_O.setStyleSheet(color)
                    Logic.letters.remove('o')
            elif letter == 'p':
                if letter in Logic.letters:
                    self.pushButton_P.setStyleSheet(color)
                    Logic.letters.remove('p')
            elif letter == 'a':
                if letter in Logic.letters:
                    self.pushButton_A.setStyleSheet(color)
                    Logic.letters.remove('a')
            elif letter == 's':
                if letter in Logic.letters:
                    self.pushButton_S.setStyleSheet(color)
                    Logic.letters.remove('s')
            elif letter == 'd':
                if letter in Logic.letters:
                    self.pushButton_D.setStyleSheet(color)
                    Logic.letters.remove('d')
            elif letter == 'f':
                if letter in Logic.letters:
                    self.pushButton_F.setStyleSheet(color)
                    Logic.letters.remove('f')
            elif letter == 'g':
                if letter in Logic.letters:
                    self.pushButton_G.setStyleSheet(color)
                    Logic.letters.remove('g')
            elif letter == 'h':
                if letter in Logic.letters:
                    self.pushButton_H.setStyleSheet(color)
                    Logic.letters.remove('h')
            elif letter == 'j':
                if letter in Logic.letters:
                    self.pushButton_J.setStyleSheet(color)
                    Logic.letters.remove('j')
            elif letter == 'k':
                if letter in Logic.letters:
                    self.pushButton_K.setStyleSheet(color)
                    Logic.letters.remove('k')
            elif letter == 'l':
                if letter in Logic.letters:
                    self.pushButton_L.setStyleSheet(color)
                    Logic.letters.remove('l')
            elif letter == 'z':
                if letter in Logic.letters:
                    self.pushButton_Z.setStyleSheet(color)
                    Logic.letters.remove('z')
            elif letter == 'x':
                if letter in Logic.letters:
                    self.pushButton_X.setStyleSheet(color)
                    Logic.letters.remove('x')
            elif letter == 'c':
                if letter in Logic.letters:
                    self.pushButton_C.setStyleSheet(color)
                    Logic.letters.remove('c')
            elif letter == 'v':
                if letter in Logic.letters:
                    self.pushButton_V.setStyleSheet(color)
                    Logic.letters.remove('v')
            elif letter == 'b':
                if letter in Logic.letters:
                    self.pushButton_B.setStyleSheet(color)
                    Logic.letters.remove('b')
            elif letter == 'n':
                if letter in Logic.letters:
                    self.pushButton_N.setStyleSheet(color)
                    Logic.letters.remove('n')
            elif letter == 'm':
                if letter in Logic.letters:
                    self.pushButton_M.setStyleSheet(color)
                    Logic.letters.remove('m')
        elif color == 'background-color: rgb(255, 255, 0)':
            if letter == 'q':
                if letter in Logic.letters:
                    self.pushButton_Q.setStyleSheet(color)
                    Logic.letters.remove('q')
            elif letter == 'w':
                if letter in Logic.letters:
                    self.pushButton_W.setStyleSheet(color)
                    Logic.letters.remove('w')
            elif letter == 'e':
                if letter in Logic.letters:
                    self.pushButton_E.setStyleSheet(color)
                    Logic.letters.remove('e')
            elif letter == 'r':
                if letter in Logic.letters:
                    self.pushButton_R.setStyleSheet(color)
                    Logic.letters.remove('r')
            elif letter == 't':
                if letter in Logic.letters:
                    self.pushButton_T.setStyleSheet(color)
                    Logic.letters.remove('t')
            elif letter == 'y':
                if letter in Logic.letters:
                    self.pushButton_Y.setStyleSheet(color)
                    Logic.letters.remove('y')
            elif letter == 'u':
                if letter in Logic.letters:
                    self.pushButton_U.setStyleSheet(color)
                    Logic.letters.remove('u')
            elif letter == 'i':
                if letter in Logic.letters:
                    self.pushButton_I.setStyleSheet(color)
                    Logic.letters.remove('i')
            elif letter == 'o':
                if letter in Logic.letters:
                    self.pushButton_O.setStyleSheet(color)
                    Logic.letters.remove('o')
            elif letter == 'p':
                if letter in Logic.letters:
                    self.pushButton_P.setStyleSheet(color)
                    Logic.letters.remove('p')
            elif letter == 'a':
                if letter in Logic.letters:
                    self.pushButton_A.setStyleSheet(color)
                    Logic.letters.remove('a')
            elif letter == 's':
                if letter in Logic.letters:
                    self.pushButton_S.setStyleSheet(color)
                    Logic.letters.remove('s')
            elif letter == 'd':
                if letter in Logic.letters:
                    self.pushButton_D.setStyleSheet(color)
                    Logic.letters.remove('d')
            elif letter == 'f':
                if letter in Logic.letters:
                    self.pushButton_F.setStyleSheet(color)
                    Logic.letters.remove('f')
            elif letter == 'g':
                if letter in Logic.letters:
                    self.pushButton_G.setStyleSheet(color)
                    Logic.letters.remove('g')
            elif letter == 'h':
                if letter in Logic.letters:
                    self.pushButton_H.setStyleSheet(color)
                    Logic.letters.remove('h')
            elif letter == 'j':
                if letter in Logic.letters:
                    self.pushButton_J.setStyleSheet(color)
                    Logic.letters.remove('j')
            elif letter == 'k':
                if letter in Logic.letters:
                    self.pushButton_K.setStyleSheet(color)
                    Logic.letters.remove('k')
            elif letter == 'l':
                if letter in Logic.letters:
                    self.pushButton_L.setStyleSheet(color)
                    Logic.letters.remove('l')
            elif letter == 'z':
                if letter in Logic.letters:
                    self.pushButton_Z.setStyleSheet(color)
                    Logic.letters.remove('z')
            elif letter == 'x':
                if letter in Logic.letters:
                    self.pushButton_X.setStyleSheet(color)
                    Logic.letters.remove('x')
            elif letter == 'c':
                if letter in Logic.letters:
                    self.pushButton_C.setStyleSheet(color)
                    Logic.letters.remove('c')
            elif letter == 'v':
                if letter in Logic.letters:
                    self.pushButton_V.setStyleSheet(color)
                    Logic.letters.remove('v')
            elif letter == 'b':
                if letter in Logic.letters:
                    self.pushButton_B.setStyleSheet(color)
                    Logic.letters.remove('b')
            elif letter == 'n':
                if letter in Logic.letters:
                    self.pushButton_N.setStyleSheet(color)
                    Logic.letters.remove('n')
            elif letter == 'm':
                if letter in Logic.letters:
                    self.pushButton_M.setStyleSheet(color)
                    Logic.letters.remove('m')
        elif color == 'background-color: rgb(150, 150, 150)':
            if letter == 'q':
                if letter in Logic.letters:
                    self.pushButton_Q.setStyleSheet(color)
                    Logic.letters.remove('q')
            elif letter == 'w':
                if letter in Logic.letters:
                    self.pushButton_W.setStyleSheet(color)
                    Logic.letters.remove('w')
            elif letter == 'e':
                if letter in Logic.letters:
                    self.pushButton_E.setStyleSheet(color)
                    Logic.letters.remove('e')
            elif letter == 'r':
                if letter in Logic.letters:
                    self.pushButton_R.setStyleSheet(color)
                    Logic.letters.remove('r')
            elif letter == 't':
                if letter in Logic.letters:
                    self.pushButton_T.setStyleSheet(color)
                    Logic.letters.remove('t')
            elif letter == 'y':
                if letter in Logic.letters:
                    self.pushButton_Y.setStyleSheet(color)
                    Logic.letters.remove('y')
            elif letter == 'u':
                if letter in Logic.letters:
                    self.pushButton_U.setStyleSheet(color)
                    Logic.letters.remove('u')
            elif letter == 'i':
                if letter in Logic.letters:
                    self.pushButton_I.setStyleSheet(color)
                    Logic.letters.remove('i')
            elif letter == 'o':
                if letter in Logic.letters:
                    self.pushButton_O.setStyleSheet(color)
                    Logic.letters.remove('o')
            elif letter == 'p':
                if letter in Logic.letters:
                    self.pushButton_P.setStyleSheet(color)
                    Logic.letters.remove('p')
            elif letter == 'a':
                if letter in Logic.letters:
                    self.pushButton_A.setStyleSheet(color)
                    Logic.letters.remove('a')
            elif letter == 's':
                if letter in Logic.letters:
                    self.pushButton_S.setStyleSheet(color)
                    Logic.letters.remove('s')
            elif letter == 'd':
                if letter in Logic.letters:
                    self.pushButton_D.setStyleSheet(color)
                    Logic.letters.remove('d')
            elif letter == 'f':
                if letter in Logic.letters:
                    self.pushButton_F.setStyleSheet(color)
                    Logic.letters.remove('f')
            elif letter == 'g':
                if letter in Logic.letters:
                    self.pushButton_G.setStyleSheet(color)
                    Logic.letters.remove('g')
            elif letter == 'h':
                if letter in Logic.letters:
                    self.pushButton_H.setStyleSheet(color)
                    Logic.letters.remove('h')
            elif letter == 'j':
                if letter in Logic.letters:
                    self.pushButton_J.setStyleSheet(color)
                    Logic.letters.remove('j')
            elif letter == 'k':
                if letter in Logic.letters:
                    self.pushButton_K.setStyleSheet(color)
                    Logic.letters.remove('k')
            elif letter == 'l':
                if letter in Logic.letters:
                    self.pushButton_L.setStyleSheet(color)
                    Logic.letters.remove('l')
            elif letter == 'z':
                if letter in Logic.letters:
                    self.pushButton_Z.setStyleSheet(color)
                    Logic.letters.remove('z')
            elif letter == 'x':
                if letter in Logic.letters:
                    self.pushButton_X.setStyleSheet(color)
                    Logic.letters.remove('x')
            elif letter == 'c':
                if letter in Logic.letters:
                    self.pushButton_C.setStyleSheet(color)
                    Logic.letters.remove('c')
            elif letter == 'v':
                if letter in Logic.letters:
                    self.pushButton_V.setStyleSheet(color)
                    Logic.letters.remove('v')
            elif letter == 'b':
                if letter in Logic.letters:
                    self.pushButton_B.setStyleSheet(color)
                    Logic.letters.remove('b')
            elif letter == 'n':
                if letter in Logic.letters:
                    self.pushButton_N.setStyleSheet(color)
                    Logic.letters.remove('n')
            elif letter == 'm':
                if letter in Logic.letters:
                    self.pushButton_M.setStyleSheet(color)
                    Logic.letters.remove('m')



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

    def clear_game(self):
        self.label_R1_C1.setText('')
        self.label_R1_C2.setText('')
        self.label_R1_C3.setText('')
        self.label_R1_C4.setText('')
        self.label_R1_C5.setText('')
        self.label_R2_C1.setText('')
        self.label_R2_C2.setText('')
        self.label_R2_C3.setText('')
        self.label_R2_C4.setText('')
        self.label_R2_C5.setText('')
        self.label_R3_C1.setText('')
        self.label_R3_C2.setText('')
        self.label_R3_C3.setText('')
        self.label_R3_C4.setText('')
        self.label_R3_C5.setText('')
        self.label_R4_C1.setText('')
        self.label_R4_C2.setText('')
        self.label_R4_C3.setText('')
        self.label_R4_C4.setText('')
        self.label_R4_C5.setText('')
        self.label_R5_C1.setText('')
        self.label_R5_C2.setText('')
        self.label_R5_C3.setText('')
        self.label_R5_C4.setText('')
        self.label_R5_C5.setText('')
        self.label_R6_C1.setText('')
        self.label_R6_C2.setText('')
        self.label_R6_C3.setText('')
        self.label_R6_C4.setText('')
        self.label_R6_C5.setText('')
        self.label_R1_C1.setStyleSheet('background-color: rgb(255, 255, 255)')
        self.label_R1_C2.setStyleSheet('background-color: rgb(255, 255, 255)')
        self.label_R1_C3.setStyleSheet('background-color: rgb(255, 255, 255)')
        self.label_R1_C4.setStyleSheet('background-color: rgb(255, 255, 255)')
        self.label_R1_C5.setStyleSheet('background-color: rgb(255, 255, 255)')
        self.label_R2_C1.setStyleSheet('background-color: rgb(255, 255, 255)')
        self.label_R2_C2.setStyleSheet('background-color: rgb(255, 255, 255)')
        self.label_R2_C3.setStyleSheet('background-color: rgb(255, 255, 255)')
        self.label_R2_C4.setStyleSheet('background-color: rgb(255, 255, 255)')
        self.label_R2_C5.setStyleSheet('background-color: rgb(255, 255, 255)')
        self.label_R3_C1.setStyleSheet('background-color: rgb(255, 255, 255)')
        self.label_R3_C2.setStyleSheet('background-color: rgb(255, 255, 255)')
        self.label_R3_C3.setStyleSheet('background-color: rgb(255, 255, 255)')
        self.label_R3_C4.setStyleSheet('background-color: rgb(255, 255, 255)')
        self.label_R3_C5.setStyleSheet('background-color: rgb(255, 255, 255)')
        self.label_R4_C1.setStyleSheet('background-color: rgb(255, 255, 255)')
        self.label_R4_C2.setStyleSheet('background-color: rgb(255, 255, 255)')
        self.label_R4_C3.setStyleSheet('background-color: rgb(255, 255, 255)')
        self.label_R4_C4.setStyleSheet('background-color: rgb(255, 255, 255)')
        self.label_R4_C5.setStyleSheet('background-color: rgb(255, 255, 255)')
        self.label_R5_C1.setStyleSheet('background-color: rgb(255, 255, 255)')
        self.label_R5_C2.setStyleSheet('background-color: rgb(255, 255, 255)')
        self.label_R5_C3.setStyleSheet('background-color: rgb(255, 255, 255)')
        self.label_R5_C4.setStyleSheet('background-color: rgb(255, 255, 255)')
        self.label_R5_C5.setStyleSheet('background-color: rgb(255, 255, 255)')
        self.label_R6_C1.setStyleSheet('background-color: rgb(255, 255, 255)')
        self.label_R6_C2.setStyleSheet('background-color: rgb(255, 255, 255)')
        self.label_R6_C3.setStyleSheet('background-color: rgb(255, 255, 255)')
        self.label_R6_C4.setStyleSheet('background-color: rgb(255, 255, 255)')
        self.label_R6_C5.setStyleSheet('background-color: rgb(255, 255, 255)')
        self.pushButton_Q.setStyleSheet('background-color: rgb(255, 255, 255)')
        self.pushButton_W.setStyleSheet('background-color: rgb(255, 255, 255)')
        self.pushButton_E.setStyleSheet('background-color: rgb(255, 255, 255)')
        self.pushButton_R.setStyleSheet('background-color: rgb(255, 255, 255)')
        self.pushButton_T.setStyleSheet('background-color: rgb(255, 255, 255)')
        self.pushButton_Y.setStyleSheet('background-color: rgb(255, 255, 255)')
        self.pushButton_U.setStyleSheet('background-color: rgb(255, 255, 255)')
        self.pushButton_I.setStyleSheet('background-color: rgb(255, 255, 255)')
        self.pushButton_O.setStyleSheet('background-color: rgb(255, 255, 255)')
        self.pushButton_P.setStyleSheet('background-color: rgb(255, 255, 255)')
        self.pushButton_A.setStyleSheet('background-color: rgb(255, 255, 255)')
        self.pushButton_S.setStyleSheet('background-color: rgb(255, 255, 255)')
        self.pushButton_D.setStyleSheet('background-color: rgb(255, 255, 255)')
        self.pushButton_F.setStyleSheet('background-color: rgb(255, 255, 255)')
        self.pushButton_G.setStyleSheet('background-color: rgb(255, 255, 255)')
        self.pushButton_H.setStyleSheet('background-color: rgb(255, 255, 255)')
        self.pushButton_J.setStyleSheet('background-color: rgb(255, 255, 255)')
        self.pushButton_K.setStyleSheet('background-color: rgb(255, 255, 255)')
        self.pushButton_L.setStyleSheet('background-color: rgb(255, 255, 255)')
        self.pushButton_Z.setStyleSheet('background-color: rgb(255, 255, 255)')
        self.pushButton_X.setStyleSheet('background-color: rgb(255, 255, 255)')
        self.pushButton_C.setStyleSheet('background-color: rgb(255, 255, 255)')
        self.pushButton_V.setStyleSheet('background-color: rgb(255, 255, 255)')
        self.pushButton_B.setStyleSheet('background-color: rgb(255, 255, 255)')
        self.pushButton_N.setStyleSheet('background-color: rgb(255, 255, 255)')
        self.pushButton_M.setStyleSheet('background-color: rgb(255, 255, 255)')
        self.set_box(0)
        Logic.letters = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
        Logic.guess = [['-', '-', '-', '-', '-']]
        Logic.colors = ['-', '-', '-', '-', '-']
        Logic.num_guesses = 0


    def delete(self):
        for c in range(4, -1, -1):
            if Logic.guess[-1][c] != '-':
                Logic.guess[-1][c] = '-'
                self.adding_letter('', self.get_box())
                self.set_box(-1)
                break

    def enter(self):
        Logic.num_guesses += 1
        self.word_letters = Logic.guess[-1]
        if self.valid_word_check(self.word_letters) == True:
            win = self.check_for_win(self.word_letters)
            #TODO: Add events for winning and losing
            if Logic.colors[0] == Logic.colors[1] == Logic.colors[2] == Logic.colors[3] == Logic.colors[4] == 'background-color: rgb(0, 255, 0)':
                self.stackedWidget.setCurrentIndex(2)
                self.label_win_lose.setText('You Win!')
            else:
                if Logic.num_guesses == 6:
                    self.stackedWidget.setCurrentIndex(2)
                    self.label_win_lose.setText('You Lose!')
            self.coloring()

            Logic.guess.append(['-', '-', '-', '-', '-'])
            self.set_box(5)

# --------------------------------------------------------------------------------------------------------------------------------------------------
    # Home Page
    def guest(self):
        self.stackedWidget.setCurrentIndex(1)
        self.get_word_to_guess()

    def login(self):
        pass

# --------------------------------------------------------------------------------------------------------------------------------------------------
    # Game Page
    def letter_guess(self, letter):
        box = self.letters_check(letter)
        self.adding_letter(letter, box)

# --------------------------------------------------------------------------------------------------------------------------------------------------
    # Results Page
    def play_again(self):
        self.stackedWidget.setCurrentIndex(1)
        self.clear_game()
        Logic.word_to_guess_determiner = 0
        self.get_word_to_guess()