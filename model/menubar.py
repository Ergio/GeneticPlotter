from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QWidget
from PyQt5.QtWidgets import (QTextEdit, QPushButton, QMessageBox, QHBoxLayout, 
                             QAction, QLabel, QMenuBar, QAction,  QListWidget,
                             QStyleFactory)
from PyQt5.QtGui import QKeySequence, QIcon
from PyQt5.QtCore import Qt,QFile,QTextStream, QDir,QFileInfo
# ToolBar
class MenuBar(QMenuBar):

    def __init__(self):
        super().__init__()
        
        self.currentFile = "No opened files found"
        
        self.aboutAct = QAction("&About", self,
                statusTip="Show the application's About box",
                triggered=self.about)
        
      

        
        

        
        self.init_ui()
        

    def init_ui(self):
        
        self.fileMenu = self.addMenu("&File")
        
        
        self.addSeparator()
                
        self.plotMenu = self.addMenu("&Plot")

        self.addSeparator()

        self.helpMenu = self.addMenu("&Help")
        self.helpMenu.addAction(self.aboutAct)
    
    def about(self):
        QMessageBox.about(self, "About Application",
                "The <b>Application</b> example demonstrates how to write "
                "modern GUI applications using Qt, with a menu bar, "
                "toolbars, and a status bar.")

        
    def savePlotPNG(self):
        format = 'png'
        initialPath = QDir.currentPath() + "/untitled." + format

        fileName, _ = QFileDialog.getSaveFileName(self, "Save As", initialPath,
                "%s Files (*.%s);;All Files (*)" % (format.upper(), format))
        if fileName:
            self.plot.print_png(fileName)

        

