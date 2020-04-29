#!/usr/bin/env python3

import sys
import re

from PySide2.QtCore import Qt, QUrl, QCommandLineParser, QSettings
from PySide2.QtWidgets import QApplication
from PySide2.QtQml import QQmlApplicationEngine
from PySide2.QtWebEngine import QtWebEngine

import webviewer.resources
from webviewer import __version__


def has_no_scheme(url):
    match = re.search("\\w+:", url)
    return (match is None) or (match.span()[0] > 0)


def _main():
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QtWebEngine.initialize()
    
    app = QApplication(sys.argv)
    app.setApplicationName("webviewer")
    app.setOrganizationName("webviewer")
    app.setOrganizationDomain("webviewer")
    app.setApplicationVersion(__version__)

    QSettings.setDefaultFormat(QSettings.IniFormat)
    
    parser = QCommandLineParser()
    parser.setApplicationDescription("Displays a website in a window.")
    parser.addHelpOption()
    parser.addVersionOption()
    parser.addPositionalArgument("URL", "Address of the website to show.")
    parser.process(app)    
   
    if len(parser.positionalArguments()) == 0:
        parser.showHelp()
        
    rawUrl = parser.positionalArguments()[0]
    if has_no_scheme(rawUrl):
        print("The given url has no scheme. Https is assumed.")
        rawUrl = "https://" + rawUrl
    url = QUrl(rawUrl)

    appEngine = QQmlApplicationEngine()
    appEngine.rootContext().setContextProperty("website", url)
    appEngine.load('qrc:/main.qml')
    
    sys.exit(app.exec_())


if __name__ == '__main__':
    _main()
