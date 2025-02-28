import sys
from os import write

from PyQt6.QtDBus import QDBusMessage
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QDialog, QApplication, QMessageBox, QInputDialog, QColorDialog, QFontDialog, QFileDialog

from layout import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.ok.clicked.connect(self.data)
        self.ui.countryButton.clicked.connect(self.choose)
        self.ui.colorButton.clicked.connect(self.color)
        self.ui.font.clicked.connect(self.fonting)
        self.ui.save.clicked.connect(self.savefile)
        self.ui.read.clicked.connect(self.readfile)
        self.show()

    def data(self):
        if len(self.ui.name.text()) == 0 or len(self.ui.surname.text()) == 0:
            message = QMessageBox()
            message.setText("Puste pola")
            message.exec()
        else:
            self.ui.name.clear()
            self.ui.surname.clear()

    def choose(self):
        countryName, ok = QInputDialog.getItem(self, "Wybierz państwo", "Lista Państw",
                                               ['Polska', 'Niemcy', 'Francja'], 0, False)
        if ok:
            self.ui.country.setText(countryName)

    def color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.ui.colorEdit.setStyleSheet(f"background-color: {color.name()}")

    def fonting(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.ui.fontEdit.setFont(font)

    #def saving(self):
    #   with open('./data.txt', 'w') as file:
    #   file.write(self.ui.fontEdit.toPlainText())

    def savefile(self):
        file_name, _ = QFileDialog().getSaveFileName(self, "Zapisz plik", ".", "")
        if file_name != '':
            if not file_name.endswitch('.txt'):
                file_name += ".txt"
            with open(file_name, 'w') as file:
                file.write(self.ui.fontEdit.toPlainText())

    def readfile(self):
        file_name = QFileDialog().getOpenFileName(self, "Otwórz plik", '.', "*.txt")
        if file_name != '':
            with open(file_name, 'r') as file:
                file.write(self.ui.fontEdit.toPlainText())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyForm()
    sys.exit(app.exec())
