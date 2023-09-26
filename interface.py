from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QSizePolicy
import sys



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.background = QtWidgets.QFrame(self.centralwidget)
        self.background.setStyleSheet("#background{background-color: rgb(255, 255, 255);}")
        self.background.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.background.setFrameShadow(QtWidgets.QFrame.Raised)
        self.background.setObjectName("background")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.background)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.header = QtWidgets.QFrame(self.background)
        self.header.setMinimumSize(QtCore.QSize(800, 120))
        self.header.setMaximumHeight(250)
        self.header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header.setObjectName("header")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.header)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.frame_4 = QtWidgets.QFrame(self.header)
        self.frame_4.setMinimumSize(QtCore.QSize(320, 0))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.menuButton = QtWidgets.QPushButton(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.menuButton.setFont(font)
        self.menuButton.setStyleSheet("QPushButton {color: rgb(134,52,41);}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/hamburger_menu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuButton.setIcon(icon)
        self.menuButton.setIconSize(QtCore.QSize(40, 40))
        self.menuButton.setObjectName("menuButton")
        self.horizontalLayout_3.addWidget(self.menuButton)
        self.horizontalLayout.addWidget(self.frame_4, 0, QtCore.Qt.AlignLeft)

        self.frame_5 = QtWidgets.QFrame(self.header)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.logo = QtWidgets.QLabel(self.frame_5)
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("img/logo.jpeg"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.verticalLayout_5.addWidget(self.logo)
        self.horizontalLayout.addWidget(self.frame_5)

        self.verticalLayout_2.addWidget(self.header, 0, QtCore.Qt.AlignTop)
        self.main = QtWidgets.QFrame(self.background)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main.sizePolicy().hasHeightForWidth())
        self.main.setSizePolicy(sizePolicy)
        self.main.setMinimumSize(QtCore.QSize(800, 300))
        self.main.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main.setObjectName("main")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.main)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.side_menu = QtWidgets.QWidget(self.main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.side_menu.sizePolicy().hasHeightForWidth())
        self.side_menu.setSizePolicy(sizePolicy)
        self.side_menu.setObjectName("side_menu")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.side_menu)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame = QtWidgets.QFrame(self.side_menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(320, 0))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.ptButton = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.ptButton.setFont(font)
        self.ptButton.setStyleSheet("QPushButton {text-align: left; color: rgb(134,52,41);}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/presentation.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ptButton.setIcon(icon1)
        self.ptButton.setIconSize(QtCore.QSize(40, 40))
        self.ptButton.setObjectName("ptButton")
        self.verticalLayout_4.addWidget(self.ptButton)
        self.videoButton = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.videoButton.setFont(font)
        self.videoButton.setStyleSheet("QPushButton {text-align: left; color: rgb(134,52,41);}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/video.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.videoButton.setIcon(icon2)
        self.videoButton.setIconSize(QtCore.QSize(40, 40))
        self.videoButton.setObjectName("videoButton")
        self.verticalLayout_4.addWidget(self.videoButton)
        self.verticalLayout_3.addWidget(self.frame, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        self.horizontalLayout_2.addWidget(self.side_menu, 0, QtCore.Qt.AlignRight)
        self.main_body = QtWidgets.QFrame(self.main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_body.sizePolicy().hasHeightForWidth())
        self.main_body.setSizePolicy(sizePolicy)
        self.main_body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_body.setObjectName("main_body")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.main_body)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QtWidgets.QStackedWidget(self.main_body)
        self.stackedWidget.setObjectName("stackedWidget")
        self.stackedWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)

        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.page_1)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.scrollArea = QtWidgets.QScrollArea(self.page_1)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollAreaWidgetContents_1 = QtWidgets.QWidget()
        # self.scrollAreaWidgetContents_1.setGeometry(QtCore.QRect(0, 0, 555, 431))
        self.scrollAreaWidgetContents_1.setObjectName("scrollAreaWidgetContents_1")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_1)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setVerticalSpacing(20)
        self.frame_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout.addWidget(self.frame_2, 0, 0, 1, 1, QtCore.Qt.AlignVCenter)

        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.page_2)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollArea_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        # self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 76, 16))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_3.setObjectName("gridLayout3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setVerticalSpacing(20)
        self.frame_3 = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_3.addWidget(self.frame_3, 0, 0, 1, 1, QtCore.Qt.AlignVCenter)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_1)
        self.verticalLayout_7.addWidget(self.scrollArea)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget.addWidget(self.page_1)
        
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_8.addWidget(self.scrollArea_2)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget.addWidget(self.page_2)
        self.verticalLayout_6.addWidget(self.stackedWidget)
        self.horizontalLayout_2.addWidget(self.main_body)
        self.verticalLayout_2.addWidget(self.main)
        self.verticalLayout.addWidget(self.background)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Chevalkova", "Чевалкова"))
        self.menuButton.setText(_translate("MENU", "МЕНЮ"))
        self.ptButton.setText(_translate("Presentation", "Презентации"))
        self.videoButton.setText(_translate("Video", "Видео"))
        


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())