import os
import main_menu
import channel
import playlist
import video
import ui

choice = 1

ui.create_window()

while (choice != 0):
    if (os.name == "posix"):
        _ = os.system('clear')
    choice = main_menu.main_menu()
    if (choice == 1):
        channel.download()
    if (choice == 2):
        playlist.download()
    if (choice == 3):
        video.download()
print("Program Ended")