from PyQt5.QtWidgets import QApplication
from autolocke.ui import MainWindow, TipsDialog, TutorialSteps
from autolocke.textCopy import ImageDiscover
import sys
import time


"""
Main file for initializing the GUI (ui.py) and therefore the rest of the 
functions.

stylesheet:
with open('autolocke\style.qss', 'r') as f:

"""

if __name__ == '__main__':
    app = QApplication([])
    with open('autolocke\style.qss', 'r') as f:
        style = f.read()
    app.setStyleSheet(style)
    tutorial1 = TutorialSteps()
    tutorial1.exec()
    tips_dialog = TipsDialog()
    tips_dialog.exec()
    window = MainWindow()
    window.show()
    app.exec_()
