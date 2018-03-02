# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 13:44:54 2018

@author: Bandi
"""

from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog

import nibabel as nib
import sys

class Ui_MainWindow(QMainWindow): 

    
    def __init__(self):
        super(Ui_MainWindow,self).__init__()
        
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(None, "QFileDialog.getOpenFileNames()", "","All Files (*);;Nifti files (*.nii.gz)", options=options)
        image = nib.load(files[0])  
        image_data = image.get_data()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Ui_MainWindow()
    #centralWidget = QWidget()
    
    window.show()
    sys.exit(app.exec_())        