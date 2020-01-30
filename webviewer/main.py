#!/usr/bin/env python3

import sys
from PySide2.QtCore import QUrl, QCommandLineParser
from PySide2.QtWidgets import QApplication
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtWebEngine import QtWebEngine

import webviewer.resources


def _main():
    QtWebEngine.initialize()
    
    app = QApplication(sys.argv)
    app.setApplicationName("webviewer")
    app.setApplicationVersion("0.0.0.1")
    
    parser = QCommandLineParser()
    parser.setApplicationDescription("Displays a website in a window.")
    parser.addHelpOption()
    parser.addVersionOption()
    parser.addPositionalArgument("URL", "Address of the website to show.")
    parser.process(app)    
   
    if len(parser.positionalArguments()) == 0:
        parser.showHelp()
        
    url = QUrl(parser.positionalArguments()[0])
    
    appEngine = QQmlApplicationEngine()
    appEngine.rootContext().setContextProperty("website", url)
    appEngine.load('qrc:/main.qml')
    
    sys.exit(app.exec_())


if __name__ == '__main__':
    _main()
