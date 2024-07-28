# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chat_gui_main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QStackedWidget, QVBoxLayout, QWidget)
import chat_gui_app_rc
import chat_gui_app_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(750, 450)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color:rgb(237, 235, 255)")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.main_header = QFrame(self.centralwidget)
        self.main_header.setObjectName(u"main_header")
        self.main_header.setMinimumSize(QSize(0, 50))
        self.main_header.setMaximumSize(QSize(16777215, 50))
        self.main_header.setStyleSheet(u"QFrame{\n"
"	border-bottom: 1px solid  #a970c8;\n"
"	\n"
"	background-color: #a970c8;\n"
"}")
        self.main_header.setFrameShape(QFrame.WinPanel)
        self.main_header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.main_header)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.tittle_bar_container = QFrame(self.main_header)
        self.tittle_bar_container.setObjectName(u"tittle_bar_container")
        self.tittle_bar_container.setFrameShape(QFrame.StyledPanel)
        self.tittle_bar_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.tittle_bar_container)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.left_menu_toggle = QFrame(self.tittle_bar_container)
        self.left_menu_toggle.setObjectName(u"left_menu_toggle")
        self.left_menu_toggle.setMinimumSize(QSize(50, 0))
        self.left_menu_toggle.setMaximumSize(QSize(50, 16777215))
        self.left_menu_toggle.setStyleSheet(u"QFrame{\n"
"	background-color: #a970c8;\n"
"}\n"
"QPushButton{\n"
"	padding: 5px 10px;\n"
"	border: none;\n"
"	border-radius: 5px;\n"
"	background-color:#a970c8;\n"
"	color: #fff;\n"
"}\n"
"")
        self.left_menu_toggle.setFrameShape(QFrame.StyledPanel)
        self.left_menu_toggle.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.left_menu_toggle)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_5.addWidget(self.left_menu_toggle)

        self.tittle_bar = QFrame(self.tittle_bar_container)
        self.tittle_bar.setObjectName(u"tittle_bar")
        self.tittle_bar.setStyleSheet(u"QLabel{\n"
"	color:#6fd2e5;\n"
"}")
        self.tittle_bar.setFrameShape(QFrame.StyledPanel)
        self.tittle_bar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.tittle_bar)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(-1, 0, -1, 0)
        self.label_6 = QLabel(self.tittle_bar)
        self.label_6.setObjectName(u"label_6")
        font = QFont()
        font.setFamilies([u"Open Sans Semibold"])
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_6)


        self.horizontalLayout_5.addWidget(self.tittle_bar)


        self.horizontalLayout_2.addWidget(self.tittle_bar_container)

        self.top_right_btns = QFrame(self.main_header)
        self.top_right_btns.setObjectName(u"top_right_btns")
        self.top_right_btns.setMaximumSize(QSize(100, 16777215))
        self.top_right_btns.setStyleSheet(u"QPushButton{\n"
"background-color:#6fd2e5;\n"
"	border-radius: 5px;\n"
"}\n"
"")
        self.top_right_btns.setFrameShape(QFrame.StyledPanel)
        self.top_right_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.top_right_btns)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.minimizeButton = QPushButton(self.top_right_btns)
        self.minimizeButton.setObjectName(u"minimizeButton")
        self.minimizeButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/icons/cil-minus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minimizeButton.setIcon(icon)
        self.minimizeButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.minimizeButton)

        self.restoreButton = QPushButton(self.top_right_btns)
        self.restoreButton.setObjectName(u"restoreButton")
        self.restoreButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/cil-window-maximize.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.restoreButton.setIcon(icon1)
        self.restoreButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.restoreButton)

        self.closeButton = QPushButton(self.top_right_btns)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/cil-x.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.closeButton.setIcon(icon2)
        self.closeButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.closeButton)


        self.horizontalLayout_2.addWidget(self.top_right_btns)


        self.verticalLayout.addWidget(self.main_header)

        self.main_body = QFrame(self.centralwidget)
        self.main_body.setObjectName(u"main_body")
        self.main_body.setStyleSheet(u"")
        self.main_body.setFrameShape(QFrame.StyledPanel)
        self.main_body.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.main_body)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.center_main_items = QFrame(self.main_body)
        self.center_main_items.setObjectName(u"center_main_items")
        self.center_main_items.setStyleSheet(u"")
        self.center_main_items.setFrameShape(QFrame.StyledPanel)
        self.center_main_items.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.center_main_items)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.center_main_items)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.welcome_page = QWidget()
        self.welcome_page.setObjectName(u"welcome_page")
        self.verticalLayout_16 = QVBoxLayout(self.welcome_page)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.frame_7 = QFrame(self.welcome_page)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_7)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_11 = QLabel(self.frame_7)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(800, 400))
        self.label_11.setStyleSheet(u"QLabel{\n"
"font-weight:bold;\n"
"font-size:100px;\n"
"color:#a970c8;\n"
"}\n"
"QLabel:hover{\n"
"color:#6fd2e5;\n"
"}")
        self.label_11.setScaledContents(True)

        self.verticalLayout_17.addWidget(self.label_11)


        self.verticalLayout_16.addWidget(self.frame_7)

        self.stackedWidget.addWidget(self.welcome_page)
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.home_page.setStyleSheet(u"")
        self.verticalLayout_7 = QVBoxLayout(self.home_page)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_2 = QFrame(self.home_page)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_2)
        self.verticalLayout_11.setSpacing(50)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"QLabel{\n"
