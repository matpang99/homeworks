# options in menu


# change nothing into '-', change blank into '_'
def word_str(word):
    if word == '':
        word = '-'
    else:
        for i in range(len(word)):
            if word[i] == ' ':
                word = word[:i]+'_'+word[i+1:]
    return word


# make LIST from lib.txt
def lib_list(number):
    lib = open('lib.txt', 'r')
    wholeList = lib.readlines()
    lib.close()
    listOfList = []
    for i in range(len(wholeList)):
        listOfList.append(wholeList[i][0:len(wholeList[i])-1].split())
    keyList = []
    for j in range(len(listOfList)):
        keyList.append(listOfList[j][number] + str(j))
    keyList.sort()
    listOfList2 = []
    for k in range(len(listOfList)):
        listOfList2.append(listOfList[int(keyList[k][-1])])
    return listOfList2


# add music
def addMusic():
    print '''
***********************************************************************************
**                                                                               **
**                              >>> Add Music <<<                                **
**                                                                               **
***********************************************************************************
'''
    while True:
        name = word_str(raw_input('Enter the NAME of the song : '))
        artist = word_str(raw_input('Enter the ARTIST of the song : '))
        album = word_str(raw_input('Enter the ALBUM name of the song : '))
        genre = word_str(raw_input('Enter the GENRE of the song : '))
        print
        print '<Information you entered>'
        print '* NAME   : ' + name
        print '* ARTIST : ' + artist
        print '* ALBUM  : ' + album
        print '* GENRE  : ' + genre
        while True:
            print 'Correct? ( Y ) Yes  ( N ) No  ( C ) Cancel'
            answer = raw_input()
            if answer == 'Y' or answer == 'y' or answer == 'N' or answer =='n' or answer == 'C' or answer == 'c':
                break
            else:
                print 'Enter option Y or N or C.'
        if answer == 'Y' or answer == 'y':
            lib = open('lib.txt', 'a')
            data = name + ' ' + artist + ' ' + album + ' ' + genre + '\n'
            lib.write(data)
            lib.close()
            print 'Added successfully!'
            while True:
                print 'Add more? ( Y ) Yes ( N ) No'
                answer2 = raw_input()
                if answer2 == 'Y' or answer2 == 'y' or answer2 == 'N' or answer2 == 'n':
                    break
                else:
                    print 'Please type Y or N.'
            if answer2 == 'Y' or answer2 == 'y':
                continue
            if answer2 == 'N' or answer2 == 'n':
                break
        elif answer == 'N' or answer == 'n':
            print 'Enter the information again.'
            continue
        elif answer == 'C' or answer == 'c':
            while True:
                print 'Add more? ( Y ) Yes ( N ) No'
                answer3 = raw_input()
                if answer3 == 'Y' or answer3 == 'y' or answer3 == 'N' or answer3 == 'n':
                    break
                else:
                    print 'Please type Y or N.'
            if answer3 == 'Y' or answer3 == 'y':
                continue
            if answer3 == 'N' or answer3 == 'n':
                break


