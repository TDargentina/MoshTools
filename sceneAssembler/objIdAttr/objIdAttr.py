import os
from StringIO import StringIO
from xml.etree import ElementTree as xml
 
import pysideuic
from shiboken import wrapInstance
from PySide import QtCore, QtGui
 
from maya import cmds
from maya import OpenMayaUI as omui
 
 
def loadUiType(uiFile):
        """
       Pyside lacks the "loadUiType" command, so we have to convert the ui file to py code in-memory first
       and then execute it in a special frame to retrieve the form_class.
       """
        parsed = xml.parse(uiFile)
        widget_class = parsed.find('widget').get('class')
        form_class = parsed.find('class').text
        with open(uiFile, 'r') as f:
            o = StringIO()
            frame = {}
            pysideuic.compileUi(f, o, indent=0)
            pyc = compile(o.getvalue(), '<string>', 'exec')
            exec pyc in frame
            # Fetch the base_class and form class based on their type in the
            # xml from designer
            form_class = frame['Ui_%s' % form_class]
            base_class = eval('QtGui.%s' % widget_class)
        return form_class, base_class
 
 
def maya_main_window():
    maya_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(long(maya_window_ptr), QtGui.QMainWindow)
 
 
uifile = "D:/NAS/17_GDRIVE/MOSH/DESARROLLO/gitHub/MoshTools/sceneAssembler/ui/customGeoUiDiag.ui"

form_class, base_class = loadUiType(uifile)
 
 
class test(base_class, form_class):
 
    def __init__(self, parent):
        '''A custom window with a demo set of ui widgets'''
        # init our ui using the MayaWindow as parent
        super(test, self).__init__(parent)
        # uic adds a function to our class called setupUi, calling this creates
        # all the widgets from the .ui file
        self.setupUi(self)
        #self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        #self.setObjectName('myWindow')
        #self.setWindowTitle("My Qt Demo Window")
        self.create_connections()
           
    def create_connections(self):
        self.process_Btn.clicked.connect(self.processPrefix)
        
                   
    def processPrefix(self):
        
        prefix=self.lineEdit.text()
        selObj=cmds.ls(sl=True)
        for obj in selObj:
            cmds.select(obj)
            cmds.addAttr( longName="objIdName", dt='string')
            cmds.setAttr( '%s.objIdName'%(obj), prefix + "_"+ obj ,type="string")
 
 
anchor = maya_main_window()
for x in anchor.children():
    if isinstance(x, test):
        x.close()
 
test(anchor).show()