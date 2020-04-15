import pickle
import getpass
import time
from csv import writer
from os import system as sys 

with open('Hash.pickle', 'rb') as f :
    d = pickle.load(f)

keys, values = zip(*d.items())
password = d['Password']

attempts = 5
verified = False
while attempts > 0 :
    pswd = getpass.getpass(prompt='Enter password to access : ')
    attempts -= 1

    if pswd == password :
        verified = True
        print('\n\nAuthorisation successful!')
        time.sleep(0.5)
        print('Loading')
        time.sleep(1)
        break

    if attempts > 0 :
        print(f'\n\nIncorrect Password. Attempts left : {attempts}. Try again..')   
    

if not verified :
    print('\n\nAuthorisation Failed! Aborting!!....')
    time.sleep(1)

else :
    while True :
        sys('cls')
        choice = input('\n\n\t\tCHOOSE OPERATION\n\n\n1) Add Password\n2) Retrieve Password\n3) Exit\n\n\nYour Choice : ')

        while True :
            try :
                choice = int(choice)
            except ValueError :
                print('Choice number should be numeric in nature!')
                choice = input('Try again : ')
            else :
                if choice < 1 or choice > 5 :
                    print('Choice not present : ')
                    choice = input('Try again : ')
                else :
                    break 

        if choice is 1 :
            sys('cls')
            
            name = input('\n\n\nEnter name for the password: ')
            pswd = getpass.getpass(prompt='Enter Password : ')

            hashed = ''
            for i in pswd :
                hashed += values[keys.index(i)]
                hashed += 'I~!@3'
            hashed = hashed[:-5]

            with open('Passwords.csv', 'a') as f :
                w = writer(f)
                row = [name, hashed]
                w.writerow(row)

            print('Password encrypted and saved successfully!')
            time.sleep(1)

        elif choice is 2 :
            sys('cls')

            hashed = input('\n\n\nEnter hashed password : ')

            hashed = hashed.split('I~!@3')
            pswd = ''
            for i in hashed :
                pswd += keys[values.index(i)]

            sys(f'echo {pswd} | clip')

            print('Password copied to Clipboard...Hit "Paste" or "Ctrl+V" to paste your password.')
            time.sleep(2)

        else :
            break


            


