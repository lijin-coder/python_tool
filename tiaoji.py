
from urllib import request
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
import time
import ssl





headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}

viewed_list = [
    '宁波大学关于2023年硕士研究生复试调剂工作的声明'
]

key_list = [
['湘潭大学', 'https://yjsc.xtu.edu.cn/zsgl/dtxx.htm', 'a'],
['北京信息科技大学', 'https://yanjiusheng.bistu.edu.cn/zsgl/zsxx/zsgg/', 'span'],
['河北工业大学', 'https://yjs.hebut.edu.cn/zsgz/ssyjszszl/gszl1/index.htm', 'li'],
['成都计算所', 'http://www.casit.ac.cn/index.php?c=category&id=15', 'li'],
['深圳大学', 'https://yz.szu.edu.cn/sszs/gg.htm', 'li'],
['浙江理工大学', 'https://gradadmission.zstu.edu.cn/bkzx.htm', 'li'],
['宁波大学', 'http://graduate.nbu.edu.cn/zsgz/ssszs.htm', 'h4'],
['大连海事大学', 'http://grs.dlmu.edu.cn/zsgz/ssyjs.htm', 'li'],
['合肥工业大学', 'http://yjszs.hfut.edu.cn/13533/list.htm', 'li'],
['华侨大学', 'https://grs.hqu.edu.cn/jnzs.htm', 'li'],
['福建师范大学', 'https://yjsy.fjnu.edu.cn/4227/list.htm', 'td'],
['广州大学', 'http://yjsy.gzhu.edu.cn/zsxx/zsdt.htm', 'a'],
['河海大学', 'https://gs.hhu.edu.cn/17279/list1.htm', 'li'],
['上海电力大学', 'https://yjsc.shiep.edu.cn/948/list1.htm', 'li'],
['杭州电子科技大学', 'https://grs.hdu.edu.cn/1721/list1.htm', 'a'],
['浙江师范大学', 'http://yzw.zjnu.edu.cn/qrzssszs/list1.htm', 'a'],
['郑州大学', 'http://gs.zzu.edu.cn/zsgz/zxtz.htm', 'li']
]

ret_str = ''

class log_my:
    def __init__(self) -> None:
        self.log_file = "/home/pi/py_cratch.log"
    def log_write(self, str) -> None :
        with open(self.log_file, 'a') as file_object:
            file_object.write( '[ ' + time.asctime(time.localtime()) + ' ] :  ')
            file_object.write(str + '\n')

class py_cratch:
    def get_url(self, index):
        self.index = index
        context = ssl._create_unverified_context()
        req = request.Request(url=key_list[self.index][1], headers=headers)
        res = request.urlopen(req, context=context)
        self.html = res.read().decode('utf-8')
    def parse_html(self ):
        div_buf = BeautifulSoup(self.html, features="html.parser")
        li = div_buf.find_all(key_list[self.index][2])
        global ret_str
        flag1 = False
        temp_str = '[ ' +  key_list[self.index][0] + ' ]\n'
        for tt in li:
            str1 = str(tt.text)
            flag2 = False
            for str_t in viewed_list :
                if str1.find(str_t) >= 0 :
                    flag2 = True
            if flag2 == False and str1.find('调剂') >= 0 and str1.find('2023') >= 0 :
                temp_str +=  ' ==> ' +  tt.text + '\n'
                flag1 = True

        if flag1 == True :
            ret_str += temp_str + '\n'

def send_msg_to_qq(info : str):
    subject = '[新]复试调剂信息更新' 
    sender = 'xxx@163.com'
    content = info 
    recver = 'xxx@qq.com'
    passwd = 'xxxxxxxx'
    message = MIMEText(content, "plain", "utf-8")

    message['Subject'] = subject
    message['To'] = recver
    message['From'] = sender

    smtp = smtplib.SMTP_SSL("smtp.163.com", 994)
    smtp.login(sender, passwd)
    smtp.sendmail(sender, [recver], message.as_string())
    smtp.close()


if __name__ == '__main__':
    log_ = log_my() 
    log_.log_write ("hello world")
    send_msg_to_qq('hello world! I start to work...')
    ky = py_cratch()
    while True:
        try:
            for i in range(0,len(key_list)):
                ky.get_url(i)
                ky.parse_html()
            if ret_str != '':
                send_msg_to_qq(ret_str)
            ret_str = ''
            time.sleep(2100)
            log_.log_write ("Send ok!  I am running...\n" + ret_str)
        except Exception as rt:
            log_.log_write (str(rt))
            time.sleep(10)





