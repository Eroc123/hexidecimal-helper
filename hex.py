

from os import system
from random import choice
from time import sleep, time
debug = False


hex = {
    '0':'0000',
    '1':'0001',
    '2':'0010',
    '3':'0011',
    '4':'0100',
    '5':'0101',
    '6':'0110',
    '7':'0111',
    '8':'1000',
    '9':'1001',
    'A':'1010',
    'B':'1011',
    'C':'1100',
    'D':'1101',
    'E':'1110',
    'F':'1111',
}

hexlist = [i for i in hex]
correct = 0
wrong = 0
start = 0
end = 0
pasttime = []
incorrecthex = []
h = 0
while True:
    queation = choice(hexlist)
    if not debug:
        system('cls')
    print('Type EXIT to exit')
    print('\n')
    print('Amount correct : ', correct)
    print('Amount wrong   : ', wrong)
    try:
        print('Percentage : ', round((correct/(correct+wrong))*100, 0), '%')
    except ZeroDivisionError:
        print('Percentage : 100 %')
    j = 0
    for i in pasttime:
        j += i
    try:
        j = j/len(pasttime)
    except ZeroDivisionError:
        j = 0
    print('Time per queation : ' , round(j, 1), 'sec')
    print('\n')
    start = time()
    awnser = input(queation + '\n')

    if awnser.upper() == 'EXIT':
        break
    elif awnser == hex[queation]:
        print('Correct')
        correct += 1
        if queation in incorrecthex:
            del incorrecthex[incorrecthex.index(queation)]
            h += 1
    else:
        print('Incorrect')
        print(queation, ' is ' ,hex[queation])
        sleep(5)
        wrong += 1
        incorrecthex.append(queation)
        h -= 1
    end = time()
    hexlist += incorrecthex
    pasttime.append(round(end - start, 1))
    if h >= 5:
        hexlist = [i for i in hex]
    if debug == True:
        print('\nDEBUG INFO - To turn off set `debug` variable to False')
        allvar = dir()
        for name in allvar:
            if not name.startswith('__'):
                print(name, eval(name))
        sleep(10)