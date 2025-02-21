import sys

from PyQt6.QtWidgets import QDialog, QApplication

from layout import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.ok.clicked.connect(self.dane)
        self.show()

    def dane(self):
        if len(self.ui.name.text()) or len(self.ui.surname.text()) == 0:
            self.ui.warn.setText("Brak danych")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyForm()
    sys.exit(app.exec())
