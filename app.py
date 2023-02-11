import sys, os, subprocess, json, time, re
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QSystemTrayIcon, QMenu
from PySide6.QtCore import QFile, QObject, QThread, Signal
from PySide6.QtGui import QIcon, QAction, QIntValidator
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

        # 一些初始化
        self.setup_thread()
        self.bt_list = [self.ui.bt_format, self.ui.bt_audio, self.ui.bt_mz, self.ui.bt_good, self.ui.bt_crf]
        self.app_icon = QIcon("./assets/images/app.png")

        # 窗口配置
        self.setWindowTitle('视频工作台')
        self.setWindowIcon(self.app_icon)

        # 验证器
        self.ui.good_size.setValidator(QIntValidator())

        # 一些绑定
        self.ui.get_video.clicked.connect(self.get_video)
        self.ui.use_about.clicked.connect(self.about)
        # 合成命令相关
        self.ui.good_size.textEdited.connect(self.v_rate_idea)
        self.ui.good_size.setEnabled(False)

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
    # 函数 选取视频
    def get_video(self):
        fname, _ = QFileDialog.getOpenFileName(self, '选择文件', self.root_file)
        if fname == "":
            return
        self.get_video_path = fname
        self.ui.good_size.setEnabled(True)
        self.get_video_info(fname)
        self.work_tips()
        self.ui.progressBar.setValue(0)
    # 函数 获取视频信息
    def get_video_info(self, v_path):
        p= subprocess.Popen(f'ffprobe -v quiet -print_format json -show_streams -i "{v_path}"', 
            shell=True, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.STDOUT,
            universal_newlines=True,
            encoding='UTF-8')
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
        if self.get_video_duration:
            if self.ui.good_size.text() != '':
                v_rate_idea_size = int(float(self.ui.good_size.text()))
                v_duration = int(float(self.get_video_duration))
                avg_rate = (v_rate_idea_size/v_duration)*8
                self.ui.good_value.setText(str(round(avg_rate,2))+'M')
        else:
            self.message('警告', '请先选取视频！')
    # 合成命令
    def do_comline(self, type=None):
        视频路径 = self.get_video_path
        视频格式 = os.path.splitext(self.get_video_path)[-1]
        输出 = f'{self.root_file}\{time.time()}'
        帧率 = f'-r {self.ui.i_z.text()}' if self.ui.i_z.text() else ''
        码率 = f'-b:v {self.ui.i_m.text()}' if self.ui.i_m.text() else ''
        视编码器 = self.ui.v_codec_value.currentText()
        音编码器 = self.ui.a_codec_value.currentText()
        视格式 = self.ui.v_format_value.text()
        音格式 = self.ui.a_format_value.text()
        理想大小 = self.ui.good_size.text()
        理想码率 = self.ui.good_value.text()
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
        # 传递信号给work线程
        self.mw_sig.connect(self.work_thread.run_proc)

        self.work_thread.stop_sig.connect(self.stop_thread)
        self.work_thread.log_text.connect(self.update_log)
        self.work_thread.progressBar.connect(self.progress)

        

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
        
class WorkThread(QObject):
    stop_sig = Signal(str)
    log_text = Signal(str)
    progressBar = Signal(int)
    def __init__(self):
        super().__init__()

    def run_proc(self, r):
        duration = None
        p = subprocess.Popen(r, 
            shell=True, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.STDOUT,
            universal_newlines=True,
            encoding='UTF-8')
        for i in p.stdout:
            self.log_text.emit(i.replace('\n', ''))
            duration_res = re.search(r'Duration: (?P<duration>\S+)', i)
            if duration_res is not None:
                duration = duration_res.groupdict()['duration']
                duration = re.sub(r',', '', duration)

            result = re.search(r'time=(?P<time>\S+)', i)
            # print(duration, result)
            if result is not None and duration is not None:
                elapsed_time = result.groupdict()['time']

                currentTime = self.get_seconds(elapsed_time)
                allTime = self.get_seconds(duration)

                progress = currentTime * 100/allTime
                # print(int(progress))
                self.progressBar.emit(int(progress))
        p.wait()
        self.stop_sig.emit(str(p.returncode))

    def get_seconds(self, time):
        h = int(time[0:2])
        m = int(time[3:5])
        s = int(time[6:8])
        ms = int(time[9:12])
        ts = (h * 60 * 60) + (m * 60) + s + (ms / 1000)
        return ts

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())