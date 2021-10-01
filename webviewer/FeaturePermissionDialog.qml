import QtQuick
import QtQuick.Controls
import QtQuick.Layouts


Dialog {
    property string origin: "origin"
    property int feature: -1

    title: qsTr("Feature request")
    modal: true
    standardButtons: Dialog.Yes | Dialog.No

    property var featureRequestNames: [qsTr("geolocation"),
        qsTr("audio capture"),
        qsTr("video capture"),
        qsTr("audio and video capture"),
        qsTr("desktop video capture"),
        qsTr("desktop audio and video capture"),
        qsTr("notifications")]

    RowLayout {
        anchors.fill: parent

        Label {
            text: qsTr("The site " + origin + " is requesting "
                  + "access for:\n"
                  + featureRequestNames[feature])
        }
    }
}
