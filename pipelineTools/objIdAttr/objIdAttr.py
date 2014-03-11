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
        self.create_connections()
           
    def create_connections(self):
        self.process_Btn.clicked.connect(self.procesarPrefix)
        self.cancel_btn.clicked.connect(self.cerrarVentana)
        self.overWriteCheckBox.clicked.connect(self.testPrint)
        
    #def testPrint(self):
        #print self.overWriteCheckBox.checkState()
        
        
    def cerrarVentana(self):
        self.close()               
        
        
                   
    def procesarPrefix(self):
        
        prefix=self.lineEdit.text()
        selObj=cmds.ls(sl=True)
        attrName="objIdName"
        listarAtt=cmds.listAttr( ud=True)
        for obj in selObj:
            cmds.select(obj)
			if "|" in obj:
				obj=obj.split("|")
				obj=obj[-1]
            
            if not listarAtt:
			
                cmds.addAttr( longName="objIdName", dt='string')
                cmds.setAttr( '%s.objIdName'%(obj), prefix + "_"+ obj ,type="string")
            else:
                for lista in listarAtt: 

                    if attrName in lista and self.overWriteCheckBox.checkState() == QtCore.Qt.CheckState.Unchecked:
                        print "ya existe en %s el valor es %s"%(obj,cmds.getAttr("%s.%s"%(obj,attrName)))
        
                    elif attrName in lista and self.overWriteCheckBox.checkState() == QtCore.Qt.CheckState.Checked:
                        cmds.setAttr( '%s.objIdName'%(obj), prefix + "_"+ obj ,type="string")	
				
        self.close()
        
        
anchor = maya_main_window()
for x in anchor.children():
    if isinstance(x, test):
        x.close()
 
test(anchor).show()