from PyQt5.QtWidgets import (QMainWindow, QFileDialog, QWidget,QMenuBar,
                             QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout, 
                             QAction, QLabel, QToolBar, QListWidget)
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt, QDir,QFileInfo
from PyQt5.QtGui import QKeySequence, QIcon


    
class MainWindow(QMainWindow):
    
    #self.ldw,self.mb,self.plot inherreted by V4g class
    
    def __init__(self):
        super().__init__()
        self.setMinimumSize(600,400)
        self.setContentsMargins(0,0,0,0)
        self.setContextMenuPolicy(Qt.NoContextMenu)
        
