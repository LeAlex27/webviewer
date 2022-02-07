import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import QtWebEngine
import Qt.labs.settings


Dialog {
    title: qsTr("Settings")
    modal: false
    standardButtons: Dialog.Close
    
    required property WebEngineProfile webEngineProfile
    property alias minimizeOnClose: minimizeOnCloseCheckBox.checked
    
    Settings {
        category: "settings"
        
        property alias minimizeOnClose: minimizeOnCloseCheckBox.checked
    }

    ColumnLayout {
        anchors.fill: parent

        CheckBox {
            id: minimizeOnCloseCheckBox
            text: qsTr("Minimize on close")
            checked: true
        }
        
        Label {
            text: storageName != "" ? qsTr("Storage name: " + storageName) : qsTr("Storage is not persistent.")
        }
        
        Label {
            text: "http user agent: " + webEngineProfile.httpUserAgent
        }
    }
}
