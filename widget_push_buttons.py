from PySide6.QtWidgets import QWidget, QPushButton, QHBoxLayout


class WidgetPushButtons(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Custom Main Window")

        button = QPushButton("Click")

        button.clicked.connect(self.button_clicked)

        button.pressed.connect(self.button_pressed)

        button.released.connect(self.button_released)

        layout = QHBoxLayout()

        layout.addWidget(button)

        self.setLayout(layout)

    
    """ Methods """
    def button_clicked(self):
        print("Button clicked.")

    def button_pressed(self):
        print("Button pressed.")

    def button_released(self):
        print("Button released.")
