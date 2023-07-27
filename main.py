import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
from PyQt5.uic import loadUi
import os

source_dir = ''
destination_dir = ''


class StartGUI(QtWidgets.QMainWindow):
    def __init__(self):
        super(StartGUI, self).__init__()
        loadUi('start.ui', self)

        self.setFixedWidth(450)
        self.setFixedHeight(300)

        self.browse1.clicked.connect(self.browsefiles_source)
        self.browse2.clicked.connect(self.browsefiles_dest)

    def browsefiles_source(self):
        dir_name = QFileDialog.getExistingDirectory(self, 'Choose directory', '')
        self.image_dir.setText(dir_name)

    def browsefiles_dest(self):
        dir_name = QFileDialog.getExistingDirectory(self, 'Choose directory', 'C:/')
        self.destination_dir.setText(dir_name)


def main():
    app = QApplication(sys.argv)
    mainwindow = StartGUI()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(mainwindow)
    widget.setWindowTitle('image-transfer-to-USB')
    widget.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