"font-weight:bold;\n"
"font-size:50px;\n"
"color:#6fd2e5;\n"
"}\n"
"QLabel:hover{\n"
"color:#a970c8;\n"
"}")

        self.verticalLayout_11.addWidget(self.label, 0, Qt.AlignHCenter)

        self.label_8 = QLabel(self.frame_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(0, 0))
        self.label_8.setMaximumSize(QSize(500, 16777215))
        self.label_8.setStyleSheet(u"QLabel{\n"
"font-size:25px;\n"
"color:#a970c8;\n"
"}\n"
"QLabel:hover{\n"
"font-size:30x;\n"
"color:#6fd2e5;\n"
"}")

        self.verticalLayout_11.addWidget(self.label_8, 0, Qt.AlignHCenter)


        self.verticalLayout_7.addWidget(self.frame_2)

        self.frame = QFrame(self.home_page)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame)
        self.horizontalLayout_6.setSpacing(50)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.customer_chatbot_btn = QPushButton(self.frame)
        self.customer_chatbot_btn.setObjectName(u"customer_chatbot_btn")
        self.customer_chatbot_btn.setMinimumSize(QSize(0, 50))
        self.customer_chatbot_btn.setMaximumSize(QSize(300, 16777215))
        self.customer_chatbot_btn.setStyleSheet(u".QPushButton {\n"
"border: 2px  solid #6fd2e5;\n"
"border-radius:10px;\n"
"color: #a970c8;\n"
"font-size: 20px;\n"
"background-color: #6fd2e5;\n"
"}\n"
".QPushButton:hover {\n"
"	font-size: 22px;\n"
"	color: #6fd2e5;\n"
"	background-color: #a970c8 ;\n"
"}")

        self.horizontalLayout_6.addWidget(self.customer_chatbot_btn)


        self.verticalLayout_7.addWidget(self.frame, 0, Qt.AlignBottom)

        self.stackedWidget.addWidget(self.home_page)
        self.customer_chatbot_page = QWidget()
        self.customer_chatbot_page.setObjectName(u"customer_chatbot_page")
        self.verticalLayout_12 = QVBoxLayout(self.customer_chatbot_page)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_3 = QFrame(self.customer_chatbot_page)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_3)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.start_chatting_text = QLabel(self.frame_3)
        self.start_chatting_text.setObjectName(u"start_chatting_text")
        self.start_chatting_text.setStyleSheet(u"Qlabel{\n"
"	font-size:15px;\n"
"    color:#a970c8;\n"
"}\n"
"QLabel:hover{\n"
"font-size:20px;\n"
"color:#6fd2e5;\n"
"}\n"
"")

        self.verticalLayout_13.addWidget(self.start_chatting_text)

        self.chat_frame = QFrame(self.frame_3)
        self.chat_frame.setObjectName(u"chat_frame")
        self.chat_frame.setFrameShape(QFrame.StyledPanel)
        self.chat_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.chat_frame)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.chat_layout = QVBoxLayout()
        self.chat_layout.setObjectName(u"chat_layout")

        self.verticalLayout_18.addLayout(self.chat_layout)


        self.verticalLayout_13.addWidget(self.chat_frame)


        self.verticalLayout_12.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.customer_chatbot_page)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 50))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, 0, -1, 0)
        self.user_input_to_chatbot = QLineEdit(self.frame_4)
        self.user_input_to_chatbot.setObjectName(u"user_input_to_chatbot")
        self.user_input_to_chatbot.setMinimumSize(QSize(0, 45))
        self.user_input_to_chatbot.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(228, 232, 255);\n"
