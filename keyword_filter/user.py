import utils
import key_globel as gl
import os



def keyword_filter_process_interface():
    print ('hello')
    #TODO:初始化 包括 conf的配置， scan_list， 检查文件是否存在
    gl.CONFIG_DICT = utils.parse_ini_file(gl.CONFIG_PATH)
    gl.SCAN_LIST = utils.parse_scan_list(gl.SCAN_LIST_PATH)

    #TODO：读取文件，一行一行的处理， 将结果存到list中 list:[str1_list]   str1_list:[str1_dict,str2_dict...] str1_dict:{'data':xxx, 'color':xx}
    if os.path.exists(gl.LOG_PATH) == False:
        print ('false')
    list1 = []
    with open(gl.LOG_PATH, 'rb') as file_object:
        str1 = file_object.readline()
        line_str = ''
        i = 0
        while str1:
            try:
                line_str = str1.decode('utf-8')
            except Exception as rt:
                line_str = str1.decode('gbk')
                # print (line_str)
            utils.parse_log_data(line_str.strip('\n'))
            str1 = file_object.readline()

    # print (str(gl.OUTPUT_LIST))


