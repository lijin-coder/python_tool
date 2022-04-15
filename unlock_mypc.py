import pyautogui as pag
import pynput
import threading
import time
import colorama
from colorama import init,Fore,Back,Style
import requests
from bs4 import BeautifulSoup
import json
import os
import random


time_count_max = 300
data_list = []
data_read_json = {}
global_flag_scrath = True

def read_json():
    try:
        with open('test.json', 'r', encoding='utf-8') as file_object:
            data_re = json.load(file_object)
        if 'flag' in data_re:
            if data_re['flag'] == '1':
                global global_flag_scrath 
                global_flag_scrath = False 
                for key in data_re:
                    if key == 'flag':
                        continue
                    data_list.append(data_re[key])
        
    except Exception as rt:
        print ('error: %s' %(rt))

def url_get_data():
    try:
        read_json()
        if global_flag_scrath == False:
            # print (data_list)
            return
        type_tuple = ("写风", "春天","夏天", "秋天", "冬天","爱国","写雪",'思念','爱情','思乡','离别','月亮','梅花','励志',
                    '荷花','写雨','友情','感恩','写风','西湖','读书','菊花','长江',
            '黄河','竹子','哲理','泰山','边塞','柳树','写鸟','桃花','老师','母亲','伤感','田园','写云','庐山','山水','星星',
            '荀子','孟子','论语','墨子','老子','史记','中庸','礼记','尚书','晋书','左传','论衡','管子','说苑','列子','国语',
            '节日','春节','元宵节','寒食节','清明节','端午节','七夕节','中秋节','重阳节','韩非子','罗织经','菜根谭','红楼梦','弟子规','战国策','后汉书','淮南子','商君书',
            '水浒传','西游记','格言联璧','围炉夜话','增广贤文','吕氏春秋','文心雕龙','醒世恒言','警世通言','幼学琼林','小窗幽记','三国演义','贞观政要')
        auto_tuple = ('李白','杜甫','苏轼','王维','杜牧','陆游','李煜','元稹','韩愈','岑参','齐己','贾岛','柳永','曹操','李贺','曹植','张籍','孟郊','皎然','许浑','罗隐','贯休',
                    '韦庄','屈原','王勃','张祜','王建','晏殊','岳飞','姚合','卢纶','秦观','钱起','朱熹','韩偓','高适','方干','李峤','赵嘏','贺铸','郑谷','郑燮','张说','张炎',
                    '白居易','辛弃疾','李清照','刘禹锡','李商隐','陶渊明','孟浩然','柳宗元','王安石','欧阳修','韦应物','温庭筠','刘长卿','王昌龄','杨万里','诸葛亮','范仲淹',
                    '陆龟蒙','晏几道','周邦彦','杜荀鹤','吴文英','马致远','皮日休','左丘明','张九龄','权德舆','黄庭坚','司马迁','皇甫冉','卓文君','文天祥','刘辰翁','陈子昂','纳兰性德')
        dyna_tuple = ('先秦','两汉','魏晋','南北朝','隋代','唐代','五代','宋代','金朝','元代','明代','清代')
        flex_tuple = ('诗文','古籍','谚语','对联')
        class_dict = {'tstr':type_tuple, 'astr':auto_tuple, 'cstr':dyna_tuple, 'xstr':flex_tuple}
        json_data = {'flag': '1'}
        count_index = 0
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'
        headers = {'User-Agent':user_agent}
        for key in class_dict:
            for i in range(len(class_dict[key])):
                target = 'https://so.gushiwen.cn/mingjus/default.aspx?' + key + '=' + class_dict[key][i]
                req = requests.get(url=target, headers=headers)
                # print(req.text)
                bf = BeautifulSoup(req.text, 'html.parser')
                text = bf.find_all('div', class_ = 'cont', style=" margin-top:12px;border-bottom:1px dashed #DAD9D1; padding-bottom:7px;")
                # print (text)
                for i in range(len(text)):
                    # print(text[i].text.replace('\xa0'*8,'\n\n'))
                    data_list.append(text[i].text.replace('\xa0'*8,'\n\n'))
                    json_data[str(count_index)] = text[i].text.replace('\xa0'*8,'\n\n')
                    count_index += 1
        with open('test.json', 'w', encoding='utf-8') as file_object:
            json.dump(json_data, file_object, indent=4, ensure_ascii=False)  #dump将数据写到文件， indent是缩进
    except Exception as rt:
        print ('error %s'%(rt))
    

class mouse_listen(threading.Thread):
    mouse_flag = False
    def __init__(self):
        super(mouse_listen, self).__init__()
    def run(self) -> None:
        while True:
            with pynput.mouse.Events() as event:
                for i in event:
                    if isinstance(i, pynput.mouse.Events.Move):
                        # print (i.x, i.y)
                        self.mouse_flag = True
                    elif isinstance(i, pynput.mouse.Events.Click):
                        # print (i.x, i.y, i.button, i.pressed)
                        self.mouse_flag = True
                    elif isinstance(i, pynput.mouse.Events.Scroll):
                        # print (i.x, i.y, i.dy)
                        self.mouse_flag = True
                    break
                i = event.get(1)
    def get_flag(self):
        return self.mouse_flag
    def set_flag(self, flag = False):
        self.mouse_flag = flag


class keyboard_listen(threading.Thread):
    keyboard_flag = False
    def __init__(self):
        super(keyboard_listen, self).__init__()
    def run(self) -> None:
        while True:
            with pynput.keyboard.Events() as event:
                for i in event:
                    key_event = i
                    break
                # key_event = event.get()
            if isinstance(key_event, pynput.keyboard.Events.Press):
                # print ('press')
                self.keyboard_flag = True
            elif isinstance(key_event, pynput.keyboard.Events.Release):
                # print ('release')
                self.keyboard_flag = True
            # try:
            #     print (key_event.key.name)
            # except AttributeError:
            #     print (key_event.key.char)
    def get_flag(self):
        return self.keyboard_flag
    def set_flag(self, flag = False):
        self.keyboard_flag = flag

class unlock_scren(threading.Thread):
    def __init__(self):
        super(unlock_scren, self).__init__()
        self.mouse_l = mouse_listen()
        self.keyboard_l = keyboard_listen()
        self.mouse_l.start()
        self.keyboard_l.start()
    def run(self) -> None:
        count_time = 0
        show_time = 0
        init(autoreset=True)
        while True:
            if self.mouse_l.get_flag() == True or self.keyboard_l.get_flag() == True:
                count_time = 0
                self.mouse_l.set_flag()
                self.keyboard_l.set_flag()
                print ('=', end='')
            else:
                print ('-', end='')
                count_time += 1
            if show_time % 60 == 0:
                print ('>')
                print ('\033[1;' + str(count_time%8+30) + ";40m" + data_list[random.randint(0, len(data_list)-1)] + "\033[0m" )
            if count_time >= time_count_max - 2:
                pag.press('winleft')
                time.sleep(1)
                pag.press('winleft')
                #with ctr.pressed(pynput.keyboard.Key.shift):
                #    pass
                #count_time = 0
                continue
            show_time += 1
            time.sleep(1)


if __name__ == '__main__':
    print ('-----------------------------------------------------------', end='')
    url_get_data()
    # time_count_max = int(input("input the second(>0):"))
    # if time_count_max <= 0:
    #     exit(0)
    press_key_to_unlock = unlock_scren()
    press_key_to_unlock.start()
    