"	border-radius: 10px;\n"
"	border: 2px solid #a970c8;\n"
"	font-size:18px;\n"
"	padding-left: 10px;\n"
"	selection-color: #fff;\n"
"	selection-background-color: #6fd2e5;\n"
"    color: #6fd2e5;\n"
"}\n"
"")

        self.horizontalLayout_7.addWidget(self.user_input_to_chatbot)

        self.send_message_btn = QPushButton(self.frame_4)
        self.send_message_btn.setObjectName(u"send_message_btn")
        self.send_message_btn.setMinimumSize(QSize(50, 30))
        self.send_message_btn.setStyleSheet(u".QPushButton{\n"
"border: 2px  solid #6fd2e5;\n"
"border-radius:5px;\n"
"color: rgb(235, 237, 255);\n"
"font-size: 20px;\n"
"background-color:#6fd2e5;\n"
"}\n"
".QPushButton:hover {\n"
"	font-size: 22px;\n"
"	color: #6fd2e5;\n"
"	background-color: #a970c8 ;\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/cil-paper-plane.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.send_message_btn.setIcon(icon3)
        self.send_message_btn.setIconSize(QSize(50, 40))

        self.horizontalLayout_7.addWidget(self.send_message_btn)


        self.verticalLayout_12.addWidget(self.frame_4)

        self.stackedWidget.addWidget(self.customer_chatbot_page)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.center_main_items)


        self.verticalLayout.addWidget(self.main_body)

        self.main_footer = QFrame(self.centralwidget)
        self.main_footer.setObjectName(u"main_footer")
        self.main_footer.setMinimumSize(QSize(0, 30))
        self.main_footer.setMaximumSize(QSize(16777215, 30))
        self.main_footer.setStyleSheet(u"QFrame{\n"
"	background-color: #a970c8;\n"
"	border-top-color: solid 1px  rgb(0, 0, 0);\n"
"}\n"
"QLabel{\n"
"	color: #fff;\n"
"}")
        self.main_footer.setFrameShape(QFrame.WinPanel)
        self.main_footer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.main_footer)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(11, 0, 0, 0)
        self.label_7 = QLabel(self.main_footer)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"color:gray;")

        self.verticalLayout_10.addWidget(self.label_7)


        self.verticalLayout.addWidget(self.main_footer, 0, Qt.AlignTop)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Chat GUI", None))
        self.minimizeButton.setText("")
        self.restoreButton.setText("")
        self.closeButton.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Chat GUI</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Our Chat", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Chat Gui built with pyside6</span></p></body></html>", None))
        self.customer_chatbot_btn.setText(QCoreApplication.translate("MainWindow", u"Ask", None))
        self.start_chatting_text.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Now, You can ask what ever you want!</span></p></body></html>", None))
        self.user_input_to_chatbot.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type a message", None))
        self.send_message_btn.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Copyright", None))
    # retranslateUi

