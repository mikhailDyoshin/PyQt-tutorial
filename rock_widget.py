from PySide6.QtWidgets import QWidget, QPushButton, QHBoxLayout


class RockWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Rock Widget")

        # Creating buttons
        button1 = QPushButton("Button1")
        button2 = QPushButton("Button2")

        # Creating a layout
        button_layout = QHBoxLayout()
        button_layout.addWidget(button1)
        button_layout.addWidget(button2)

        # Connecting buttons to their slots
        button1.clicked.connect(self.button1_clicked)
        button2.clicked.connect(self.button2_clicked)

        # Setting the layout as an attribute of RockWidget() object
        self.setLayout(button_layout)

    
    def button1_clicked(self):
        print("Button1 clicked.")

    def button2_clicked(self):
        print("Button2 clicked.")
