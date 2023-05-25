import json
import threading
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from PyQt5 import QtCore
from autolocke.textCopy import ImageDiscover
from PyQt5.QtCore import QTimer, Qt, QStringListModel
from PyQt5.QtGui import QMovie, QFont, QFontDatabase
from time import sleep
import os

cordsDictionary = {
    'Route':[242, 47, 745, 121],
    'Pokemon':[300, 110, 450, 121],
    'Caught':[270, 800, 380, 207]
}


with open('autolocke\Data\data.json') as json_filePoke:
    routePokemonDict = json.load(json_filePoke)

ab = ImageDiscover(cordsDictionary=cordsDictionary,routeDict=routePokemonDict)


class TipsDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Tips')
        layout = QVBoxLayout()
        self.setWindowIcon(QtGui.QIcon('autolocke/UI/logo.png'))


        # Create a QHBoxLayout layout for the top right side of the dialog
        top_layout = QHBoxLayout()

        # Create a QLabel widget and set the QMovie as its pixmap

        gif_label = QLabel()
        gif_movie = QMovie('autolocke/UI/479.gif')
        gif_label.setMovie(gif_movie)
        gif_movie.start()
        gif_label.setAlignment(Qt.AlignCenter)

        # Set the stylesheet of the parent widget to position the GIF label absolutely
        self.setLayout(layout)
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)

        # Add the tips label and next button to the main QVBoxLayout layout
        label2 = QLabel('Here are some tips:\n\nTip 1 - Make sure to keep the tracker anchored to the TOP RIGHT of the Emulator.\nTip 2 - So far, the tracker only works for Pokemon Fire Red and Leaf Green\nTip 3 - If you have any issues or suggestions, please open a discussion on https://github.com/muabdali/autoLocke')
        label2.setFont(QFont("Verdana"))
        layout.addWidget(label2)
        next_button = QPushButton('Next')
        next_button.clicked.connect(self.close)  # Close the dialog
        layout.addWidget(next_button)

        selectLabel = QLabel('Select your game version')
        top_layout.addWidget(selectLabel)
        selectGameVersion = QComboBox()
        top_layout.addWidget(selectGameVersion)
        layout.addLayout(top_layout)
        

        # Add the GIF label to the main QVBoxLayout layout
        layout.addWidget(gif_label)




class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('autoLocke')
        self.table = QTableWidget()
        self.load_button = QPushButton('Load')
        self.save_button = QPushButton('Save')
        self.clear_button = QPushButton('Clear')
        self.edit_button = QRadioButton('Edit')
        self.clear_button.clicked.connect(self.delete_all_values)
        self.load_button.clicked.connect(self.load_json_file)
        self.save_button.clicked.connect(self.save_json_file)
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)
        layout.addWidget(self.table)
        layout.addWidget(self.load_button)
        layout.addWidget(self.save_button)
        layout.addWidget(self.clear_button)
        layout.addWidget(self.edit_button)
        self.edit_button.setStyleSheet('QRadioButton { text-align: center; }')
        self.setCentralWidget(central_widget)
        self.data = {}
        self.load_json_file()
        self.timer = QTimer()
        self.timer.timeout.connect(self.screenshotLoop)
        self.timer.timeout.connect(self.load_json_file)
        self.timer.start(250)
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
        self.setWindowIcon(QtGui.QIcon('autolocke/UI/logo.png'))


    def load_json_file(self):
        if self.edit_button.isChecked():
            return
        with open('autolocke\Data\data.json', 'r') as f:
            self.data = json.load(f)
        self.table.setRowCount(len(self.data))
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(['Location', 'Pokemon'])
        row = 0
        print("JSONLOAD")
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
        with open('autolocke\Data\data.json', 'w') as f:
            json.dump(self.data, f, indent=4)

    def delete_all_values(self):
        self.edit_button.setChecked(True)
        with open('autolocke\Data\data.json', 'r') as f:
            self.data = json.load(f)
        self.table.setRowCount(len(self.data))
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(['Location', 'Pokemon'])
        row = 0
        for location, pokemon in self.data.items():
            self.table.setItem(row, 0, QTableWidgetItem(location))
            self.table.setItem(row, 1, QTableWidgetItem(None))   
            row += 1
            self.save_json_file

    def screenshotLoop(self):
        route_thread = threading.Thread(target=self.analyzeRoute)
        caught_thread = threading.Thread(target=self.analyzeCaught)
        route_thread.start()
        caught_thread.start()


    def analyzeRoute(self):
        currentRouteSS = ab.takeScreenshot('Route')
        imagePath = os.path.join('autolocke', 'Images', 'routeImage.png')
        currentRouteAN = ab.screenshotAnalyze(imagePath)
        print(currentRouteAN)

    def analyzeCaught(self):
        pokemonCaughSS = ab.takeScreenshot('Caught')
        imagePath = os.path.join('autolocke', 'Images', 'CaughtImage.png')
        pokemonCaught = ab.screenshotAnalyze(imagePath)
        if pokemonCaught is not None:
            self.data['Caught'] = pokemonCaught
            self.load_json_file()




if __name__ == '__main__':
    app = QApplication([])
    with open('style.qss', 'r') as f:
        style = f.read()
    app.setStyleSheet(style)
    tips_dialog = TipsDialog()
    tips_dialog.exec()
    window = MainWindow()
    window.show()
    app.exec_()
