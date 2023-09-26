from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QButtonGroup, QPushButton
from interface import Ui_MainWindow
from PyQt5.QtCore import Qt
import os, sys, keyboard
from time import sleep

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent=parent)
        self.setupUi(self)
        self.menuButton.clicked.connect(self.hidesidemenu)
        self.side_menu.setVisible(False)
        self.arg = 0
        self.ptButton.clicked.connect(self.active_tab)
        self.videoButton.clicked.connect(self.active_tab2)

        self.buttongroup = QButtonGroup()
        self.buttongroup.buttonClicked[int].connect(self.openFile1)
        self.ptAddButton()

        

        self.buttongroup2 = QButtonGroup()
        self.buttongroup2.buttonClicked[int].connect(self.openFile2)
        self.videoAddButton()


    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
             self.close()

    
    def hidesidemenu(self):
        if self.arg == 1:
            self.side_menu.setVisible(False)
            self.arg = 0
        else:
            self.side_menu.setVisible(True)
            self.arg = 1

    def active_tab(self):
        self.stackedWidget.setCurrentIndex(0)

    def active_tab2(self):
        self.stackedWidget.setCurrentIndex(1)

    def openFile1(self, id):
        for button in self.buttongroup.buttons():
            if button is self.buttongroup.button(id):
                os.startfile(f"presentation\pt{id}.ppsx")
    
    def openFile2(self, id):
        for button2 in self.buttongroup2.buttons():
            if button2 is self.buttongroup2.button(id):
                os.startfile(f"move\move{id}.mp4")
                sleep(3)
                keyboard.press("f11")
                sleep(1)
                keyboard.release("f11")

    def ptAddButton(self):                   #создаем кнопки в зависимости от количества файлов в папке presentation
        DIR = 'presentation/'
        j = 0
        for i in range(len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])):
            button = QPushButton()
            button.setMaximumSize(250, 400)
            button.setIcon(QtGui.QIcon(f'img/pt{i+1}.png'))
            button.setIconSize(QtCore.QSize(250, 400))
            self.buttongroup.addButton(button, i+1)
            self.gridLayout_2.addWidget(button, i//4, j)
            j += 1
            if j > 3:
                j = 0
        j = 0

    def videoAddButton(self):
        DIR = 'move/'
        j = 0
        for i in range(len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])):
            button2 = QPushButton()
            button2.setMaximumSize(250, 400)
            button2.setIcon(QtGui.QIcon(f'img/video{i+1}.png'))
            button2.setIconSize(QtCore.QSize(250, 400))
            self.buttongroup2.addButton(button2, i+1)
            self.gridLayout_4.addWidget(button2, i//4, j)
            j += 1
            if j > 3:
                j = 0
        j = 0


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.showFullScreen()
    sys.exit(app.exec_())