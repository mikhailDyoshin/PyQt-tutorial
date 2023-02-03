from PySide6.QtWidgets import QWidget, QLineEdit, QLabel, QHBoxLayout, QVBoxLayout, QPushButton


class WidgetLineEdit(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("QLineEdit and QLabel")

        # Creating a label for a line edit
        label = QLabel("Fullname: ")
        
        """ Line Edit """
        # Creating the line edit
        self.line_edit = QLineEdit()

        # Triggering text_changed method when line-edit's text is changed 
        self.line_edit.textChanged.connect(self.text_changed)

        # Triggering cursor_changed method when cursor in the line-edit widget moves
        # self.line_edit.cursorPositionChanged.connect(self.cursor_changed)

        # Triggering editing_finished method when editing in the line-edit widget is finished
        self.line_edit.editingFinished.connect(self.editing_finished)

        # Triggering selection_changed method when some text in line-edit widget is selected
        # self.line_edit.selectionChanged.connect(self.selection_changed)

        # Triggering text_edited method when some text in line-edit widget is edited
        self.line_edit.textEdited.connect(self.text_edited)

        """ Button """
        # Creating a button
        button = QPushButton("Grab data")

        # Triggering the grab_data method when button is pushed
        button.clicked.connect(self.grab_data)

        """ Label-textholder """
        # Creating a label as a text holder
        self.text_holder_label = QLabel("I AM HERE")

        """ Layouts """
        # Setting the horisontal layout for line edit and its label 
        h_layout = QHBoxLayout()
        h_layout.addWidget(label)
        h_layout.addWidget(self.line_edit)

        # Setting vertical layout for the previous layout and other widgets
        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(button)
        v_layout.addWidget(self.text_holder_label)

        self.setLayout(v_layout)


    """ Methods """
    def grab_data(self):
        """
            Puts a text, that was tiped in the line edit,
            into the text-holder-label
            after the push-button was clicked.
        """
        self.text_holder_label.setText(self.line_edit.text())

    def text_changed(self):
        """
            Puts a text, that was tiped in the line edit,
            into the text-holder-label
            when that text is changed. 
        """
        self.text_holder_label.setText(self.line_edit.text())

    def cursor_changed(self, old, new):
        """ 
            Prints an old and a new position
            of the cursor which placed in the line-edit widget.
        """
        print("Old position: ", old, "| New position: ", new)

    def editing_finished(self):
        """
            Prints a text below
            when editing of the text
            in line-edit widget is finished. 
        """
        print("Editing finished")

    def selection_changed(self):
        """
            Prints currently selected text
            in the line-edit widget.
        """
        print("Selected text: ", self.line_edit.selectedText())

    def text_edited(self, new_text):
        """
            Prints new edited text
            of the line-edit widget.
        """
        print("New text: ", new_text)
