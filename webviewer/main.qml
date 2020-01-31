import QtQuick 2.14
import QtQuick.Window 2.14
import QtWebEngine 1.10
import Qt.labs.platform 1.1
import Qt.labs.settings 1.0


Window {
    id: window
    visible: true
    width: 1280
    height: 800
    
    title: webEngineView.title

    Settings {
        category: "window"

        property alias x: window.x
        property alias y: window.y
        property alias width: window.width
        property alias height: window.height
    }
    
    WebEngineView {
        id: webEngineView
        anchors.fill: parent
        url: website

        onFeaturePermissionRequested: {
            featurePermissionDialog.origin = securityOrigin.toString()
            featurePermissionDialog.feature = feature
            featurePermissionDialog.open()
        }
    }

    FeaturePermissionDialog {
        id: featurePermissionDialog
        anchors.centerIn: parent

        onAccepted: {
            webEngineView.grantFeaturePermission(origin, feature, true)
        }

        onRejected: {
            webEngineView.grantFeaturePermission(origin, feature, false)
        }
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
                text: qsTr("Hide window")
                onTriggered: window.hide()
            }
            MenuItem {
                text: qsTr("Quit")
                onTriggered: Qt.quit()
            }
        }
    }
}
