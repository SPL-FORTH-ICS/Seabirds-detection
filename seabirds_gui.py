from PyQt5 import QtCore, QtGui, QtWidgets
import sys, os, glob
sys.path.append("./resources/gui_icons")


import warnings
warnings.filterwarnings('ignore')
version = "0.7"
MWname = "MainWindow"
modelFolderPath = "./model/"
html_pre = "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7.8pt;\">"
html_suf = "</span></p></body></html>"
class Ui_MW(object):
    def setupUi(self, MW):
        MW.setObjectName("MW")
        MW.resize(800, 700)
        self.centralwidget = QtWidgets.QWidget(MW)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 801, 700))
        self.stackedWidget.setLineWidth(1)
        self.stackedWidget.setObjectName("stackedWidget")
        self.MainPage = QtWidgets.QWidget()
        self.MainPage.setObjectName("MainPage")
        self.frame = QtWidgets.QFrame(self.MainPage)
        self.frame.setGeometry(QtCore.QRect(0, 0, 801, 701))
        self.frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(221, 231, 199, 255), stop:1 rgba(238, 248, 214, 255));\n"
"border-radius: 10px\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(30, 60, 741, 531))
        self.frame_2.setStyleSheet("background-color: rgb(227, 227, 227);border-radius:10px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.files_label = QtWidgets.QLabel(self.frame_2)
        self.files_label.setGeometry(QtCore.QRect(20, 160, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setUnderline(True)
        self.files_label.setFont(font)
        self.files_label.setObjectName("files_label")
        self.in_set_label = QtWidgets.QLabel(self.frame_2)
        self.in_set_label.setGeometry(QtCore.QRect(20, 120, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setUnderline(True)
        self.in_set_label.setFont(font)
        self.in_set_label.setObjectName("in_set_label")
        self.in_set_frame = QtWidgets.QFrame(self.frame_2)
        self.in_set_frame.setGeometry(QtCore.QRect(170, 100, 441, 51))
        self.in_set_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.in_set_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.in_set_frame.setObjectName("in_set_frame")
        self.include_sub = QtWidgets.QCheckBox(self.in_set_frame)
        self.include_sub.setGeometry(QtCore.QRect(20, 10, 91, 32))
        self.include_sub.setObjectName("include_sub")
        self.exclude_timestamps = QtWidgets.QCheckBox(self.in_set_frame)
        self.exclude_timestamps.setGeometry(QtCore.QRect(280, 10, 151, 32))
        self.exclude_timestamps.setObjectName("exclude_timestamps")

        # self.include_sub = QtWidgets.QCheckBox(self.frame_2)
        # self.include_sub.setGeometry(QtCore.QRect(630, 20, 91, 32))
        # self.include_sub.setObjectName("include_sub")
        # self.exclude_timestamps = QtWidgets.QCheckBox(self.frame_2)
        # self.exclude_timestamps.setGeometry(QtCore.QRect(630, 55, 91, 42))
        # self.exclude_timestamps.setObjectName("exclude_timestamps")
        self.btn_dir_IN = QtWidgets.QPushButton(self.frame_2)
        self.btn_dir_IN.setGeometry(QtCore.QRect(10, 20, 151, 81))
        CalibFont = QtGui.QFont("Calibri", 12, QtGui.QFont.Normal)
        self.btn_dir_IN.setFont(CalibFont)
        self.btn_dir_IN.setStyleSheet("QPushButton{ \n"
"border:0.5px solid grey; \n"
"border-radius: 7px; \n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(60, 137, 109, 255), stop:1 rgba(60, 137, 109, 100));\n"
"}\n"
"QPushButton:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(172, 194, 170, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        self.btn_dir_IN.setObjectName("btn_dir_IN")
        self.wavs = QtWidgets.QTextBrowser(self.frame_2)
        self.wavs.setGeometry(QtCore.QRect(180, 160, 541, 81))
        wavFont = QtGui.QFont("Helvetica", 9)
        self.wavs.setFont(wavFont)
        self.wavs.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.wavs.setObjectName("wavs")
        self.pathIN = QtWidgets.QTextBrowser(self.frame_2)
        self.pathIN.setGeometry(QtCore.QRect(180, 30, 541, 61))
        self.pathIN.setFont(wavFont)
        self.pathIN.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.pathIN.setObjectName("pathIN")
        self.dir_label = QtWidgets.QLabel(self.frame_2)
        self.dir_label.setGeometry(QtCore.QRect(180, 10, 161, 16))
        dirFont = QtGui.QFont("Helvetica", 9, QtGui.QFont.Normal)
        dirFont.setUnderline(True)
        self.dir_label.setFont(dirFont)
        self.dir_label.setStyleSheet("")
        self.dir_label.setObjectName("dir_label")
        
        self.out_set_label = QtWidgets.QLabel(self.frame_2)
        self.out_set_label.setGeometry(QtCore.QRect(20, 370, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setUnderline(True)
        self.out_set_label.setFont(font)
        self.out_set_label.setObjectName("out_set_label")
        
        self.out_set_frame = QtWidgets.QFrame(self.frame_2)
        self.out_set_frame.setGeometry(QtCore.QRect(170, 350, 441, 41))
        self.out_set_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.out_set_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.out_set_frame.setObjectName("out_set_frame")
        self.extract_wav = QtWidgets.QCheckBox(self.out_set_frame)
        self.extract_wav.setGeometry(QtCore.QRect(20, 10, 141, 32))
        self.extract_wav.setObjectName("extract_wav")
        self.extract_tg = QtWidgets.QCheckBox(self.out_set_frame)
        self.extract_tg.setGeometry(QtCore.QRect(280, 10, 151, 32))
        self.extract_tg.setObjectName("extract_tg")
        self.line = QtWidgets.QFrame(self.frame_2)
        self.line.setGeometry(QtCore.QRect(20, 400, 701, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

                 
        self.cpu_frame = QtWidgets.QFrame(self.frame_2)
        self.cpu_frame.setGeometry(QtCore.QRect(170, 420, 549, 41))
        self.cpu_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.cpu_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cpu_frame.setObjectName("cpu_frame")
        self.label_2 = QtWidgets.QLabel(self.cpu_frame)
        self.label_2.setGeometry(QtCore.QRect(20, -8, 111, 58))
        self.label_2.setObjectName("label_2")
        self.gridLayoutWidget = QtWidgets.QWidget(self.cpu_frame)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(220, 5, 291, 31))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        # self.radio_low = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radio_no = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radio_no.setObjectName("radio_no")
        self.radio_no.setChecked(True)
        self.gridLayout.addWidget(self.radio_no, 0, 0, 1, 1)
        self.radio_mid = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radio_mid.setObjectName("radio_mid")
        # self.radio_mid.setChecked(True)
        self.gridLayout.addWidget(self.radio_mid, 0, 1, 1, 1)
        self.radio_high = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radio_high.setObjectName("radio_high")
        self.gridLayout.addWidget(self.radio_high, 0, 2, 1, 1)
        self.btn_dir_IN_OUT = QtWidgets.QPushButton(self.frame_2)
        self.btn_dir_IN_OUT.setGeometry(QtCore.QRect(10, 260, 151, 80))
        btn_dir_IN_OUT_font = QtGui.QFont("Calibri", 12, QtGui.QFont.Normal)
        self.btn_dir_IN_OUT.setFont(btn_dir_IN_OUT_font)
        self.btn_dir_IN_OUT.setStyleSheet("QPushButton{ \n"
"border:0.5px solid grey; \n"
"border-radius: 7px; \n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(60, 137, 109, 255), stop:1 rgba(60, 137, 109, 100));\n"
"}\n"
"QPushButton:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(172, 194, 170, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        self.btn_dir_IN_OUT.setObjectName("btn_dir_IN_OUT")
        self.pathOUT = QtWidgets.QTextBrowser(self.frame_2)
        self.pathOUT.setGeometry(QtCore.QRect(180, 270, 541, 60))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pathOUT.setFont(font)
        self.pathOUT.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.pathOUT.setObjectName("pathOUT")
        self.files_label_2 = QtWidgets.QLabel(self.frame_2)
        self.files_label_2.setGeometry(QtCore.QRect(20, 431, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setUnderline(True)
        self.files_label_2.setFont(font)
        self.files_label_2.setObjectName("files_label_2")

        self.prob_label = QtWidgets.QLabel(self.frame_2)
        self.prob_label.setGeometry(QtCore.QRect(190, 471, 151, 58))
        self.prob_label.setObjectName("prob_label")
        self.prob_spinbox = QtWidgets.QDoubleSpinBox(self.frame_2)
        self.prob_spinbox.setGeometry(QtCore.QRect(390, 478, 111, 41))
        self.prob_spinbox.setMinimum(0.01)
        self.prob_spinbox.setMaximum(0.99)
        self.prob_spinbox.setSingleStep(0.01)
        self.prob_spinbox.setProperty("value", 0.75)
        self.prob_spinbox.setObjectName("prob_spinbox")

        self.frame_title = QtWidgets.QFrame(self.frame)
        self.frame_title.setGeometry(QtCore.QRect(0, 0, 801, 31))
        self.frame_title.setStyleSheet("background-color: rgba(1, 32, 15, 100)")
        self.frame_title.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_title.setObjectName("frame_title")
        self.btn_min = QtWidgets.QPushButton(self.frame_title)
        self.btn_min.setGeometry(QtCore.QRect(740, 5, 20, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_min.setFont(font)
        self.btn_min.setStyleSheet("QPushButton{ \n"
"border:none; \n"
"border-radius: 7px; \n"
"background-color:rgb(240, 135, 0);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(240, 135, 0, 150);\n"
"}")
        self.btn_min.setObjectName("btn_min")
        self.btn_exit = QtWidgets.QPushButton(self.frame_title)
        self.btn_exit.setGeometry(QtCore.QRect(770, 5, 20, 20))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_exit.setFont(font)
        self.btn_exit.setStyleSheet("QPushButton{ \n"
"border:none; \n"
"border-radius: 7px; \n"
"background-color: rgb(235, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(235,0,0, 150);\n"
"}")
        self.btn_exit.setObjectName("btn_exit")
        self.title = QtWidgets.QLabel(self.frame_title)
        self.title.setGeometry(QtCore.QRect(11, -3, 381, 41))
        font = QtGui.QFont()
        font.setFamily("Caladea")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setAutoFillBackground(False)
        self.title.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.title.setObjectName("title")
        self.btn_run = QtWidgets.QPushButton(self.frame)
        self.btn_run.setGeometry(QtCore.QRect(300, 610, 221, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_run.setFont(font)
        self.btn_run.setStyleSheet("QPushButton{ \n"
"border:0.5px solid grey; \n"
"border-radius: 7px; \n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(60, 137, 109, 255), stop:1 rgba(60, 137, 109, 100));\n"
"}\n"
"QPushButton:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(172, 194, 170, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(172, 194, 170, 10), stop:1 rgba(255, 255, 255, 10));\n"
"}\n"
"\n"
"")
        self.btn_run.setObjectName("btn_run")
        self.stackedWidget.addWidget(self.MainPage)
        self.DetectionsPage = QtWidgets.QWidget()
        self.DetectionsPage.setObjectName("DetectionsPage")
        self.frame_4 = QtWidgets.QFrame(self.DetectionsPage)
        self.frame_4.setGeometry(QtCore.QRect(0, 0, 801, 701))
        self.frame_4.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(221, 231, 199, 255), stop:1 rgba(238, 248, 214, 255));\n"
"border-radius: 10px\n"
"")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        self.frame_5.setGeometry(QtCore.QRect(30, 120, 741, 461))
        self.frame_5.setStyleSheet("background-color: rgb(227, 227, 227);border-radius:10px;")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.results = QtWidgets.QPlainTextEdit(self.frame_5)
        self.results.setGeometry(QtCore.QRect(20, 130, 701, 301))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.results.setFont(font)
        self.results.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.results.setReadOnly(True)
        self.results.setObjectName("results")
        self.dir_label_2 = QtWidgets.QLabel(self.frame_5)
        self.dir_label_2.setGeometry(QtCore.QRect(20, 20, 221, 52))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.dir_label_2.setFont(font)
        self.dir_label_2.setStyleSheet("")
        self.dir_label_2.setObjectName("dir_label_2")
        self.pathIN_2 = QtWidgets.QTextBrowser(self.frame_5)
        self.pathIN_2.setGeometry(QtCore.QRect(250, 20, 471, 61))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pathIN_2.setFont(font)
        self.pathIN_2.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.pathIN_2.setObjectName("pathIN_2")
        self.textEdit = QtWidgets.QTextEdit(self.frame_5)
        self.textEdit.setGeometry(QtCore.QRect(680, 140, 31, 31))
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame_5)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 90, 701, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.checkBox_sc = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_sc.setObjectName("checkBox_sc")
        self.horizontalLayout.addWidget(self.checkBox_sc)
        self.checkBox_yel = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_yel.setObjectName("checkBox_yel")
        self.horizontalLayout.addWidget(self.checkBox_yel)
        self.checkBox_sc.setChecked(True)
        self.checkBox_yel.setChecked(True)

        self.checkBox_sc.stateChanged.connect(self.update_df)
        self.checkBox_yel.stateChanged.connect(self.update_df)
        
        self.frame_title_3 = QtWidgets.QFrame(self.frame_4)
        self.frame_title_3.setGeometry(QtCore.QRect(0, 0, 801, 31))
        self.frame_title_3.setStyleSheet("background-color: rgba(1, 32, 15, 100)")
        self.frame_title_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_title_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_title_3.setObjectName("frame_title_3")
        self.btn_min_3 = QtWidgets.QPushButton(self.frame_title_3)
        self.btn_min_3.setGeometry(QtCore.QRect(740, 5, 20, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_min_3.setFont(font)
        self.btn_min_3.setStyleSheet("QPushButton{ \n"
"border:none; \n"
"border-radius: 7px; \n"
"background-color:rgb(240, 135, 0);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(240, 135, 0, 150);\n"
"}")
        self.btn_min_3.setObjectName("btn_min_3")
        self.btn_exit_3 = QtWidgets.QPushButton(self.frame_title_3)
        self.btn_exit_3.setGeometry(QtCore.QRect(770, 5, 20, 20))
        font = QtGui.QFont()
        font.setFamily("Corbel")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn_exit_3.setFont(font)
        self.btn_exit_3.setStyleSheet("QPushButton{ \n"
"border:none; \n"
"border-radius: 7px; \n"
"background-color: rgb(235, 0, 0);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(235,0,0, 150);\n"
"}")
        self.btn_exit_3.setObjectName("btn_exit_3")
        self.title_4 = QtWidgets.QLabel(self.frame_title_3)
        self.title_4.setGeometry(QtCore.QRect(11, -3, 381, 41))
        font = QtGui.QFont()
        font.setFamily("Caladea")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.title_4.setFont(font)
        self.title_4.setAutoFillBackground(False)
        self.title_4.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.title_4.setObjectName("title_4")
        self.title_det = QtWidgets.QLabel(self.frame_4)
        self.title_det.setGeometry(QtCore.QRect(30, 70, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Caladea")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.title_det.setFont(font)
        self.title_det.setAutoFillBackground(False)
        self.title_det.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.title_det.setObjectName("title_det")
        self.btn_xlsx = QtWidgets.QPushButton(self.frame_4)
        self.btn_xlsx.setGeometry(QtCore.QRect(470, 620, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_xlsx.setFont(font)
        self.btn_xlsx.setStyleSheet("QPushButton{ \n"
"border:0.5px solid grey; \n"
"border-radius: 7px; \n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(60, 137, 109, 255), stop:1 rgba(60, 137, 109, 100));\n"
"}\n"
"QPushButton:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(172, 194, 170, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(172, 194, 170, 10), stop:1 rgba(255, 255, 255, 10));\n"
"}\n"
"\n"
"")
        self.btn_xlsx.setObjectName("btn_xlsx")
        self.btn_txt = QtWidgets.QPushButton(self.frame_4)
        self.btn_txt.setGeometry(QtCore.QRect(140, 620, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_txt.setFont(font)
        self.btn_txt.setStyleSheet("QPushButton{ \n"
"border:0.5px solid grey; \n"
"border-radius: 7px; \n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(60, 137, 109, 255), stop:1 rgba(60, 137, 109, 100));\n"
"}\n"
"QPushButton:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(172, 194, 170, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(172, 194, 170, 10), stop:1 rgba(255, 255, 255, 10));\n"
"}\n"
"\n"
"")
        self.btn_txt.setObjectName("btn_txt")
        self.btn_change_view = QtWidgets.QPushButton(self.frame_4)
        self.btn_change_view.setGeometry(QtCore.QRect(620, 50, 151, 61))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.btn_change_view.setFont(font)
        self.btn_change_view.setStyleSheet("QPushButton{ \n"
"border:0.5px solid grey; \n"
"border-radius: 7px; \n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(60, 137, 109, 255), stop:1 rgba(60, 137, 109, 100));\n"
"}\n"
"QPushButton:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(172, 194, 170, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        self.btn_change_view.setObjectName("btn_change_view")


        self.stackedWidget.addWidget(self.DetectionsPage)
        MW.setCentralWidget(self.centralwidget)

        self.retranslateUi(MW)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MW)

    def retranslateUi(self, MW):
        _translate = QtCore.QCoreApplication.translate
        MW.setWindowTitle(_translate("MW", "MW"))
        self.files_label.setText(_translate("MW", "Files to be processed:"))
        # self.include_sub.setText(_translate("MW", "Include\nSubfolders"))
        # self.exclude_timestamps.setText(_translate("MW", "Exclude\nfiles with\ntimestamp"))        
        self.in_set_label.setText(_translate("MainWindow", "Input settings:"))
        self.out_set_label.setText(_translate("MainWindow", "Output settings:"))
        self.include_sub.setText(_translate("MainWindow", "Include\n"
"Subfolders"))
        self.exclude_timestamps.setText(_translate("MainWindow", "Exclude files \n"
"with timestamp"))
        self.extract_wav.setText(_translate("MainWindow", "Extract a wav file \n"
"for each detection"))
        self.extract_tg.setText(_translate("MainWindow", "Extract a TextGrid file \n"
"for each input file"))

        self.btn_dir_IN.setText(_translate("MW", "Select\nInput\nDirectory"))
        self.wavs.setHtml(_translate("MW", html_pre + "[No directory selected]" + html_suf))
        self.pathIN.setHtml(_translate("MW", html_pre + "[Please select a directory]" + html_suf))
        self.dir_label.setText(_translate("MW", "Directory with wav files:"))
#         self.model_label.setText(_translate("MW", "Select model (for \n"
# "classification):"))
        self.label_2.setText(_translate("MW", "Parallelization:\n(Multiprocessing)"))
        # self.radio_low.setText(_translate("MW", "Low"))
        self.radio_mid.setText(_translate("MW", "Mid"))
        self.radio_no.setText(_translate("MW", "No"))
        self.radio_high.setText(_translate("MW", "Full"))
        
        
        max_cpus = self.count_processors()
        self.cpu_choice_list = [1, max_cpus//2, max_cpus]
        self.cpus = self.cpu_choice_list[0]
        # self.radio_low.clicked.connect(self.parse_cpu_radio)
        self.radio_no.clicked.connect(self.parse_cpu_radio)
        self.radio_mid.clicked.connect(self.parse_cpu_radio)
        self.radio_high.clicked.connect(self.parse_cpu_radio)
        self.btn_xlsx.clicked.connect(self.export_xlsx)
        self.btn_txt.clicked.connect(self.export_txt)
        self.btn_change_view.clicked.connect(self.change_view)
        
        self.btn_dir_IN_OUT.setText(_translate("MW", "Select\n"
"Output\n"
"Directory"))
        self.btn_dir_IN_OUT.clicked.connect(lambda func: self.select_dir(self.pathOUT, self.btn_dir_IN_OUT))                
        self.pathOUT.setHtml(_translate("MW", html_pre + "[Please select a directory]" + html_suf))
        self.files_label_2.setText(_translate("MW", "Advanced settings:"))
        self.prob_label.setText(_translate("MainWindow", "Probability threshold:"))
        self.btn_min.setText(_translate("MW", "_"))
        self.btn_exit.setText(_translate("MW", "X"))
        
        self.include_sub.setText(_translate("MainWindow", "Include\n"
"Subfolders"))
        self.exclude_timestamps.setText(_translate("MainWindow", "Exclude files \n"
"with timestamp"))
        self.extract_wav.setText(_translate("MainWindow", "Extract a .wav file \n"
"for each detection"))
        self.extract_tg.setText(_translate("MainWindow", "Extract a TextGrid file \n"
"for each input file"))

        self.btn_min.clicked.connect(self.minimize)       
        self.btn_exit.clicked.connect(self.on_closing)  
        self.btn_dir_IN.clicked.connect(lambda func: self.select_dir(self.pathIN, self.btn_dir_IN))                
        self.include_sub.stateChanged.connect(self.update_files)
        self.exclude_timestamps.stateChanged.connect(self.update_files)

        self.btn_run.setEnabled(False)  
        self.btn_run.clicked.connect(self.run_main)   
        
        self.title.setText(_translate("MW", f"Seabird Detector (v {version})"))
        self.btn_run.setText(_translate("MW", "Run"))
        
        
        self.dir_label_2.setText(_translate("MW", "Directory with wav files scanned:"))
        self.pathIN_2.setHtml(_translate("MW", html_pre + "[Please select a directory]" + html_suf))
        self.textEdit.setHtml(_translate("MW", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/navigation/pop-out3.png\" width=\"18\" /></p></body></html>"))
        
        self.label.setText(_translate("MainWindow", "Classes Included:"))
        self.checkBox_sc.setText(_translate("MainWindow", "Scopoli"))
        self.checkBox_yel.setText(_translate("MainWindow", "Yelkouan"))
        # self.checkBox.setText(_translate("MainWindow", "Overlap"))
        # self.checkBox_noi.setText(_translate("MainWindow", "Noise"))
        
        self.btn_min_3.setText(_translate("MW", "_"))
        self.btn_exit_3.setText(_translate("MW", "X"))
        self.btn_min_3.clicked.connect(self.minimize)       
        self.btn_exit_3.clicked.connect(self.on_closing)  
        
        self.title_4.setText(_translate("MW", f"Seabird Detector (v {version})"))
        self.title_det.setText(_translate("MW", "Detections"))
        self.btn_xlsx.setText(_translate("MW", "Save as .xlsx"))
        self.btn_txt.setText(_translate("MW", "Save as .txt"))
        self.btn_change_view.setText(_translate("MW", "View total duration \n"
"of detections \n"
"per recording"))
        
        self.files = []
        

    def update_df(self):
        classes_checked = \
            self.checkBox_sc.isChecked()*['Scopoli']+\
            self.checkBox_yel.isChecked()*['Yelkouan']
            # self.checkBox.isChecked()*['Overlap']
            # self.checkBox_noi.isChecked()*['Noise']
        if len(classes_checked)==2: 
            self.df = self.df_orig
        else:
            self.df = self.df_orig.loc[self.df_orig['class'].isin(classes_checked)]
        model = pandasModel(self.df)
        self.view.setModel(model)
        self.title_det.setText(f"Detections ({self.df.shape[0]})")
        self.title_det.adjustSize()

    def change_view(self):
        if "duration" in self.btn_change_view.text():
            self.btn_change_view.setText("Switch back to\ndefault view.")
            self.df = self.df_orig
            self.df['TotDuration'] = self.df['stop']-self.df['start']
            self.df = self.df.groupby(["class", "wavFile"]).sum()['TotDuration'].reset_index()
            self.df = self.df.round(3)
            model = pandasModel(self.df)
            self.view.setModel(model)
            self.title_det.setText(f"Total Duration per wav")
            self.title_det.adjustSize()
            [element.hide() for element in \
                [self.label, self.checkBox_sc, self.checkBox_yel]]

        else:
            self.btn_change_view.setText("View total duration \n"
                                        "of detections \n"
                                        "per recording")
            self.df = self.df_orig
            self.update_df()
            [element.show() for element in \
                [self.label, self.checkBox_sc, self.checkBox_yel]]


    def run_btn_enable(self):
        cond1 = len(self.files)>0
        cond2 = self.pathOUT.toPlainText()!="[Please select a directory]"
        if cond1 and cond2:
            self.btn_run.setEnabled(True)
            self.btn_run.setText("Run")
        else:
            self.btn_run.setEnabled(False)
            if not cond1:
                self.btn_run.setText("Run\n(Select a valid input dir)")
            elif not cond2:
                self.btn_run.setText("Run\n(Select a valid output dir)")

    def select_dir(self, text_widget, btn_widget):
        import glob
        folder = str(QtWidgets.QFileDialog.getExistingDirectory(self, "Select Directory"))
        if folder:
            text_widget.setText(folder)
        if text_widget==self.pathIN:
            self.update_files()
            btn_widget.setText("Change\nInput\nDirectory")
        else:
            if text_widget.toPlainText()!="[Please select a directory]":
                btn_widget.setText("Change\nOutput\nDirectory")
            self.run_btn_enable()
                # self.btn_run.setEnabled(True)
                # self.btn_run.setText("Run")

    def update_files(self):
        timestamp_pattern = "[0-9][0-9]h[0-9][0-9]m[0-9][0-9]s"
        folder = self.pathIN.toPlainText()
        if self.include_sub.isChecked():
            files = glob.glob(f"{folder}/**/*.wav", recursive=True)
        else:
            files = glob.glob(f"{folder}/*.wav", recursive=False)

        #CHECK THIS AGAIN
        if self.exclude_timestamps.isChecked():
            files = list(set(files) - set(glob.glob(f"{folder}/**/*{timestamp_pattern}*.wav", recursive=True)))
        
        self.files = files

        if len(files)>0:
            files = "\n".join(files).replace("\\", "/").replace(folder, "./")
            # self.files = files
            self.run_btn_enable()
            # self.btn_run.setEnabled(True)
            # self.btn_run.setText("Run")
        else:
            files = "No .wav files found in selected directory."
            # self.btn_run.setText("Run\n(Select a valid input dir)")
            # self.btn_run.setEnabled(False)
            self.files = []
            self.run_btn_enable()
        self.wavs.setText(files)

    def file_save(self):
        name = QtGui.QFileDialog.getSaveFileName(self, 'Save File')
        file = open(name,'w')
        text = self.textEdit.toPlainText()
        file.write(text)
        file.close()
        

    def export_xlsx(self):
        import os
        fname = f'{self.pathOUT.toPlainText()}/Detections_table.xlsx'
        i=1
        if os.path.exists(fname):
            fname = fname.replace(".xlsx", f"_{i}.xlsx")
            while os.path.exists(fname):
                i+=1
                fname = fname.replace(f"_{i-1}.xlsx", f"_{i}.xlsx")
        self.df.to_excel(fname, index=False)
        QtWidgets.QMessageBox.information(self, 'Save succesful!',
            f"File saved as\n{fname}", QtWidgets.QMessageBox.Ok)
        
    def export_txt(self):
        import os
        fname = f'{self.pathOUT.toPlainText()}/Detections_table.txt'
        i=1
        if os.path.exists(fname):
            fname = fname.replace(".txt", f"_{i}.txt")
            while os.path.exists(fname):
                i+=1
                fname = fname.replace(f"_{i-1}.txt", f"_{i}.txt")
        self.df.to_csv((fname), index=False, header=True, sep='\t') #, mode='a')                

        QtWidgets.QMessageBox.information(self, 'Save succesful!',
            f"File saved as\n{fname}", QtWidgets.QMessageBox.Ok)


    def minimize(self):
        self.showMinimized()

    def on_closing(self):
        import gc

        reply = QtWidgets.QMessageBox.question(self, 'Quit',
            "Are you sure to quit?", QtWidgets.QMessageBox.Yes | 
            QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            print('Thank you for using our tool!')
            self.close()
            gc.collect()

    def create_out_subfolders(self, pathOUT):
        out_subfolders = ["Scopoli", "Yelkouan"]
        for className in out_subfolders:
            subf = f"{pathOUT}/{className}" 
            if not os.path.exists(subf):
                os.makedirs(subf)
            else:
                print(f"folder {subf} already exists")
          
          
    def parse_cpu_radio(self):
        if self.radio_no.isChecked():     i=0
        elif self.radio_mid.isChecked():  i=1
        elif self.radio_high.isChecked(): i=2

        cpu_temp = self.cpu_choice_list[i]
        self.cpus = max([1, cpu_temp])        
        
               
    def count_processors(self):
        import multiprocessing
        import numpy as np
        nop=multiprocessing.cpu_count()
        # print(str(int(nop)) + ' cpus found')
        return nop            
    
    def initialize_files(self):
        import glob, os, pandas as pd, numpy as np
        pathIN = self.pathIN.toPlainText()
        self.pathIN_2.setText(pathIN)
        cwd = os.getcwd().replace("\\", "/")
        self.df = self.df_orig
        if len(glob.glob(f"{self.pathOUT.toPlainText()}\\detections\\*.csv"))<1 or self.df_orig.empty:
            self.results.setPlainText("No instances found.")
            self.results.show()
            self.results.setReadOnly(True)
            self.btn_xlsx.hide()
            self.btn_txt.hide()
            self.btn_change_view.hide()
            [element.hide() for element in \
                [self.label, self.checkBox_sc, self.checkBox_yel]]
        else:
            self.results.setPlainText(self.df.to_markdown(index=False))#, tablefmt="grid"))
            model = pandasModel(self.df)
            self.view = QtWidgets.QTableView(parent = self.frame_5)
            self.view.setGeometry(QtCore.QRect(20, 130, 701, 301))
            self.view.setModel(model)
            self.results.hide()
            self.view.show()
            self.title_det.setText(f"Detections ({self.df.shape[0]})")
            self.title_det.adjustSize()
        
    

    
    def export_analysis_report(self, dt0_1, dt1_1, pathIN, probabilityThreshold, cpus_used, all_data, analysis_files):
       
        Npositives_Scopoli, Npositives_Yelkouan, Npositives_Overlap = [sum(all_data['class'] == cl) for cl in ["Scopoli", "Yelkouan", "Overlap"]] 

        if self.radio_no.isChecked():     i="No"
        elif self.radio_mid.isChecked():  i="Mid"
        elif self.radio_high.isChecked(): i="High"

        analysis_report = ("Analysis report:\n"
                        "---------------\n"
                        f"Analysis started: {dt0_1}\n"
                        f"Analysis ended: {dt1_1}\n"
                        "\n"
                        f"Directory analyzed: {pathIN}\n"
                        f"(subfolders {'not '*(1-self.include_sub.isChecked())}included)\n"
                        "\n"
                        "Paremeters used:\n"
                        f"\tprobabilityThreshold: {probabilityThreshold}\n"
                        f"\tParallelization: '{i}' (CPUs used: {cpus_used})\n"
                        "\n"
                        "Stats:\n"
                        f"\t# of positive classified as Scopoli: {Npositives_Scopoli}\n"
                        f"\t# of positive classified as Yelkouan: {Npositives_Yelkouan}\n"
                        f"\t# of positive classified as Overlap: {Npositives_Overlap}\n"                        
                        "\n"
                        f"List of wav files processed ({len(analysis_files)}):\n")
        analysis_report += "\n".join(analysis_files)
        return analysis_report


    def run_main(self):
        import sys, os, time
        import pandas as pd
        sys.path.append("./src")
        from multiprocessing import Pool, Lock
        from lib import params
        from lib import multi_Yamnet_new
        import datetime

        remove_intermediate_csv = True
        modelFolderPath = os.path.abspath("./model/")
        # model = 'multilabel3classes_dur0p96_noRes_21Feb.hdf5'
        model = 'model2run.hdf5' #delivered with code
        recursive = self.include_sub.isChecked()
        extract_wavs = self.extract_wav.isChecked()
        extract_tgs = self.extract_tg.isChecked()
        folderIN = self.pathIN.toPlainText()
        folderOUT = self.pathOUT.toPlainText()
        probThresh = self.prob_spinbox.value()
        params['probThreshold'] = probThresh
        self.create_out_subfolders(folderOUT)
        
        print("Starting execution. Please wait...")

        filesIN = self.files
        # df = pd.DataFrame()        
        pool=Pool(self.cpus)
               
        if not os.path.exists(f"{folderOUT}\\detections"):
            os.makedirs(f"{folderOUT}\\detections")
       

        dt0 = datetime.datetime.now()
        dt0_1 = dt0.strftime("%d/%m/%Y %H:%M:%S") 
        

        classificationMatrix = None
        for wavFilePath in self.files: 
            # pdb.set_trace()
            pool.apply_async(multi_Yamnet_new, \
                    args=(params, \
                     wavFilePath, classificationMatrix, \
                     folderOUT, modelFolderPath.rstrip("/").rstrip("\\"), model,\
                     extract_wavs, extract_tgs))
        pool.close()
        pool.join()

        dt1 = datetime.datetime.now()
        dt1_1 = dt1.strftime("%d/%m/%Y %H:%M:%S") 
        tmstmp_1 = dt1.strftime("%d%m%y_%H%M%S")


        self.df_orig = pd.DataFrame()
        for csv_file in glob.glob(f"{folderOUT}\\detections\\*.csv"):
            if self.df_orig.empty:
                self.df_orig = pd.read_csv(csv_file)
            else:
                self.df_orig = pd.concat([self.df_orig, pd.read_csv(csv_file)], ignore_index=True)

        analysis_report = self.export_analysis_report(dt0_1, dt1_1, folderIN, probThresh, self.cpus, self.df_orig, self.files)

        with open(f"{folderOUT}/Analysis_report_{tmstmp_1}.txt", "w+") as fout:
            fout.write(analysis_report)

        if True:
            self.stackedWidget.setCurrentIndex(1)
            self.initialize_files()
            self.show()
            pathIN = self.pathIN.toPlainText()
            self.pathIN_2.setText(pathIN)
            
            med = (1-recursive)*"NOT "
            suffix = f"(Subfolders {med}included)"
            self.dir_label_2.setText("Directory with wav files scanned:\n"+suffix)
    
        if remove_intermediate_csv:
            try:
                for csv_file in glob.glob(f"{folderOUT}\\detections\\*.csv"):
                    os.remove(csv_file)
                
                os.rmdir(f"{folderOUT}\\detections")
            except:
                print("Couldn't delete intermediate files (folder: {folderOUT}\detections). Please remove manually.")
               
class MyWin(QtWidgets.QMainWindow, Ui_MW):
    #Stack over flow - draggable window
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.dragPos = QtCore.QPoint()
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        try:
            self.setWindowIcon(QtGui.QIcon('./resources/gui_icons/forth_disk.png'))
        except:
            pass
    def mousePressEvent(self, event):                                 # +
        self.dragPos = event.globalPos()
        
    def mouseMoveEvent(self, event):                                  # !!!
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()     


from PyQt5.QtWidgets import QApplication, QTableView
from PyQt5.QtCore import QAbstractTableModel, Qt


class pandasModel(QAbstractTableModel):

    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parnet=None):
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]
        return None



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = MyWin()
    w.show()
    sys.exit(app.exec())
    