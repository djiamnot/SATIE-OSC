

bl_info = {
    "name": "UI test",
    "author": "Michal Seta",
    "version": (0, 0, 0),
    "blender": (2, 75, 0),
    "location": "View 3D > Tool Shelf > SATIE panel",
    "warning": "Just testing boo",
    "wiki_url": "http://me.me",
    "description": "Testing some UI.",
    "category": "User",
}

if "bpy" in locals():
    import imp
    imp.reload(panel)
else:
    from . import panel

import bpy

# class ToolsPanel(bpy.types.Panel):
#     bl_label = "SATIE tool"
#     bl_space_type = "VIEW_3D"
#     bl_region_type = "TOOLS"
 
#     def draw(self, context):
#         self.layout.operator("hello.hello")

# bpy.utils.register_module(__name__)

def initialize():
    print("boo")

def register():
    initialize()
    bpy.utils.register_module(__name__)
 
def unregister():
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()
