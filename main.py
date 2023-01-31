#Importing the components we need
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

#The sys module is responsible for processing commmand line arguments
import sys

# The slot: responds when "Press me"-button is clicked
def button_clicked(data):
    print("You clicked the button, didn't you?", data)

# This element is a wrapper for all application widgets and interections
app = QApplication(sys.argv)

# Creating the main window of the application
window = QMainWindow()

# Setting title for the window
window.setWindowTitle("First python app with PySide6")

# Creating a button
button = QPushButton("Press me")

# Allows to switch the state of the button (Checked = True, Unchecked = False)
button.setCheckable(True)

# Wiring the slot to the signal from button
button.clicked.connect(button_clicked)

# Positioning the button in the center of the main window
window.setCentralWidget(button)

# Showing the window because it's hidden by default
window.show()

#Starting the event loop
app.exec()
