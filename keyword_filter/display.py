
import PyQt5
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget,QPushButton, QLabel, QFileDialog, QFrame, QTextEdit, QWidget, QDialog, QSpinBox, QLineEdit, QProgressBar,\
            QCheckBox, QRadioButton, QGroupBox, QHBoxLayout, QVBoxLayout, QComboBox, QScrollArea,QScrollBar
from PyQt5.QtGui import QIcon,QFont,QColor,QTextCursor,QTextOption,QScrollEvent, QMovie
from PyQt5.QtCore import QRect,Qt,pyqtSlot,QCoreApplication
import sys
# import user
import key_globel as gl
import utils
import os

create_qt_application = lambda : QApplication(sys.argv)
exit_qt_application = lambda argv:sys.exit(argv)

class qt_kit_tool:
    @staticmethod
    def label(object,name, rect, text, font=QFont('Consolas', 10, QFont.Bold), pos=Qt.AlignLeft):
        label1 = QLabel(object)
        label1.setObjectName(name)
        label1.setText(text)
        label1.setGeometry(rect)
        label1.setFont(font)
        label1.setAutoFillBackground(True)
        palette = PyQt5.QtGui.QPalette()
        #palette.setColor(PyQt5.QtGui.QPalette.Window, PyQt5.QtCore.Qt.white)
        #label1.setPalette(self.palette)
        label1.setAlignment(pos)
        return label1
    @staticmethod
    def push_button(object, name, rect, text, method):
        push_button1 = QPushButton(object)
        push_button1.setObjectName(name)
        push_button1.setText(text)
        push_button1.setGeometry(rect)
        push_button1.clicked.connect(method)
        return push_button1
    @staticmethod
    def text_edit(object, name, rect, data=''):
        text = QTextEdit(object)
        text.setObjectName(name)
        text.setGeometry(rect)
        text.setText(data)
        return text
    @staticmethod
    def line_edit(object, name, rect, data='', echomode=QLineEdit.Normal):
        line = QLineEdit(object)
        line.setObjectName(name)
        line.setGeometry(rect)
        line.setText(data)
        line.setEchoMode(echomode)
        return line
    @staticmethod
    def spinbox(object, name, rect, data=0, range=(0, 1000), step=1):
        box = QSpinBox(object)
        box.setObjectName(name)
        box.setGeometry(rect)
        box.setRange(*range)
        box.setValue(data)
        box.setSingleStep(step)
        return box
    @staticmethod
    def progress_bar(object, name, rect, value=0, range=(0,100)):
        pro_bar = QProgressBar(object)
        pro_bar.setObjectName(name)
        pro_bar.setGeometry(rect)
        pro_bar.setValue(value)
        pro_bar.setRange(*range)
        return pro_bar
    @staticmethod
    def checkbox(object, name, rect, data, is_ckd=False):
        ckbox = QCheckBox(object)
        ckbox.setObjectName(name)
        ckbox.setGeometry(rect)
        ckbox.setText(data)
        ckbox.setChecked(is_ckd)
        return ckbox
    @staticmethod
    def radiobox(object, name, rect, data, is_ckd=False):
        rdbox = QRadioButton(object)
        rdbox.setObjectName(name)
        rdbox.setGeometry(rect)
        rdbox.setText(data)
        rdbox.setChecked(is_ckd)
        return rdbox
    @staticmethod
    def groupbox(object, name, rect, item_set=(), layout=QHBoxLayout()):
        gpbox = QGroupBox(object)
        gpbox.setObjectName(name)
        gpbox.setGeometry(rect)
        for item in item_set:
            layout.addWidget(item)
        gpbox.setLayout(layout)
        return gpbox
    @staticmethod
    def combobox(object, name, rect, item_set=(), current_text='2048'):
        cmbox = QComboBox(object)
        cmbox.setObjectName(name)
        cmbox.setGeometry(rect)
        cmbox.addItems(item_set)
        cmbox.setCurrentText(current_text)
        return cmbox
    @staticmethod
    def widget(object, name, rect):
        wd = QWidget(object)
        wd.setObjectName(name)
        wd.setGeometry(rect)
        return wd
    @staticmethod
    def scroll(object, name, rect, widget, size=(50, 50), policy=Qt.ScrollBarAsNeeded):
        roll = QScrollArea(object)
        roll.setObjectName(name)
        roll.setGeometry(rect)
        roll.setHorizontalScrollBarPolicy(policy)
        roll.setMinimumSize(*size)
        roll.setWidget(widget)
        return roll


