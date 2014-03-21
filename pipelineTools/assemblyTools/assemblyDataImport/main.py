import sys
import os
from maya import OpenMayaUI as omui
from shiboken import wrapInstance
from PySide import QtCore, QtGui
from maya import OpenMayaUI as omui
import maya.cmds as cmds
import maya.mel as mel
import json

pathModule="C:/Users/fidel/Documents/GitHub/MoshTools/pipelineTools/"

if pathModule in sys.path:
    print "el modulo existe"
    
else:
    sys.path.append(pathModule)    

from assemblyTools.tools import tools

from assemblyTools.assemblyDataImport.modules import importerTool

reload(tools)
reload(importerTool)

def maya_main_window():
    maya_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(long(maya_window_ptr), QtGui.QMainWindow)


ui_file = "C:/Users/fidel/Documents/GitHub/MoshTools/pipelineTools/assemblyTools/assemblyDataImport/ui/assemblyDataImport.ui"

form_class, base_class = tools.loadUiType(ui_file)
 
 
class shaderExporter(base_class, form_class):
 
    def __init__(self, parent):
        '''A custom window with a demo set of ui widgets'''
        # init our ui using the MayaWindow as parent
        super(shaderExporter, self).__init__(parent)
        # uic adds a function to our class called setupUi, calling this creates
        # all the widgets from the .ui file
        self.setupUi(self)
        #assemblyDataExport_v002.listSelection()
        
        self.setConnections()
        
    def setConnections(self):
    	self.shaderImportBTN.clicked.connect(self.shaderImporter)
    	self.applyShaderBTN.clicked.connect(self.applyShader)
        self.applyAttrBTN.clicked.connect(self.applyAttr)
        
        
    def shaderImporter(self):
        
        importerTool.shaderImporter()
        
        print "funciona"
        
        
    def applyShader(self):
        
        importerTool.assignShaders(getShaderData())
                
        print "funciona"
        
        
    def applyAttr(self):
        
        importerTool.assignAttributes(getShaderData())      
        
        
        print "funciona"
        
        
anchor = maya_main_window()
for x in anchor.children():
    if isinstance(x, shaderExporter):
        x.close()
 
shaderExporter(anchor).show()