import json
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QPushButton, QVBoxLayout, QWidget
from textCopy import ImageDiscover
from PyQt5.QtCore import QTimer

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

ab = ImageDiscover(cordsDictionary=cordsDictionary,routeDict=routePokemonDict)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('autoLocke')
        self.table = QTableWidget()
        self.load_button = QPushButton('Load')
        self.save_button = QPushButton('Save')
        self.load_button.clicked.connect(self.load_json_file)
        self.save_button.clicked.connect(self.save_json_file)
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)
        layout.addWidget(self.table)
        layout.addWidget(self.load_button)
        layout.addWidget(self.save_button)
        self.setCentralWidget(central_widget)
        self.data = {}
        self.load_json_file()
        self.timer = QTimer()
        self.timer.timeout.connect(self.screenShotloop)
        self.timer.timeout.connect(self.load_json_file)
        self.timer.start(300)

    def load_json_file(self):
        with open('data.json', 'r') as f:
            self.data = json.load(f)
        self.table.setRowCount(len(self.data))
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(['Location', 'Pokemon'])
        row = 0
        for location, pokemon in self.data.items():
            self.table.setItem(row, 0, QTableWidgetItem(location))
            self.table.setItem(row, 1, QTableWidgetItem(pokemon))
            row += 1

    def save_json_file(self):
        for row in range(self.table.rowCount()):
            location_item = self.table.item(row, 0)
            pokemon_item = self.table.item(row, 1)
            location = location_item.text()
            pokemon = pokemon_item.text()
            self.data[location] = pokemon
        with open('data.json', 'w') as f:
            json.dump(self.data, f, indent=4)

    def screenShotloop(self):
        ab.takeScreenshot('Route')
        print("taken1")
        ab.screenshotAnalyze('routeImage.png')
        ab.takeScreenshot('Caught')
        ab.screenshotAnalyze('CaughtImage.png')
        print('taken2')





if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()

