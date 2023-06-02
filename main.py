from PyQt5.QtWidgets import QApplication
from autolocke.ui import MainWindow, TipsDialog, TutorialSteps
from autolocke.textCopy import ImageDiscover
import sys
import time


cordsDictionary = {
    'Route':[242, 47, 745, 121],
    'Pokemon':[300, 110, 450, 121],
    'Caught':[270, 800, 380, 207]
}



routePokemonDict = {
    'PALLET TOWN': None,
    'ROUTE 1': None,
    'VIRIDIAN CITY': None,
    'ROUTE 22': None,
    'ROUTE 2': None,
    'VIRIDIAN FOREST': None,
    'ROUTE 3': None,
    'MT. MOON': None,
    'ROUTE 4': None,
    'CERULEAN CITY': None,
    'ROUTE 24': None,
    'ROUTE 25': None,
    'ROUTE 5': None,
    'ROUTE 6': None,
    'VERMILION CITY': None,
    'S.S. ANNE': None,
    'ROUTE 11': None,
    'DIGLETTS CAVE': None,
    'ROUTE 9': None,
    'ROUTE 10': None,
    'ROCK TUNNEL': None,
    'LAVENDER TOWN':None,
    'ROUTE 8': None,
    'ROUTE 7': None,
    'CELADON CITY': None,
    'TEAM ROCKET HIDEOUT':None,
    'POKEMON TOWER':None,
    'SAFFRON CITY': None,
    'FUCHSIA CITY':None,
    'SAFARI ZONE':None,
    'ROUTE 12':None,
    'ROUTE 13':None,
    'ROUTE 14':None,
    'ROUTE 15':None,
    'SILPH CO.':None,
    'ROUTE 16': None,
    'ROUTE 17':None,
    'ROUTE 18':None,
    'POWER PLANT':None,
    'ROUTE 19':None,
    'ROUTE 20':None,
    'SEAFOAM ISLANDS':None,
    'CINNABAR ISLAND':None,
    'ROUTE 21':None,
    'ONE ISLAND':None,
    'TWO ISLAND':None,
    'THREE ISLAND':None,
    'BERRY FOREST':None,
    'BOND BRIDGE':None,
    'CAPE BRINK':None,
    'KINDLE ROAD':None,
    'MOUNT EMBER':None,
    'VIRIDIAN GYM':None,
    'VICTORY ROAD':None,
}
a = ImageDiscover(cordsDictionary=cordsDictionary, routeDict=routePokemonDict)



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
