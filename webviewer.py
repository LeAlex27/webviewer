#!/usr/bin/env python3

import sys
from PySide2.QtCore import QObject, QUrl, Signal, Property, QCommandLineParser
from PySide2.QtWidgets import QApplication
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtWebEngine import QtWebEngine


class Url(QObject):
    def __init__(self, url=''):
        super(Url, self).__init__()
        self._url = url
        
    def _url(self):
        return self._url
    
    @Signal
    def url_changed(self):
        pass
    
    url = Property(QUrl, _url, notify=url_changed)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationName("webviewer")
    app.setApplicationVersion("0.0.0.1")
    
    parser = QCommandLineParser()
    parser.addHelpOption()
    parser.addVersionOption()
    parser.addPositionalArgument("url", "help message")
    parser.process(app)
    
    QtWebEngine.initialize()
    
    url = Url(QUrl(parser.positionalArguments()[0]))
    
    appEngine = QQmlApplicationEngine()
    appEngine.rootContext().setContextProperty("website", url)
    appEngine.load('main.qml')
    
    sys.exit(app.exec_())
