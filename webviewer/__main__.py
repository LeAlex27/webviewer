import sys

from PySide6.QtCore import Qt, QUrl, QCommandLineParser, QSettings
from PySide6.QtWidgets import QApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtWebEngineQuick import QtWebEngineQuick

import webviewer.resources
from webviewer import __version__


def _main():
    QtWebEngineQuick.initialize()
    
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
        
    url = QUrl(parser.positionalArguments()[0])
    if url.isRelative():
        print("The given url has no scheme. Https is assumed.")
        url.setScheme('https')

    appEngine = QQmlApplicationEngine()
    appEngine.rootContext().setContextProperty("website", url)
    appEngine.load('qrc:/main.qml')
    
    sys.exit(app.exec())


if __name__ == '__main__':
    _main()
