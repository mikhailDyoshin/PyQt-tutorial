from PySide6.QtCore import QSize
from PySide6.QtWidgets import QMainWindow, QToolBar


class MainWindow(QMainWindow):

    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("Custom Main Window")

        """ Menu bar and menus """
        # Adding menu bar
        menu_bar = self.menuBar()

        # Creating file menu
        file_menu = menu_bar.addMenu("File")

        # Creating edit menu
        edit_menu = menu_bar.addMenu("Edit")

        # Creating another bunch of menus
        menu_bar.addMenu("Windows")
        menu_bar.addMenu("Settings")
        menu_bar.addMenu("Help")

        # Adding action to the file-menu
        quit_action = file_menu.addAction("Quit")

        # Adding actions to the edit-menu
        edit_menu.addAction("Copy")
        edit_menu.addAction("Cut")
        edit_menu.addAction("Paste")
        edit_menu.addAction("Undo")
        edit_menu.addAction("Redo")

        # Connecting quit-action to its method
        quit_action.triggered.connect(self.quit_app)


        """ Toolbar """
        # Creating toolbar
        tool_bar = QToolBar("My main toolbar")
        # Setting the size of icons in the toolbar
        tool_bar.setIconSize(QSize(16, 16))
        # Adding toolbar to the window-object
        self.addToolBar(tool_bar)

        # Adding the quit action to the toolbar
        tool_bar.addAction(quit_action)

    
    def quit_app(self):
        """ 
            The method closes the app.
            It's called when quit-action 
            in the file-menu is triggered.
        """
        self.app.quit()
