from PyQt5.QtCore import Qt, pyqtSlot, pyqtProperty, QPropertyAnimation, QSequentialAnimationGroup, \
	QParallelAnimationGroup, QEasingCurve
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QColor, QPen, QBrush, QFont


class LinkErrorWidget(QWidget):
	def __init__(self, parent=None):
		if parent is not None:
			super().__init__(parent=parent)
		elif parent is None:
			super().__init__()
		self.resize(30, 30)
		self.setFixedHeight(30)
		self._width2 = 30
		self._rounded_rect_width = 26
		self.width_animation = QPropertyAnimation(self, b"width2")
		self.width_animation.setDuration(500)
		self.width_animation.setEasingCurve(QEasingCurve.InOutExpo)
		self.delay_animation1 = QPropertyAnimation(self, b"height")
		self.delay_animation2 = QPropertyAnimation(self, b"pos")
		self.rounded_rect_animation = QPropertyAnimation(self, b"rounded_rect_width")
		self.rounded_rect_animation.setDuration(500)
		self.rounded_rect_animation.setEasingCurve(QEasingCurve.InOutExpo)
		self.width_animations = QSequentialAnimationGroup()
		self.width_animations.addAnimation(self.delay_animation1)
		self.width_animations.addAnimation(self.width_animation)
		self.rounded_rect_animations = QSequentialAnimationGroup()
		self.rounded_rect_animations.addAnimation(self.delay_animation2)
		self.rounded_rect_animations.addAnimation(self.rounded_rect_animation)
		self.hover_animations = QParallelAnimationGroup()
		self.hover_animations.addAnimation(self.width_animations)
		self.hover_animations.addAnimation(self.rounded_rect_animations)
		self.left = False
		self.hover_animations.finished.connect(lambda: self.leaveEvent() if self.left else print())

	def enterEvent(self, event):
		if self.width() < 300:
			self.hover_animations.stop()
			self.delay_animation1.setDuration(0)
			self.delay_animation2.setDuration(0)
			self.width_animation.setStartValue(self.width())
			self.width_animation.setEndValue(300)
			self.rounded_rect_animation.setStartValue(self._rounded_rect_width)
			self.rounded_rect_animation.setEndValue(296)
			self.hover_animations.start()

	def leaveEvent(self, event=None):
		if self.width() == 300:
			self.hover_animations.stop()
			self.delay_animation1.setDuration(1000)
			self.delay_animation2.setDuration(1000)
			self.width_animation.setStartValue(self.width())
			self.width_animation.setEndValue(30)
			self.rounded_rect_animation.setStartValue(296)
			self.rounded_rect_animation.setEndValue(26)
			self.left = False
			self.hover_animations.start()
		else:
			self.left = True

	def paintEvent(self, paint_event):
		painter = QPainter()
		painter.begin(self)
		painter.setRenderHint(QPainter.Antialiasing)
		painter.setPen(Qt.NoPen)
		painter.setBrush(Qt.green)
		painter.setBrush(QBrush(QColor(255, 85, 0), Qt.SolidPattern))
		painter.drawEllipse(2, 2, 26, 26)
		painter.drawRoundedRect(2, 2, self._rounded_rect_width, 26, 14, 14)
		painter.setPen(QPen(QColor(0, 0, 0), 4, Qt.SolidLine))
		painter.setFont(QFont("Segoe UI", 15))
		painter.drawText(11, 23, "!")
		painter.setFont(QFont("Segoe UI", 9))
		painter.drawText(30, 20, "The link you entered is not supported.")
		painter.end()

	def get_rounded_rect_width(self):
		return self._rounded_rect_width

	@pyqtSlot(int)
	def set_rounded_rect_width(self, value):
		self._rounded_rect_width = value
		self.update()

	rounded_rect_width = pyqtProperty(int, get_rounded_rect_width, set_rounded_rect_width)

	def get_width2(self):
		return self._width2

	@pyqtSlot(int)
	def set_width2(self, value):
		self._width2 = value
		self.resize(self._width2, self.height())
		self.update()

	width2 = pyqtProperty(int, get_width2, set_width2)
