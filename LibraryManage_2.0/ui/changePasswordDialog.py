# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'changePasswordDialog.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_changePasswordDialog(object):
    def setupUi(self, changePasswordDialog):
        changePasswordDialog.setObjectName("changePasswordDialog")
        changePasswordDialog.resize(300, 280)
        self.formLayout = QtWidgets.QFormLayout(changePasswordDialog)
        self.formLayout.setVerticalSpacing(10)
        self.formLayout.setObjectName("formLayout")
        self.studentIdLabel = QtWidgets.QLabel(changePasswordDialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.studentIdLabel.setFont(font)
        self.studentIdLabel.setObjectName("studentIdLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.studentIdLabel)
        self.studentIdEdit = QtWidgets.QLineEdit(changePasswordDialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.studentIdEdit.setFont(font)
        self.studentIdEdit.setMaxLength(12)
        self.studentIdEdit.setObjectName("studentIdEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.studentIdEdit)
        self.oldPasswordLabel = QtWidgets.QLabel(changePasswordDialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.oldPasswordLabel.setFont(font)
        self.oldPasswordLabel.setObjectName("oldPasswordLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.oldPasswordLabel)
        self.passwordLabel = QtWidgets.QLabel(changePasswordDialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.passwordLabel.setFont(font)
        self.passwordLabel.setObjectName("passwordLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.passwordLabel)
        self.confirmPasswordLabel = QtWidgets.QLabel(changePasswordDialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.confirmPasswordLabel.setFont(font)
        self.confirmPasswordLabel.setObjectName("confirmPasswordLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.confirmPasswordLabel)
        self.oldPasswordEdit = QtWidgets.QLineEdit(changePasswordDialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.oldPasswordEdit.setFont(font)
        self.oldPasswordEdit.setMaxLength(16)
        self.oldPasswordEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.oldPasswordEdit.setObjectName("oldPasswordEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.oldPasswordEdit)
        self.passwordEdit = QtWidgets.QLineEdit(changePasswordDialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.passwordEdit.setFont(font)
        self.passwordEdit.setMaxLength(16)
        self.passwordEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordEdit.setObjectName("passwordEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.passwordEdit)
        self.confirmPasswordEdit = QtWidgets.QLineEdit(changePasswordDialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.confirmPasswordEdit.setFont(font)
        self.confirmPasswordEdit.setMaxLength(16)
        self.confirmPasswordEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmPasswordEdit.setObjectName("confirmPasswordEdit")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.confirmPasswordEdit)
        self.titlelabel = QtWidgets.QLabel(changePasswordDialog)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.titlelabel.setFont(font)
        self.titlelabel.setObjectName("titlelabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.titlelabel)
        self.changePasswordButton = QtWidgets.QPushButton(changePasswordDialog)
        self.changePasswordButton.setMaximumSize(QtCore.QSize(120, 32))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.changePasswordButton.setFont(font)
        self.changePasswordButton.setObjectName("changePasswordButton")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.changePasswordButton)

        self.retranslateUi(changePasswordDialog)
        QtCore.QMetaObject.connectSlotsByName(changePasswordDialog)

    def retranslateUi(self, changePasswordDialog):
        _translate = QtCore.QCoreApplication.translate
        changePasswordDialog.setWindowTitle(_translate("changePasswordDialog", "修改密码"))
        self.studentIdLabel.setText(_translate("changePasswordDialog", "学    号："))
        self.oldPasswordLabel.setText(_translate("changePasswordDialog", "旧 密 码："))
        self.passwordLabel.setText(_translate("changePasswordDialog", "新 密 码："))
        self.confirmPasswordLabel.setText(_translate("changePasswordDialog", "确认密码："))
        self.titlelabel.setText(_translate("changePasswordDialog", "修改密码"))
        self.changePasswordButton.setText(_translate("changePasswordDialog", "确认修改"))


