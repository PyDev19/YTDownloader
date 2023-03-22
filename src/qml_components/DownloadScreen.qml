import QtQuick 6.0
import QtQuick.Controls	6.1
import QtQuick.Controls.Material 6.0
import QtQuick.Layouts 6.0
import Qt.labs.platform 1.1

Rectangle {
    id: download_screen
    color: "#303030"

    anchors.left: menu.right
    anchors.right: parent.right
    anchors.top: parent.top
    anchors.bottom: parent.bottom
    anchors.rightMargin: 0
    anchors.leftMargin: 0
    anchors.bottomMargin: 0
    anchors.topMargin: 0

    Popup {
        id: popup
        width: 700
        height: 500
        modal: true
        focus: true

        property string error_code: "internet_disconnected"
        
        anchors.centerIn: parent

        closePolicy: Popup.CloseOnEscape | Popup.CloseOnPressOutsideParent
        
        Image {
            id: internet_disconnected_icon

            source: "qrc:/icons/icons/internet_disconnected.png"
        }

        Label {
            id: internet_disconnected_title

            text: qsTr("You're not connected to the internet")
            font {
                bold: true
                family: "Times New Roman"
                pointSize: 25
            }

            anchors{
                top: internet_disconnected_icon.bottom
                topMargin: 25
            }
        }

        Label {
            id: internet_disconnected_try

            text: qsTr("Try: ")
            font {
                bold: true
                family: "Times New Roman"
                pointSize: 15
            }

            anchors{
                top: internet_disconnected_icon.bottom
                topMargin: 70
            }
        }

        Label {
            id: internet_disconnected_suggestion_1

            text: qsTr("  Checking your network cables, modem, and routers")
            font {
                family: "Times New Roman"
                pointSize: 15
            }

            anchors{
                top: internet_disconnected_icon.bottom
                topMargin: 100
            }
        }

        Label {
            id: internet_disconnected_suggestion_2
            text: qsTr("  Reconnecting to your wireless network")
            font {
                family: "Times New Roman"
                pointSize: 15
            }

            anchors{
                top: internet_disconnected_icon.bottom
                topMargin: 130
            }
        }

        Label {
            id: internet_disconnected_suggestion_3
            text: qsTr("  Running Windows Network Diagnostics")
            font {
                family: "Times New Roman"
                pointSize: 15
            }

            anchors{
                top: internet_disconnected_icon.bottom
                topMargin: 160
            }
        }

        Button{
            id: retry_button

            font.family: "Times New Roman"
            font.pointSize: 25
            text: "Retry"

            anchors.top: parent.top
            anchors.left: parent.left

            anchors.leftMargin: 575
            anchors.topMargin: 425

            onClicked: {
                popup.close()
                
                if (backend.check_internet()) {
                    popup.open()
                }
            }
        }
    }

    FolderDialog {
        id: folder_dialog

        onAccepted: {
            var path = folder_dialog.folder.toString();
            path = path.replace(/^(file:\/{3})/,"");

            output_dir_field.text = path
        }
    }

    TextField {
        id: link_field
        height: 52

        placeholderText: "Youtube Link"

        font.family: "Times New Roman"
        font.pixelSize: 30
        wrapMode: Text.Wrap

        horizontalAlignment: Text.AlignLeft
        verticalAlignment: Text.AlignVCenter

        anchors.left: parent.left
        anchors.right: parent.right
        anchors.top: parent.top

        anchors.rightMargin: 100
        anchors.leftMargin: 100
        anchors.topMargin: 75

        Material.accent: Material.Cyan
    }

    TextField {
        id: file_name_field
        height: 52

        placeholderText: "File Name"

        font.family: "Times New Roman"
        font.pixelSize: 30
        wrapMode: Text.Wrap

        horizontalAlignment: Text.AlignLeft
        verticalAlignment: Text.AlignVCenter

        anchors.left: parent.left
        anchors.right: parent.right
        anchors.top: link_field.bottom

        anchors.rightMargin: 100
        anchors.leftMargin: 100
        anchors.topMargin: 25

        Material.accent: Material.Cyan
    }

    TextField {
        id: output_dir_field
        height: 52

        placeholderText: "Output Directory"

        font.family: "Times New Roman"
        font.pixelSize: 30
        wrapMode: Text.Wrap

        horizontalAlignment: Text.AlignLeft
        verticalAlignment: Text.AlignVCenter

        anchors.left: parent.left
        anchors.right: parent.right
        anchors.top: file_name_field.bottom

        anchors.rightMargin: 100
        anchors.leftMargin: 100
        anchors.topMargin: 25

        Material.accent: Material.Cyan
    }

    Button {
        id: choose_directory_button

        text: "Choose Output Directory"
        font.family: "Times New Roman"
        font.pointSize: 25

        anchors.left: parent.left
        anchors.right: parent.right
        anchors.top: output_dir_field.bottom

        anchors.rightMargin: 150
        anchors.leftMargin: 150
        anchors.topMargin: 25

        onClicked: folder_dialog.open()
    }

    Button {
        id: download_button

        text: "Download Video"
        font.family: "Times New Roman"
        font.pointSize: 25

        anchors.left: parent.left
        anchors.right: parent.right
        anchors.top: choose_directory_button.bottom

        anchors.rightMargin: 150
        anchors.leftMargin: 150
        anchors.topMargin: 25

        onClicked: {
            console.log(backend.check_internet());
            if (backend.check_internet()) {
                popup.open()
            }
        }
    }
}
