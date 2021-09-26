import QtQuick 6.0
import QtQuick.Controls	6.0
import QtQuick.Controls.Material 6.0

Button {
    id: menu_button

    property string button_text: "  Menu"
    property url icon_source: "qrc:/menu_icons/menu.png"
    
    flat: true
    highlighted: true
    Material.accent: Material.BlueGrey

    width: menu.width

    contentItem: Item {
        Row {
            leftPadding: 7.5
            bottomPadding: -5

            Image {
                source: icon_source
                width: 20
                height: 20
                anchors.verticalCenter: parent.verticalCenter
            }

            Text {
                text: button_text
                font.family: "Times New Roman"
                font.pointSize: 20
                anchors.verticalCenter: parent.verticalCenter
                color: "#ffffff"
            }
        }
    }
}