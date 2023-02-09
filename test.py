from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
from PyQt5.QtWidgets import QRadioButton, QLabel, QMessageBox, QComboBox
from PyQt5.QtGui import QFont
import sys

app = QApplication(sys.argv)


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("1-savol")
        self.setGeometry(100, 100, 500, 500)
        self.win1 = Window1()

        self.start()

    def start(self):
        self.ball = 0
        self.savol = QLabel("2 + 2 = ", self)
        self.savol.setFont(QFont("times", 20))
        self.savol.move(50, 50)

        self.a1 = QRadioButton("4", self)
        self.setFont(QFont("times", 20))
        self.a1.move(100, 100)

        self.a2 = QRadioButton("5", self)
        self.setFont(QFont("times", 20))
        self.a2.move(100, 150)

        self.a3 = QRadioButton("1.25", self)
        self.setFont(QFont("times", 20))
        self.a3.move(100, 200)

        self.a4 = QRadioButton("6", self)
        self.setFont(QFont("times", 20))
        self.a4.move(100, 250)

        self.ok = QPushButton('Ok', self)
        self.ok.setGeometry(150, 300, 60, 60)
        self.ok.clicked.connect(self.Ok)

        self.next = QPushButton("Next", self)
        self.next.setGeometry(250, 300, 60, 60)
        self.next.clicked.connect(self.Next)

    def Ok(self):

        if self.a1.isChecked():
            a = QMessageBox(self)
            a.setText("Correct")
            self.ball += 1
            a.show()

        if self.a2.isChecked():
            a = QMessageBox(self)
            a.setText("Incorrect")
            a.show()

        if self.a3.isChecked():
            a = QMessageBox(self)
            a.setText("Incorrect")
            a.show()

        if self.a4.isChecked():
            a = QMessageBox(self)
            a.setText("Incorrect")
            a.show()

    def Next(self):
        self.win1.show()


