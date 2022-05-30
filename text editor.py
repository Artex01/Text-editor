import sys
from PyQt5.QtWidgets import *
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Text editor")
        self.text_edit()
        self.show()
    def text_edit(self):
        hbox = QHBoxLayout()

        self.textEdit = QTextEdit()
        hbox.addWidget(self.textEdit)

        vbox = QVBoxLayout()

        color_button = QPushButton("Change color")
        color_button.clicked.connect(self.change_color)
        vbox.addWidget(color_button)

        font_button = QPushButton("Change font")
        font_button.clicked.connect(self.change_font)
        vbox.addWidget(font_button)

        vbox.addLayout(hbox)
        self.setLayout(vbox)
    def change_color(self):
        color = QColorDialog.getColor()
        self.textEdit.setTextColor(color)

    def change_font(self):
        font, ok = QFontDialog().getFont()
        if ok:
            self.textEdit.setFont(font)
app = QApplication(sys.argv)
window = Window()
app.exec_()