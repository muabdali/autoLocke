import json
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QPushButton, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Table to JSON')
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


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