class Window1(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("2-savol")
        self.setGeometry(100, 100, 500, 500)
        self.win2 = Window2()

        self.start1()

    def start1(self):
        self.savol = QLabel("2 + 3 = ", self)
        self.savol.setFont(QFont("times", 20))
        self.savol.move(50, 50)

        self.a1 = QRadioButton("4", self)
        self.setFont(QFont("times", 20))
        self.a1.move(100, 100)

        self.a2 = QRadioButton("5", self)
        self.setFont(QFont("times", 20))
        self.a2.move(100, 150)

        self.a3 = QRadioButton("1.25", self)
        self.setFont(QFont("times", 20))
        self.a3.move(100, 200)

        self.a4 = QRadioButton("6", self)
        self.setFont(QFont("times", 20))
        self.a4.move(100, 250)

        self.ok = QPushButton('Ok', self)
        self.ok.setGeometry(150, 300, 60, 60)
        self.ok.clicked.connect(self.Ok)

        self.next = QPushButton("Next", self)
        self.next.setGeometry(250, 300, 60, 60)
        self.next.clicked.connect(self.Next)

    def Ok(self):

        if self.a1.isChecked():
            a = QMessageBox(self)
            a.setText("Incorrect")
            a.show()

        if self.a2.isChecked():
            a = QMessageBox(self)
            a.setText("Correct")
            win.ball += 1
            a.show()

        if self.a3.isChecked():
            a = QMessageBox(self)
            a.setText("Incorrect")
            a.show()

        if self.a4.isChecked():
            a = QMessageBox(self)
            a.setText("Incorrect")
            a.show()

    def Next(self):
        self.win2.show()


class Window2(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("3-savol")
        self.setGeometry(100, 100, 500, 500)
        self.win3 = Window3()

        self.start2()

    def start2(self):
        self.savol = QLabel("2 * 3 = ", self)
        self.savol.setFont(QFont("times", 20))
        self.savol.move(50, 50)

        self.a1 = QRadioButton("4", self)
        self.setFont(QFont("times", 20))
        self.a1.move(100, 100)

        self.a2 = QRadioButton("6", self)
        self.setFont(QFont("times", 20))
        self.a2.move(100, 150)

        self.a3 = QRadioButton("1.25", self)
        self.setFont(QFont("times", 20))
        self.a3.move(100, 200)

        self.a4 = QRadioButton("6", self)
        self.setFont(QFont("times", 20))
        self.a4.move(100, 250)

        self.ok = QPushButton('Ok', self)
        self.ok.setGeometry(150, 300, 60, 60)
        self.ok.clicked.connect(self.Ok)

        self.next = QPushButton("Next", self)
        self.next.setGeometry(250, 300, 60, 60)
        self.next.clicked.connect(self.Next)

    def Ok(self):

        if self.a1.isChecked():
            a = QMessageBox(self)
            a.setText("Incorrect")
            a.show()

        if self.a2.isChecked():
            a = QMessageBox(self)
            a.setText("Correct")
            win.ball += 1
            a.show()

        if self.a3.isChecked():
            a = QMessageBox(self)
            a.setText("Incorrect")
            a.show()

        if self.a4.isChecked():
            a = QMessageBox(self)
            a.setText("Incorrect")
            a.show()

    def Next(self):
        self.win3.show()


class Window3(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("4-savol")
        self.setGeometry(100, 100, 500, 500)
        self.win4 = Window4()

        self.start2()

    def start2(self):
        self.savol = QLabel("2 * 3(6 + 9 - 4) = ", self)
        self.savol.setFont(QFont("times", 20))
        self.savol.move(50, 50)

        self.a1 = QRadioButton("45", self)
        self.setFont(QFont("times", 20))
        self.a1.move(100, 100)

        self.a2 = QRadioButton("66", self)
        self.setFont(QFont("times", 20))
        self.a2.move(100, 150)

        self.a3 = QRadioButton("125", self)
        self.setFont(QFont("times", 20))
        self.a3.move(100, 200)

        self.a4 = QRadioButton("76", self)
        self.setFont(QFont("times", 20))
        self.a4.move(100, 250)

        self.ok = QPushButton('Ok', self)
        self.ok.setGeometry(150, 300, 60, 60)
        self.ok.clicked.connect(self.Ok)

        self.next = QPushButton("Next", self)
        self.next.setGeometry(250, 300, 60, 60)
        self.next.clicked.connect(self.Next)

    def Ok(self):

        if self.a1.isChecked():
            a = QMessageBox(self)
            a.setText("Incorrect")
            a.show()

        if self.a2.isChecked():
            a = QMessageBox(self)
            a.setText("Correct")
            win.ball += 1
            a.show()

        if self.a3.isChecked():
            a = QMessageBox(self)
            a.setText("Incorrect")
            a.show()

        if self.a4.isChecked():
            a = QMessageBox(self)
            a.setText("Incorrect")
            a.show()

    def Next(self):
        self.win4.show()


class Window4(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("5-savol")
        self.setGeometry(100, 100, 500, 500)
        self.win5 = Window5()

        self.start2()

    def start2(self):
        self.savol = QLabel("3 * 3 = ", self)
        self.savol.setFont(QFont("times", 20))
        self.savol.move(50, 50)

        self.a1 = QRadioButton("9", self)
        self.setFont(QFont("times", 20))
        self.a1.move(100, 100)

        self.a2 = QRadioButton("6", self)
        self.setFont(QFont("times", 20))
        self.a2.move(100, 150)

        self.a3 = QRadioButton("1.25", self)
        self.setFont(QFont("times", 20))
        self.a3.move(100, 200)

        self.a4 = QRadioButton("6", self)
        self.setFont(QFont("times", 20))
        self.a4.move(100, 250)

        self.ok = QPushButton('Ok', self)
        self.ok.setGeometry(150, 300, 60, 60)
        self.ok.clicked.connect(self.Ok)

        self.next = QPushButton("Next", self)
        self.next.setGeometry(250, 300, 60, 60)
        self.next.clicked.connect(self.Next)

    def Ok(self):

        if self.a1.isChecked():
            a = QMessageBox(self)
            a.setText("Correct")
            win.ball += 1
            a.show()

        if self.a2.isChecked():
            a = QMessageBox(self)
            a.setText("Incorrect")
            a.show()

        if self.a3.isChecked():
            a = QMessageBox(self)
            a.setText("Incorrect")
            a.show()

        if self.a4.isChecked():
            a = QMessageBox(self)
            a.setText("Incorrect")
            a.show()

    def Next(self):
        self.win5.show()


class Window5(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("6-savol")
        self.setGeometry(100, 100, 500, 500)
        self.win6 = Window6()

        self.start2()

    def start2(self):
        self.savol = QLabel("12 * 8 = ", self)
        self.savol.setFont(QFont("times", 20))
        self.savol.move(50, 50)

        self.a1 = QRadioButton("45", self)
        self.setFont(QFont("times", 20))
        self.a1.move(100, 100)

        self.a2 = QRadioButton("48", self)
        self.setFont(QFont("times", 20))
        self.a2.move(100, 150)

        self.a3 = QRadioButton("96", self)
        self.setFont(QFont("times", 20))
        self.a3.move(100, 200)

        self.a4 = QRadioButton("64", self)
        self.setFont(QFont("times", 20))
        self.a4.move(100, 250)

        self.ok = QPushButton('Ok', self)
        self.ok.setGeometry(150, 300, 60, 60)
        self.ok.clicked.connect(self.Ok)

        self.next = QPushButton("Next", self)
        self.next.setGeometry(250, 300, 60, 60)
        self.next.clicked.connect(self.Next)

    def Ok(self):

        if self.a1.isChecked():
            a = QMessageBox(self)
            a.setText("Incorrect")
            a.show()

        if self.a2.isChecked():
            a = QMessageBox(self)
            a.setText("Incorrect")
            a.show()

        if self.a3.isChecked():
            a = QMessageBox(self)
            a.setText("Correct")
            win.ball += 1
            a.show()

        if self.a4.isChecked():
            a = QMessageBox(self)
            a.setText("Incorrect")
            a.show()

    def Next(self):
        self.win6.show()


class Window6(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("7-savol")
        self.setGeometry(100, 100, 500, 500)
        self.win7 = Window7()

        self.start2()

    def start2(self):
        self.savol = QLabel("ab + ab + ac = ", self)
        self.savol.setFont(QFont("times", 20))
        self.savol.move(50, 50)

        self.a1 = QRadioButton("abacab", self)
        self.setFont(QFont("times", 20))
        self.a1.move(100, 100)

        self.a2 = QRadioButton("!!!", self)
        self.setFont(QFont("times", 20))
        self.a2.move(100, 150)

        self.a3 = QRadioButton("15", self)
        self.setFont(QFont("times", 20))
        self.a3.move(100, 200)

        self.a4 = QRadioButton("a(2b +c)", self)
        self.setFont(QFont("times", 20))
        self.a4.move(100, 250)

        self.ok = QPushButton('Ok', self)
        self.ok.setGeometry(150, 300, 60, 60)
        self.ok.clicked.connect(self.Ok)

        self.next = QPushButton("Next", self)
        self.next.setGeometry(250, 300, 60, 60)
        self.next.clicked.connect(self.Next)

    def Ok(self):

        if self.a1.isChecked():
            a = QMessageBox(self)
            a.setText("Incorrect")
            a.show()

        if self.a2.isChecked():
            a = QMessageBox(self)
            a.setText("Incorrect")
            a.show()

        if self.a3.isChecked():
            a = QMessageBox(self)
            a.setText("Incorrect")
            a.show()

        if self.a4.isChecked():
            a = QMessageBox(self)
            a.setText("Correct")
            win.ball += 1
            a.show()

    def Next(self):
        self.win7.show()


class Window7(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("8-savol")
        self.setGeometry(100, 100, 500, 500)
        self.win8 = Window8()

        self.start2()

    def start2(self):
        self.savol = QLabel("6 * 7 = ", self)
        self.savol.setFont(QFont("times", 20))
        self.savol.move(50, 50)

        self.a1 = QRadioButton("42", self)
        self.setFont(QFont("times", 20))
        self.a1.move(100, 100)

        self.a2 = QRadioButton("62", self)
        self.setFont(QFont("times", 20))
        self.a2.move(100, 150)

        self.a3 = QRadioButton("12", self)
        self.setFont(QFont("times", 20))
        self.a3.move(100, 200)

        self.a4 = QRadioButton("45", self)
        self.setFont(QFont("times", 20))
        self.a4.move(100, 250)

        self.ok = QPushButton('Ok', self)
        self.ok.setGeometry(150, 300, 60, 60)
        self.ok.clicked.connect(self.Ok)

        self.next = QPushButton("Next", self)
        self.next.setGeometry(250, 300, 60, 60)
        self.next.clicked.connect(self.Next)

    def Ok(self):

        if self.a1.isChecked():
            a = QMessageBox(self)
            a.setText("Correct")
            win.ball += 1
            a.show()

        if self.a2.isChecked():
            a = QMessageBox(self)
            a.setText("Incorrect")
            a.show()

        if self.a3.isChecked():
            a = QMessageBox(self)
            a.setText("Incorrect")
            a.show()

        if self.a4.isChecked():
            a = QMessageBox(self)
            a.setText("Incorrect")
            a.show()

    def Next(self):
        self.win8.show()


class Window8(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("9-savol")
        self.setGeometry(100, 100, 500, 500)

        self.start2()

    def start2(self):
        self.savol = QLabel("2 * 8 = ", self)
        self.savol.setFont(QFont("times", 20))
        self.savol.move(50, 50)

        self.a1 = QRadioButton("4", self)
        self.setFont(QFont("times", 20))
        self.a1.move(100, 100)

        self.a2 = QRadioButton("16", self)
        self.setFont(QFont("times", 20))
        self.a2.move(100, 150)

        self.a3 = QRadioButton("12", self)
        self.setFont(QFont("times", 20))
        self.a3.move(100, 200)

        self.a4 = QRadioButton("6", self)
        self.setFont(QFont("times", 20))
        self.a4.move(100, 250)

        self.ok = QPushButton('Ok', self)
        self.ok.setGeometry(150, 300, 60, 60)
        self.ok.clicked.connect(self.Ok)

        self.next = QPushButton("Next", self)
        self.next.setGeometry(250, 300, 60, 60)
        self.next.clicked.connect(self.Next)

    def Ok(self):

        if self.a1.isChecked():
            a = QMessageBox(self)
            a.setText("Incorrect")
            a.show()

        if self.a2.isChecked():
            a = QMessageBox(self)
            a.setText("Correct")
            win.ball += 1
            a.show()

        if self.a3.isChecked():
            a = QMessageBox(self)
            a.setText("Incorrect")
            a.show()

        if self.a4.isChecked():
            a = QMessageBox(self)
            a.setText("Incorrect")
            a.show()

    def Next(self):
        self.win9.show()


class Window9(Window8):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("10-savol")
        self.setGeometry(100, 100, 500, 500)
        self.win = Window8()
        self.start2()

    def start2(self):
        self.savol = QLabel("2 * 3 * 6 = ", self)
        self.savol.setFont(QFont("times", 20))
        self.savol.move(50, 50)

        self.a1 = QRadioButton("45", self)
        self.setFont(QFont("times", 20))
        self.a1.move(100, 100)

        self.a2 = QRadioButton("36", self)
        self.setFont(QFont("times", 20))
        self.a2.move(100, 150)

        self.a3 = QRadioButton("12", self)
        self.setFont(QFont("times", 20))
        self.a3.move(100, 200)

        self.a4 = QRadioButton("62", self)
        self.setFont(QFont("times", 20))
        self.a4.move(100, 250)

        self.ok = QPushButton('Ok', self)
        self.ok.setGeometry(150, 300, 60, 60)
        self.ok.clicked.connect(self.Ok)

        self.label = QLabel("", self)
        self.label.move(150, 350)
        self.label.adjustSize()

    def Ok(self):

        if self.a1.isChecked():
            a = QMessageBox(self)
            a.setText("Incorrect")
            a.show()

        if self.a2.isChecked():
            a = QMessageBox(self)
            a.setText("Correct")
            win.ball += 1
            a.show()

        if self.a3.isChecked():
            a = QMessageBox(self)
            a.setText("Incorrect")
            a.show()

        if self.a4.isChecked():
            a = QMessageBox(self)
            a.setText("Incorrect")
            a.show()


win = Window()
win.show()
sys.exit(app.exec_())
