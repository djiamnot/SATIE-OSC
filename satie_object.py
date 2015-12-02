import bpy
import liblo
import os
from . import satie_synth as ss

synths = []

def instanceHandler():
    sObj = [obj.id for obj in synths]
    if len(bpy.context.selected_objects) is 1:
        currentObj = bpy.context.object
        if currentObj.select and currentObj.useSatie:
            if currentObj.satieID in sObj:
                pass
            else:
                print("acting on ", currentObj)
                synths.append(ss.SatieSynth(currentObj, currentObj.satieID, currentObj.satieSynth))
                print("current synths", synths)
        if not currentObj.useSatie and currentObj.satieID in sObj:
            print("contents of synths before remove {}".format(synths))
            print("removing {}".format(currentObj.satieID))
            o = [x for x in synths if x.id == currentObj.satieID]
            for i in o:
                i.deleteNode()
                synths.remove(i)
            print("contents of synths after remove {}".format(synths))

def instanceCb(scene):
    instanceHandler()
    [o.updateAED() for o in synths]
    

def cleanCallbackQueue():
    if instanceCb in bpy.app.handlers.scene_update_post:
        bpy.app.handlers.scene_update_post.remove(instanceCb)


class SatieObject(bpy.types.Operator):
    bl_idname = "mesh.satie_sound"
    bl_label = "SATIE sound source"
    bl_options = {"REGISTER", "UNDO"}
    fcount = 0

    def __init__(self):
        print("init in SatieObject")
    
    def execute(self, context):
        print("Satie synth interfece instantiated")
        if instanceCb not in bpy.app.handlers.scene_update_post:
            bpy.app.handlers.scene_update_post.append(instanceCb)
        else:
            bpy.app.handlers.scene_update_post.remove(instanceCb)
        # if exeCallback not in bpy.app.handlers.scene_update_post:
        #     bpy.app.handlers.scene_update_post.append(exeCallback)
        # else:
        #     bpy.app.handlers.scene_update_post.remove(exeCallback)
        return {'FINISHED'}

    def getSatieID(self):
        print(bpy.context.object.satieID)
