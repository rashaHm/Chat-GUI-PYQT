# Chat Compenet app
# Developed by Rasha

import sys
import os
import platform
from pathlib import Path
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import (QCoreApplication,QTimer, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide6.QtGui import (QBrush,QMovie, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide6.QtWidgets import *
from chat_gui_main_window import *

# Global value for the windows status
WINDOW_SIZE = 0;
# This will help us determine if the window is minimized or maximized

# Main class
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Remove window tlttle bar
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint) 

        # Set main background to transparent
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
      
        # Apply shadow effect
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 92, 157, 150))
        # Appy shadow to central widget
        self.ui.centralwidget.setGraphicsEffect(self.shadow)

        # Button click events to our top bar buttons
        # 
        #Minimize window
        self.ui.minimizeButton.clicked.connect(lambda: self.showMinimized())
        self.ui.customer_chatbot_btn.clicked.connect(lambda: self.showCustomerChatbotPage())
        self.ui.send_message_btn.clicked.connect(lambda: self.sendMeassageToChatbot())
        self.ui.user_input_to_chatbot.returnPressed.connect(self.sendMeassageToChatbot)
        
        
        #Close window
        self.ui.closeButton.clicked.connect(lambda: self.close())
        #Restore/Maximize window
        self.ui.restoreButton.clicked.connect(lambda: self.restore_or_maximize_window())
        # ###############################################

        def moveWindow(e):
            # Detect if the window is  normal size
            # ###############################################  
            if self.isMaximized() == False: #Not maximized
                # Move window only when window is normal size  
                # ###############################################
                #if left mouse button is clicked (Only accept left mouse button clicks)
                if e.buttons() == Qt.LeftButton:  
                    #Move window 
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()
            # ###############################################

        
        # ###############################################
        # Add click event/Mouse move event/drag event to the top header to move the window
        # ###############################################
        self.ui.main_header.mouseMoveEvent = moveWindow
        # ###############################################

        # STACKED PAGES (DEFAUT /CURRENT PAGE)/////////////////
        #Set the page that will be visible by default when the app is opened 
        self.ui.stackedWidget.setCurrentWidget(self.ui.welcome_page)
        QTimer.singleShot(1000, lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.home_page))
        
        # ###############################################
        # //////////////////////////////////////
        # ############################################
        # Show window
        self.show()
        # ###############################################

    # ###############################################
    # Add mouse events to the window
    # ###############################################
    def mousePressEvent(self, event):
        # ###############################################
        # Get the current position of the mouse
        self.clickPosition = event.globalPos()
        # We will use this value to move the window
        # ###############################################
    # ###############################################

    def userInfo(self):
        self.ui.emailer_progressbar.hide()
        self.ui.emailer_progressbar.setValue(5)
        self.ui.stackedWidget.setCurrentWidget(self.ui.emailer_page)
 
    def showCustomerChatbotPage(self):
        try:
            self.ui.chat_frame.hide()
            self.ui.start_chatting_text.show()
            self.ui.send_message_btn.setEnabled(True)
            self.ui.user_input_to_chatbot.setEnabled(True)
            for i in reversed(range(self.ui.chat_layout.count())):
                self.ui.chat_layout.itemAt(i).widget().setParent(None)
            self.scroll_area = QScrollArea(self)
            self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)    
            self.content_widget = QWidget(self.scroll_area)
            self.layout = QVBoxLayout(self.content_widget)
            self.layout.addStretch()
            self.scroll_area.setWidget(self.content_widget)
            self.scroll_area.setWidgetResizable(True)
            self.ui.chat_layout.addWidget(self.scroll_area)
            self.ui.stackedWidget.setCurrentWidget(self.ui.customer_chatbot_page)
        except Exception as e:
            print(e)

    def sendMeassageToChatbot(self):
        try:
            self.ui.send_message_btn.setEnabled(False)
            self.ui.user_input_to_chatbot.setEnabled(False)
            if(self.ui.chat_frame.isHidden()):
                self.ui.start_chatting_text.hide()
                self.ui.chat_frame.show()
            user_message = self.ui.user_input_to_chatbot.text()
            
            if user_message != "":
                
                question = QLabel(user_message)
                question.setWordWrap(True)
                question.setMaximumWidth(self.ui.chat_frame.width() * 3 / 4)
                question.setStyleSheet("""
                        QLabel { 
                                    font-size: 18px; 
                                    color: #fff; 
                                    background-color:#6fd2e5;
                                    padding: 5px; 
                                    border-radius: 10px;
                                    border: 2px solid #6fd2e5;
                                    }
                    """)
                
                
                
                self.layout.addWidget(question,alignment=Qt.AlignLeft)
                self.scroll_area.verticalScrollBar().setValue(self.scroll_area.verticalScrollBar().maximum())
                self.ui.user_input_to_chatbot.setText("")
                
                ### Waiting Message
                wait_message = QLabel(self)
                wait_message.setStyleSheet("""
                        QLabel { 
                                    font-size: 18px; 
                                    color: #fff; 
                                    background-color: #a970c8;
                                    padding: 5px; 
                                    border-radius: 10px;
                                    border: 2px solid #a970c8;
                                    }
                    """)
                movie = QMovie('load.gif')
                wait_message.setMovie(movie)
                movie.start()
            #    self.layout.insertWidget(1,wait_message,alignment=Qt.AlignRight)
                self.layout.addWidget(wait_message,alignment=Qt.AlignRight)
                self.scroll_area.verticalScrollBar().setValue(self.scroll_area.verticalScrollBar().maximum())
               

                # Bot Answer
                bot_answer = QLabel("Bot Answer")
                bot_answer.setMaximumWidth(self.ui.chat_frame.width() * 3 / 4)
                bot_answer.setWordWrap(True)
                bot_answer.setStyleSheet("""
                        QLabel { 
                                    font-size: 18px; 
                                    color: #fff; 
                                    background-color: #a970c8;
                                    padding: 5px; 
                                    border-radius: 10px;
                                    border: 2px solid #a970c8;
                                    }
                    """)
                QTimer.singleShot(1000, lambda: wait_message.deleteLater())
                QTimer.singleShot(1000, lambda: self.layout.addWidget(bot_answer,alignment=Qt.AlignRight))
             #   QTimer.singleShot(1000, lambda: self.layout.insertWidget(1,bot_answer,alignment=Qt.AlignRight))
                QTimer.singleShot(1000,lambda:self.scroll_area.verticalScrollBar().setValue(self.scroll_area.verticalScrollBar().maximum()))
                self.ui.send_message_btn.setEnabled(True)
                self.ui.user_input_to_chatbot.setEnabled(True)
                
        except Exception as e:
            self.ui.send_message_btn.setEnabled(True)
            self.ui.user_input_to_chatbot.setEnabled(True)
            print(e)
            pass
         
    # Restore or maximize your window
    def restore_or_maximize_window(self):
        # Global windows state
        global WINDOW_SIZE #The default value is zero to show that the size is not maximized
        win_status = WINDOW_SIZE

        if win_status == 0:
        	# If the window is not maximized
        	WINDOW_SIZE = 1 #Update value to show that the window has been maxmized
        	self.showMaximized()

        	# Update button icon  when window is maximized
        	self.ui.restoreButton.setIcon(QtGui.QIcon(u":/icons/icons/cil-window-restore.png"))#Show minized icon
        else:
        	# If the window is on its default size
            WINDOW_SIZE = 0 #Update value to show that the window has been minimized/set to normal size (which is 800 by 400)
            self.showNormal()

            # Update button icon when window is minimized
            self.ui.restoreButton.setIcon(QtGui.QIcon(u":/icons/icons/cil-window-maximize.png"))#Show maximize icon

  
# Execute app
if __name__ == "__main__":
   
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
   
else:
	print(__name__, "hh")


