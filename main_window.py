from PySide6.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):

    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("Custom Main Window")

        # Adding menu bar
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("&File")

        # Adding action to the file-menu
        quit_action = file_menu.addAction("Quit")

        # Connecting quit-action to its method
        quit_action.triggered.connect(self.quit_app)

    
    def quit_app(self):
        """ 
            The method closes the app.
            It's called when quit-action 
            in the file-menu is triggered.
        """
        self.app.quit()
