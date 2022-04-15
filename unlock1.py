import pyautogui as pag
import pynput
import threading
import time
import configparser
import os

# user=''
passwd=''

if __name__ == '__main__':
    print ('hello')
    button_right = False
    conf = configparser.ConfigParser()
    if os.path.exists('conf.ini') == False:
        passwd = input('输入你的密码: ')
        conf.add_section('info')
        conf.set('info', 'passwd', passwd)
        conf.write(open('./conf.ini', 'w'))
    else:
        conf.read('conf.ini')
        passwd = conf.get('info', 'passwd')
    print ('读取用户密码: ' + passwd)
    with pynput.mouse.Events() as event:
        for i in event:
            if isinstance(i, pynput.mouse.Events.Move):
                pass
            elif isinstance(i, pynput.mouse.Events.Click):
                print (i.x, i.y, i.button, i.pressed)
                if str(i.button) == 'Button.right':
                    button_right = True
                    print ('右键点击 ')
            elif isinstance(i, pynput.mouse.Events.Scroll):
                pass
            if button_right == True:
                break
        i = event.get(1)
    if button_right == True:
        ctr = pynput.keyboard.Controller()

        with ctr.pressed(pynput.keyboard.Key.ctrl, pynput.keyboard.Key.alt, pynput.keyboard.Key.delete ):
            print ('ctrl+alt+del')
            pass

        time.sleep(1)
        with ctr.pressed(pynput.keyboard.Key.enter):
            pass
        with ctr.pressed(pynput.keyboard.Key.enter):
            print ('enter')
            pass
        # time.sleep(1)
        #
        pag.typewrite(passwd)
        with ctr.pressed(pynput.keyboard.Key.enter):
           print ('输入密码并确认')
           pass

