from PySide6.QtWidgets import QMainWindow, QPushButton


# Subclass of the QMainWindow class to customize my application's main window
class ButtonHolder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Button Holder App")
        button = QPushButton("Press me!")
        self.setCentralWidget(button)
