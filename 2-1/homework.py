# coding : matpang99
while True:
    print 'mode 0 : continue, 1 : exit'
    mode = int(raw_input())
    if mode == 1:
        break
    elif mode == 0:
        print 'Hello! What is your name?'
        name = raw_input()
        print 'StudentNumber :'
        studentNumber = raw_input()
        print 'PhoneNumber :'
        phoneNumber = raw_input()
        print 'University :'
        university = raw_input()
        print name, '\'s Information'
        print university, studentNumber
        print 'PhoneNumber :', phoneNumber
