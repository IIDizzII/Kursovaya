from PyQt5.QtWidgets import *
from PyQt5.Qt import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys


class SearchHighLight(QSyntaxHighlighter):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.pattern = QRegularExpression()
        self.format = QTextCharFormat()
        self.format.setBackground(Qt.green)

    def highlightBlock(self, text):
        match_iterator = self.pattern.globalMatch(text)
        while match_iterator.hasNext():
            match = match_iterator.next()
            self.setFormat(match.capturedStart(), match.capturedLength(), self.format)

    def searchText(self, text):
        self.pattern = QRegularExpression(text)
        self.rehighlight()
