import json
import threading
from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore, QtWidgets
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
currentGen = None
currentGenDirectory = None

# TODO- Change save button so that file explorer pops up, and prompts user to save data.json to new location.

class TipsDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Tips')
        layout = QVBoxLayout()
        self.setWindowIcon(QtGui.QIcon('autolocke/UI/logo.png'))
        self.clasCurrentGen = None

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
        next_button.clicked.connect(self.convertGenJson)
        layout.addWidget(next_button)

        selectLabel = QLabel('Select your game version')
        top_layout.addWidget(selectLabel)
        self.selectGameVersion = QComboBox()
        top_layout.addWidget(self.selectGameVersion)
        layout.addLayout(top_layout)
        self.selectGameVersion.addItem("")        
        self.selectGameVersion.addItem("Fire Red")
        self.selectGameVersion.addItem("Emerald")
        self.selectGameVersion.currentTextChanged.connect(self.changeGen)
        layout.addWidget(gif_label)

    def changeGen(self, value):
        global currentGenDirectory
        self.clasCurrentGen = value
        if value == "Fire Red":
            print("FR")
            self.clasCurrentGen = 'autolocke//Data//fireredroutes.txt'
            currentGenDirectory = self.clasCurrentGen            
        elif value == "Emerald":
            self.clasCurrentGen = 'autolocke//Data//emeraldroutes.txt'
            currentGenDirectory = self.clasCurrentGen
        return currentGenDirectory, currentGen
    
    def convertGenJson(self):
        global currentGenDirectory
        currentGenDirectory = self.clasCurrentGen  # Assign returned values to variables
        print("GEN" + currentGenDirectory)
        with open(currentGenDirectory, 'r') as f:
            routes = f.read().splitlines()
        route_dict = {route: None for route in routes}
        json_data = json.dumps(route_dict, indent=4)
        with open('autolocke/Data/data.json', 'w') as file:
            file.write(json_data)




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
        self.save_button.clicked.connect(self.save_json_file_buttonFunction)
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
        self.timer = QTimer()
        self.timer.timeout.connect(self.screenshotLoop)
        self.timer.timeout.connect(self.reload_given_json)
        self.timer.start(250)
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
        self.setWindowIcon(QtGui.QIcon('autolocke/UI/logo.png'))
        # self.file_path is the current file path for the data.json VERY IMPORTANT FOR NEXT PATCH
        self.file_path = 'autolocke/Data/data.json'

    def reload_given_json(self):
        if self.edit_button.isChecked():
            return
        with open(self.file_path, 'r') as f:
            self.data = json.load(f)
        self.table.setRowCount(len(self.data))
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(['Location', 'Pokemon'])
        row = 0
        print("JSONRE")
        for location, pokemon in self.data.items():
            self.table.setItem(row, 0, QTableWidgetItem(location))
            self.table.setItem(row, 1, QTableWidgetItem(pokemon))
            row += 1


        



    def load_json_file(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Select JSON File", "", "JSON Files (*.json)", options=options
        )

        if file_path:
            try:
                with open(file_path, 'r') as source_file:
                    data = json.load(source_file)
                with open('autolocke/Data/data.json', 'w') as destination_file:
                    json.dump(data, destination_file, indent=4)
                print("Data loaded and saved to data.json")
                self.file_path = 'autolocke/Data/data.json'  # Update the file path
                self.reload_given_json()  # Reload the data in the table
            except Exception as e:
                print(f"Error loading and saving data: {e}")
        else:
            print("No file selected. Operation canceled.")

    def save_json_file(self):
        for row in range(self.table.rowCount()):
            location_item = self.table.item(row, 0)
            pokemon_item = self.table.item(row, 1)
            location = location_item.text()
            pokemon = pokemon_item.text()
            self.data[location] = pokemon
        with open('autolocke\Data\data.json', 'w') as f:
            json.dump(self.data, f, indent=4)

# i dont know how, i dont want to know how, but for whatever reason adding any type of self variable to this function breaks the overall UI execution and closes the whole application
# DO NOT TOUCH V
    def save_json_file_buttonFunction(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getSaveFileName(None, "Save File", "", "All Files (*);;Text Files (*.txt)", options=options)
        
        if file_path:
            try:
                with open('autolocke/Data/data.json', 'r') as source_file:
                    data = source_file.read()
                with open(file_path, 'w') as destination_file:
                    destination_file.write(data)
                print("Data saved to:", file_path)
            except Exception as e:
                print(f"Error saving data: {e}")
        else:
            print("No file selected. Operation canceled.")

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
        currentRouteAN = ab.screenshotAnalyze(imagePath, currentDirectory=currentGenDirectory)
        print(currentRouteAN)

    def analyzeCaught(self):
        pokemonCaughSS = ab.takeScreenshot('Caught')
        imagePath = os.path.join('autolocke', 'Images', 'CaughtImage.png')
        pokemonCaught = ab.screenshotAnalyze(imagePath, currentDirectory=currentGenDirectory)
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
