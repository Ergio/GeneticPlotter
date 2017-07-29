
from PyQt5.QtWidgets import (QTextEdit, QPushButton, QVBoxLayout, QTableWidget, 
                             QLabel,QStyleFactory,QDockWidget, QDialog,
                             QSpacerItem,QWidget,QListWidgetItem, QAbstractItemView)
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt, QAbstractItemModel, QModelIndex

from calc import GenConst

class LeftDockWidget(QDockWidget):

    def __init__(self):
        super().__init__()
        
        self.setFeatures(QDockWidget.NoDockWidgetFeatures)
        self.setFixedWidth(300)
        self.tbw = LeftDockWidgetMain()
        self.setWidget(self.tbw)
        

class LeftDockWidgetMain(QWidget):
    def __init__(self):
        super().__init__()
        file_data = ["name","genes","kb"]
        self.vb = QVBoxLayout()

        self.tableWidget = QTableWidget(1,4)
        self.tableWidget.setHorizontalHeaderLabels(file_data)
        self.tableWidget.setCurrentCell(-1, -1)
        self.tableWidget.setSelectionMode(QAbstractItemView.NoSelection)

        

        for week in range(2):
            for day in range(2):
                index = self.tableWidget.model().index(week, day);
                
                self.tableWidget.model().setData(index, "data");


        self.vb.addWidget(self.tableWidget)
        self.add1 = QPushButton("add")
        
        self.vb.addWidget(self.add1)
        self.add1.clicked.connect(lambda : self.tableWidget.setRowCount(self.tableWidget.rowCount()+1))
        self.setLayout(self.vb)
        


