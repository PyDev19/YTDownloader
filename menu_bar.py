import webbrowser
from tkinter import *

# toggle menu bool
menu_active: bool = False


def load(main, icons, menu_buttons_style, tabs, root):
    # menu frame
    menu_frame = Frame(main, bg="#21252B")
    menu_frame.place(relx=0, rely=0, relheight=1, width=58.4)

    # menu button
    menu_button = Button(menu_frame, menu_buttons_style, image=icons[0], text="Hide",
                         command=lambda: toggle_menu(root, menu_frame))
    menu_button.grid(column=0, row=0)

    # home button
    home_button = Button(menu_frame, menu_buttons_style, image=icons[1], text="Home",
                         command=lambda: select_screen(tabs, 0, home_button, download_button, menu_frame, root))
    home_button.grid(column=0, row=1)

    # download button
    download_button = Button(menu_frame, menu_buttons_style, image=icons[2], text="Download",
                             command=lambda: select_screen(tabs, 1, download_button, home_button, menu_frame, root))
    download_button.grid(column=0, row=2)

    # github button
    github_button = Button(menu_frame, menu_buttons_style, image=icons[3], text="GitHub",
                           command=lambda: webbrowser.open("https://github.com/YamiAtem/YTDownloader", new=0,
                                                           autoraise=True))
    github_button.grid(column=0, row=3)

    # website button
    website_button = Button(menu_frame, menu_buttons_style, image=icons[4], text="App Website",
                            command=lambda: webbrowser.open("https://yamiatem.github.io/YTDownloader/", new=0,
                                                            autoraise=True))
    website_button.grid(column=0, row=4)

    # update button
    update_button = Button(menu_frame, menu_buttons_style, image=icons[5], text="Latest Update",
                           command=lambda: webbrowser.open("https://github.com/YamiAtem/YTDownloader/releases",
                                                           new=0, autoraise=True))
    update_button.grid(column=0, row=5)


# open and close of menu
def toggle_menu(root, menu_frame):
    global menu_active

    if not menu_active:
        for i in range(int(58.4), 301, 5):
            menu_frame.place(width=i)
            root.update()

        menu_active = True
    elif menu_active:
        for i in range(300, int(56), -3):
            menu_frame.place(width=i)
            root.update()

        menu_active = False


# switch to home screen
def select_screen(tabs, index, button, button_2, frame, root):
    global menu_active

    tabs.select(index)
    button.configure(bg="#282C34")
    button_2.configure(bg="#21252B")

    if menu_active:
        for i in range(300, int(56), -3):
            frame.place(width=i)
            root.update()

        menu_active = False
