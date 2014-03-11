import pymel.core as pm
import os
import json

def getData():
    
    shaderPath="Y:/TRABAJOS/PECERA_MALVINAS/1_Shot_Related/_ASSETS_GENERALES/04_SHADING/2_EXPORTS/shaders/"
    listFiles=os.listdir(shaderPath)
    fileteredList=[]
    for list in listFiles:
        if "shd" in list:
            fileteredList.append(list)
            
    return fileteredList
    

def assignShaders(shadersName):
    
    objSelected=pm.ls(sl=True)
    for obj in objSelected:
        
        
        
    #shaderPath="Y:/TRABAJOS/PECERA_MALVINAS/1_Shot_Related/_ASSETS_GENERALES/04_SHADING/2_EXPORTS/shaders/"
    #json_data=open(jsonFilePath).read()
    #jsonList = json.loads(json_data)
    
       
    


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
            