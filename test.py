import os
import pickle
import Character
import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *

basdir = os.path.dirname(__file__)




class list_model(QAbstractListModel):
    def __init__(self, lst={}):
        super().__init__()
        self._list = list(lst.keys()) or {}
    
    def data(self, index, role = ...):
        if role == Qt.DisplayRole:
            text = self._list[index.row()]
            return text
    
    def rowCount(self, index):
        return len(self._list)

class MainWindow(QMainWindow):
    def __init__(self):

        self.character_path_name ={"Ben": "here", "Cat": "There"}
        super().__init__()
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.model = list_model(self.character_path_name)
        self.modelView = QListView()
        self.modelView.setModel(self.model)

        self.line_edit = QLineEdit()
        self.quitbutton = QPushButton("Quit")
        self.quitbutton.pressed.connect(self.close)


        self.set_button = QPushButton("Set")
        self.set_button.pressed.connect(self.add)






        self.central_layout = QGridLayout()
        self.central_widget.setLayout(self.central_layout)
        self.central_layout.addWidget(QLabel("Hello"), 0,0)
        self.central_layout.addWidget(self.modelView,1,0)
        self.central_layout.addWidget(self.line_edit,2,0)
        self.central_layout.addWidget(self.set_button,3,0)
        self.central_layout.addWidget(self.quitbutton,4,0)

    def add(self):
        #adds an item to the model
        text = self.line_edit.text()
        text = text.strip()
        if text:
            self.model._list.append((False, text))
            self.model.layoutChanged.emit()
            self.line_edit.setText("")


def main():
    app = QApplication()
    window = MainWindow()
    window.show()

    sys.exit(app.exec())

if __name__ == '__main__':
    main()