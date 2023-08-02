from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
from PyQt5.uic import loadUi


class ImageFrame(QtWidgets.QDialog):
    def __init__(self):
        self.isMaximized()
