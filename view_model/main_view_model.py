from PyQt5.QtWidgets import (QMainWindow, QFileDialog, QWidget,QMenuBar,
                             QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout, 
                             QAction, QLabel, QToolBar, QListWidget)
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt, QDir,QFileInfo
from PyQt5.QtGui import QKeySequence, QIcon

from model.v4g import V4g

    
class MainViewModel(V4g):
    
    #self.ldw,self.mb,self.plot inherreted by V4g class
    
    def __init__(self):
        
        super().__init__()

        #self.ldwEvents()
        self.mbEvents()
        #self.tbEvents()
        
    def tbEvents(self):
        print("no events")

    def ldwEvents(self):
        #  draw the plot
        self.ldw.PushB_make.clicked.connect(self.replot)
        
        self.ldw.PushB_options.clicked.connect(self.openOptions)
        
        
    def mbEvents(self):
        #  draw the plot
        root = QFileInfo(__file__).absolutePath()
        self.mb.plot = self.plot
        
        self.mb.savePlotAct1 = QAction(QIcon(root + '/images/save.png'), "&Save as png",
                self.mw, shortcut=QKeySequence.Save,
                statusTip="Save a plot", 
                triggered = self.mb.savePlotPNG)
         
        self.mb.plotMenu.addAction(self.mb.savePlotAct1)
        
        self.mb.openAct = QAction(QIcon(root + '/images/open.png'), "&Open...",
                self.mw, shortcut=QKeySequence.Open,
                statusTip="Open an existing file", triggered=self.openFile)
        self.mb.fileMenu.addAction(self.mb.openAct)
        
        
        
        
