import sys

from PySide6.QtCore import Qt, QUrl, QSettings, QCommandLineParser, QCommandLineOption
from PySide6.QtWidgets import QApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtWebEngineQuick import QtWebEngineQuick

import webviewer.resources
from webviewer import __version__


def _main():
    QApplication.setApplicationName("webviewer")
    QApplication.setApplicationVersion(__version__)
    QSettings.setDefaultFormat(QSettings.IniFormat)
    QtWebEngineQuick.initialize()

    app = QApplication(sys.argv)
    
    parser = QCommandLineParser()
    parser.setApplicationDescription("Displays a website in a window.")
    parser.addHelpOption()
    parser.addVersionOption()
    parser.addPositionalArgument("URL", "Address of the website to show.")
    parser.addOption(QCommandLineOption(["storage-name"],
                                        "Storage name for the web profile.", "storage name"));
    parser.addOption(QCommandLineOption(["strip-user-agent"],
                                        "Removes \"QtWebEngine/X.X.X\" from user agent."));
    parser.process(app)
   
    if len(parser.positionalArguments()) == 0:
        parser.showHelp()

    url = QUrl(parser.positionalArguments()[0])
    if url.isRelative():
        print("The given url has no scheme. Https is assumed.")
        url.setScheme('https')

    appEngine = QQmlApplicationEngine()
    appEngine.rootContext().setContextProperty("website", url)
    appEngine.rootContext().setContextProperty("storageName", parser.value("storage-name"))
    appEngine.rootContext().setContextProperty("stripUserAgent", parser.isSet("strip-user-agent"))
    appEngine.load(QUrl('qrc:/main.qml'))

    sys.exit(app.exec())


if __name__ == '__main__':
    _main()
