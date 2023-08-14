from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.uic import loadUi
import image_frame
import os
from PIL import Image
from datetime import datetime


class StartGUI(QtWidgets.QMainWindow):
    def __init__(self):
        super(StartGUI, self).__init__()
        self.new_window = None
        self.sorted_image_files = None
        loadUi('start.ui', self)

        self.setFixedWidth(450)
        self.setFixedHeight(300)

        self.browse1.clicked.connect(self.browse_files_source)
        self.browse2.clicked.connect(self.browse_files_dest)
        self.start.clicked.connect(self.start_pressed)
        self.setWindowTitle('image-transfer-to-USB')
        self.show()

    def browse_files_source(self):
        dir_name = QFileDialog.getExistingDirectory(self, 'Choose directory', 'C:/')
        self.image_dir.setText(dir_name)
        self.get_sorted_images()

    def browse_files_dest(self):
        dir_name = QFileDialog.getExistingDirectory(self, 'Choose directory', 'C:/')
        self.destination_dir.setText(dir_name)

    def start_pressed(self):
        self.new_window = image_frame.ImageFrame(self.sorted_image_files, self.destination_dir.text())
        self.close()

    def get_sorted_images(self):
        directory_path = self.image_dir.text()

        files = os.listdir(directory_path)

        image_files = []
        for file_name in files:
            if file_name.lower().endswith(".jpg"):
                file_path = os.path.join(directory_path, file_name)
                try:
                    with Image.open(file_path) as img:
                        exif_data = img._getexif()
                        if exif_data:
                            creation_date = exif_data.get(36867)  # "DateTimeOriginal" tag
                            if creation_date:
                                creation_date = datetime.strptime(creation_date, "%Y:%m:%d %H:%M:%S")
                                image_files.append((file_path, creation_date))
                except (IOError, AttributeError):
                    pass
            elif file_name.lower().endswith(".png"):
                file_path = os.path.join(directory_path, file_name)
                try:
                    modification_date = datetime.fromtimestamp(os.path.getmtime(file_path))
                    image_files.append((file_path, modification_date))
                except (IOError, AttributeError):
                    pass

        self.sorted_image_files = sorted(image_files, key=lambda x: x[1], reverse=True)

        for file_path, creation_date in self.sorted_image_files:
            print(f"File: {file_path}, Creation Date: {creation_date}")
