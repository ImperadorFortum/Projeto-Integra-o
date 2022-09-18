from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QHeaderView
from PyQt5 import uic




FILE_UI = 'view/main_window.ui'


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi(FILE_UI, self)
