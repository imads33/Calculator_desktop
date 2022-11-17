import sys
from PyQt5 import QtWidgets
from calculator import Ui_MainWindow

class Myapp(QtWidgets.QMainWindow):
    def __init__(self):
        super(Myapp,self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Addition.clicked.connect(self.calculate)
        self.ui.Substraction.clicked.connect(self.calculate)
        self.ui.Multiplication.clicked.connect(self.calculate)
        self.ui.Division.clicked.connect(self.calculate)

    def calculate(self):
        sender=self.sender()
        result=0

        if sender.text() == "Addition":
            result =int(self.ui.Number1.text())+int(self.ui.Number2.text())

        if sender.text() == 'Substraction':
            result =int(self.ui.Number1.text())-int(self.ui.Number2.text())

        if sender.text() == 'Multiplication':
            result =int(self.ui.Number1.text())*int(self.ui.Number2.text())

        if sender.text() == 'Division':
            result =int(self.ui.Number1.text())/int(self.ui.Number2.text())

        self.ui.label_3.setText('Result : '+str(result))

def App():
    app=QtWidgets.QApplication(sys.argv)
    window=Myapp()
    window.show()
    sys.exit(app.exec_())

App()