import configparser
import os
import key_globel as gl
import re

def parse_ini_file(filepath:str, encoding1='utf-8'):
    config = configparser.ConfigParser()
    if os.path.exists(filepath) == True:
        config.read(filepath, encoding=encoding1)
    return config

def parse_scan_list(filepath : str):
    list1 = []
    if os.path.exists(filepath) == True:
        print ('exi')
        with open(filepath, 'rt', encoding='utf8') as file_object:
            str1 = file_object.readline().strip('\n')
            while str1:
                list1.append(str1)
                str1 = file_object.readline().strip('\n')

    return list1

def parse_log_data(line_str : str):

    line_list = line_str.split(':')
    value_str = line_list[-1]
    filter_flag = 0
    test_flag_is_in_str = 0
    test_flag_is_suffix = 0
    #过滤
    if gl.CONFIG_DICT.__contains__('include') == True and gl.CONFIG_DICT.__contains__('exclude') == True and gl.CONFIG_DICT.__contains__('suffix') == True:
        for item_value in gl.CONFIG_DICT['include'].values():
            if item_value in line_str:
                test_flag_is_in_str = 1
                break
        if test_flag_is_in_str:
            for item_value in gl.CONFIG_DICT['exclude'].values():
                if item_value in line_str:
                    filter_flag = 1
                    break
        file_suffix = ''
        for i in range(len(line_list) - 1):
            if line_list[i+1].isdigit() == True:
                file_suffix = line_list[i].split('.')[-1]

        # print (file_suffix)
        if filter_flag == 0:
            for item_value in gl.CONFIG_DICT['suffix'].values():
                # print ('========')
                # print (item_value)
                if file_suffix != '' and  item_value in file_suffix:
                    test_flag_is_suffix = 1

                    break
    #查找
    if filter_flag == 0 and test_flag_is_in_str == 1 and test_flag_is_suffix == 0:
        print ('===========')
        print (line_str)

    # print (test_flag_is_suffix)
    if filter_flag == 0 and test_flag_is_in_str == 1 and test_flag_is_suffix == 1:
        for i in range(len(gl.SCAN_LIST)):
            pos = value_str.find(gl.SCAN_LIST[i])
            if pos != -1:
                str1_dict = {'value':line_str, 'start':line_str.rfind(':') + 1 + pos, 'end':line_str.rfind(':') + 1 + pos + len(gl.SCAN_LIST[i]), 'color':1}
                if pos == 0 and value_str[pos+len(gl.SCAN_LIST[i])].isalnum() == False:
                    str1_dict['color'] = 2
                elif pos != 0 and pos == len(value_str)-1 and value_str[pos-1].isalnum() == False:
                    str1_dict['color'] = 2
                elif value_str[pos - 1].isalnum() == False and value_str[pos+len(gl.SCAN_LIST[i])].isalnum() == False:
                    str1_dict['color'] = 2
                #TODO:现在暂时考虑， 一行中 只有一个敏感词， 后续要考虑有多个敏感词，这里先这样是为了效率
                if len(gl.OUTPUT_LIST) == 0:
                    gl.OUTPUT_LIST.append(str1_dict)
                for i in range(len(gl.OUTPUT_LIST)):
                    if str1_dict['color'] > gl.OUTPUT_LIST[i]['color']:
                        gl.OUTPUT_LIST.insert(i, str1_dict)
                        break
                    if i == len(gl.OUTPUT_LIST) - 1:
                        gl.OUTPUT_LIST.append(str1_dict)

                break

def read_ini_file():
    if os.path.exists(gl.CONFIG_PATH) == False:
        return False
    with open(gl.CONFIG_PATH, 'rt', encoding='utf8') as file_object:
        str1 = file_object.readline()
        while str1:
            gl.INFORM.append(str1.strip('\n'))
            str1 = file_object.readline()
    return True
def write_ini_file(str1 : str):
    with open(gl.CONFIG_PATH, 'wt') as file_object:
        file_object.write(str1)

