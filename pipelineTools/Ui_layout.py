from PySide import QtCore
from PySide import QtGui

import maya.OpenMayaUI as omui
from shiboken import wrapInstance

def maya_main_window():
    maya_window_ptr=  omui.MQtUtil.mainWindow()
    return wrapInstance(long(maya_window_ptr),QtGui.QWidget)
    
def hello_world():
    label=QtGui.QLabel("id attribute",parent=maya_main_window())
    label.setWindowFlags(QtCore.Qt.Window)
    label.show()
    
if __name__== "__main__":
    hello_world()
