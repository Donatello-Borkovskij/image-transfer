from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QVBoxLayout, QWidget, QLabel
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPixmap, QTransform, QImage
from PyQt5.QtCore import Qt, QSize
import shutil
import sys


def copy_image_to_directory(image_path, target_directory):
    try:
        shutil.copy(image_path, target_directory)
        print(f"Image copied to {target_directory}")
    except Exception as e:
        print("Error:", e)


class ImageFrame(QtWidgets.QMainWindow):
    def __init__(self, images, dest_directory):
        super().__init__()

        self.image_paths = images
        self.current_image_index = 0
        self.directory = dest_directory

        self.setWindowTitle('image-transfer-to-USB')

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.image_label)
        self.central_widget.setLayout(self.layout)

        self.showMaximized()
        self.update_image()

    def update_image(self):
        image_path = self.image_paths[self.current_image_index][0]
        original_image = QImage(image_path)

        scale_size = QSize(self.centralWidget().width()-50, self.centralWidget().height()-50)

        scaled_image = original_image.scaled(scale_size, Qt.KeepAspectRatio)

        pixmap = QPixmap.fromImage(scaled_image)

        self.image_label.setPixmap(pixmap)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Left:
            self.current_image_index = (self.current_image_index - 1) % len(self.image_paths)
            # self.current_image_index = (self.current_image_index - 1)
            self.update_image()
        elif event.key() == Qt.Key_Right:
            self.current_image_index = (self.current_image_index + 1) % len(self.image_paths)
            # self.current_image_index = (self.current_image_index + 1)
            self.update_image()
        elif event.key() == Qt.Key_Up:
            copy_image_to_directory(self.image_paths[self.current_image_index][0], self.directory)
