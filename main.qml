import QtQuick 2.13
import QtQuick.Window 2.13
import QtWebEngine 1.9
import Qt.labs.platform 1.1

Window {
    id: window
    visible: true
    width: 1280
    height: 800
    
    title: webEngineView.title
    
    WebEngineView {
        id: webEngineView
        anchors.fill: parent
        url: website
    }
    
    SystemTrayIcon {
        visible: true
        icon.source: webEngineView.icon

        menu: Menu {
            MenuItem {
                text: qsTr("Show window")
                onTriggered: {
                    window.show()
                    window.raise()
                }
            }
            MenuItem {
                text: qsTr("Quit")
                onTriggered: Qt.quit()
            }
        }
    }
}
