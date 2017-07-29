
from PyQt5.QtWidgets import (QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout, 
                             QLabel,QListWidget,QStyleFactory,QDockWidget,
                             QSpacerItem,QWidget,QListWidgetItem)
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt

from calc import GenConst
from widgets.leftdock_widget import LeftDockWidget

class LeftDock(LeftDockWidget):

    def __init__(self):
        super().__init__()
        
        