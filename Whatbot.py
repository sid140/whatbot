import pyautogui as rub
import webbrowser as kiss
import time as good

while True:
    cold = rub.alert(text='Welcome to Whatbot, a Whatsapp bot created SJK', title='Circus', button='OK')
    print("Selfish advertisement: This bot is developed by Sid\n")
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
