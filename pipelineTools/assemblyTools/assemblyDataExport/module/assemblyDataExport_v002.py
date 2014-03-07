def listSelection():
    import maya.cmds as cmds
    import maya.mel as mel
    
    listSel=cmds.ls(sl=True)
    
    return listSel
    

def saveAtrributes(objSelected):
    
    import maya.cmds as cmds
    import maya.mel as mel

    for obj in objSelected:
        shdGroup=cmds.listConnections(obj,type='shadingEngine')
        if shdGroup is None:
            pass
        else:
            shaderName=cmds.ls(cmds.listConnections(shdGroup),materials=1)           
                
            objName=cmds.listRelatives(obj, parent=True)
        
        # atributos a guardar, tambien se guarda el nombre del shader asignado a la geometria
            dict2={"aiOpaque":cmds.getAttr('%s.aiOpaque'%(obj))
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
                        
            dict1.update({objName[0]:dict2})            
            dict2={}
            mel.eval("select -r -ne %s"%(shdGroup[0]))
            
            dict2={}
            #break
            #print objName
            #cmds.hyperShade(smn=True)
            
            #Elegir solo shading group
            mel.eval("select -r -ne %s"%(shdGroup[0]))
        
        
            if os.path.exists(shaderPath +"/"+shaderName[0]+".ma"):
                print "ya existe el shader"                                
            else:
                cmds.file("%s/%s.ma" %(shaderPath,shaderName[0]), es=True, type="mayaAscii")
                materialDict.append("%s/%s.ma" %(shaderPath,shaderName[0]))
    
    