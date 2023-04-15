import sys, os, subprocess, json, time, re
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QSystemTrayIcon, QMenu
from PySide6.QtCore import QFile, QObject, QThread, Signal
from PySide6.QtGui import QIcon, QAction, QIntValidator
from assets.ui.ui_app import Ui_MainWindow


class MainWindow(QMainWindow):
    # 线程信号
    mw_sig = Signal(str)
    # 全局属性
    root_file = os.environ['HOMEDRIVE'] + os.environ['HOMEPATH'] + '\Downloads'
    get_video_path = ''
    get_video_duration = 0
    
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('视频工作台')
        self.app_icon = QIcon("./assets/images/app.png")
        self.setWindowIcon(self.app_icon)

        # 一些初始化
        self.setup_thread()
        self.bt_list = [self.ui.bt_format, self.ui.bt_audio, self.ui.bt_mz, self.ui.bt_good, self.ui.bt_crf]

        # 验证器
        self.ui.good_size.setValidator(QIntValidator())
        self.ui.i_m.setValidator(QIntValidator())
        self.ui.i_z.setValidator(QIntValidator())
        self.ui.crf_value.setValidator(QIntValidator())

        # 杂项按钮组
        self.ui.get_video.clicked.connect(self.get_video)
        self.ui.lay_v.clicked.connect(self.v_output)
        self.ui.use_about.clicked.connect(self.about)

        # 托盘
        self.createTrayIcon()
        self.trayIcon.show()
    def about(self):
        a = open("./assets/about/about.txt", encoding='UTF-8')
        a = a.read()
        self.message('使用说明', a)
    def message(self,title,content):
        msgBox = QMessageBox()
        msgBox.setWindowIcon(self.app_icon)
        msgBox.setWindowTitle(title)
        msgBox.setText(content)
        msgBox.exec()
    # 选取视频
    def get_video(self):
        fname, _ = QFileDialog.getOpenFileName(self, '选择文件', self.root_file)
        if fname == "":
            return
        self.get_video_path = fname
        self.video_init(fname)
        self.ui.v_input.setText(fname)
    # 设置存放位置
    def v_output(self):
        fname = QFileDialog.getExistingDirectory(self, '选择存放路径', self.root_file)
        if fname == "":
            return
        self.ui.v_output.setText(fname)
    # 数据初始化
    def video_init(self, v_path):
        self.ui.good_size.setEnabled(True)
        self.work_tips()
        self.ui.progressBar.setValue(0)
        # 视频信息初始化
        video_data = self.get_video_info(v_path)
        self.ui.v_bit_rate.setText(video_data["bit_rate"])
        self.ui.v_fps.setText(video_data["fps"])
        self.ui.codec_name.setText(video_data["v_code"])
        self.ui.a_codec_name.setText(video_data["a_code"])
        # 获取视频时常
        self.get_video_duration = video_data["v_duration"]
    # 获取视频信息
    def get_video_info(self, v_path):
        p= subprocess.Popen(f'ffprobe -v quiet -print_format json -show_streams -i "{v_path}"', 
            shell=True, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.STDOUT,
            universal_newlines=True,
            encoding='UTF-8')
        json_data = json.loads(p.stdout.read())
        # 码率
        bit_rate = float(json_data['streams'][0]['bit_rate'])
        bit_rate = str(int(bit_rate) // 1000) + "Kbps"
        # 帧率
        fps = json_data['streams'][0]['r_frame_rate']
        fps = str(int(fps[0:fps.rfind('/')]) / int(fps.split("/")[1])) + "帧/秒"
        # 视频编码
        v_code = json_data['streams'][0]['codec_name']
        # 音频编码
        a_code = json_data['streams'][1]['codec_name']
        # 视频时长
        v_duration = json_data['streams'][0]['duration']
        return {'bit_rate': bit_rate, "fps": fps, "v_code": v_code, "a_code": a_code, "v_duration": v_duration}
    # 码率计算
    def v_rate_idea(self):
        if self.get_video_duration:
            if self.ui.good_size.text() != '':
                v_rate_idea_size = int(float(self.ui.good_size.text()))
                v_duration = int(float(self.get_video_duration))
                avg_rate = (v_rate_idea_size/v_duration)*8
                return str(round(avg_rate,2))+'M'
    # 合成命令
    def do_comline(self, type=None):
        视频路径 = self.get_video_path
        视频格式 = os.path.splitext(self.get_video_path)[-1]
        输出 = f'{self.ui.v_output.text()}/{time.time()}' if self.ui.v_output.text() else f'{self.root_file}\{time.time()}'
        帧率 = f'-r {self.ui.i_z.text()}' if self.ui.i_z.text() else ''
        码率 = f'-b:v {self.ui.i_m.text()}K' if self.ui.i_m.text() else ''
        视编码器 = self.ui.v_codec_value.currentText()
        音编码器 = self.ui.a_codec_value.currentText()
        视格式 = self.ui.v_format_value.text()
        音格式 = self.ui.a_format_value.text()
        理想大小 = self.ui.good_size.text()
        理想码率 = self.v_rate_idea()
        CRF = self.ui.crf_value.text()
        if type == 0:
            if 视格式:
                return f'ffmpeg -i "{视频路径}" -c:v {视编码器} {输出}.{视格式}'
        elif type == 1:
            if 音格式:
                return f'ffmpeg -i "{视频路径}" -vn -c:a {音编码器} {输出}.{音格式}'
        elif type == 2:
            if 理想大小:
                return f'ffmpeg -i "{视频路径}" -b:v {理想码率} {输出}{视频格式}'
        elif type == 3:
            if CRF:
                return f'ffmpeg -i "{视频路径}" -crf {CRF} {输出}{视频格式}'
        else:
            if 帧率 or 码率:
                return f'ffmpeg -i "{视频路径}" {帧率} {码率} {输出}{视频格式}'
    # 状态变化
    def work_tips(self, text='待处理...', color='black'): 
        self.ui.work_tips.setText(text)
        self.ui.work_tips.setStyleSheet("color:" + color)
        self.ui.work_tips.repaint()
    # 线程初始化
    def setup_thread(self):
        self.main_thread = QThread(self)
        self.work_thread = WorkThread()
        self.work_thread.moveToThread(self.main_thread)
        # self.main_thread.finished.connect(self.work_thread.deleteLater)
        # self.main_thread.finished.connect(lambda: print(self.work_thread))
        self.ui.bt_format.clicked.connect(lambda: self.start_thread(self.do_comline(0)))
        self.ui.bt_audio.clicked.connect(lambda: self.start_thread(self.do_comline(1)))
        self.ui.bt_good.clicked.connect(lambda: self.start_thread(self.do_comline(2)))
        self.ui.bt_crf.clicked.connect(lambda: self.start_thread(self.do_comline(3)))
        self.ui.bt_mz.clicked.connect(lambda: self.start_thread(self.do_comline()))
        
        self.mw_sig.connect(self.work_thread.run_proc)
        self.work_thread.stop_sig.connect(self.stop_thread)
        self.work_thread.log_text.connect(self.update_log)
        self.work_thread.progressBar.connect(self.progress)

        
    # 线程启动
    def start_thread(self, comline):
        if self.get_video_path and comline:
            for i in self.bt_list:
                i.setEnabled(False)
            self.ui.log_text.clear()
            self.work_tips('处理中...', 'green')
            self.main_thread.start()
            self.mw_sig.emit(comline)
        else:
            self.message('警告','请先选取视频！并填写必要参数')
    def update_log(self,r):
        self.ui.log_text.append(r)
    def progress(self,r):
        # print(r)
        self.ui.progressBar.setValue(r)
    def stop_thread(self,r):
        self.main_thread.quit()
        self.main_thread.wait()
        if r == '0':
            self.work_tips('完成', 'green')
        else:
            self.work_tips('失败啦！', 'red')
        for i in self.bt_list:
            i.setEnabled(True)

    #创建托盘图标
    def createTrayIcon(self):
        aRestore = QAction('显示', self, triggered = self.showNormal)
        aQuit = QAction('退出', self, triggered = QApplication.instance().quit)
        
        menu = QMenu(self)
        menu.addAction(aRestore)
        menu.addAction(aQuit)
        
        self.trayIcon = QSystemTrayIcon(self)
        self.trayIcon.setIcon(self.app_icon)
        self.trayIcon.setContextMenu(menu)
    def closeEvent(self, event):
        if self.trayIcon.isVisible() and self.main_thread.isRunning():
            self.message('提示','当前还有任务在执行，将最小化到托盘')
            self.hide()
            event.ignore()

# 任务类     
class WorkThread(QObject):
    stop_sig = Signal(str)
    log_text = Signal(str)
    progressBar = Signal(int)
    duration_re = re.compile(r'Duration:\s*(\d+):(\d+):(\d+\.\d+),')
    time_re = re.compile(r"time=\s*(\d+):(\d+):(\d+\.\d+)")
    duration = None
    time = None

    def __init__(self):
        super().__init__()
    # 视频处理
    def run_proc(self, r):
        p = subprocess.Popen(r, 
            shell=True, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.STDOUT,
            universal_newlines=True,
            encoding='UTF-8')
        for i in p.stdout:
            line = i.replace('\n', '')
            progress = self.funProgressBar(line)
            self.log_text.emit(line)
            if progress is not None:
                self.progressBar.emit(progress)
           
        p.wait()
        self.stop_sig.emit(str(p.returncode))
    # 进度条
    def funProgressBar(self, line):
        duration_match = self.duration_re.search(line)
        if duration_match:
            hours, minutes, seconds = map(float, duration_match.groups())
            self.duration = hours * 3600 + minutes * 60 + seconds

        time_match = self.time_re.search(line)
        if time_match:
            hours, minutes, seconds = map(float, time_match.groups())
            self.time = hours * 3600 + minutes * 60 + seconds

        if self.duration is not None and self.time is not None:
            progress = self.time / self.duration
            progress = int(float('{:.2f}'.format(progress)) * 100)
            return progress


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
