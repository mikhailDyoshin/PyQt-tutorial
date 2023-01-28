#Importing the components we need
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

#The sys module is responsible for processing commmand line arguments
import sys


# This element is a wrapper for all application widgets and interections
app = QApplication(sys.argv)

# Creating the main window of the application
window = QMainWindow()

# Setting title for the window
window.setWindowTitle("First python app with PySide6")

# Creating a button
button = QPushButton()

# Plasing a text into the button-widget
button.setText("Push me")

# Positioning the button in the center of the main window
window.setCentralWidget(button)

# Showing the window because it's hidden by default
window.show()

#Starting the event loop
app.exec()
