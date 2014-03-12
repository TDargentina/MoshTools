import maya.cmds as cmds
import pymel.core as pm
import os
import json

def getShaderData():
    
    shaderPath="Y:/TRABAJOS/PECERA_MALVINAS/1_Shot_Related/_ASSETS_GENERALES/04_SHADING/2_EXPORTS/shaders/"
    listFiles=os.listdir(shaderPath)
    fileteredList=[]
    for list in listFiles:
        if "shd" in list:
            fileteredList.append(list)
            
    return fileteredList
    

def assignShaders(shadersName):
    
    shaderPath="Y:/TRABAJOS/PECERA_MALVINAS/1_Shot_Related/_ASSETS_GENERALES/04_SHADING/2_EXPORTS/shaders/"    
    #print shadersName
    
    objSelected=cmds.ls(sl=True)
    objFiltered=maya.cmds.listRelatives(objSelected, allDescendents=True, noIntermediate=True, fullPath=True, type="mesh")
    
    for obj in objFiltered:
        
        objName=cmds.listRelatives(obj, parent=True)
        #print objName
        obj= obj.rsplit('|', 1)
        obj=obj[0]
        #print obj[0]
        if '|' in obj[0]:
            obj=obj[1: ]
            attrName=cmds.getAttr("%s.objIdName"%(obj))
            #print attrName.split("_")[0]            
            for shader in shadersName:                
                
                if ".json" in shader and attrName.split("_")[0] in shader:
                    
                    json_data=open(shaderPath+shader).read()
                    jsonList = json.loads(json_data)
                    shaderName= jsonList[attrName]
                    cmds.select(obj)
                    shaderName=shaderName["shader"]
                    cmds.hyperShade(assign=shaderName)
    cmds.select(objSelected)
                    
def assignAttributes(shadersName):
    
    shaderPath="Y:/TRABAJOS/PECERA_MALVINAS/1_Shot_Related/_ASSETS_GENERALES/04_SHADING/2_EXPORTS/shaders/"    
    #print shadersName
    
    objSelected=cmds.ls(sl=True)
    objFiltered=maya.cmds.listRelatives(objSelected, allDescendents=True, noIntermediate=True, fullPath=True, type="mesh")
    
    for obj in objFiltered:
        
        objName=cmds.listRelatives(obj, parent=True)
        #print objName
        obj= obj.rsplit('|', 1)
        obj=obj[0]
        #print obj[0]
        if '|' in obj[0]:
            obj=obj[1: ]
            attrName=cmds.getAttr("%s.objIdName"%(obj))
            #print attrName.split("_")[0]            
            for shader in shadersName:                
                
                if ".json" in shader and attrName.split("_")[0] in shader:
                    
                    json_data=open(shaderPath+shader).read()
                    jsonList = json.loads(json_data)
                    shaderName= jsonList[attrName]
                    
                    for k,v in shaderName.iteritems():
                        
                        if not k =="shader":
                            #print k
                            cmds.setAttr('%s.%s'%(obj,k), v)

def shaderImporter():
    
    shaderPath="Y:/TRABAJOS/PECERA_MALVINAS/1_Shot_Related/_ASSETS_GENERALES/04_SHADING/2_EXPORTS/shaders/"
    listFiles=os.listdir(shaderPath)
    listaMa=[]
    checklist=[]
    jsonFilePath="Y:/TRABAJOS/PECERA_MALVINAS/1_Shot_Related/004/10/2_3D_Related/2_Assets_Toma/04_SCENE_COMPOSING/1_PROYECTOS/1_MAYA/data/shader.json"
    
    if not os.path.exists(jsonFilePath):        
        jsonList={"shaderName":[]}
        
    else:
        json_data=open(jsonFilePath).read()
        jsonList = json.loads(json_data)
        #print jsonList
    for list in listFiles:
        if "shd" in list and not ".json" in list:
            listaMa.append(list)
    #print listaMa
    objSelect=pm.ls( selection=True )
    for obj in objSelect:
        idName= obj.getAttr("objIdName")
        idName=idName.split("_")[0]
        for list in listaMa:
            if idName in list:
                #print obj + " tiene el shader " + list
                if not list in checklist:
                    checklist.append(list)
                    
    #print checklist
    
    
    
    for shader in checklist:
        
        if not shader in jsonList["shaderName"]:
            cmds.file(shaderPath + shader,i=True,type="mayaAscii")
            jsonList["shaderName"].append(shader)
            with open('%s'%(jsonFilePath), 'wb') as fp:
                json.dump(jsonList, fp)
                
        else:
            
            print "el shader existe en la escena"