# search music
def searchMusic():
    display = '''
***********************************************************************************
**                                                                               **
**                            >>> Search Music <<<                               **
**                                                                               **
**             >>> ( N ) by NAME of the song                                     **
**             >>> ( A ) by ARTIST of the song                                   **
**             >>> ( L ) by ALBUM name of the song                               **
**             >>> ( G ) by GENRE of the song                                    **
**             >>> ( C ) Cancel                                                  **
**                                                                               **
***********************************************************************************
'''
    print display
    option = raw_input('Enter option : ')
    while True:
        if option == 'N' or option == 'n':
            while True:
                nameSearch = word_str(raw_input('Search : '))
                print
                nameList=[]
                for i in range(len(lib_list(0))):
                    nameList.append(lib_list(0)[i][0])
                for j in range(len(nameList)):
                    if nameSearch.lower() in nameList[j].lower():
                        print ' / '.join(lib_list(0)[j])
                while True:
                    print
                    print 'Search by NAME again? ( Y ) Yes. ( N ) No.'
                    answer = raw_input()
                    if answer == 'Y' or answer == 'y' or answer == 'N' or answer == 'n':
                        break
                    else:
                        print 'Please type Y or N.'
                if answer == 'Y' or answer == 'y':
                    continue
                if answer == 'N' or answer == 'n':
                    break
            print display
            option = raw_input('Enter option : ')
        elif option == 'A' or option == 'a':
            while True:
                artistSearch = word_str(raw_input('Search : '))
                print
                artistList=[]
                for i in range(len(lib_list(1))):
                    artistList.append(lib_list(1)[i][1])
                for j in range(len(artistList)):
                    if artistSearch.lower() in artistList[j].lower():
                        print ' / '.join(lib_list(1)[j])
                while True:
                    print
                    print 'Search by ARTIST again? ( Y ) Yes. ( N ) No.'
                    answer2 = raw_input()
                    if answer2 == 'Y' or answer2 == 'y' or answer2 == 'N' or answer2 == 'n':
                        break
                    else:
                        print 'Please type Y or N.'
                if answer2 == 'Y' or answer2 == 'y':
                    continue
                if answer2 == 'N' or answer2 == 'n':
                    break
            print display
            option = raw_input('Enter option : ')
        elif option == 'L' or option == 'l':
            while True:
                albumSearch = word_str(raw_input('Search : '))
                print
                albumList=[]
                for i in range(len(lib_list(2))):
                    albumList.append(lib_list(2)[i][2])
                for j in range(len(albumList)):
                    if albumSearch.lower() in albumList[j].lower():
                        print ' / '.join(lib_list(2)[j])
                while True:
                    print
                    print 'Search by ALBUM again? ( Y ) Yes. ( N ) No.'
                    answer3 = raw_input()
                    if answer3 == 'Y' or answer3 == 'y' or answer3 == 'N' or answer3 == 'n':
                        break
                    else:
                        print 'Please type Y or N.'
                if answer3 == 'Y' or answer3 == 'y':
                    continue
                if answer3 == 'N' or answer3 == 'n':
                    break
            print display
            option = raw_input('Enter option : ')
        elif option == 'G' or option == 'g':
            while True:
                genreSearch = word_str(raw_input('Search : '))
                print
                genreList=[]
                for i in range(len(lib_list(3))):
                    genreList.append(lib_list(3)[i][3])
                for j in range(len(genreList)):
                    if genreSearch.lower() in genreList[j].lower():
                        print ' / '.join(lib_list(3)[j])
                while True:
                    print
                    print 'Search by GENRE again? ( Y ) Yes. ( N ) No.'
                    answer4 = raw_input()
                    if answer4 == 'Y' or answer4 == 'y' or answer4 == 'N' or answer4 == 'n':
                        break
                    else:
                        print 'Please type Y or N.'
                if answer4 == 'Y' or answer4 == 'y':
                    continue
                if answer4 == 'N' or answer4 == 'n':
                    break
            print display
            option = raw_input('Enter option : ')
        elif option == 'C' or option == 'c':
            break
        else:
            option = raw_input('Wrong option. Please type again : ')


