import sys
from PyQt5.QtWidgets import QApplication, QStyleFactory
from view_model.main_view_model import MainViewModel 
from PyQt5.QtCore import Qt, QDir,QFileInfo, QFile, QTextStream
from PyQt5.QtGui import QKeySequence, QIcon, QPalette, QColor


if __name__ == '__main__':

    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create("Fusion"))

 # setup stylesheet
    file = QFile("light.qss")
    file.open(QFile.ReadOnly | QFile.Text)
    stream = QTextStream(file)
    app.setStyleSheet(stream.readAll())

    ex = MainViewModel()
    sys.exit(app.exec_())
    