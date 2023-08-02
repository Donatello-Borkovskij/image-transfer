from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
from PyQt5.uic import loadUi
import image_frame


class StartGUI(QtWidgets.QDialog):
    def __init__(self):
        super(StartGUI, self).__init__()
        loadUi('start_dialog.ui', self)

        self.setFixedWidth(450)
        self.setFixedHeight(300)

        self.browse1.clicked.connect(self.browse_files_source)
        self.browse2.clicked.connect(self.browse_files_dest)
        self.start.clicked.connect(self.start_pressed)
        self.show()

    def browse_files_source(self):
        dir_name = QFileDialog.getExistingDirectory(self, 'Choose directory', 'C:/')
        self.image_dir.setText(dir_name)
        print(self.image_dir.text())

    def browse_files_dest(self):
        dir_name = QFileDialog.getExistingDirectory(self, 'Choose directory', 'C:/')
        self.destination_dir.setText(dir_name)

    def start_pressed(self):
        image_frame.ImageFrame()
        # self.close()
