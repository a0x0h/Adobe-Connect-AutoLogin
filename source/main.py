# Adobe Connect Auto-Loginer
# Made by SirA-
# CopyRight (C) 2021


# import time
import sys

# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.utils import ChromeType
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from pynput.keyboard import Key, Controller
from PyQt5.QtCore import Qt, QEvent, QPoint, QPropertyAnimation, QParallelAnimationGroup, QSettings, QBasicTimer
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLineEdit, QLabel, QToolTip, QGraphicsDropShadowEffect
from PyQt5.QtGui import QColor, QPixmap, QFont
from PyQt5.QtTest import QTest

from Main_widget import Ui_Form
from Show_Password_Button import ShowPasswordButton
from Loading_Widget import LoadingWidget
from Link_Error_Widget import LinkErrorWidget
from QWindowButtons import QWindowCloseButton, QWindowMinimizeButton
from Place_Holder_Label import PlaceHolderLabel

# keyboard = Controller()

skyroom = [
	"https://www.skyroom.online",
	"https://skyroom.online",
	"http://www.skyroom.online",
	"http://skyroom.online",
	"skyroom.online"
]
zoom = [
	"https://www.zoom.us",
	"https://zoom.us",
	"http://www.zoom.us",
	"http://zoom.us",
	"zoom.us"
]
adobe_connect = [
	"AdobeConnect"
]

normal_line_edit_stylesheet = """QLineEdit {
	color: rgb(0, 0, 0);
	background-color: rgb(222, 222, 222);
	border: 2px solid;
	border-radius: 6px;
	border-color: rgba(0, 0, 0, 0);
	padding-left: 10px;
	padding-right: 10px;
}
QLineEdit:hover {
	background-color: rgb(200, 200, 200);
	border-color: rgb(116, 116, 116);
}
QLineEdit:focus {
	background-color: rgb(240, 240, 240);
	border-color: rgb(0, 170, 255);
}"""
unfilled_line_edit_stylesheet = """QLineEdit {
	color: rgb(0, 0, 0);
	background-color: rgb(222, 222, 222);
	border: 2px solid;
	border-radius: 6px;
	border-color: rgb(255, 0, 0);
	padding-left: 10px;
	padding-right: 10px;
}
QLineEdit:hover {
	background-color: rgb(200, 200, 200);
}
QLineEdit:focus {
	background-color: rgb(240, 240, 240);
}"""
password_line_edit_stylesheet = """QLineEdit {
	color: rgb(0, 0, 0);
	background-color: rgb(222, 222, 222);
	border: 2px solid;
	border-radius: 6px;
	border-color: rgba(0, 0, 0, 0);
	padding-left: 10px;
	padding-right: 30px;
	lineedit-password-mask-delay: 1000;
}
QLineEdit:hover {
	background-color: rgb(200, 200, 200);
	border-color: rgb(116, 116, 116);
}
QLineEdit:focus {
	background-color: rgb(240, 240, 240);
	border-color: rgb(0, 170, 255);
}"""
unfilled_password_line_edit_stylesheet = """QLineEdit {
	color: rgb(0, 0, 0);
	background-color: rgb(222, 222, 222);
	border: 2px solid;
	border-radius: 6px;
	border-color: rgb(255, 0, 0);
	padding-left: 10px;
	padding-right: 30px;
	lineedit-password-mask-delay: 1000;
}
QLineEdit:hover {
	background-color: rgb(200, 200, 200);
}
QLineEdit:focus {
	background-color: rgb(240, 240, 240);
}"""


