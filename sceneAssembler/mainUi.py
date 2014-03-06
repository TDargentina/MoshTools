from PySide import QtCore
from PySide import QtGui

import maya.OpenMayaUI as omui
import maya.cmds as cmds
from shiboken import wrapInstance

def maya_main_window():
    maya_window_ptr=  omui.MQtUtil.mainWindow()
    return wrapInstance(long(maya_window_ptr),QtGui.QWidget)
    
def customGeoId(QtGui.QDialog):
    def __init__(self,parent=maya_main_window()):
        super(customGeoId,self).__init__(parent)
        self.setWindowTitle("test")
        self.setWindowFlags(QtCore.Qt.Tool)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        
if __name__== "__main__":
    try:
        ui.close()
    except:
        pass
    ui=customGeoId()
    ui.show()
