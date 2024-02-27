# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RustScrapper.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(550, 300)
        Dialog.setMinimumSize(QtCore.QSize(550, 300))
        Dialog.setMaximumSize(QtCore.QSize(550, 300))
        Dialog.setStyleSheet("QDialog {\n"
"    color: white;\n"
"    width:  600px;\n"
"   height: 400px;\n"
"    background-image: url(\"design/main.png\");\n"
"    background-repeat: no-repeat;\n"
"}\n"
"\n"
"QPushButton {\n"
"    border-radius: 15px;\n"
"    background-color: green;\n"
"    border: 3px solid white;\n"
"}\n"
"\n"
"QRadioButton {\n"
"    color:                  white;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width:                  10px;\n"
"    height:                 10px;\n"
"    border-radius:          7px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:       red;\n"
"    border:                 2px solid white;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:       black;\n"
"    border:                 2px solid white;\n"
"}\n"
"\n"
"QLabel {\n"
"  color: white;\n"
"}")
        self.radioButton = QtWidgets.QRadioButton(Dialog)
        self.radioButton.setGeometry(QtCore.QRect(220, 40, 140, 23))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_2.setGeometry(QtCore.QRect(220, 70, 140, 23))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_3.setGeometry(QtCore.QRect(220, 100, 140, 23))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_4.setGeometry(QtCore.QRect(220, 130, 140, 23))
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_5 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_5.setGeometry(QtCore.QRect(370, 40, 150, 23))
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_6 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_6.setGeometry(QtCore.QRect(370, 70, 150, 23))
        self.radioButton_6.setObjectName("radioButton_6")
        self.radioButton_7 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_7.setGeometry(QtCore.QRect(370, 100, 150, 23))
        self.radioButton_7.setObjectName("radioButton_7")
        self.radioButton_8 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_8.setGeometry(QtCore.QRect(370, 130, 150, 23))
        self.radioButton_8.setObjectName("radioButton_8")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(30, 70, 121, 31))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 40, 151, 17))
        self.label.setObjectName("label")
        self.radioButton_9 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_9.setGeometry(QtCore.QRect(370, 160, 150, 23))
        self.radioButton_9.setObjectName("radioButton_9")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(390, 270, 141, 20))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.radioButton.setText(_translate("Dialog", "Compost to scrap"))
        self.radioButton_2.setText(_translate("Dialog", "Stone to tree"))
        self.radioButton_3.setText(_translate("Dialog", "Cloth to scrap"))
        self.radioButton_4.setText(_translate("Dialog", "MHQ to scrap"))
        self.radioButton_5.setText(_translate("Dialog", "Iron to scrap"))
        self.radioButton_6.setText(_translate("Dialog", "Corn to scrap"))
        self.radioButton_7.setText(_translate("Dialog", "Smoke granade"))
        self.radioButton_8.setText(_translate("Dialog", "Green card to scrap"))
        self.pushButton.setText(_translate("Dialog", "F2"))
        self.label.setText(_translate("Dialog", "Bind the hot key"))
        self.radioButton_9.setText(_translate("Dialog", "Fish to scrap"))
        self.label_2.setText(_translate("Dialog", "NASA PRODUCTION"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
