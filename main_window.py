from PySide6.QtGui import QAction, QIcon
from PySide6.QtCore import QSize
from PySide6.QtWidgets import QMainWindow, QToolBar, QPushButton, QStatusBar


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
        toolbar = QToolBar("My main toolbar")
        # Setting the size of icons in the toolbar
        toolbar.setIconSize(QSize(16, 16))
        # Adding toolbar to the window-object
        self.addToolBar(toolbar)

        # Adding the quit action to the toolbar
        toolbar.addAction(quit_action)

        # Creating another action
        action1 = QAction("Some action", self)
        action1.setStatusTip("Status message for some action")
        action1.triggered.connect(self.toolbar_button_click)

        # Creating another action with an icon
        action2 = QAction(QIcon("./start.png"), "Some other action with an icon", self)
        action2.setStatusTip("Status message from action with icon")
        action2.triggered.connect(self.toolbar_icon_click)

        # Adding an action to the toolbar
        toolbar.addAction(action1)
        toolbar.addAction(action2)

        # Adding a separator to the toolbar
        toolbar.addSeparator()

        # Adding a button to to the toolbar
        toolbar.addWidget(QPushButton("Push me"))

        """ Status bar """
        # Creating a status bar
        self.setStatusBar(QStatusBar(self))

        """ Central button """
        button1 = QPushButton("Press me")
        button1.clicked.connect(self.button1_clicked)
        self.setCentralWidget(button1)


    """ Methods """
    def quit_app(self):
        """ 
            The method closes the app.
            It's called when quit-action 
            in the file-menu is triggered.
        """
        self.app.quit()

    def toolbar_button_click(self):
        """
            The method sends a message 
            to the status bar 
            when toolbar button is clicked.
            After 3 seconds the message disappears.
        """
        self.statusBar().showMessage("Toolbar button clicked.", 3000)

    def toolbar_icon_click(self):
        """
            The method sends a message 
            to the status bar 
            when toolbar icon is clicked.
            After 3 seconds the message disappears.
        """
        self.statusBar().showMessage("Toolbar icon clicked.", 3000)

    def button1_clicked(self):
        """
            The method prints a message into console
            when central button is clicked.
        """
        print("Button1 clicked.")
