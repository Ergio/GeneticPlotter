import sys
 
from PyQt5.QtWidgets import QSizePolicy

 
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
from calc import GenConst,GeneCalc,ChartCalc

class PlotCanvas(FigureCanvas):
 
    def __init__(self, parent=None, width=6, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
 
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
 
        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.FileName ="no file"
        
        
    def loadFile(self):
        self.seq = GenConst()
        self.seq.genome_read(self.FileName)
        
 
    def plot(self):
        
        genObj = GeneCalc(self.current_codon,self.seq.genes)
        genObj.calcSubseqPos()
        
        calcObj = ChartCalc(genObj.positions_in_gene)
        calcObj.subseqDensity()
        data = calcObj.data4plot
        
        ax = self.figure.add_subplot(111)
        ax.clear()
        ax.plot(data, 'r-',label = self.current_codon)
        ax.set_title(self.current_codon)
        
        legend = ax.legend(loc = 'upper right', fontsize = 'x-large')
        legend.get_frame().set_facecolor("#00FFCC")
        self.draw()
        
        
        #self.print_png("plot.png")
        
    def replot_chart(self,str):
        self.current_codon = str
        self.plot()
