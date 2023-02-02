# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_app.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QTextBrowser, QToolButton,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(646, 496)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_8 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.log_text = QTextBrowser(self.groupBox)
        self.log_text.setObjectName(u"log_text")

        self.horizontalLayout_8.addWidget(self.log_text)


        self.horizontalLayout.addWidget(self.groupBox)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMaximumSize(QSize(310, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.groupBox_3)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.get_video = QToolButton(self.groupBox_3)
        self.get_video.setObjectName(u"get_video")

        self.horizontalLayout_2.addWidget(self.get_video)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_10 = QLabel(self.groupBox_3)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_7.addWidget(self.label_10)

        self.codec_name = QLabel(self.groupBox_3)
        self.codec_name.setObjectName(u"codec_name")

        self.horizontalLayout_7.addWidget(self.codec_name)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_6)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.groupBox_3)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.v_bit_rate = QLabel(self.groupBox_3)
        self.v_bit_rate.setObjectName(u"v_bit_rate")

        self.horizontalLayout_3.addWidget(self.v_bit_rate)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.groupBox_3)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.v_fps = QLabel(self.groupBox_3)
        self.v_fps.setObjectName(u"v_fps")

        self.horizontalLayout_4.addWidget(self.v_fps)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(-1, 20, -1, -1)
        self.label_4 = QLabel(self.groupBox_3)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_11.addWidget(self.label_4)

        self.a_codec_name = QLabel(self.groupBox_3)
        self.a_codec_name.setObjectName(u"a_codec_name")

        self.horizontalLayout_11.addWidget(self.a_codec_name)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_5)


        self.verticalLayout_2.addLayout(self.horizontalLayout_11)


        self.verticalLayout.addWidget(self.groupBox_3)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMaximumSize(QSize(310, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.bt_format = QPushButton(self.groupBox_2)
        self.bt_format.setObjectName(u"bt_format")
        self.bt_format.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout_5.addWidget(self.bt_format)

        self.v_codec_value = QComboBox(self.groupBox_2)
        self.v_codec_value.addItem("")
        self.v_codec_value.setObjectName(u"v_codec_value")

        self.horizontalLayout_5.addWidget(self.v_codec_value)

        self.v_format_value = QLineEdit(self.groupBox_2)
        self.v_format_value.setObjectName(u"v_format_value")
        self.v_format_value.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_5.addWidget(self.v_format_value)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.bt_audio = QPushButton(self.groupBox_2)
        self.bt_audio.setObjectName(u"bt_audio")
        self.bt_audio.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout_9.addWidget(self.bt_audio)

        self.a_codec_value = QComboBox(self.groupBox_2)
        self.a_codec_value.addItem("")
        self.a_codec_value.setObjectName(u"a_codec_value")

        self.horizontalLayout_9.addWidget(self.a_codec_value)

        self.a_format_value = QLineEdit(self.groupBox_2)
        self.a_format_value.setObjectName(u"a_format_value")
        self.a_format_value.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_9.addWidget(self.a_format_value)


        self.verticalLayout_3.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.bt_mz = QPushButton(self.groupBox_2)
        self.bt_mz.setObjectName(u"bt_mz")
        self.bt_mz.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout_10.addWidget(self.bt_mz)

        self.i_m = QLineEdit(self.groupBox_2)
        self.i_m.setObjectName(u"i_m")

        self.horizontalLayout_10.addWidget(self.i_m)

        self.i_z = QLineEdit(self.groupBox_2)
        self.i_z.setObjectName(u"i_z")

        self.horizontalLayout_10.addWidget(self.i_z)


        self.verticalLayout_3.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.v_rate_idea = QPushButton(self.groupBox_2)
        self.v_rate_idea.setObjectName(u"v_rate_idea")

        self.horizontalLayout_13.addWidget(self.v_rate_idea)

        self.v_rate_idea_size = QLineEdit(self.groupBox_2)
        self.v_rate_idea_size.setObjectName(u"v_rate_idea_size")

        self.horizontalLayout_13.addWidget(self.v_rate_idea_size)

        self.v_rate_idea_value = QLineEdit(self.groupBox_2)
        self.v_rate_idea_value.setObjectName(u"v_rate_idea_value")

        self.horizontalLayout_13.addWidget(self.v_rate_idea_value)


        self.verticalLayout_3.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 20, -1, -1)
        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_6.addWidget(self.label_5)

        self.work_tips = QLabel(self.groupBox_2)
        self.work_tips.setObjectName(u"work_tips")

        self.horizontalLayout_6.addWidget(self.work_tips)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_13 = QLabel(self.groupBox_2)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_12.addWidget(self.label_13)

        self.out_path = QTextBrowser(self.groupBox_2)
        self.out_path.setObjectName(u"out_path")
        self.out_path.setMaximumSize(QSize(16777215, 40))

        self.horizontalLayout_12.addWidget(self.out_path)


        self.verticalLayout_3.addLayout(self.horizontalLayout_12)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"color: gray;")
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.label_7)


        self.verticalLayout.addWidget(self.groupBox_2)


        self.horizontalLayout.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u65e5\u5fd7", None))
        self.log_text.setPlaceholderText(QCoreApplication.translate("MainWindow", u"FFmpeg\u8fd0\u884c\u65e5\u5fd7", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u53c2\u6570", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u89c6\u9891\uff1a", None))
        self.get_video.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u89c6\u9891\u7f16\u7801\uff1a", None))
        self.codec_name.setText(QCoreApplication.translate("MainWindow", u"\u6682\u65e0", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u89c6\u9891\u7801\u7387\uff1a", None))
        self.v_bit_rate.setText(QCoreApplication.translate("MainWindow", u"\u6682\u65e0", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u89c6\u9891\u5e27\u7387\uff1a", None))
        self.v_fps.setText(QCoreApplication.translate("MainWindow", u"\u6682\u65e0", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u97f3\u9891\u7f16\u7801\uff1a", None))
        self.a_codec_name.setText(QCoreApplication.translate("MainWindow", u"\u6682\u65e0", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u64cd\u4f5c", None))
        self.bt_format.setText(QCoreApplication.translate("MainWindow", u"\u683c\u5f0f\u8f6c\u6362", None))
        self.v_codec_value.setItemText(0, QCoreApplication.translate("MainWindow", u"libx264", None))

        self.v_codec_value.setPlaceholderText("")
        self.v_format_value.setText(QCoreApplication.translate("MainWindow", u"mp4", None))
        self.bt_audio.setText(QCoreApplication.translate("MainWindow", u"\u63d0\u53d6\u97f3\u9891", None))
        self.a_codec_value.setItemText(0, QCoreApplication.translate("MainWindow", u"mp3", None))

        self.a_format_value.setText(QCoreApplication.translate("MainWindow", u"mp3", None))
        self.bt_mz.setText(QCoreApplication.translate("MainWindow", u"\u7801/\u5e27\u7387\u5904\u7406", None))
        self.i_m.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u7801\u7387(\u9ed8\u8ba4\u4e0d\u4fee\u6539)", None))
        self.i_z.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u5e27\u7387(\u9ed8\u8ba430)", None))
        self.v_rate_idea.setText(QCoreApplication.translate("MainWindow", u"\u7801\u7387\u8ba1\u7b97", None))
        self.v_rate_idea_size.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u7406\u60f3\u89c6\u9891\u5927\u5c0f", None))
        self.v_rate_idea_value.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u7ed3\u679c", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u72b6\u6001\uff1a", None))
        self.work_tips.setText(QCoreApplication.translate("MainWindow", u"\u5f85\u5904\u7406...", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u51fa\uff1a", None))
        self.out_path.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8f93\u51fa\u8def\u5f84", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u6765\u81ea\uff1awww.dnxrzl.com", None))
    # retranslateUi

