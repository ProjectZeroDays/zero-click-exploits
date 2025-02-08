import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt
from archive.archive_analyzer import analyze_sources

class ArchiveGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Archive Analyzer')

        layout = QVBoxLayout()

        button = QPushButton('Analyze Sources')
        button.clicked.connect(self.analyze_sources)
        layout.addWidget(button)

        self.setLayout(layout)

    def analyze_sources(self):
        analyze_sources()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ArchiveGUI()
    ex.show()
    sys.exit(app.exec_())
