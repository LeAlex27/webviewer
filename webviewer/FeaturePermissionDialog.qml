import QtQuick 2.14
import QtQuick.Controls 2.14
import QtQuick.Layouts 1.14


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
