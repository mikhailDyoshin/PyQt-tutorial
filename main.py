#Importing the components we need
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

#The sys module is responsible for processing commmand line arguments
import sys

# Importing the ButtonHolder class
from button_holder import ButtonHolder

# Importing the RockWidget class
from rock_widget import RockWidget

# Importing the MainWindow class
from main_window import MainWindow


# This element is a wrapper for all application widgets and interections
app = QApplication(sys.argv)

# Creating the main window of the application
window = MainWindow(app)

# Showing the window because it's hidden by default
window.show()

#Starting the event loop
app.exec()
