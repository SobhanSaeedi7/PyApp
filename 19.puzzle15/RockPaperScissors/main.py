import sys
from random import randint
from functools import partial
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.scissors.setText("🤞")
        self.ui.paper.setText("🖐")
        self.ui.rock.setText("✊")

        self.round = 0
        self.player_score = 0
        self.computer_score = 0

        self.ui.scissors.clicked.connect(partial(self.play, 1))
        self.ui.paper.clicked.connect(partial(self.play, 2))
        self.ui.rock.clicked.connect(partial(self.play, 3))
        self.ui.newgame.clicked.connect(self.new_game)

    def play(self, choice):
        computer_choice = randint(1, 3)
        if computer_choice == 1 and choice == 2:
            self.computer_score += 1
            self.round += 1
            self.ui.player.setText("🖐")
            self.ui.computer.setText("🤞")
            self.ui.result.setText(">")
            self.ui.copmputer_score.setText(f"Score : {self.computer_score}")
            self.ui.round.setText(f"Round : {self.round}")

        elif computer_choice == 2 and choice == 3:
            self.computer_score += 1
            self.round += 1
            self.ui.player.setText("✊")
            self.ui.computer.setText("🖐")
            self.ui.result.setText(">")
            self.ui.copmputer_score.setText(f"Score : {self.computer_score}")
            self.ui.round.setText(f"Round : {self.round}")

        elif computer_choice == 3 and choice == 1:
            self.computer_score += 1
            self.round += 1
            self.ui.player.setText("🤞")
            self.ui.computer.setText("✊")
            self.ui.result.setText(">")
            self.ui.copmputer_score.setText(f"Score : {self.computer_score}")
            self.ui.round.setText(f"Round : {self.round}")

        elif computer_choice == 1 and choice == 3:
            self.player_score += 1
            self.round += 1
            self.ui.player.setText("✊")
            self.ui.computer.setText("🤞")
            self.ui.result.setText("<")
            self.ui.player_score.setText(f"Score : {self.player_score}")
            self.ui.round.setText(f"Round : {self.round}")

        elif computer_choice == 2 and choice == 1:
            self.player_score += 1
            self.round += 1
            self.ui.player.setText("🤞")
            self.ui.computer.setText("🖐")
            self.ui.result.setText("<")
            self.ui.player_score.setText(f"Score : {self.player_score}")
            self.ui.round.setText(f"Round : {self.round}")

        elif computer_choice == 3 and choice == 2:
            self.player_score += 1
            self.round += 1
            self.ui.player.setText("🖐")
            self.ui.computer.setText("✊")
            self.ui.result.setText("<")
            self.ui.player_score.setText(f"Score : {self.player_score}")
            self.ui.round.setText(f"Round : {self.round}")

        else:
            if choice == 1:
                self.ui.player.setText("🤞")
                self.ui.computer.setText("🤞")
            elif choice == 2:
                self.ui.player.setText("🖐")
                self.ui.computer.setText("🖐") 
            elif choice == 3:
                self.ui.player.setText("✊")
                self.ui.computer.setText("✊")
            self.ui.result.setText("=")  
            self.ui.round.setText("Draw")


    def new_game(self):
        self.ui.round.setText("Round : 1")
        self.round = 0
        self.ui.computer.setText("")
        self.ui.copmputer_score.setText("Score : 0")
        self.computer_score = 0
        self.ui.player.setText("")
        self.ui.player_score.setText("Score : 0")
        self.player_score = 0
        self.ui.result.setText("N\nE\nW")

  


if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    app.exec()