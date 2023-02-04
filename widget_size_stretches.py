from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QSizePolicy


class WidgetSizeStretches(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Widget with Size Policies and Stretches")

        " Widgets "
        label = QLabel("Some text :")
        line_edit = QLineEdit()

        button_1 = QPushButton("One")
        # Setting size policy: first arg - horizontal direction, second - vertical one.
        button_1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding) # Grows in both directions
        button_2 = QPushButton("Two")
        button_2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed) # Grows only horizontally
        button_3 = QPushButton("Three")
        button_3.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding) # Grows only vertically

        """ Layouts """
        h1_layout = QHBoxLayout()
        h1_layout.addWidget(label)
        h1_layout.addWidget(line_edit)

        h2_layout = QHBoxLayout()
        # Now the first button takes 2/4 (2+1+1=4) of the layout's space, others take what is left.
        h2_layout.addWidget(button_1, 2)
        h2_layout.addWidget(button_2, 1)
        h2_layout.addWidget(button_3, 1)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h1_layout)
        v_layout.addLayout(h2_layout)

        self.setLayout(v_layout)
