from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QVBoxLayout, QWidget, QLabel
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPixmap, QTransform
from PyQt5.QtCore import Qt
import sys


class ImageFrame(QtWidgets.QMainWindow):
    def __init__(self, images, dest_directory):
        super().__init__()

        self.image_paths = images
        self.current_image_index = 0
        self.directory = dest_directory

        self.setWindowTitle('image-transfer-to-USB')

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.image_label = QLabel(self)
        self.layout.addWidget(self.image_label)

        self.update_image()
        self.showMaximized()

    def update_image(self):
        pixmap = QPixmap(self.image_paths[self.current_image_index][0])

        max_width = self.central_widget.width()
        max_height = self.central_widget.height()

        transform = QTransform().rotate(90)
        rotated_pixmap = pixmap.transformed(transform, Qt.SmoothTransformation)

        scaled_pixmap = rotated_pixmap.scaled(max_width, max_height, Qt.KeepAspectRatio)

        self.image_label.setPixmap(scaled_pixmap)
        self.layout.setAlignment(Qt.AlignCenter)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Left:
            self.current_image_index = (self.current_image_index - 1) % len(self.image_paths)
            self.update_image()
        elif event.key() == Qt.Key_Right:
            self.current_image_index = (self.current_image_index + 1) % len(self.image_paths)
            self.update_image()
