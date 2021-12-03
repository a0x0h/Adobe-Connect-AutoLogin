# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main_widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from Place_Holder_Label import PlaceHolderLabel


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 600)
        Form.setMinimumSize(QtCore.QSize(400, 600))
        Form.setMaximumSize(QtCore.QSize(400, 600))
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        Form.setFont(font)
        Form.setStyleSheet("QWidget#Form {\n"
"    background-color: qlineargradient(spread:pad, x1:0.279, y1:0, x2:1, y2:0.914773, stop:0 rgba(50, 22, 107, 255), stop:1 rgba(47, 191, 199, 255));\n"
"}\n"
"QLabel {\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton {\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 116, 228);\n"
"    border: none;\n"
"    border-radius: 6px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(40, 138, 232);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(61, 149, 234);\n"
"}")
        self.welcome_label = QtWidgets.QLabel(Form)
        self.welcome_label.setGeometry(QtCore.QRect(137, 60, 127, 43))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.welcome_label.setFont(font)
        self.welcome_label.setAlignment(QtCore.Qt.AlignCenter)
        self.welcome_label.setObjectName("welcome_label")
        self.username_line_edit = QtWidgets.QLineEdit(Form)
        self.username_line_edit.setGeometry(QtCore.QRect(50, 245, 300, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.username_line_edit.setFont(font)
        self.username_line_edit.setStyleSheet("QLineEdit {\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(222, 222, 222);\n"
"    border: 2px solid;\n"
"    border-radius: 6px;\n"
"    border-color: rgba(0, 0, 0, 0);\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"    background-color: rgb(200, 200, 200);\n"
"    border-color: rgb(116, 116, 116);\n"
"}\n"
"QLineEdit:focus {\n"
"    background-color: rgb(240, 240, 240);\n"
"    border-color: rgb(0, 170, 255);\n"
"}")
        self.username_line_edit.setPlaceholderText("")
        self.username_line_edit.setObjectName("username_line_edit")
        self.password_line_edit = QtWidgets.QLineEdit(Form)
        self.password_line_edit.setGeometry(QtCore.QRect(50, 308, 300, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.password_line_edit.setFont(font)
        self.password_line_edit.setStyleSheet("QLineEdit {\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(222, 222, 222);\n"
"    border: 2px solid;\n"
"    border-radius: 6px;\n"
"    border-color: rgba(0, 0, 0, 0);\n"
"    padding-left: 10px;\n"
"    padding-right: 30px;\n"
"    lineedit-password-mask-delay: 1000;\n"
"}\n"
"QLineEdit:hover {\n"
"    background-color: rgb(200, 200, 200);\n"
"    border-color: rgb(116, 116, 116);\n"
"}\n"
"QLineEdit:focus {\n"
"    background-color: rgb(240, 240, 240);\n"
"    border-color: rgb(0, 170, 255);\n"
"}")
        self.password_line_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_line_edit.setObjectName("password_line_edit")
        self.password_label = PlaceHolderLabel(Form)
        self.password_label.setGeometry(QtCore.QRect(62, 323, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.password_label.setFont(font)
        self.password_label.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.password_label.setStyleSheet("color: rgb(120, 120, 120)")
        self.password_label.setAlignment(QtCore.Qt.AlignCenter)
        self.password_label.setObjectName("password_label")
        self.username_label = PlaceHolderLabel(Form)
        self.username_label.setGeometry(QtCore.QRect(62, 260, 66, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.username_label.setFont(font)
        self.username_label.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.username_label.setStyleSheet("color: rgb(120, 120, 120)")
        self.username_label.setAlignment(QtCore.Qt.AlignCenter)
        self.username_label.setObjectName("username_label")
        self.log_in_button = QtWidgets.QPushButton(Form)
        self.log_in_button.setGeometry(QtCore.QRect(132, 420, 137, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.log_in_button.setFont(font)
        self.log_in_button.setFlat(True)
        self.log_in_button.setObjectName("log_in_button")
        self.remember_check_box = QtWidgets.QCheckBox(Form)
        self.remember_check_box.setGeometry(QtCore.QRect(50, 372, 127, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.remember_check_box.setFont(font)
        self.remember_check_box.setStyleSheet("QCheckBox {\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"    border-image: url(:/resources/resources/checkbox_unchecked.png)\n"
"}\n"
"QCheckBox::indicator:unchecked:hover {\n"
"    border-image: url(:/resources/resources/checkbox_unchecked_hover.png);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    border-image: url(:/resources/resources/checkbox_checked.png);\n"
"}\n"
"QCheckBox::indicator:checked:hover {\n"
"    border-image: url(:/resources/resources/checkbox_checked_hover.png);\n"
"}")
        self.remember_check_box.setObjectName("remember_check_box")
        self.link_line_edit = QtWidgets.QLineEdit(Form)
        self.link_line_edit.setGeometry(QtCore.QRect(50, 150, 300, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.link_line_edit.setFont(font)
        self.link_line_edit.setStyleSheet("QLineEdit {\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgb(222, 222, 222);\n"
"    border: 2px solid;\n"
"    border-radius: 6px;\n"
"    border-color: rgba(0, 0, 0, 0);\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"    background-color: rgb(200, 200, 200);\n"
"    border-color: rgb(116, 116, 116);\n"
"}\n"
"QLineEdit:focus {\n"
"    background-color: rgb(240, 240, 240);\n"
"    border-color: rgb(0, 170, 255);\n"
"}")
        self.link_line_edit.setPlaceholderText("")
        self.link_line_edit.setObjectName("link_line_edit")
        self.link_label = PlaceHolderLabel(Form)
        self.link_label.setGeometry(QtCore.QRect(62, 165, 26, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.link_label.setFont(font)
        self.link_label.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.link_label.setStyleSheet("color: rgb(120, 120, 120)")
        self.link_label.setAlignment(QtCore.Qt.AlignCenter)
        self.link_label.setObjectName("link_label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.link_line_edit, self.username_line_edit)
        Form.setTabOrder(self.username_line_edit, self.password_line_edit)
        Form.setTabOrder(self.password_line_edit, self.remember_check_box)
        Form.setTabOrder(self.remember_check_box, self.log_in_button)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.welcome_label.setText(_translate("Form", "Welcome!"))
        self.password_label.setText(_translate("Form", "Password"))
        self.username_label.setText(_translate("Form", "Username"))
        self.log_in_button.setText(_translate("Form", "Log in"))
        self.remember_check_box.setText(_translate("Form", "Remember me"))
        self.link_label.setText(_translate("Form", "Link"))
import Widget_Resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
