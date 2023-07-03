import pyautogui as rub
import webbrowser as kiss
import time as good

jimmy = '''
I8,        8        ,8I 88        88        db   888888888888 88888888ba    ,ad8888ba, 888888888888
`8b       d8b       d8' 88        88       d88b       88      88      "8b  d8"'    `"8b     88
 "8,     ,8"8,     ,8"  88        88      d8'`8b      88      88      ,8P d8'        `8b    88
  Y8     8P Y8     8P   88aaaaaaaa88     d8'  `8b     88      88aaaaaa8P' 88          88    88
  `8b   d8' `8b   d8'   88""""""""88    d8YaaaaY8b    88      88""""""8b, 88          88    88
   `8a a8'   `8a a8'    88        88   d8""""""""8b   88      88      `8b Y8,        ,8P    88
    `8a8'     `8a8'     88        88  d8'        `8b  88      88      a8P  Y8a.    .a8P     88
     `8'       `8'      88        88 d8'          `8b 88      88888888P"    `"Y8888Y"'      88
'''

print(jimmy)

while True:
    cold = rub.alert(text='Welcome to Whatbot, a Whatsapp bot created SJK', title='Circus', button='OK')
    print("Shameless advertisement: This bot is developed by Sid\n")
    runner = input('Enter the Whatsapp name: ')
    lind = input("Enter the first link: ")
    msg = input("Enter the message: \n")
    
    if cold == 'OK':
        rub.press('win', interval=0.2)
        rub.write('Whatsapp', interval=0.2)
        rub.press('enter', interval=0.2)
        good.sleep(3)
        rub.write(runner, interval=0.4)
        rub.press('tab', interval=0.4)
        rub.press('enter', interval=0.3)
        rub.write(lind, interval=0.4)
        rub.press(msg, interval=0.2)
        rub.press('enter', interval=0.2)
        good.sleep(3)
        rub.write(msg, interval=0.2)
        rub.press('enter', interval=0.2)

    repeat = input("Do you want to send another message? (yes/no): ")
    if repeat.lower() == 'no':
        break
