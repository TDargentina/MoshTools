import json
import maya.cmds as cmds

jsonPath="Y:/TRABAJOS/PECERA_MALVINAS/1_Shot_Related/_ASSETS_GENERALES/04_SHADING/1_PROYECTOS/ESPECIES/TONINAOVERA/shaders/data.json"

def selection():
   selObj=cmds.ls(sl=True)
   attrObj=[]
   for obj in selObj:
       attrObj.append(cmds.getAttr("%s.xformName"%(obj)))
       
   return attrObj
   
   

def importShaders(jsonFile):
    
    jsonFile=open(jsonFile)
    jsonFile=json.load(jsonFile)
    
    #import shaders    
    for shaders in jsonFile["materialPath"]:
        
        cmds.file(shaders,i=True,type="mayaAscii")
        
        #break
        
        #print shaders
        
def assignShaders(jsonFile,objName):
    
    jsonFile=open(jsonFile)
    jsonFile=json.load(jsonFile)
    for obj in objName:
        #print obj
        for k,v in jsonFile[obj].iteritems():
            if k=="shader":                
                cmds.select( '%s'%(obj))
                #slShader = cmds.shadingNode(v, asShader=True)
                #print obj
                #cmds.sets("%s"%(obj), edit=True, forceElement="%s"%(v)+"SG")
                cmds.hyperShade(assign=v)
                print v
            else:
                pass
            
def assignAttr(jsonFile,objName):
    
    jsonFile=open(jsonFile)
    jsonFile=json.load(jsonFile)
    for obj in objName:
        print obj
        for k,v in jsonFile[obj].iteritems():
            if k=="shader":
                pass
            else:
                cmds.setAttr("%s.%s"%(obj,k),v)