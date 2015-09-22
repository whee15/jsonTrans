import maya.cmds as cmds
import json
import os


class jsonTrans:

    def __init__(self,filename):

        self.object = {}
        self.filename = filename
        self.transformAttrList = ('translate','rotate','scale')


    def PathSet(self):

        self.devPath = '/dexter/Cache_DATA/MDL/member/whee/Scripts/dev/'


    def ExportTransform(self):

        for selobj in cmds.ls(sl = 1):

            transform = {}

            for Tr in self.transformAttrList:
                transform[Tr] = cmds.getAttr('%s.%s'%(selobj,Tr))[0]

            self.object[selobj] = transform

            self.FileIO(filename,'export')


    def ImportTransforms(self):

        for toObj in cmds.ls(sl = 1):

            for Tra in self.transformAttrList:

                cmds.setAttr('%s.%s'%(toObj,Tra),*transfromJ[toObj][Tra])

            self.FileIO(filename,'import')


    def FileIO(self,filename,flag):

        if flag == 'export':

            with open(self.devPath + filename + '.json','w') as exportjson:
                exportjson.write(json.dumps(self.object,indent=4))
                exportjson.close()

        if flag == 'import':

            with open(self.devPath + filename + '.json','r') as importjson:
                transfromJ = json.load(importjson)
                importjson.close()
