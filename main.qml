import QtQuick 6.0
import QtQuick.Controls	6.0
import QtQuick.Controls.Material 6.0
import QtQuick.Layouts 6.0

import "qml_components"

ApplicationWindow {
    visible: true
    width: 800
    height: 600
    title: "YT Downloader"
    id: window

    Material.theme: Material.Dark

    // Side Bar Drawer Menu
    Rectangle {
        id: menu
        width: 50
        color: "#3d3d3d"

        anchors.left: parent.left
        anchors.top: parent.top
        anchors.bottom: parent.bottom

        clip: true

        anchors.topMargin: 0
        anchors.bottomMargin: 0
        anchors.leftMargin: 0

        function switch_screen(screen_index) {
            stack_layout.currentIndex = screen_index
        }

        PropertyAnimation {
            id: menu_animation
            target: menu

            property: "width"
            to: if (menu.width == 50) return 300; else return 50;

            duration: 500
            easing.type: Easing.InOutQuint
        }

        Column {
            id: menu_column

            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: parent.top
            anchors.bottom: parent.bottom

            clip: true

            anchors.rightMargin: 0
            anchors.leftMargin: 0
            anchors.bottomMargin: 90
            anchors.topMargin: 0

            MenuButton {
                id: menu_toggle_button

                button_text: qsTr("  Menu")
                icon_source: "qrc:/menu_icons/menu_icons/menu.png"

                function toggle_menu() {
                    menu_animation.running = true
                    if (menu.width == 50) {
                        menu_toggle_button.icon_source = "qrc:/menu_icons/menu_icons/menu_2.png"
                    } else {
                        menu_toggle_button.icon_source = "qrc:/menu_icons/menu_icons/menu.png"
                    }
                }

                onClicked: toggle_menu()
            }

            MenuButton {
                id: home_menu_button

                button_text: qsTr("  Home")
                icon_source: "qrc:/menu_icons/menu_icons/home.png"

                onClicked: menu.switch_screen(0)
            }

            MenuButton {
                id: download_menu_button

                button_text: qsTr("  Download")
                icon_source: "qrc:/menu_icons/menu_icons/download.png"

                onClicked: menu.switch_screen(1)
            }

            MenuButton {
                id: github_menu_button

                button_text: qsTr("  Github")
                icon_source: "qrc:/menu_icons/menu_icons/github.png"

                onClicked: Qt.openUrlExternally("https://github.com/PyDev19");
            }

            MenuButton {
                id: repo_menu_button

                button_text: qsTr("  Repository")
                icon_source: "qrc:/menu_icons/menu_icons/repository.png"

                onClicked: Qt.openUrlExternally("https://github.com/PyDev19/YTDownloader/");
            }
        }
    }

    // Stack Layout
    StackLayout{
        id: stack_layout

        anchors.left: menu.right
        anchors.right: parent.right
        anchors.top: parent.top
        anchors.bottom: parent.bottom
        anchors.rightMargin: 0
        anchors.topMargin: 0
        anchors.leftMargin: 0
        anchors.bottomMargin: 0
        
        currentIndex: 0

        HomeScreen {
            id: home_screen
        }

        DownloadScreen {
            id: download_screen
        }
    }
}
