from PySide6.QtWidgets import QWidget, QMainWindow, QPushButton, QVBoxLayout, QMessageBox


class Widget(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("QMessageBox")

        """ Buttons """
        button_hard = QPushButton("Hard")
        button_hard.clicked.connect(self.button_clicked_hard)

        button_critical = QPushButton("Critical")
        button_critical.clicked.connect(self.button_clicked_critical)

        button_question = QPushButton("Question")
        button_question.clicked.connect(self.button_clicked_question)

        button_information = QPushButton("Information")
        button_information.clicked.connect(self.button_clicked_information)

        button_warning = QPushButton("Warning")
        button_warning.clicked.connect(self.button_clicked_warning)

        button_about = QPushButton("About")
        button_about.clicked.connect(self.button_clicked_about)

        """ Layout """
        # Creating a layout
        layout = QVBoxLayout()

        # Adding widgets to the layout
        layout.addWidget(button_hard)
        layout.addWidget(button_critical)
        layout.addWidget(button_question)
        layout.addWidget(button_information)
        layout.addWidget(button_warning)
        layout.addWidget(button_about)

        # Setting the layout
        self.setLayout(layout)


    """ Methods """
    # This is a hard way to represent a message box: hard
    def button_clicked_hard(self):

        """
            The method shows a message box 
            with title, text, informative text, 
            an icon and standard buttons.
            Also it can check 
            which one of the default buttons was clicked.
        """

        message = QMessageBox()
        message.setMinimumSize(700, 200)
        message.setWindowTitle("Some title")
        message.setText("Something happend")
        message.setInformativeText("Do you want to do something?")
        message.setIcon(QMessageBox.Critical)
        message.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        message.setDefaultButton(QMessageBox.Ok)

        # Showing the message-box
        ret = message.exec()

        # Checking which one of the default buttons was clicked.
        if ret == QMessageBox.Ok:
            print("Ok")
        else:
            print("Cancel")

    # This is an easy way to represent a message box: critical
    def button_clicked_critical(self):
        ret = QMessageBox.critical(
            self, 
            "Message title", 
            "Critical warning!", 
            QMessageBox.Ok|QMessageBox.Cancel,
        )

        if ret == QMessageBox.Ok:
            print("Ok")
        else:
            print("Cancel")

    # Question
    def button_clicked_question(self):
        ret = QMessageBox.question(
            self, 
            "Message title", 
            "Asking a question?", 
            QMessageBox.Ok|QMessageBox.Cancel,
        )

        if ret == QMessageBox.Ok:
            print("Ok")
        else:
            print("Cancel")

    #Information
    def button_clicked_information(self):
        ret = QMessageBox.information(
            self, 
            "Message title", 
            "Some information.", 
            QMessageBox.Ok|QMessageBox.Cancel,
        )

        if ret == QMessageBox.Ok:
            print("Ok")
        else:
            print("Cancel")

    # Warning
    def button_clicked_warning(self):
        ret = QMessageBox.warning(
            self, 
            "Message title", 
            "Some warning!", 
            QMessageBox.Ok|QMessageBox.Cancel,
        )

        if ret == QMessageBox.Ok:
            print("Ok")
        else:
            print("Cancel")

    # About
    def button_clicked_about(self):
        QMessageBox.about(
            self, 
            "Message title", 
            "Some about message.",
        )
