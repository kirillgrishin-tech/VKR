# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainForm.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.SearchButton = QtWidgets.QPushButton(self.centralwidget)
        self.SearchButton.setGeometry(QtCore.QRect(50, 320, 120, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SearchButton.sizePolicy().hasHeightForWidth())
        self.SearchButton.setSizePolicy(sizePolicy)
        self.SearchButton.setMinimumSize(QtCore.QSize(120, 40))
        self.SearchButton.setMaximumSize(QtCore.QSize(120, 40))
        font = QtGui.QFont()
        font.setPointSize(5)
        self.SearchButton.setFont(font)
        self.SearchButton.setObjectName("SearchButton")
        self.table_search = QtWidgets.QTableView(self.centralwidget)
        self.table_search.setEnabled(True)
        self.table_search.setGeometry(QtCore.QRect(50, 110, 700, 200))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_search.sizePolicy().hasHeightForWidth())
        self.table_search.setSizePolicy(sizePolicy)
        self.table_search.setMinimumSize(QtCore.QSize(700, 200))
        self.table_search.setMaximumSize(QtCore.QSize(700, 200))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.table_search.setFont(font)
        self.table_search.setObjectName("table_search")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 200, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(5)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(280, 380, 100, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(5)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(300, 430, 100, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(5)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.NDVIButton = QtWidgets.QPushButton(self.centralwidget)
        self.NDVIButton.setGeometry(QtCore.QRect(380, 500, 350, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NDVIButton.sizePolicy().hasHeightForWidth())
        self.NDVIButton.setSizePolicy(sizePolicy)
        self.NDVIButton.setMinimumSize(QtCore.QSize(350, 50))
        self.NDVIButton.setMaximumSize(QtCore.QSize(300, 50))
        self.NDVIButton.setObjectName("NDVIButton")
        self.BrwEditNir = QtWidgets.QLineEdit(self.centralwidget)
        self.BrwEditNir.setEnabled(False)
        self.BrwEditNir.setGeometry(QtCore.QRect(380, 380, 280, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BrwEditNir.sizePolicy().hasHeightForWidth())
        self.BrwEditNir.setSizePolicy(sizePolicy)
        self.BrwEditNir.setMinimumSize(QtCore.QSize(200, 20))
        self.BrwEditNir.setMaximumSize(QtCore.QSize(280, 20))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.BrwEditNir.setFont(font)
        self.BrwEditNir.setObjectName("BrwEditNir")
        self.BrwEditRed = QtWidgets.QLineEdit(self.centralwidget)
        self.BrwEditRed.setEnabled(False)
        self.BrwEditRed.setGeometry(QtCore.QRect(380, 430, 280, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BrwEditRed.sizePolicy().hasHeightForWidth())
        self.BrwEditRed.setSizePolicy(sizePolicy)
        self.BrwEditRed.setMaximumSize(QtCore.QSize(280, 20))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.BrwEditRed.setFont(font)
        self.BrwEditRed.setObjectName("BrwEditRed")
        self.BrwButonNir = QtWidgets.QPushButton(self.centralwidget)
        self.BrwButonNir.setGeometry(QtCore.QRect(680, 380, 100, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BrwButonNir.sizePolicy().hasHeightForWidth())
        self.BrwButonNir.setSizePolicy(sizePolicy)
        self.BrwButonNir.setMinimumSize(QtCore.QSize(100, 20))
        self.BrwButonNir.setMaximumSize(QtCore.QSize(100, 20))
        font = QtGui.QFont()
        font.setPointSize(5)
        self.BrwButonNir.setFont(font)
        self.BrwButonNir.setObjectName("BrwButonNir")
        self.BrwButtonRed = QtWidgets.QPushButton(self.centralwidget)
        self.BrwButtonRed.setGeometry(QtCore.QRect(680, 430, 100, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BrwButtonRed.sizePolicy().hasHeightForWidth())
        self.BrwButtonRed.setSizePolicy(sizePolicy)
        self.BrwButtonRed.setMinimumSize(QtCore.QSize(100, 20))
        self.BrwButtonRed.setMaximumSize(QtCore.QSize(100, 20))
        font = QtGui.QFont()
        font.setPointSize(5)
        self.BrwButtonRed.setFont(font)
        self.BrwButtonRed.setObjectName("BrwButtonRed")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(380, 470, 100, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(100, 20))
        self.label_4.setMaximumSize(QtCore.QSize(100, 20))
        font = QtGui.QFont()
        font.setPointSize(5)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.SearchEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.SearchEdit.setGeometry(QtCore.QRect(60, 70, 100, 20))
        self.SearchEdit.setMinimumSize(QtCore.QSize(100, 20))
        self.SearchEdit.setMaximumSize(QtCore.QSize(100, 20))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.SearchEdit.setFont(font)
        self.SearchEdit.setObjectName("SearchEdit")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 80, 35, 10))
        font = QtGui.QFont()
        font.setPointSize(5)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.MinEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.MinEdit.setGeometry(QtCore.QRect(50, 450, 51, 20))
        self.MinEdit.setObjectName("MinEdit")
        self.MaxEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.MaxEdit.setGeometry(QtCore.QRect(140, 450, 51, 20))
        self.MaxEdit.setObjectName("MaxEdit")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(50, 420, 35, 10))
        font = QtGui.QFont()
        font.setPointSize(5)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(140, 420, 35, 10))
        font = QtGui.QFont()
        font.setPointSize(5)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(50, 370, 141, 31))
        self.label_8.setObjectName("label_8")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSearch = QtWidgets.QAction(MainWindow)
        self.actionSearch.setObjectName("actionSearch")
        self.actionNDVI = QtWidgets.QAction(MainWindow)
        self.actionNDVI.setObjectName("actionNDVI")
        self.actionBrwNir = QtWidgets.QAction(MainWindow)
        self.actionBrwNir.setObjectName("actionBrwNir")
        self.actionBrwRed = QtWidgets.QAction(MainWindow)
        self.actionBrwRed.setObjectName("actionBrwRed")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.SearchButton.setText(_translate("MainWindow", "Собрать данные"))
        self.label.setText(_translate("MainWindow", "Таблица проблемных регионов по округу"))
        self.label_2.setText(_translate("MainWindow", "Ближний ИФ"))
        self.label_3.setText(_translate("MainWindow", "Красный"))
        self.NDVIButton.setText(_translate("MainWindow", "NDVI"))
        self.BrwButonNir.setText(_translate("MainWindow", "обзор..."))
        self.BrwButtonRed.setText(_translate("MainWindow", "обзор..."))
        self.label_4.setText(_translate("MainWindow", "Рвссчитать NDVI"))
        self.label_5.setText(_translate("MainWindow", "Округ"))
        self.MinEdit.setText(_translate("MainWindow", "-1"))
        self.MaxEdit.setText(_translate("MainWindow", "1"))
        self.label_6.setText(_translate("MainWindow", "Мин."))
        self.label_7.setText(_translate("MainWindow", "Макс."))
        self.label_8.setText(_translate("MainWindow", "Классификация"))
        self.actionSearch.setText(_translate("MainWindow", "Search"))
        self.actionNDVI.setText(_translate("MainWindow", "NDVI"))
        self.actionBrwNir.setText(_translate("MainWindow", "BrwNir"))
        self.actionBrwRed.setText(_translate("MainWindow", "BrwRed"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
