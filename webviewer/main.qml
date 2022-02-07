import QtQuick
import QtQuick.Window
import QtWebEngine
import Qt.labs.platform
import Qt.labs.settings


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

        Component.onCompleted: {
            if (stripUserAgent) {
                console.log("stripping user agent of QtWebEngine information")
                var newUserAgent = profile.httpUserAgent.replace(/QtWebEngine\/[0-9|.]* /, '')
                console.log("user agent:", profile.httpUserAgent);
                console.log("new user agent:", newUserAgent);
                profile.httpUserAgent = newUserAgent;
            }

            if (storageName != "") {
                profile.offTheRecord = false;
                profile.storageName = storageName;
                console.log("persistentStoragePath:", profile.persistentStoragePath)
            }
        }

        onFeaturePermissionRequested: function(securityOrigin, feature) {
            featurePermissionDialog.origin = securityOrigin.toString();
            featurePermissionDialog.feature = feature;
            featurePermissionDialog.open();
        }

        onNewWindowRequested: function(request) {
            if (request.userInitiated)
                Qt.openUrlExternally(request.requestedUrl);
        }

        Connections {
            target: webEngineView.profile

            function onPresentNotification(notification) {
                systemTrayIcon.showMessage(notification.title,
                                           notification.message,
                                           webEngineView.icon,
                                           2000);
            }
        }
    }

    SettingsDialog {
        id: settingsDialog
        webEngineProfile: webEngineView.profile
        anchors.centerIn: parent
    }

    FeaturePermissionDialog {
        id: featurePermissionDialog
        anchors.centerIn: parent

        onAccepted: webEngineView.grantFeaturePermission(origin, feature, true)
        onRejected: webEngineView.grantFeaturePermission(origin, feature, false)
    }
    
    SystemTrayIcon {
        id: systemTrayIcon
        visible: true
        icon.source: webEngineView.icon

        menu: Menu {
            MenuItem {
                text: qsTr("Show window")
                onTriggered: {
                    window.show();
                    window.raise();
                }
            }
            MenuItem {
                text: qsTr("Hide window")
                onTriggered: window.hide()
            }
            MenuItem {
                text: qsTr("Settings")
                onTriggered: settingsDialog.open()
            }
            MenuItem {
                text: qsTr("Quit")
                onTriggered: Qt.quit()
            }
        }

        onActivated: function(reason) {
            if (reason === SystemTrayIcon.Trigger) {
                window.show();
                window.raise();
            }
        }
    }

    onClosing: function(close) {
        if (settingsDialog.minimizeOnClose) {
            close.accepted = false;
            hide();
        }
    }
}
