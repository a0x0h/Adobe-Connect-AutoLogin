import sys

from PyQt5.QtCore import Qt, pyqtSlot, pyqtProperty, QPropertyAnimation, QParallelAnimationGroup, QEasingCurve
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor, QPen, QBrush, QFont
from PyQt5.QtTest import QTest


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
		self.rounded_rect_animation = QPropertyAnimation(self, b"rounded_rect_width")
		self.rounded_rect_animation.setDuration(500)
		self.rounded_rect_animation.setEasingCurve(QEasingCurve.InOutExpo)
		self.hover_animations = QParallelAnimationGroup()
		self.hover_animations.addAnimation(self.width_animation)
		self.hover_animations.addAnimation(self.rounded_rect_animation)

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

	def enterEvent(self, event):
		self.hover_animations.stop()
		self.width_animation.setStartValue(self.width())
		self.width_animation.setEndValue(300)
		self.rounded_rect_animation.setStartValue(26)
		self.rounded_rect_animation.setEndValue(296)
		self.hover_animations.start()

	def leaveEvent(self, event):
		QTest.qWait(1000)
		self.width_animation.setStartValue(self.width())
		self.width_animation.setEndValue(30)
		self.rounded_rect_animation.setStartValue(296)
		self.rounded_rect_animation.setEndValue(26)
		self.hover_animations.start()

	def paintEvent(self, paint_event):
		painter = QPainter()
		painter.begin(self)
		painter.setRenderHint(QPainter.Antialiasing)
		painter.setPen(Qt.NoPen)
		painter.setBrush(Qt.green)
		# painter.drawRect(0, 0, self.width(), self.height())
		painter.setBrush(QBrush(QColor(255, 85, 0), Qt.SolidPattern))
		painter.drawEllipse(2, 2, 26, 26)
		painter.drawRoundedRect(2, 2, self._rounded_rect_width, 26, 14, 14)
		painter.setPen(QPen(QColor(0, 0, 0), 4, Qt.SolidLine))
		painter.setFont(QFont("Segoe UI", 15))
		painter.drawText(11, 23, "!")
		painter.setFont(QFont("Segoe UI", 9))
		painter.drawText(30, 20, "The link you entered is not supported.")
		painter.end()


class Form(QWidget):
	def __init__(self):
		super().__init__()
		self.init_ui()

	def init_ui(self):
		self.resize(400, 300)
		self.setWindowTitle("Test")
		widget = LinkErrorWidget(self)
		widget.move(20, 20)
		self.show()


# app = QApplication(sys.argv)
# form = Form()
# sys.exit(app.exec_())
