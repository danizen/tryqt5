#!/usr/bin/env python
import sys
from PyQt5.QtCore import Qt
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
        okButton.clicked.connect(self.buttonClicked)
        cancelButton.clicked.connect(self.buttonClicked)

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

    def buttonClicked(self):
        button_text = self.sender().text()
        print('"{}" button was pressed'.format(button_text))
        self.close()


    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()


if __name__ == '__main__':
    app = QApplication([])
    w = UsernamePassword()
    w.show()
    sys.exit(app.exec_())
