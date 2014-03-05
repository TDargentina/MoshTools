def shaderExporter():

    import maya.cmds as cmds
    import maya.mel as mel
    import os
    import json
    
    project=cmds.workspace(q=True, rd=True)
    
    objSelected=cmds.ls(dag=1,o=1,s=1,sl=1)
    dict1={}
    materialDict=[]
    shaderPath="%s/%s" %(project,"shaders")
    
    for obj in objSelected:
        
        #print obj
        #cmds.select(obj)
        #print obj
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
        
            #print objName[0]
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
    
    dict1.update({"materialPath":materialDict})
    dict1.update({"shaderPath":shaderPath})          
    with open('%s/data.json'%(shaderPath), 'wb') as fp:
        json.dump(dict1, fp)
        materialDict.append('%s/data.json'%(shaderPath))
        print materialDict
        
    #print dict1
        
shaderExporter()

def xformNameToAttrib():
    import maya.cmds as cmds

    slXform=cmds.ls(sl=True)
    
    for obj in slXform:
        
        cmds.select(obj)
        cmds.addAttr( longName="xformName", dt='string')
        cmds.setAttr( '%s.xformName'%(obj), obj ,type="string")
        
        
xformNameToAttrib()
