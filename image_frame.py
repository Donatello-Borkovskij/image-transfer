from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
from PyQt5.uic import loadUi


class ImageFrame(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('image-transfer-to-USB')
        self.showMaximized()
