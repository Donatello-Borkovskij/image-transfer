import sys
from PyQt5.QtWidgets import QApplication
import start_ui


def main():
    app = QApplication(sys.argv)
    window = start_ui.StartGUI()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
