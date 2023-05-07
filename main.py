from PyQt5.QtWidgets import QApplication
from ui import MainWindow
from textCopy import ImageDiscover
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
    'ROUTE 4': None,
    'MT. MOON': None,
    'CERULEAN CITY': None,
    'ROUTE 24': None,
    'ROUTE 25': None,
    'ROUTE 5': None,
    'ROUTE 6': None,
    'VERMILION CITY': None,
    'ROUTE 11': None,
    'DIGLETTS CAVE': None,
    'ROUTE 9': None,
    'ROUTE 10': None,
    'ROCK TUNNEL': None,
    'POKÉMON TOWER': None,
    'ROUTE 12': None,
    'ROUTE 8': None,
    'ROUTE 7': None,
    'CELADON CITY': None,
    'SAFFRON CITY': None,
    'ROUTE 16': None,
    'ONE ISLAND':None,
    'TWO ISLAND':None,
    'THREE ISLAND':None,
    'BERRY FOREST':None,
    'BOND BRIDGE':None,
    'MOUNT EMBER':None,
    'ROUTE 18':None,
    'ROUTE 20':None,
    'KINDLE ROAD':None,
    'ROUTE 18':None,
    'SAFARI ZONE':None,
    'ROUTE 15':None

}
a = ImageDiscover(cordsDictionary=cordsDictionary, routeDict=routePokemonDict)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

    # Call the takeScreenshot function
