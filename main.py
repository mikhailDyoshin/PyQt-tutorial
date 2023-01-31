#Importing the components we need
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QSlider
from PySide6.QtCore import Qt

#The sys module is responsible for processing commmand line arguments
import sys


""" Slots """
# The slot: responds when "Press me"-button is clicked
def button_clicked(data):
    print("You clicked the button, didn't you?", data)

# The slot: responds when value of the slider is changed
def respond_to_slider(data):
    print("Slider moved to: ", data)


""" Setting the app and its window """
# This element is a wrapper for all application widgets and interections
app = QApplication(sys.argv)

# Creating the main window of the application
window = QMainWindow()

# Setting title for the window
window.setWindowTitle("First python app with PySide6")


""" Creating a push-button """
# Creating a button
button = QPushButton("Press me")

# Allows to switch the state of the button (Checked = True, Unchecked = False)
button.setCheckable(True)

# Wiring the slot to the signal from button
button.clicked.connect(button_clicked)


""" Creating a slider """
slider = QSlider(Qt.Horizontal)
slider.setMinimum(1)
slider.setMaximum(100)
slider.setValue(25)
slider.valueChanged.connect(respond_to_slider)


# Positioning the button in the center of the main window
# window.setCentralWidget(button)

window.setCentralWidget(slider)

# Showing the window because it's hidden by default
window.show()

#Starting the event loop
app.exec()
