import random
import sys
from pathlib import Path

from PIL import Image
from PyQt5 import QtCore, QtGui, QtWidgets

import ctypes
from PyQt5.QtWidgets import QPushButton, \
    QGraphicsColorizeEffect, QMessageBox
from PyQt5.QtGui import QColor
from PyQt5.QtCore import QPropertyAnimation, Qt

import pathlib
from pathlib import Path

user32 = ctypes.windll.user32  # ffas
user32.SetProcessDPIAware()
w = user32.GetSystemMetrics(0)
h = user32.GetSystemMetrics(1)
path = str(Path(pathlib.Path.cwd(), "pictures"))
score = 0
image_in_class_work_image = ""
len = 11
answers = [["одиночка", "singleton"], ["mvvm", "мввм"], ["mvp", "мвп"], ["mvt", "мвт"],
           ["команда", "command"], ["состояние", "state"], ["итератор", "iterator"],
           ["мост", "bridge"], ["строитель", "builder"], ["mvc", "мвс"],
           ["адаптер", "adapter"]]
flag_er = 0
def close_program():
    global ui
    exit(0)


class BeautifulButton(QPushButton):
    def __init__(self, *args, **kwargs):
        super(BeautifulButton, self).__init__(*args, **kwargs)
        effect = QGraphicsColorizeEffect(self)
        self.setGraphicsEffect(effect)
        self.animation = QPropertyAnimation(effect, b"color")

        self.animation.setStartValue(QColor(Qt.cyan))
        self.animation.setEndValue(QColor(255, 255, 255))
        self.animation.setDuration(5000)


class new_QMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

    def closeEvent(self, event):
        print(event)
        global score
        reply = QMessageBox.question \
            (self, 'Вы нажали на крестик',
             f"Вы уверены, что хотите уйти? Ваш счёт {score}",
             QMessageBox.Yes,
             QMessageBox.No)
        if reply == QMessageBox.Yes:
            close_program()
            event.accept()
        else:
            event.ignore()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1202, 1129)
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("icon.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(w // 4, 0, w // 4 * 3 - 50, h - 100)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tabWidget.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")

        self.label_for_img1 = QtWidgets.QLabel(self.tab_2)
        self.label_for_img1.setEnabled(True)
        self.label_for_img1.setGeometry(
            QtCore.QRect(0, 0, w // 4 * 3 - 50, h - 100))

        self.label_for_img1.setAcceptDrops(False)
        self.label_for_img1.setToolTip("")
        self.label_for_img1.setToolTipDuration(-1)
        self.label_for_img1.setAccessibleDescription("")
        self.label_for_img1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_for_img1.setAutoFillBackground(False)
        self.label_for_img1.setStyleSheet("")
        self.label_for_img1.setText("")
        self.label_for_img1.setScaledContents(False)
        self.label_for_img1.setObjectName("label_for_img1")

        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(
            QtCore.QRect(5, 5, w // 4 - 20, h - 100))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(40)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setStyleSheet("border-bottom: 2px solid black;\n"
                                 "border-radius: 0px;\n"
                                 "padding-bottom: 5px;")
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)

        self.label_score = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(300)
        self.label_score.setFont(font)
        self.label_score.setObjectName("label_score")
        self.verticalLayout_2.addWidget(self.label_score)
        self.lineEdit_for_point = QtWidgets.QLineEdit(
            self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setUnderline(False)
        self.lineEdit_for_point.setFont(font)
        self.lineEdit_for_point.setAccessibleDescription("")
        self.lineEdit_for_point.setStyleSheet("border: 1px solid;\n"
                                              "    border-radius: 20px;\n"
                                              "    background-color: gainsboro;\n"
                                              "padding-left: 10px;")
        self.lineEdit_for_point.setMaxLength(32769)
        self.lineEdit_for_point.setFrame(False)
        self.lineEdit_for_point.setObjectName("lineEdit_for_point")
        self.verticalLayout_2.addWidget(self.lineEdit_for_point)

        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.pushButton_input = BeautifulButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_input.setFont(font)
        self.pushButton_input.setObjectName("pushButton_input")
        self.horizontalLayout_12.addWidget(self.pushButton_input)

        self.pushButton_cancel = BeautifulButton(self.verticalLayoutWidget_2)
        self.pushButton_cancel.setFont(font)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.horizontalLayout_12.addWidget(self.pushButton_cancel)
        self.verticalLayout_2.addLayout(self.horizontalLayout_12)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.push_button_function()

    def push_button_function(self):
        global app
        self.pushButton_input.clicked.connect(self.input)
        self.pushButton_cancel.clicked.connect(self.cansel)

    def cansel(self):
        global score, MainWindow
        self.reply = QMessageBox.question \
            (MainWindow, 'Вы хотите выйти?',
             f"В этой игре ваш счёт {score}",
             QMessageBox.Yes,
             QMessageBox.No)
        if self.reply == QMessageBox.Yes:
            close_program()

    def find_answer(self, answer):
        if answer in answers[self.p - 1]:
            return True
        return False
    def input(self):
        global score
        answer = self.lineEdit_for_point.text().lower()
        if self.find_answer(answer):
            score += 1
        model.main_code()

    def set_model(self, model):
        self.model = model

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Игра"))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2),
                                  _translate("MainWindow", "1"))
        self.label.setText(_translate("MainWindow", "Счёт :   "))
        self.pushButton_cancel.setText(_translate("MainWindow", "Закончить"))

        self.pushButton_input.setText(_translate("MainWindow", "Отправить"))
    def start_load(self):
        self.loading_file()
    def score_set(self, score_count):
        self.label_score.setText(score_count)
    def loading_file(self):
        global path
        _translate = QtCore.QCoreApplication.translate
        picture = random.randint(1, len)
        self.p = picture
        picture = str(picture) + '.png'
        path_to_photo = path + "/" + picture
        self.image_before = Image.open(path_to_photo)
        Work_with_file.correct_photo(path_to_photo, self)
        self.pic = QtGui.QPixmap(path_to_photo)
        self.label_for_img1.setPixmap(self.pic)


class Work_with_file:
    def correct_photo(image_path, ui): #f
        global image_in_class_work_image
        if Path(image_path).suffix == '.jpg' or Path(
                image_path).suffix == '.png' or Path(
            image_path).suffix == ".jpeg":
            image_in_class_work_image = Image.open(image_path)
            image_in_class_work_image.thumbnail(size=(w // 4 * 3 - 100, h - 200))
            image_in_class_work_image.save(image_path)
            print(image_in_class_work_image.size)
            return 1












class Model:
    def __init__(self, ui):
        self.student = None
        self.ui = ui

    def main_code(self):
        global score
        ui.score_set(str(score))
        ui.lineEdit_for_point.setText("")
        ui.start_load()



def start_program():
    MainWindow.showMaximized()
    model.main_code()


app = QtWidgets.QApplication(sys.argv)
MainWindow = new_QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
model = Model(ui)
ui.set_model(model)
start_program()
sys.exit(app.exec_())
