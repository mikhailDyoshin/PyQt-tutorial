#Importing the components we need
from PySide6.QtWidgets import QApplication

#The sys module is responsible for processing commmand line arguments
import sys

from widget_grid_layout import WidgetGridLayout

# This element is a wrapper for all application widgets and interections
app = QApplication(sys.argv)

# Creating the main window of the application
window = WidgetGridLayout()

# Showing the window because it's hidden by default
window.show()

#Starting the event loop
app.exec()
