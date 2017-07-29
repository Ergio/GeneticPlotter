from PyQt5.QtWidgets import (QMainWindow, QFileDialog, QWidget,QMenuBar,
                             QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout, 
                             QAction, QLabel, QMessageBox, QListWidget)
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt, QDir,QFileInfo
from PyQt5.QtGui import QKeySequence, QIcon

from model.mainwindow import MainWindow
from model.leftdock import LeftDock
from model.chart import PlotCanvas
from model.menubar import MenuBar
from model.dialog_opt import DialogOptions
from model.toolbar import ToolBar

class V4g:

    def __init__(self):
        self.mw = MainWindow()
        self.plot = PlotCanvas()
        self.mb = MenuBar()
        self.tb = ToolBar()
        self.tb.setContextMenuPolicy(Qt.NoContextMenu)
        self.do = DialogOptions()
        self.ldw = LeftDock()
        self.init_ui()

    def init_ui(self):
        self.mw.setCentralWidget(self.plot)
        self.mw.setMenuBar(self.mb)
        self.mw.addToolBar(Qt.LeftToolBarArea, self.tb)
        self.mw.addDockWidget(Qt.LeftDockWidgetArea,self.ldw,Qt.Vertical)
        
        self.mw.show()
        
#  update plot for current codon, binds the plot and toolbar
    def replot(self):
        if ((self.mb.currentFile == "No opened files found")):
            msg = QMessageBox()
            msg.setWindowTitle("MessageBox")
            
            
            
            msg.setIcon(QMessageBox.Information)
            msg.setText("You can`t make a chart now!")
            msg.setInformativeText("No opened files found.")
            
            msg.setDetailedText("No opened files found. Click on File -> Open... in MenuBar and choose the file.")
            msg.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
            msg.exec_()
        else:
            if(self.plot.FileName != self.mb.currentFile):
                self.plot.FileName = self.mb.currentFile
                self.plot.loadFile()
                
            self.plot.replot_chart(self.ldw.current_codon())
        
    
    


        
    def openFile(self):
        fileName = QFileDialog.getOpenFileName(self)[0]
        #TODO:dick
        self.mb.currentFile =  fileName.replace("/","//")
        if(self.mb.currentFile.__len__()<1):
            self.mb.currentFile =  "No opened files found"
        self.ldw.labelFile.setText(self.mb.currentFile.split("//")[-1])
    
    
    def openOptions(self):
        
        self.do.ok_b.clicked.connect(self.do.close)
        self.do.cancel_b.clicked.connect(self.do.close)
        self.do.exec_()
