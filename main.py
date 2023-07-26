from PyQt5.QtWidgets import *
from PyQt5 import uic


def main():
    app = QApplication([])
    window = QWidget()
    window.setWindowTitle("image-transfer-to-USB")

    window.showMaximized()
    app.exec_()


if __name__ == "__main__":
    main()