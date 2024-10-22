# -*- coding：utf-8 -*- #
# (C)LeonMMcoset 2021-2024.All rights reserved.
from PyQt5 import QtWidgets, uic, QtGui
from PyQt5.QtWidgets import QApplication, QStyleFactory, QMessageBox
import threading
import sys
import os

# 注意：ui界面文件是个对话框，那么MyApp就必须继承 QDialog
# 类似的，若ui界面文件是个MainWindow，那么MyApp就必须继承 QMainWindow
try:
    print('[System_UI]Loading "app" type with argument "-index"...')
    class MyApp(QtWidgets.QMainWindow):
        def __init__(self):
            super().__init__()
            uic.loadUi('_internal/ui/index.ui', self)

        def indexgotoinfo(self):
            print('[APP]Spawn window:"app.info"')
            # 后两项分别为按钮(以|隔开，共有7种按钮类型，见示例后)、默认按钮(省略则默认为第一个按钮)
            QMessageBox.information(self, "APP信息", "学校电脑信息显示器\n专为北京师大附中所使用\nLeonMMcoset编写\n--------------------------\n版本：11.45.14", QMessageBox.Yes,
                                            QMessageBox.Yes)

        def indexshutdown(self):
            os.system('shutdown -p')

    app = QApplication(sys.argv)
    myapp = MyApp()
    myapp.show()
    print('[APP]APP window load done,showing...')
    sys.exit(app.exec_())
except Exception as r:
    print('[APP]Unknown error:' % (r))