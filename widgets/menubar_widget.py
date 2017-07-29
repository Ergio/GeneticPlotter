from PyQt5.QtWidgets import QMenuBar


class MenuBarWidget(QMenuBar):

    def __init__(self):
        super().__init__()
        self.fileMenu = self.addMenu("&File")
        self.addSeparator()
        self.plotMenu = self.addMenu("&Plot")
        self.addSeparator()
        self.helpMenu = self.addMenu("&Help")
    

        

