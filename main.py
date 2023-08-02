import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
import os
import start_ui


def main():
    app = QApplication(sys.argv)
    # mainwindow = start_ui.StartGUI()
    # widget = QtWidgets.QStackedWidget()
    # widget.addWidget(mainwindow)
    # widget.setWindowTitle('image-transfer-to-USB')
    # widget.show()
    window = start_ui.StartGUI()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
