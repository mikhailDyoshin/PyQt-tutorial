#Importing the components we need
from PySide6.QtWidgets import QApplication, QWidget

#The sys module is responsible for processing commmand line arguments
import sys


# This element is a wrapper for all application widgets and interections
app = QApplication(sys.argv)

# Creating a window of the application
window = QWidget()

# Showing the window because it's hidden by default
window.show()

#Starting the event loop
app.exec()
