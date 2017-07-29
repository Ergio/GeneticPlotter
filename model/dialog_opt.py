from PyQt5.QtWidgets import (QDialog,QPushButton, QVBoxLayout, QHBoxLayout,
                             QRadioButton, QLineEdit,QButtonGroup)

class DialogOptions(QDialog):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle(u"Options")
        self.resize(200, 300)
        
        
        self.init_ui()
        self.bg.buttonClicked.connect(self.lineEditStat)
        
    def init_ui(self):
        self.ok_b = QPushButton("Ok")
        self.cancel_b = QPushButton("Cancel")
        
        self.triplets_b = QRadioButton("triplets")
        self.tetraplets_b = QRadioButton("tetraplets")
        self.subseq_b = QRadioButton("subseqence")
        self.subseq_ed = QLineEdit()
        self.lineEditStat()
        
        
        
        ####
        
        self.triplets_b.setChecked(True)
        
        self.bg = QButtonGroup()
        self.bg.addButton(self.triplets_b)
        self.bg.addButton(self.tetraplets_b)
        self.bg.addButton(self.subseq_b)
        
        
        
            
        ####
        main_layout = QVBoxLayout()
        
        
        
        end_hl = QHBoxLayout()
        end_hl.addWidget(self.ok_b)
        end_hl.addWidget(self.cancel_b)
        
        
        
        
        subseq_hl = QHBoxLayout()
        subseq_hl.addWidget(self.subseq_b)
        subseq_hl.addWidget(self.subseq_ed)
        
        rb_vl = QVBoxLayout()
        rb_vl.addWidget(self.triplets_b)
        rb_vl.addWidget(self.tetraplets_b)
        rb_vl.addLayout(subseq_hl)
        
        
        
        main_layout.addLayout(rb_vl)
        main_layout.addLayout(end_hl)
        self.setLayout(main_layout)
        
    def lineEditStat(self):
        if(self.subseq_b.isChecked()):
            self.subseq_ed.setReadOnly(False)
        else:
            self.subseq_ed.setReadOnly(True)
            self.subseq_ed.setText("")