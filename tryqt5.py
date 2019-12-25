#!/usr/bin/env python
import sys
from argparse import ArgumentParser

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QGridLayout,
    QInputDialog,
    QLabel,
    QLineEdit,
)


class UsernamePasswordDialog(QWidget):

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
            print('"Escape" key was pressed')
            self.close()


class PinDialog(QWidget):

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

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        pinLabel = QLabel('PIN')
        pinText = QLineEdit()

        grid = QGridLayout()
        grid.addWidget(pinLabel, 1, 0)
        grid.addWidget(pinText, 1, 1)

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
            print('"Escape" key was pressed')
            self.close()


def username_password_example(opts):
    app = QApplication([])
    w = UsernamePasswordDialog()
    w.show()
    sys.exit(app.exec_())


def pin_example(opts):
    app = QApplication([])
    w = PinDialog()
    w.show()
    sys.exit(app.exec_())

def create_parser(prog_name):
    parser = ArgumentParser(prog=prog_name, description='Run Qt5 examples', epilog='You are a chungus')
    sp = parser.add_subparsers(help='commands')
    passwd = sp.add_parser('password', help='username/password dialog')
    passwd.set_defaults(func=username_password_example)
    pin = sp.add_parser('pin', help='collect user pin')
    pin.set_defaults(func=pin_example)
    return parser


def main():
    parser = create_parser(sys.argv[0])
    opts = parser.parse_args(sys.argv[1:])
    if not hasattr(opts, 'func'):
        parser.print_help()
        sys.exit(1)
    opts.func(opts)


if __name__ == '__main__':
    main()
