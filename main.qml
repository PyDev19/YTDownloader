import QtQuick 6.0
import QtQuick.Controls	6.0
import QtQuick.Controls.Material 6.0
import QtQuick.Layouts 6.0

import "qml_components"

ApplicationWindow {
    visible: true

    width: 1000
    height: 600
    maximumHeight: 600
    maximumWidth: 1000
    minimumHeight: 600
    minimumWidth: 1000

    title: "YT Downloader"
    id: window

    flags: Qt.Window | Qt.FramelessWindowHint

    Material.theme: Material.Dark

    property int previous_x
    property int previous_y

    QtObject{
        id: funtions

        function switch_screen(screen_index) {
            stack_layout.currentIndex = screen_index
        }

        function toggle_menu() {
            menu_animation.running = true
            top_bar_icon_animation.running = true

            if (menu.width == 50) {
                menu_toggle_button.icon_source = "qrc:/menu_icons/menu_icons/menu_2.png"
            } else {
                menu_toggle_button.icon_source = "qrc:/menu_icons/menu_icons/menu.png"
            }
        }
    }

    MouseArea {
        id: top_area
        height: 5
        
        anchors {
            top: parent.top
            left: parent.left
            right: parent.right
        }

        cursorShape: Qt.SizeVerCursor

        onPressed: {
            previous_y = mouseY
        }

        onMouseYChanged: {
            var dy = mouseY - previous_y
            window.setY(window.y + dy)
            window.setHeight(window.height - dy)
        }
    }

    MouseArea {
        id: bottom_area
        height: 5

        anchors {
            bottom: parent.bottom
            left: parent.left
            right: parent.right
        }

        cursorShape: Qt.SizeVerCursor
 
        onPressed: {
            previous_y = mouseY
        }
 
        onMouseYChanged: {
            var dy = mouseY - previous_y
            window.setHeight(window.height + dy)
        }
    }

    MouseArea {
        id: left_area
        width: 5

        anchors {
            top: top_area.bottom
            bottom: bottom_area.top
            left: parent.left
        }

        cursorShape: Qt.SizeHorCursor
 
        onPressed: {
            previous_x = mouseX
        }
 
        onMouseXChanged: {
            var dx = mouseX - previous_x
            window.setX(window.x + dx)
            window.setWidth(window.width - dx)
        }
    }

    MouseArea {
        id: right_area
        width: 5

        anchors {
            top: top_area.bottom
            bottom: bottom_area.top
            right: parent.right
        }

        cursorShape: Qt.SizeHorCursor
 
        onPressed: {
            previous_x = mouseX
        }
 
        onMouseXChanged: {
            var dx = mouseX - previous_x
            window.setWidth(window.width + dx)
        }
    }

    Rectangle {
        id: top_bar
        height: 50
        color: "#3d3d3d"
        
        anchors.left: parent.left
        anchors.right: parent.right
        anchors.top: parent.top
        anchors.rightMargin: 0
        anchors.leftMargin: 0
        anchors.topMargin: 0

        MouseArea {
            anchors.fill: parent
    
            onPressed: {
                previous_x = mouseX
                previous_y = mouseY
            }
    
            onMouseXChanged: {
                var dx = mouseX - previous_x
                window.setX(window.x + dx)
            }
    
            onMouseYChanged: {
                var dy = mouseY - previous_y
                window.setY(window.y + dy)
            }
        }


        Rectangle {
            id: top_bar_icon
            width: 50
            height: 50
            color: "#00000000"
            anchors.left: parent.left
            anchors.top: parent.top
            anchors.bottom: parent.bottom
            clip: true
            anchors.leftMargin: 0
            anchors.bottomMargin: 0
            anchors.topMargin: 0

            PropertyAnimation {
                id: top_bar_icon_animation
                target: top_bar_icon

                property: "width"
                to: if (top_bar_icon.width == 50) return 300; else return 50;

                duration: 500
                easing.type: Easing.InOutQuint
            }

            Image {
                id: image
                x: 5
                y: 5
                width: 42
                height: 42
                source: "qrc:/icons/icons/icon-32x32.png"
                fillMode: Image.PreserveAspectFit
            }

            Label {
                id: label
                width: 300
                color: "#ffffff"
                text: qsTr("Yt Downloader")

                anchors.left: image.right
                anchors.right: parent.right
                anchors.top: parent.top
                anchors.bottom: parent.bottom
                anchors.topMargin: 0
                anchors.bottomMargin: 0
                anchors.rightMargin: 5
                anchors.leftMargin: 5

                verticalAlignment: Text.AlignVCenter
                font.pointSize: 25
                font.family: "Times New Roman"
            }
        }

        TopBarButton {
            id: close_button
            icon_source: "qrc:/menu_icons/menu_icons/close.png"
            onClicked: window.close()
        }

        TopBarButton {
            id: minimize_button
            icon_source: "qrc:/menu_icons/menu_icons/minimize.png"
            anchor_right: close_button.left

            onClicked: {
                window.showMinimized()
            }
        }

        TopBarButton {
            id: setting_button
            icon_source: "qrc:/menu_icons/menu_icons/settings.png"
            anchor_right: minimize_button.left
        }

        Label {
            id: title

            text: qsTr("Yt Downloader - Youtube Video Downloader")

            anchors.verticalCenter: parent.verticalCenter
            anchors.left: top_bar_icon.right
            anchors.leftMargin: 15

            verticalAlignment: Text.AlignVCenter
            font.pointSize: 15
            font.family: "Times New Roman"
        }
    }

    // Side Bar Drawer Menu
    Rectangle {
        id: menu
        width: 50
        color: "#3d3d3d"
        clip: true

        anchors.left: parent.left
        anchors.top: top_bar.bottom
        anchors.bottom: parent.bottom
        anchors.bottomMargin: 0
        anchors.topMargin: 0
        anchors.leftMargin: 0

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

                onClicked: funtions.toggle_menu()
            }

            MenuButton {
                id: home_menu_button

                button_text: qsTr("  Home")
                icon_source: "qrc:/menu_icons/menu_icons/home.png"

                onClicked: funtions.switch_screen(0)
            }

            MenuButton {
                id: download_menu_button

                button_text: qsTr("  Download")
                icon_source: "qrc:/menu_icons/menu_icons/download.png"

                onClicked: funtions.switch_screen(1)
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
        anchors.top: top_bar.bottom
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
