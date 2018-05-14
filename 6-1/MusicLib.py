# Music Lib v1.0
# Copyright.2018ChanwooPark
import display
import options

display.startmenu()
option = raw_input('Enter option : ')
while True:
    if option == 's' or option == 'S':
        options.searchMusic()
        display.startmenu2()
        option = raw_input('Enter option : ')
    elif option == 'a' or option == 'A':
        options.addMusic()
        display.startmenu2()
        option = raw_input('Enter option : ')
    elif option == 'r' or option == 'R':
        options.removeMusic()
        display.startmenu2()
        option = raw_input('Enter option : ')
    elif option == 'l' or option == 'L':
        options.musicList()
        display.startmenu2()
        option = raw_input('Enter option : ')
    elif option == 'x' or option == 'X':
        break
    else:
        option = raw_input('Wrong option. Please type again : ')
