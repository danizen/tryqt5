#!/usr/bin/env python
import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QGridLayout,
    QLabel,
    QLineEdit,
)


class UsernamePassword(QWidget):

    def __init__(self):
        super().__init__()
        self.init_guts()

    def init_guts(self):
        self.resize(400, 150)
        self.move(300, 300)
        self.setWindowTitle('Chungus')

        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")

        usernameLabel = QLabel('Username')
        passwordLabel = QLabel('Password')
        usernameText = QLineEdit()
        passwordText = QLineEdit()

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        grid = QGridLayout()
        grid.addWidget(usernameLabel, 1, 0)
        grid.addWidget(usernameText, 1, 1)
        grid.addWidget(passwordLabel, 2, 0)
        grid.addWidget(passwordText, 2, 1)

        vbox = QVBoxLayout()
        vbox.addLayout(grid)
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        
        self.setLayout(vbox)


if __name__ == '__main__':
    app = QApplication([])
    w = UsernamePassword()
    w.show()
    sys.exit(app.exec_())
