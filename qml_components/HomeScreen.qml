import QtQuick 6.0
import QtQuick.Controls	6.0
import QtQuick.Controls.Material 6.0
import QtQuick.Layouts 6.0

Rectangle {
    color: "#303030"

    anchors.left: menu.right
    anchors.right: parent.right
    anchors.top: parent.top
    anchors.bottom: parent.bottom
    anchors.rightMargin: 0
    anchors.leftMargin: 0
    anchors.bottomMargin: 0
    anchors.topMargin: 0

    Image {
        id: home_screen_image

        anchors.verticalCenter: parent.verticalCenter
        anchors.horizontalCenter: parent.horizontalCenter

        horizontalAlignment: Image.AlignHCenter
        verticalAlignment: Image.AlignVCenter

        source: "qrc:/icons/icons/icon-512x512.png"
    }
}