# music list
def musicList():
    display = '''
***********************************************************************************
**                                                                               **
**                              >>> Music List <<<                               **
**                                                                               **
**             >>> ( N ) sort by NAME of the song                                **
**             >>> ( A ) sort by ARTIST of the song                              **
**             >>> ( L ) sort by ALBUM name of the song                          **
**             >>> ( G ) sort by GENRE of the song                               **
**             >>> ( C ) Cancel                                                  **
**                                                                               **
***********************************************************************************
'''
    print display
    option = raw_input('Enter option : ')
    while True:
        if option == 'N' or option == 'n':
            while True:
                while True:
                    print 'Sort in which order? ( A ) Ascending ( D ) Descending'
                    sortOfN = raw_input()
                    if sortOfN == 'A' or sortOfN == 'a' or sortOfN == 'D' or sortOfN == 'd':
                        break
                    else:
                        print 'Please type A or D.'
                print
                if sortOfN == 'A' or sortOfN == 'a':
                    for i in range(len(lib_list(0))):
                        print ' / '.join(lib_list(0)[i])
                if sortOfN == 'D' or sortOfN == 'd':
                    for i in range(len(lib_list(0))):
                        print ' / '.join(lib_list(0)[len(lib_list(0))-1-i])
                print
                while True:
                    print 'Sort by NAME again? ( Y ) Yes. ( N ) No.'
                    answer = raw_input()
                    if answer == 'Y' or answer == 'y' or answer == 'N' or answer == 'n':
                        break
                    else:
                        print 'Please type Y or N.'
                if answer == 'Y' or answer == 'y':
                    continue
                if answer == 'N' or answer == 'n':
                    break
            print display
            option = raw_input('Enter option : ')
        elif option == 'A' or option == 'a':
            while True:
                while True:
                    print 'Sort in which order? ( A ) Ascending ( D ) Descending'
                    sortOfA = raw_input()
                    if sortOfA == 'A' or sortOfA == 'a' or sortOfA == 'D' or sortOfA == 'd':
                        break
                    else:
                        print 'Please type A or D.'
                print
                if sortOfA == 'A' or sortOfA == 'a':
                    for i in range(len(lib_list(1))):
                        print ' / '.join(lib_list(1)[i])
                if sortOfA == 'D' or sortOfA == 'd':
                    for i in range(len(lib_list(1))):
                        print ' / '.join(lib_list(1)[len(lib_list(1))-1-i])
                print
                while True:
                    print 'Sort by ARTIST again? ( Y ) Yes. ( N ) No.'
                    answer2 = raw_input()
                    if answer2 == 'Y' or answer2 == 'y' or answer2 == 'N' or answer2 == 'n':
                        break
                    else:
                        print 'Please type Y or N.'
                if answer2 == 'Y' or answer2 == 'y':
                    continue
                if answer2 == 'N' or answer2 == 'n':
                    break
            print display
            option = raw_input('Enter option : ')
        elif option == 'L' or option == 'l':
            while True:
                while True:
                    print 'Sort in which order? ( A ) Ascending ( D ) Descending'
                    sortOfL = raw_input()
                    if sortOfL == 'A' or sortOfL == 'a' or sortOfL == 'D' or sortOfL == 'd':
                        break
                    else:
                        print 'Please type A or D.'
                print
                if sortOfL == 'A' or sortOfL == 'a':
                    for i in range(len(lib_list(2))):
                        print ' / '.join(lib_list(2)[i])
                if sortOfL == 'D' or sortOfL == 'd':
                    for i in range(len(lib_list(2))):
                        print ' / '.join(lib_list(2)[len(lib_list(2))-1-i])
                print
                while True:
                    print 'Sort by ALBUM again? ( Y ) Yes. ( N ) No.'
                    answer3 = raw_input()
                    if answer3 == 'Y' or answer3 == 'y' or answer3 == 'N' or answer3 == 'n':
                        break
                    else:
                        print 'Please type Y or N.'
                if answer3 == 'Y' or answer3 == 'y':
                    continue
                if answer3 == 'N' or answer3 == 'n':
                    break
            print display
            option = raw_input('Enter option : ')
        elif option == 'G' or option == 'g':
            while True:
                while True:
                    print 'Sort in which order? ( A ) Ascending ( D ) Descending'
                    sortOfG = raw_input()
                    if sortOfG == 'A' or sortOfG == 'a' or sortOfG == 'D' or sortOfG == 'd':
                        break
                    else:
                        print 'Please type A or D.'
                print
                if sortOfG == 'A' or sortOfG == 'a':
                    for i in range(len(lib_list(3))):
                        print ' / '.join(lib_list(3)[i])
                if sortOfG == 'D' or sortOfG == 'd':
                    for i in range(len(lib_list(3))):
                        print ' / '.join(lib_list(3)[len(lib_list(3))-1-i])
                print
                while True:
                    print 'Sort by GENRE again? ( Y ) Yes. ( N ) No.'
                    answer4 = raw_input()
                    if answer4 == 'Y' or answer4 == 'y' or answer4 == 'N' or answer4 == 'n':
                        break
                    else:
                        print 'Please type Y or N.'
                if answer4 == 'Y' or answer4 == 'y':
                    continue
                if answer4 == 'N' or answer4 == 'n':
                    break
            print display
            option = raw_input('Enter option : ')
        elif option == 'C' or option == 'c':
            break
        else:
            option = raw_input('Wrong option. Please type again : ')


