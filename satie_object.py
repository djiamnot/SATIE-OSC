import bpy
import liblo
import os


def instanceHandler():
    if len(bpy.context.selected_objects) is 1:
        currentObj = bpy.context.object
        if currentObj.select:
            print("acting on ", currentObj)

def instanceCb(scene):
    instanceHandler()

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
