from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout, QVBoxLayout, QPushButton


class WidgetLabelImages(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Widget Qlabel with Images")

        """ Label with Image """
        image_label = QLabel()
        image_label.setPixmap(QPixmap("./images/minions.png"))
        
        """ Layout """
        layout = QVBoxLayout()
        layout.addWidget(image_label)

        self.setLayout(layout)

        