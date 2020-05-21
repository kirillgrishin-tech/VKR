from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui     import *
from PyQt5.QtCore    import *
from PyQt5.QtWidgets import *
from MainForm_ui import Ui_MainWindow
from search import Search
from rastr import Rastr
import shapefile
import sys

class TaskModel(QtCore.QAbstractTableModel):
    def __init__(self, tasks):
        super().__init__()
        self.__tasks = tasks
        self.__headers = ["Область", "Кол-во упом.", "Долгота", "Широта"]

    def rowCount(self, *args, **kwargs):
        return len(self.__tasks)

    def columnCount(self, *args, **kwargs):
        coln = len(self.__tasks[0])
        return coln

    def headerData(self, section, orientation, role):
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                return self.__headers[section]
            else:
                return "%s" % str(section+1)

    def data(self, index, role):
        row = index.row()
        col = index.column()
        value = self.__tasks[row][col]
        if role == QtCore.Qt.DisplayRole:
            return value


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        try:
            super(mywindow, self).__init__()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)
            self.ui.SearchButton.clicked.connect(self.on_search)
            self.ui.NDVIButton.clicked.connect(self.on_NDVI)
            self.ui.BrwButonNir.clicked.connect(self.on_Nir)
            self.ui.BrwButtonRed.clicked.connect(self.on_Red)
        except:
           self.Error()
    
    def on_search(self):
        if len(self.ui.SearchEdit.text())>0:
            self.avb = Search(self.ui.SearchEdit.text())
            w = shapefile.Writer('cities.shp',shapeType=1)
            w.field("Местность","C")
            for i in range(len(self.avb)):
                w.point(float(self.avb[i][2]),float(self.avb[i][3]))
                w.record(self.avb[i][0])
            w.close()
            self.b= TaskModel(self.avb)
            self.ui.table_search.setModel(self.b)
        else:
            self.Error(0)

    def Error(self,nm):
            txt = ['округ','ближний ИФ','красный','диапозонов']
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Ошибка")
            msg.setInformativeText('Введены некоректные данные в поле '+txt[nm])
            msg.setWindowTitle("Ошибка")
            msg.exec_()
    
    def on_Nir(self):
        dr,frm = QFileDialog.getOpenFileName(self,"Выбрать папку",".","TIFF Files(*.tif *.tiff)")
        if len(dr)>0:
            self.ui.BrwEditNir.setText(dr)
        else:
            self.Error(1)

    def on_Red(self):
        dr,frm = QFileDialog.getOpenFileName(self,"Выбрать папку",".","TIFF Files(*.tif *.tiff)")
        if len(dr)>0:
            self.ui.BrwEditRed.setText(dr)
        else:
            self.Error(2)

    def on_NDVI(self):
        if len(self.ui.BrwEditNir.text())>0 and len(self.ui.BrwEditRed.text())>0 and len(self.ui.MinEdit.text())>0 and len(self.ui.MaxEdit.text())>0:
            Rastr(self.ui.BrwEditNir.text(),self.ui.BrwEditRed.text(),float(self.ui.MinEdit.text()),float(self.ui.MaxEdit.text()))
        else:
            if len(self.ui.BrwEditNir.text())==0:
                self.Error(1)
            if len(self.ui.BrwEditRed.text())==0:
                self.Error(2)
            if len(self.ui.MinEdit.text())==0 or self.ui.MaxEdit.text()==0:
                self.Error(3)

app = QtWidgets.QApplication([])
application = mywindow()
application.show()
sys.exit(app.exec_())