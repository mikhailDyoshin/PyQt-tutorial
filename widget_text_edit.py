from PySide6.QtWidgets import QWidget, QPushButton, QTextEdit, QHBoxLayout, QVBoxLayout


class WidgetTextEdit(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Text Edit Widget")

        """ Text Edit Widget """
        self.text_edit = QTextEdit()

        """ Buttons """
        select_all_button = QPushButton("Select all")
        select_all_button.clicked.connect(self.select_all) 

        copy_button = QPushButton("Copy")
        copy_button.clicked.connect(self.text_edit.copy)

        cut_button = QPushButton("Cut")
        cut_button.clicked.connect(self.text_edit.cut)

        paste_button = QPushButton("Paste")
        paste_button.clicked.connect(self.text_edit.paste)

        undo_button = QPushButton("Undo")
        undo_button.clicked.connect(self.text_edit.undo)

        redo_button = QPushButton("Redo")
        redo_button.clicked.connect(self.text_edit.redo)

        set_plain_text_button = QPushButton("Set plain text")
        set_plain_text_button.clicked.connect(self.set_plain_text)

        set_html_button = QPushButton("Set html")
        set_html_button.clicked.connect(self.set_html)

        set_markdown_button = QPushButton("Set markdown")
        set_markdown_button.clicked.connect(self.set_markdown)

        clear_button = QPushButton("Clear")
        clear_button.clicked.connect(self.text_edit.clear)

        """ Layouts """
        h_layout = QHBoxLayout()
        h_layout.addWidget(select_all_button)
        h_layout.addWidget(copy_button)
        h_layout.addWidget(cut_button)
        h_layout.addWidget(paste_button)
        h_layout.addWidget(undo_button)
        h_layout.addWidget(redo_button)
        h_layout.addWidget(set_plain_text_button)
        h_layout.addWidget(set_html_button)
        h_layout.addWidget(set_markdown_button)
        h_layout.addWidget(clear_button)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(self.text_edit)

        self.setLayout(v_layout)


    """ Methods """
    def select_all(self):
        """
            Selects all text 
            in the edit-text widget.
        """
        self.text_edit.selectAll()

    def set_plain_text(self):
        """
            Puts a text below
            into edit-text widget like a plaint text.
        """
        self.text_edit.setPlainText("Hello, it's a plain text!")

    def set_html(self):
        """
            Puts a text below
            into edit-text widget in html format.
        """
        self.text_edit.setHtml("<h1>Hello, it's an html!</h1>")

    def set_markdown(self):
        """
            Puts a text below
            into edit-text widget in markdown format.
        """
        self.text_edit.setMarkdown("# Hello, it's a markdown!")
