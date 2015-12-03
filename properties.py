import bpy

from . import satie_object as so

class SatieProperties(bpy.types.Panel):
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "object"
    bl_label = "SATIE properties"
#    def draw(self, context) :
#        TheCol = self.layout.column(align = True)
#        TheCol.prop(context.scene, "make_satie_properties")
#        TheCol.operator("mesh.add_satie_properties", text = "SATIE properties")
#        TheCol.prop(self, "useSatie")
#        TheCol.prop(self, "satieID")
 
    def draw(self, context) :
        objs = context.selected_objects
        if len(objs) is not 1:
            self.layout.label('Select exactly ONE object')
        else:
            TheCol = self.layout.column(align = True)
            #TheCol.prop(context.scene, "make_satie_properties")
            #TheCol.operator("mesh.add_satie_properties", text = "SATIE properties")
            TheCol.prop(context.object, "useSatie")
            TheCol.prop(context.object, "satieID")
            TheCol.prop(context.object, "satieSynth")
            TheCol.prop(context.object, "satieGroup")
            TheCol.prop(context.object, "sendToSATIE")
            TheCol.prop(context.object, "state")
            TheCol.operator("satieinfo.button")

class OBJECT_OT_Button(bpy.types.Operator):
    bl_idname = "satieinfo.button"
    bl_label = "Info"
    bl_description = "Display some info"
    def execute(self, context):
        self.report({'INFO'}, "{}".format(context.object))
        return{'FINISHED'}


#bpy.utils.register_module(__name__)