# remove music
def removeMusic():
    display = '''
***********************************************************************************
**                                                                               **
**                            >>> Remove Music <<<                               **
**                                                                               **
**             >>> ( N ) Search the NAME of the song                             **
**             >>> ( A ) Search the ARTIST of the song                           **
**             >>> ( L ) Search the ALBUM name of the song                       **
**             >>> ( G ) Search the GENRE of the song                            **
**             >>> ( C ) Cancel                                                  **
**                                                                               **
***********************************************************************************
'''
    print display
    option = raw_input('Enter option : ')
    while True:
        if option == 'N' or option == 'n':
            while True:
                nameSearch = word_str(raw_input('Search : '))
                print
                nameList=[]
                for i in range(len(lib_list(0))):
                    nameList.append(lib_list(0)[i][0])

                howmany = 0
                removenum = 0
                for j in range(len(nameList)):
                    if nameSearch.lower() in nameList[j].lower():
                        print ' / '.join(lib_list(0)[j])
                        howmany = howmany + 1
                        removenum = j
                print

                if howmany == 1:
                    while True:
                        print 'Do you really want to REMOVE this? ( Y ) Yes. ( N ) No.'
                        really = raw_input()
                        if really == 'Y' or really == 'y' or really == 'N' or really == 'n':
                            break
                        else:
                            print 'Please type Y or N.'
                    if really == 'Y' or really == 'y':
                        number = 0
                        f = open('lib.txt','r')
                        whole = f.readlines()
                        f.close()
                        listList = []
                        for i in range(len(whole)):
                            listList.append(whole[i][0:len(whole[i])-1].split())
                        listKey = []
                        for j in range(len(listList)):
                            listKey.append(listList[j][number] + str(j))
                        listKey.sort()
                        removenumAddress = int(listKey[removenum][-1])
                        f = open('lib.txt','r')
                        fullString = f.read()
                        fullList = fullString.split('\n')
                        del fullList[removenumAddress]
                        data = '\n'.join(fullList) + '\n'
                        f = open('lib.txt','w+')
                        f.write(data)
                        f.close()
                        print 'Removed successfully!'
                        print
                        break
                    if really == 'N' or really == 'n':
                        break
                elif howmany == 0:
                    print 'No matching results found.'
                    print
                    break
                else:
                    print 'Search specifically again.'
                    continue
            print display
            option = raw_input('Enter option : ')
        elif option == 'A' or option == 'a':
            while True:
                artistSearch = word_str(raw_input('Search : '))
                print
                artistList=[]
                for i in range(len(lib_list(1))):
                    artistList.append(lib_list(1)[i][1])

                howmany = 0
                removenum = 0
                for j in range(len(artistList)):
                    if artistSearch.lower() in artistList[j].lower():
                        print ' / '.join(lib_list(1)[j])
                        howmany = howmany + 1
                        removenum = j
                print

                if howmany == 1:
                    while True:
                        print 'Do you really want to REMOVE this? ( Y ) Yes. ( N ) No.'
                        really = raw_input()
                        if really == 'Y' or really == 'y' or really == 'N' or really == 'n':
                            break
                        else:
                            print 'Please type Y or N.'
                    if really == 'Y' or really == 'y':
                        number = 1
                        f = open('lib.txt','r')
                        whole = f.readlines()
                        f.close()
                        listList = []
                        for i in range(len(whole)):
                            listList.append(whole[i][0:len(whole[i])-1].split())
                        listKey = []
                        for j in range(len(listList)):
                            listKey.append(listList[j][number] + str(j))
                        listKey.sort()
                        removenumAddress = int(listKey[removenum][-1])
                        f = open('lib.txt','r')
                        fullString = f.read()
                        fullList = fullString.split('\n')
                        del fullList[removenumAddress]
                        data = '\n'.join(fullList) + '\n'
                        f = open('lib.txt','w+')
                        f.write(data)
                        f.close()
                        print 'Removed successfully!'
                        print
                        break
                    if really == 'N' or really == 'n':
                        break
                elif howmany == 0:
                    print 'No matching results found.'
                    print
                    break
                else:
                    print 'Search specifically again.'
                    continue
            print display
            option = raw_input('Enter option : ')
        elif option == 'L' or option == 'l':
            while True:
                albumSearch = word_str(raw_input('Search : '))
                print
                albumList=[]
                for i in range(len(lib_list(2))):
                    albumList.append(lib_list(2)[i][2])

                howmany = 0
                removenum = 0
                for j in range(len(albumList)):
                    if albumSearch.lower() in albumList[j].lower():
                        print ' / '.join(lib_list(2)[j])
                        howmany = howmany + 1
                        removenum = j
                print

                if howmany == 1:
                    while True:
                        print 'Do you really want to REMOVE this? ( Y ) Yes. ( N ) No.'
                        really = raw_input()
                        if really == 'Y' or really == 'y' or really == 'N' or really == 'n':
                            break
                        else:
                            print 'Please type Y or N.'
                    if really == 'Y' or really == 'y':
                        number = 2
                        f = open('lib.txt','r')
                        whole = f.readlines()
                        f.close()
                        listList = []
                        for i in range(len(whole)):
                            listList.append(whole[i][0:len(whole[i])-1].split())
                        listKey = []
                        for j in range(len(listList)):
                            listKey.append(listList[j][number] + str(j))
                        listKey.sort()
                        removenumAddress = int(listKey[removenum][-1])
                        f = open('lib.txt','r')
                        fullString = f.read()
                        fullList = fullString.split('\n')
                        del fullList[removenumAddress]
                        data = '\n'.join(fullList) + '\n'
                        f = open('lib.txt','w+')
                        f.write(data)
                        f.close()
                        print 'Removed successfully!'
                        print
                        break
                    if really == 'N' or really == 'n':
                        break
                elif howmany == 0:
                    print 'No matching results found.'
                    print
                    break
                else:
                    print 'Search specifically again.'
                    continue
            print display
            option = raw_input('Enter option : ')
        elif option == 'G' or option == 'g':
            while True:
                genreSearch = word_str(raw_input('Search : '))
                print
                genreList=[]
                for i in range(len(lib_list(3))):
                    genreList.append(lib_list(3)[i][3])

                howmany = 0
                removenum = 0
                for j in range(len(genreList)):
                    if genreSearch.lower() in genreList[j].lower():
                        print ' / '.join(lib_list(3)[j])
                        howmany = howmany + 1
                        removenum = j
                print

                if howmany == 1:
                    while True:
                        print 'Do you really want to REMOVE this? ( Y ) Yes. ( N ) No.'
                        really = raw_input()
                        if really == 'Y' or really == 'y' or really == 'N' or really == 'n':
                            break
                        else:
                            print 'Please type Y or N.'
                    if really == 'Y' or really == 'y':
                        number = 3
                        f = open('lib.txt','r')
                        whole = f.readlines()
                        f.close()
                        listList = []
                        for i in range(len(whole)):
                            listList.append(whole[i][0:len(whole[i])-1].split())
                        listKey = []
                        for j in range(len(listList)):
                            listKey.append(listList[j][number] + str(j))
                        listKey.sort()
                        removenumAddress = int(listKey[removenum][-1])
                        f = open('lib.txt','r')
                        fullString = f.read()
                        fullList = fullString.split('\n')
                        del fullList[removenumAddress]
                        data = '\n'.join(fullList)
                        f = open('lib.txt','w+')
                        f.write(data)
                        f.close()
                        print 'Removed successfully!'
                        print
                        break
                    if really == 'N' or really == 'n':
                        break
                elif howmany == 0:
                    print 'No matching results found.'
                    print
                    break
                else:
                    print 'Search specifically again.'
                    continue
            print display
            option = raw_input('Enter option : ')
        elif option == 'C' or option == 'c':
            break
        else:
            option = raw_input('Wrong option. Please type again : ')
