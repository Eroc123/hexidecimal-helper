import os
os.system('cls')
while True:
    try:
        print('hexidecimal practice\ntype EXIT to exit\n\nhex to decimal (1)\ndecimal to hex (2)\n\nmore practices comming later')
        choice = input('')
        if choice == '1':
            os.system('py bin.py')
            os.system('cls')
        elif choice == '2':
            os.system('py hex.py')
            os.system('cls')
        elif choice.lower() == 'exit':
            break
        else:
            os.system('cls')
            continue
    except KeyboardInterrupt:
        pass