class Form(QMainWindow, Ui_Form):
	def __init__(self):
		super().__init__()

		self.setupUi(self)

		self.init_ui()

	def init_ui(self):
		self.define_animations()
		QToolTip.setFont(QFont("Segoe UI", 9))
		self.link_line_edit.textChanged.connect(lambda: self.link_line_edit.setStyleSheet(normal_line_edit_stylesheet))
		self.link_line_edit.textChanged.connect(self.recognize_link)
		self.link_line_edit.setToolTip("Enter the meeting link")
		self.link_label.setAttribute(Qt.WA_TransparentForMouseEvents)
		self.username_line_edit.textChanged.connect(lambda: self.username_line_edit.setStyleSheet(normal_line_edit_stylesheet))
		self.username_line_edit.setToolTip("Enter username")
		self.username_label.setAttribute(Qt.WA_TransparentForMouseEvents)
		self.password_line_edit.textChanged.connect(lambda: self.password_line_edit.setStyleSheet(password_line_edit_stylesheet))
		self.password_line_edit.setToolTip("Enter password")
		self.password_label.setAttribute(Qt.WA_TransparentForMouseEvents)
		self.link_line_edit.installEventFilter(self)
		self.username_line_edit.installEventFilter(self)
		self.password_line_edit.installEventFilter(self)
		self.link_loading_widget = LoadingWidget(
			self,
			back_circle_color=QColor(67, 0, 202),
			front_arc_color=QColor(255, 255, 255))
		self.link_loading_widget.move(54, 206)
		self.link_loading_widget.setToolTip("Recognizing link...")
		self.link_loading_widget.hide()
		self.link_error_widget = LinkErrorWidget(self)
		self.link_error_widget.move(51, 206)
		self.link_error_widget.hide()
		self.skyroom_logo = QLabel("", self)
		self.skyroom_logo.setScaledContents(True)
		self.skyroom_logo.resize(30, 30)
		self.skyroom_logo.setPixmap(QPixmap(":/resources/resources/skyroom.png"))
		self.skyroom_logo.move(54, 206)
		self.skyroom_logo.setToolTip("Skyroom")
		self.skyroom_logo.hide()
		self.zoom_logo = QLabel("", self)
		self.zoom_logo.setScaledContents(True)
		self.zoom_logo.resize(30, 30)
		self.zoom_logo.setPixmap(QPixmap(":/resources/resources/zoom.png"))
		self.zoom_logo.move(54, 206)
		self.zoom_logo.setToolTip("Zoom")
		self.zoom_logo.hide()
		self.adobe_connect_logo = QLabel("", self)
		self.adobe_connect_logo.setScaledContents(True)
		self.adobe_connect_logo.resize(30, 30)
		self.adobe_connect_logo.setPixmap(QPixmap(":/resources/resources/AdobeConnect.png"))
		self.adobe_connect_logo.move(54, 206)
		self.adobe_connect_logo.setToolTip("Adobe Connect")
		self.adobe_connect_logo.hide()
		self.show_password_button = ShowPasswordButton(self, bg_color=QColor(0, 0, 0, 0))
		self.show_password_button.move(320, 322)
		self.show_password_button.setToolTip("Show password")
		self.show_password_button.visibilityChanged.connect(lambda: self.password_line_edit.setEchoMode(QLineEdit.Normal) if self.show_password_button.enabled else self.password_line_edit.setEchoMode(QLineEdit.Password))
		self.show_password_button.visibilityChanged.connect(lambda: self.show_password_button.setToolTip("Hide password") if self.show_password_button.enabled else self.show_password_button.setToolTip("Show password"))
		self.setWindowFlag(Qt.FramelessWindowHint)
		self.window_close_button = QWindowCloseButton(self)
		self.window_close_button.move(self.width() - self.window_close_button.width(), 0)
		self.window_close_button.setToolTip("Close")
		self.window_close_button.clicked.connect(self.close)
		self.window_minimize_button = QWindowMinimizeButton(
			self,
			bg_hover_color=QColor(48, 112, 156),
			bg_press_color=QColor(48, 152, 178))
		self.window_minimize_button.move(self.width() - self.window_close_button.width() - self.window_minimize_button.width(), 0)
		self.window_minimize_button.setToolTip("Minimize")
		self.window_minimize_button.clicked.connect(self.showMinimized)
		self.remember_check_box.setToolTip("Save entered info")
		self.log_in_button.setToolTip("Login")
		self.log_in_button.clicked.connect(self.login)
		self.loading_widget = LoadingWidget(
			self,
			back_circle_color=QColor(67, 0, 202),
			front_arc_color=QColor(255, 255, 255))
		self.loading_widget.move(185, 422)
		self.loading_widget.setToolTip("Loading")
		self.loading_widget.hide()

		self.settings = QSettings("Adobe-Connect-Auto-Login", "Adobe-Connect-Auto-Login")
		if self.settings.contains("username") and self.settings.contains("password"):
			self.username_line_edit.setText(self.settings.value("username"))
			self.password_line_edit.setText(self.settings.value("password"))
			self.username_label_anims.start()
			self.password_label_anims.start()
			self.remember_check_box.setChecked(True)
			self.seconds = 10
			self.log_in_button.setText(f"Login ({self.seconds})")
			self.timer = QBasicTimer()
			self.username_line_edit.textEdited.connect(self.timer.stop)
			self.username_line_edit.textEdited.connect(lambda: self.log_in_button.setText("Login"))
			self.password_line_edit.textEdited.connect(self.timer.stop)
			self.password_line_edit.textEdited.connect(lambda: self.log_in_button.setText("Login"))
			self.timer.start(1000, self)
		for child in self.findChildren(QWidget):
			if type(child) not in [QWindowCloseButton, QWindowMinimizeButton, ShowPasswordButton, PlaceHolderLabel]:
				shadow = QGraphicsDropShadowEffect()
				shadow.setBlurRadius(30)
				child.setGraphicsEffect(shadow)
		self.show()

	def timerEvent(self, timer_event):
		if self.seconds > 0:
			self.seconds -= 1
			self.log_in_button.setText(f"Login ({self.seconds})")
		elif self.seconds == 0:
			self.timer.stop()
			self.login()
		return super().timerEvent(timer_event)

	def recognize_link(self):
		for content in skyroom:
			if content in self.link_line_edit.text():
				self.link_loading_widget.hide()
				self.skyroom_logo.show()
				return "skyroom"
		for content in zoom:
			if content in self.link_line_edit.text():
				self.link_loading_widget.hide()
				self.zoom_logo.show()
				return "zoom"
		for content in adobe_connect:
			if content in self.link_line_edit.text():
				self.link_loading_widget.hide()
				self.adobe_connect_logo.show()
				return "adobe connect"
		self.link_error_widget.hide()
		self.skyroom_logo.hide()
		self.zoom_logo.hide()
		self.adobe_connect_logo.hide()
		self.link_loading_widget.show()
		return False

	def login(self):
		try:
			self.timer.stop()
		except AttributeError:
			pass
		if self.link_line_edit.text() == "":
			self.link_loading_widget.hide()
			self.link_line_edit.setStyleSheet(unfilled_line_edit_stylesheet)
			return
		if self.username_line_edit.text() == "":
			self.link_loading_widget.hide()
			self.username_line_edit.setStyleSheet(unfilled_line_edit_stylesheet)
			return
		if self.password_line_edit.text() == "":
			self.link_loading_widget.hide()
			self.password_line_edit.setStyleSheet(unfilled_password_line_edit_stylesheet)
			return
		if not self.recognize_link():
			self.link_loading_widget.hide()
			self.link_error_widget.show()
			self.link_line_edit.setStyleSheet(unfilled_line_edit_stylesheet)
			return
		self.log_in_button.setText("")
		self.loading_widget.show()
		QTest.qWait(2000)

		if self.remember_check_box.isChecked():
			self.settings.setValue("username", self.username_line_edit.text())
			self.settings.setValue("password", self.password_line_edit.text())
		elif not self.remember_check_box.isChecked():
			self.settings.clear()

	# userna = self.username_line_edit.text()
	# passwo = self.password_line_edit.text()
	# driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.GOOGLE).install())
	# driver.get("") # Removed link
	#
	# user = driver.find_element_by_name("login")
	# user.send_keys(userna)
	#
	# password = driver.find_element_by_name("password")
	# password.send_keys(passwo)
	# password.send_keys(Keys.RETURN)
	# time.sleep(3)
	# adobe = driver.find_element_by_xpath("//div[@class='open-in-app-button']")
	# adobe.click()
	#
	# time.sleep(2)
	#
	# keyboard.press(Key.left)
	# keyboard.release(Key.left)
	#
	# keyboard.press(Key.enter)
	# keyboard.release(Key.enter)

	def define_animations(self):
		self.username_label_anim = QPropertyAnimation(self.username_label, b"pos")
		self.username_label_anim.setDuration(150)
		self.username_label_anim.setStartValue(QPoint(62, 260))
		self.username_label_anim.setEndValue(QPoint(54, 248))

		self.username_label_anim_reverse = QPropertyAnimation(self.username_label, b"pos")
		self.username_label_anim_reverse.setDuration(150)
		self.username_label_anim_reverse.setStartValue(QPoint(54, 248))
		self.username_label_anim_reverse.setEndValue(QPoint(62, 260))

		self.username_label_font_anim = QPropertyAnimation(self.username_label, b"point_size")
		self.username_label_font_anim.setDuration(150)
		self.username_label_font_anim.setStartValue(9)
		self.username_label_font_anim.setEndValue(6)

		self.username_label_font_anim_reverse = QPropertyAnimation(self.username_label, b"point_size")
		self.username_label_font_anim_reverse.setDuration(150)
		self.username_label_font_anim_reverse.setStartValue(6)
		self.username_label_font_anim_reverse.setEndValue(9)

		self.password_label_anim = QPropertyAnimation(self.password_label, b"pos")
		self.password_label_anim.setDuration(150)
		self.password_label_anim.setStartValue(QPoint(62, 323))
		self.password_label_anim.setEndValue(QPoint(54, 310))

		self.password_label_anim_reverse = QPropertyAnimation(self.password_label, b"pos")
		self.password_label_anim_reverse.setDuration(150)
		self.password_label_anim_reverse.setStartValue(QPoint(54, 310))
		self.password_label_anim_reverse.setEndValue(QPoint(62, 323))

		self.password_label_font_anim = QPropertyAnimation(self.password_label, b"point_size")
		self.password_label_font_anim.setDuration(150)
		self.password_label_font_anim.setStartValue(9)
		self.password_label_font_anim.setEndValue(6)

		self.password_label_font_anim_reverse = QPropertyAnimation(self.password_label, b"point_size")
		self.password_label_font_anim_reverse.setDuration(150)
		self.password_label_font_anim_reverse.setStartValue(6)
		self.password_label_font_anim_reverse.setEndValue(9)

		self.link_label_anim = QPropertyAnimation(self.link_label, b"pos")
		self.link_label_anim.setDuration(150)
		self.link_label_anim.setStartValue(QPoint(62, 165))
		self.link_label_anim.setEndValue(QPoint(54, 152))

		self.link_label_anim_reverse = QPropertyAnimation(self.link_label, b"pos")
		self.link_label_anim_reverse.setDuration(150)
		self.link_label_anim_reverse.setStartValue(QPoint(54, 152))
		self.link_label_anim_reverse.setEndValue(QPoint(62, 165))

		self.link_label_font_anim = QPropertyAnimation(self.link_label, b"point_size")
		self.link_label_font_anim.setDuration(150)
		self.link_label_font_anim.setStartValue(9)
		self.link_label_font_anim.setEndValue(6)

		self.link_label_font_anim_reverse = QPropertyAnimation(self.link_label, b"point_size")
		self.link_label_font_anim_reverse.setDuration(150)
		self.link_label_font_anim_reverse.setStartValue(6)
		self.link_label_font_anim_reverse.setEndValue(9)

		self.username_label_anims = QParallelAnimationGroup()
		self.username_label_anims.addAnimation(self.username_label_anim)
		self.username_label_anims.addAnimation(self.username_label_font_anim)

		self.username_label_anims2 = QParallelAnimationGroup()
		self.username_label_anims2.addAnimation(self.username_label_anim_reverse)
		self.username_label_anims2.addAnimation(self.username_label_font_anim_reverse)

		self.password_label_anims = QParallelAnimationGroup()
		self.password_label_anims.addAnimation(self.password_label_anim)
		self.password_label_anims.addAnimation(self.password_label_font_anim)

		self.password_label_anims2 = QParallelAnimationGroup()
		self.password_label_anims2.addAnimation(self.password_label_anim_reverse)
		self.password_label_anims2.addAnimation(self.password_label_font_anim_reverse)

		self.link_label_anims = QParallelAnimationGroup()
		self.link_label_anims.addAnimation(self.link_label_anim)
		self.link_label_anims.addAnimation(self.link_label_font_anim)

		self.link_label_anims2 = QParallelAnimationGroup()
		self.link_label_anims2.addAnimation(self.link_label_anim_reverse)
		self.link_label_anims2.addAnimation(self.link_label_font_anim_reverse)

	def mousePressEvent(self, event):
		self.oldPos = event.globalPos()

	def mouseMoveEvent(self, event):
		try:
			delta = QPoint(event.globalPos() - self.oldPos)
			self.move(self.x() + delta.x(), self.y() + delta.y())
			self.oldPos = event.globalPos()
		except AttributeError:
			pass

	def eventFilter(self, source_object, event):
		if source_object == self.username_line_edit:
			if event.type() == QEvent.FocusIn and self.username_line_edit.text() == "":
				self.username_label_anims.start()
			elif event.type() == QEvent.FocusOut and self.username_line_edit.text() == "":
				self.username_label_anims2.start()
		if source_object == self.password_line_edit:
			if event.type() == QEvent.FocusIn and self.password_line_edit.text() == "":
				self.password_label_anims.start()
			elif event.type() == QEvent.FocusOut and self.password_line_edit.text() == "":
				self.password_label_anims2.start()
		if source_object == self.link_line_edit:
			if event.type() == QEvent.FocusIn and self.link_line_edit.text() == "":
				self.link_label_anims.start()
			elif event.type() == QEvent.FocusOut and self.link_line_edit.text() == "":
				self.link_label_anims2.start()
		return super().eventFilter(source_object, event)


app = QApplication(sys.argv)
form = Form()
sys.exit(app.exec_())
