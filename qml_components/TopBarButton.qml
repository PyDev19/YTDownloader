import QtQuick 6.0
import QtQuick.Controls	6.0
import QtQuick.Controls.Material 6.0
import QtQuick.Layouts 6.0

Button {
    property url icon_source: "qrc:/menu_icons/menu_icons/close.png"
    property var anchor_right: parent.right

    width: 34
    height: 34

    anchors.verticalCenter: parent.verticalCenter
    anchors.right: anchor_right
    anchors.rightMargin: 20

    Image {
        source: icon_source

        anchors.verticalCenter: parent.verticalCenter
        anchors.horizontalCenter: parent.horizontalCenter
    }
}