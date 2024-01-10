from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
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
            if file_name.lower().endswith((".jpg", ".png")):
                file_path = os.path.join(directory_path, file_name)

                try:
                    with Image.open(file_path) as img:
                        exif_data = img._getexif()
                        if exif_data:
                            creation_date = exif_data.get(36867)  # "DateTimeOriginal" tag
                            if creation_date:
                                creation_date = datetime.strptime(creation_date, "%Y:%m:%d %H:%M:%S")
                                image_files.append((file_path, creation_date))
                                continue  # Skip adding the same image with creation date

                except (IOError, AttributeError) as e:
                    print(f"Error processing file {file_name}: {e}")

                # For images without EXIF or creation date, use modification date
                modification_time = os.path.getmtime(file_path)
                modification_date = datetime.fromtimestamp(modification_time)
                image_files.append((file_path, modification_date))

        # Sort the image files prioritizing EXIF creation date over modification date
        self.sorted_image_files = sorted(image_files, key=lambda x: x[1] if x[1] != None else datetime.min,
                                         reverse=True)

        for file_path, date in self.sorted_image_files:
            print(f"File: {file_path}, Date: {date}")

