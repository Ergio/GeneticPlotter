from widgets.toolbar_widget import ToolBarWidget
from PyQt5.QtCore import Qt

class ToolBar(ToolBarWidget):

    def __init__(self):
        super().__init__()
        self.setContextMenuPolicy(Qt.NoContextMenu)