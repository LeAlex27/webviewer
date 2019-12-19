#!/usr/bin/env python3

import sys
from PySide2.QtCore import QObject, QUrl, Signal, Property, QCommandLineParser
from PySide2.QtWidgets import QApplication
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtWebEngine import QtWebEngine


def _main():
    QtWebEngine.initialize()
    
    app = QApplication(sys.argv)
    app.setApplicationName("webviewer")
    app.setApplicationVersion("0.0.0.1")
    
    parser = QCommandLineParser()
    parser.addHelpOption()
    parser.addVersionOption()
    parser.addPositionalArgument("url", "help message")
    parser.process(app)    
   
    url = QUrl(parser.positionalArguments()[0])
    
    appEngine = QQmlApplicationEngine()
    appEngine.rootContext().setContextProperty("website", url)
    appEngine.load('main.qml')
    
    sys.exit(app.exec_())

if __name__ == '__main__':
    _main()
