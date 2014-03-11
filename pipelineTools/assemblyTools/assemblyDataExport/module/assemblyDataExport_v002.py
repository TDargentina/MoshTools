import maya.cmds as cmds
import maya.mel as mel


def getMayaSceneFolder():
	
	import maya.cmds as cmds
	
	filePath=cmds.file(loc=True,q=True)
	
	shaderPath=filePath.rsplit("/",1)
	
	#shaderPath=shaderPath[0]+"/shaders/"
	
	return shaderPath


def listSelection():
    import maya.cmds as cmds
    import maya.mel as mel
    
    listSel=cmds.ls(sl=True)
    
    print listSel
	

def getMaterials():
    dict1=[]
    objSelected=cmds.ls(dag=1,o=1,s=1,sl=1)
    
    for obj in objSelected:
        shdGroup=cmds.listConnections(obj,type='shadingEngine')
        if shdGroup is None:
            pass
        else:
			if not shdGroup[0] in dict1:			
				dict1.append(shdGroup[0])
    return dict1	
    

import maya.cmds as cmds

def getAtributes():   
    
    dict1={}
    objSelected=cmds.ls(dag=1,o=1,s=1,sl=1)
    
    for obj in objSelected:
        shdGroup=cmds.listConnections(obj,type='shadingEngine')
        if shdGroup is None:
            pass
            
        else:
            shaderName=cmds.ls(cmds.listConnections(shdGroup[0]),materials=1)
            #print shaderName[0]
            objName=cmds.listRelatives(obj, parent=True)
			objIdName=cmds.getAttr("%s.objIdName"%(objName))
            #print objName[0]
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
                        
            dict1.update({objIdName:attrDict})
            
    return dict1