from PyQt5.QtWidgets import QFileDialog, QApplication, QMainWindow, QPushButton
import sys
import PIL

class MainWindow(QMainWindow):
    # Initialize window
    def __init__(self):
        super().__init__()

        # You may delete it later :)
        self.setWindowTitle("Bulk Crop Tester")
        self.setGeometry(100, 100, 300, 200)

        self.target_dir = None

        self.pickFolderButton = QPushButton("Select Folder", self)
        self.pickFolderButton.setGeometry(50, 50, 200, 40)
        self.pickFolderButton.clicked.connect(self.on_select_dir)
        # You may delete it later :)
    
    # Select directory for bulk image cropping
    def select_dir(self, title="Select Folder"):
        path = QFileDialog.getExistingDirectory(
            self, 
            title, 
            "", 
            QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks
        )
        return path or None
    
    # Update target directory
    def on_select_dir(self):
        folder = self.select_dir()
        if folder:
            self.target_dir = folder
            print("Selected folder: " + self.target_dir)

# Perform bulk image crop on entire folder
def bulk_crop():
    None

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())