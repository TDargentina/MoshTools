import sys
import os
from maya import OpenMayaUI as omui
from shiboken import wrapInstance
from PySide import QtCore, QtGui
from maya import OpenMayaUI as omui
import maya.cmds as cmds

pathModule="C:/Users/fidel/Documents/GitHub/MoshTools/pipelineTools/"

if pathModule in sys.path:
    print "el modulo existe"
    
else:
    sys.path.append(pathModule)    

from assemblyTools.tools import tools

from assemblyTools.assemblyDataExport.module import assemblyDataExport_v002

reload(tools)
reload(assemblyDataExport_v002)

def maya_main_window():
    maya_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(long(maya_window_ptr), QtGui.QMainWindow)


ui_file = "C:/Users/fidel/Documents/GitHub/MoshTools/pipelineTools/assemblyTools/assemblyDataExport/ui/assemblyDataExport.ui"

form_class, base_class = tools.loadUiType(ui_file)
 
 
class test(base_class, form_class):
 
    def __init__(self, parent):
        '''A custom window with a demo set of ui widgets'''
        # init our ui using the MayaWindow as parent
        super(test, self).__init__(parent)
        # uic adds a function to our class called setupUi, calling this creates
        # all the widgets from the .ui file
        self.setupUi(self)
        #assemblyDataExport_v002.listSelection()
        
        self.setConnections()
        
        self.pathOutput()
        
        
        
    def setConnections(self):
    	self.fileBtn.clicked.connect(self.selectOutput)
    	self.cancelBtn.clicked.connect(self.closeWindow)
        self.exportBtn.clicked.connect(self.processBtn)
    	
    def closeWindow(self):
		self.close()
		
    def processBtn(self):
		self.attributes=assemblyDataExport_v002.getAtrributes()
		self.materials=assemblyDataExport_v002.getMaterials()
		print self.attributes
       
    def selectOutput(self):
        
        #print "funciona"
        singleFilter="json (*.json)"
        mayaPath=assemblyDataExport_v002.getMayaSceneFolder()
        jsonFile=cmds.fileDialog2(dir=mayaPath+"/shaders",fileFilter=singleFilter, dialogStyle=2)
        #print jsonFIle
        self.outputLineEdit.setText(mayaPath+jsonFile[0])
        
    def pathOutput(self):
    	
    	mayaPath=assemblyDataExport_v002.getMayaSceneFolder()
    	self.outputLineEdit.setText(mayaPath + "/" + ".json")
        
        
anchor = maya_main_window()
for x in anchor.children():
    if isinstance(x, test):
        x.close()
 
test(anchor).show()
