#Importing the components we need
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

#The sys module is responsible for processing commmand line arguments
import sys

# Importing the ButtonHolder class
from button_holder import ButtonHolder


# This element is a wrapper for all application widgets and interections
app = QApplication(sys.argv)

# Creating the main window of the application
window = ButtonHolder()

# Showing the window because it's hidden by default
window.show()

#Starting the event loop
app.exec()