class display_main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        print ('hello')
    def init_ui(self):
        self.resize(1800, 1000)
        self.center()
        self.setWindowTitle('keyword_filter')
        self.setWindowIcon(QIcon('.\\source\\配置.ico'))

        self.label_title = qt_kit_tool.label(self, 'label_title', QRect(700, 0, 400, 40), '关键词过滤', QFont('微软雅黑', 20, QFont.Bold))
        height = 40
        self.label_config_title = qt_kit_tool.label(self, 'label_config_title', QRect(30, height, 100, 30), '配置文件:')
        self.label_config_path = qt_kit_tool.label(self, 'label_config_path', QRect(140, height, 500, 30), gl.CONFIG_PATH)
        self.button_config_cat = qt_kit_tool.push_button(self, 'pushbutton_config_cat', QRect(700, height, 50, 30), '查看', self.on_slot_config_cat)
        self.button_config_mod = qt_kit_tool.push_button(self, 'pushbutton_config_mod', QRect(760, height, 50, 30), '修改', self.on_slot_config_mod)
        self.button_config_mod.setEnabled(False)
        height += 30
        self.label_scan_list_title = qt_kit_tool.label(self, 'label_scan_list_title', QRect(30, height, 100, 30), 'scan_list:')
        self.label_scan_list_path = qt_kit_tool.label(self, 'label_scan_list_path', QRect(140, height, 500, 30), gl.SCAN_LIST_PATH)
        self.button_scan_list = qt_kit_tool.push_button(self, 'pushbutton_scan_list', QRect(700, height, 50, 30), '选择',  self.on_slot_scan_list)

        height += 30
        self.label_scan_log_title = qt_kit_tool.label(self, 'label_scan_log_title', QRect(30, height, 100, 30), 'scan_log:')
        self.label_scan_log_path = qt_kit_tool.label(self, 'label_scan_log_path', QRect(140, height, 500, 30), gl.LOG_PATH)
        self.button_scan_log = qt_kit_tool.push_button(self, 'pushbutton_scan_log', QRect(700, height, 50, 30), '选择', self.on_slot_scan_log)

        self.button_process_run = qt_kit_tool.push_button(self, 'pushbutton_process_run', QRect(900, height, 50, 30), '开始', self.on_slot_process_run)
        # self.label_loading_gif = qt_kit_tool.label(self, 'label_loading_gif', QRect(1000, height-20, 50, 50), '')
        # self.movie_loading_gif = QMovie('.\\source\\loading.jpg')
        # self.label_loading_gif.setMovie(self.movie_loading_gif)
        self.progressbar_output = qt_kit_tool.progress_bar(self, 'progress_bar_output', QRect(960, height, 780, 30))

        height += 30
        self.text_output_line = qt_kit_tool.text_edit(self, 'text_output_line', QRect(20, height, 1760, 850))
        self.text_output_line.setWordWrapMode(QTextOption.NoWrap)
        self.text_output_line.setFont(QFont('Consolas', 10, QFont.Bold))
        # self.text_output_line.setHorizontalScrollBar(QScrollBar())
        self.show()

    def center(self):
        qrect = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qrect.moveCenter(cp)
        self.move(qrect.topLeft())
    def font_to_convert(self, level : str, color_str):
        if gl.CONFIG_DICT.__contains__('color') == True:
            if gl.CONFIG_DICT['color'].__contains__(level) == True:
                color_str = gl.CONFIG_DICT['color'][level]
        self.text_output_line.setTextColor(QColor(color_str))
    def on_slot_config_cat(self):
        gl.INFORM.clear()
        self.text_output_line.clear()
        if utils.read_ini_file() == False:
            self.text_output_line.append('配置文件打开失败!')
            return
        for i in range(len(gl.INFORM)):
            self.text_output_line.append(gl.INFORM[i])
        self.button_config_mod.setEnabled(True)
    def on_slot_config_mod(self):
        self.button_config_mod.setEnabled(False)
        utils.write_ini_file(self.text_output_line.toPlainText())
        self.text_output_line.clear()
        self.text_output_line.append('修改配置文件成功!')
    def on_slot_scan_list(self):
        try:
            self.scan_list_path_name = QFileDialog.getOpenFileName(self, 'select file', '.\\source')
            print (self.scan_list_path_name)
            if self.scan_list_path_name[0] == '':
                gl.SCAN_LIST_PATH = '.\\source\\scan_list'
            else:
                gl.SCAN_LIST_PATH = self.scan_list_path_name[0]
            self.label_scan_list_path.setText(gl.SCAN_LIST_PATH)
        except Exception as rt:
            print (rt)
    def on_slot_scan_log(self):
        try:
            self.scan_log_path_name = QFileDialog.getOpenFileName(self, 'select file', '.\\')
            if self.scan_log_path_name[0] == '':
                gl.LOG_PATH = ''
            else:
                gl.LOG_PATH = self.scan_log_path_name[0]
            self.label_scan_log_path.setText(gl.LOG_PATH)
        except Exception as rt:
            print (rt)
    def on_slot_process_run(self):
        try:
            self.text_output_line.clear()
            self.button_process_run.setEnabled(False)
            # self.movie_loading_gif.start()
            keyword_filter_process_interface()
            self.progressbar_output.setMinimum(0)
            self.progressbar_output.setMaximum(len(gl.OUTPUT_LIST))

            for i in range(len(gl.OUTPUT_LIST)):
                self.font_to_convert('default', 'black')
                self.text_output_line.append(gl.OUTPUT_LIST[i]['value'][0:gl.OUTPUT_LIST[i]['start']])
                self.text_output_line.moveCursor(QTextCursor.EndOfLine)
                if gl.OUTPUT_LIST[i]['color'] == 1:
                    self.font_to_convert('warning', 'blue')
                elif gl.OUTPUT_LIST[i]['color'] == 2:
                    self.font_to_convert('error', 'red')
                self.text_output_line.insertPlainText(gl.OUTPUT_LIST[i]['value'][gl.OUTPUT_LIST[i]['start']:gl.OUTPUT_LIST[i]['end']])
                self.text_output_line.moveCursor(QTextCursor.EndOfLine)
                self.font_to_convert('default', 'black')
                self.text_output_line.insertPlainText(gl.OUTPUT_LIST[i]['value'][gl.OUTPUT_LIST[i]['end']:len(gl.OUTPUT_LIST[i]['value'])])
                self.progressbar_output.setValue(i+1)
            self.button_process_run.setEnabled(True)
            self.text_output_line.moveCursor(QTextCursor.Start)
        # self.movie_loading_gif.stop()
        except Exception as rt:
            str1 = "%s  ----> line: %d"%(rt, rt.__traceback__.tb_lineno)
            self.text_output_line.clear()
            self.text_output_line.append(str1)
            self.button_process_run.setEnabled(True)


def keyword_filter_process_interface():
    print ('hello')
    #TODO:初始化 包括 conf的配置， scan_list， 检查文件是否存在
    gl.CONFIG_DICT.clear()
    gl.CONFIG_DICT = utils.parse_ini_file(gl.CONFIG_PATH)
    gl.SCAN_LIST.clear()
    gl.SCAN_LIST = utils.parse_scan_list(gl.SCAN_LIST_PATH)
    gl.OUTPUT_LIST.clear()
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
