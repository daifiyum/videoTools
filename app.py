import sys, os, subprocess, json, time
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PySide6.QtCore import QFile, QObject, QThread, Signal
from PySide6.QtGui import QIcon
from assets.ui.ui_app import Ui_MainWindow


class MainWindow(QMainWindow):
    mw_sig = Signal(str)
    # 全局变量
    root_file = os.environ['HOMEDRIVE'] + os.environ['HOMEPATH'] + '\Downloads'
    get_video_path = ''
    get_video_duration = 0
    
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # 窗口配置
        self.setWindowTitle('视频工作台')
        self.setWindowIcon(QIcon("./assets/images/app.png"))
        # 一些初始化
        self.setup_thread()
        self.bt_list = [self.ui.bt_format, self.ui.bt_audio, self.ui.bt_mz]
        # 选取视频
        self.ui.get_video.clicked.connect(self.get_video)
        self.ui.v_rate_idea.clicked.connect(self.v_rate_idea)
    def message(self,title,content):
        msgBox = QMessageBox()
        msgBox.setWindowIcon(QIcon("./assets/images/app.png"))
        msgBox.setWindowTitle(title)
        msgBox.setText(content)
        msgBox.exec()
    # 函数 选取视频
    def get_video(self):
        fname, _ = QFileDialog.getOpenFileName(self, '选择文件', self.root_file)
        if fname == "":
            return
        self.get_video_path = fname
        self.get_video_info(fname)
        self.work_tips()
        self.ui.out_path.clear()
    # 函数 获取视频信息
    def get_video_info(self, v_path):
        p= subprocess.Popen(f'ffprobe -v quiet -print_format json -show_streams -i {v_path}', 
            shell=True, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.STDOUT,
            universal_newlines=True)
        json_data = json.loads(p.stdout.read())
        bit_rate = float(json_data['streams'][0]['bit_rate'])
        def convert(value):
            units = ["b/s", "kb/s", "Mb/s", "Gb/s"]
            size = 1024.0
            for i in range(len(units)):
                if (value / size) < 1:
                    return "%.2f%s" % (value, units[i])
                value = value / size
        bit_rate = convert(bit_rate)
        fps = json_data['streams'][0]['r_frame_rate'].replace('/1', '帧/秒')
        self.ui.v_bit_rate.setText(bit_rate)
        self.ui.v_fps.setText(fps)
        self.ui.codec_name.setText(json_data['streams'][0]['codec_name'])
        a_codec = json_data['streams'][1]['codec_name']
        if a_codec:
            self.ui.a_codec_name.setText(a_codec)
        # 获取视频时常
        self.get_video_duration = json_data['streams'][0]['duration']
    # 码率计算
    def v_rate_idea(self):
        if self.ui.v_rate_idea_size.text() and self.get_video_duration:
            v_rate_idea_size = int(float(self.ui.v_rate_idea_size.text()))
            v_duration = int(float(self.get_video_duration))
            avg_rate = (v_rate_idea_size/v_duration)*8
            self.ui.i_m.setText(str(round(avg_rate,2))+'M')
            self.ui.v_rate_idea_value.setText(str(round(avg_rate,2))+'M')
        else:
            self.message('警告','请先选取视频并填写理想视频大小！')
    # 合成命令
    def do_comline(self, type=None):
        def if_m():
            if self.ui.i_m.text():
                return f' -b:v {self.ui.i_m.text()}'
            else:
                return ''
        if type == 0:
            return f'ffmpeg -i "{self.get_video_path}" -c:v {self.ui.v_codec_value.currentText()} {self.root_file}\{time.time()}.{self.ui.v_format_value.text()}'
        elif type == 1:
            return f'ffmpeg -i "{self.get_video_path}" -vn -c:a {self.ui.a_codec_value.currentText()} {self.root_file}\{time.time()}.{self.ui.a_format_value.text()}'
        else:
            return f'ffmpeg -i "{self.get_video_path}" -r {self.ui.i_z.text() if self.ui.i_z.text() else str(30) }{if_m()} {self.root_file}\{time.time()}{os.path.splitext(self.get_video_path)[-1]}'
    # 状态变化
    def work_tips(self, text='待处理...', color='black'): 
        self.ui.work_tips.setText(text)
        self.ui.work_tips.setStyleSheet("color:" + color)
        self.ui.work_tips.repaint()
    def setup_thread(self):
        self.main_thread = QThread(self)
        self.work_thread = WorkThread()
        self.work_thread.moveToThread(self.main_thread)

        self.ui.bt_format.clicked.connect(lambda: self.start_thread(self.do_comline(0)))
        self.ui.bt_audio.clicked.connect(lambda: self.start_thread(self.do_comline(1)))
        self.ui.bt_mz.clicked.connect(lambda: self.start_thread(self.do_comline()))
        self.mw_sig.connect(self.work_thread.run_proc)
        self.work_thread.stop_sig.connect(self.stop_thread)
        self.work_thread.log_text.connect(self.update_log)

    def start_thread(self, comline):
        if self.get_video_path:
            self.ui.log_text.clear()
            self.work_tips('处理中...', 'green')
            self.main_thread.start()
            self.mw_sig.emit(comline)
            for i in self.bt_list:
                i.setEnabled(False)
        else:
            self.message('警告','请先选取视频！')
    def update_log(self,r):
        self.ui.log_text.append(r)
    def stop_thread(self):
        self.main_thread.quit()
        self.main_thread.wait()
        self.work_tips('完成啦~', 'green')
        self.ui.out_path.setText(self.root_file)
        for i in self.bt_list:
            i.setEnabled(True)


class WorkThread(QObject):
    stop_sig = Signal()
    log_text = Signal(str)
    def __init__(self):
        super().__init__()

    def run_proc(self, r):
        p = subprocess.Popen(r, 
            shell=True, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.STDOUT,
            universal_newlines=True)
        for line in p.stdout:
            self.log_text.emit(line.replace('\n', ''))
        self.stop_sig.emit()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())