def getMayaSceneFolder():
	
	import maya.cmds as cmds
	
	filePath=cmds.file(loc=True,q=True)
	
	shaderPath=filePath.split("/scenes")
	
	shaderPath=shaderPath[0]+"/shaders"
	
	return shaderPath


def listSelection():
    import maya.cmds as cmds
    import maya.mel as mel
    
    listSel=cmds.ls(sl=True)
    
    print listSel
    

def saveAtrributes():
    
    import maya.cmds as cmds
    import maya.mel as mel
    
    dict1={}
    objSelected=cmds.ls(sl=True)

    for obj in objSelected:
        shdGroup=cmds.listConnections(obj,type='shadingEngine')
        if shdGroup is None:
            pass
        else:
            shaderName=cmds.ls(cmds.listConnections(shdGroup),materials=1)           
                
            objName=cmds.listRelatives(obj, parent=True)
        
        # atributos a guardar, tambien se guarda el nombre del shader asignado a la geometria
            attrDict={"aiOpaque":cmds.getAttr('%s.aiOpaque'%(obj))
                    ,"aiSelfShadows":cmds.getAttr('%s.aiSelfShadows'%(obj))
                    ,"aiVisibleInDiffuse":cmds.getAttr('%s.aiVisibleInDiffuse'%(obj))
                    ,"aiVisibleInGlossy":cmds.getAttr('%s.aiVisibleInGlossy'%(obj))
                    ,"aiSubdivType":cmds.getAttr('%s.aiSubdivType'%(obj))
                    ,"aiSubdivIterations":cmds.getAttr('%s.aiSubdivIterations'%(obj))
                    ,"aiDispHeight":cmds.getAttr('%s.aiDispHeight'%(obj))
                    ,"aiDispPadding":cmds.getAttr('%s.aiDispPadding'%(obj))
                    ,"aiDispZeroValue":cmds.getAttr('%s.aiDispZeroValue'%(obj))
                    ,"aiDispAutobump":cmds.getAttr('%s.aiDispAutobump'%(obj))
                    ,"doubleSided":cmds.getAttr('%s.doubleSided'%(obj))
                    ,"shader":shaderName[0]                    
                        }
                        
            dict1.update({objName[0]:attrDict})
                        
            attrDict={}
            print attrDict


            
            #mel.eval("select -r -ne %s"%(shdGroup[0]))
        
        
            #if os.path.exists(shaderPath +"/"+shaderName[0]+".ma"):
                #print "ya existe el shader"                                
            #else:
                #cmds.file("%s/%s.ma" %(shaderPath,shaderName[0]), es=True, type="mayaAscii")
                #materialDict.append("%s/%s.ma" %(shaderPath,shaderName[0]))