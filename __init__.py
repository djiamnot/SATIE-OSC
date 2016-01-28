

bl_info = {
    "name": "SATIE OSC",
    "author": "Michal Seta",
    "version": (0, 1, 1),
    "blender": (2, 75, 0),
    "location": "View 3D > Tool Shelf > SATIE panel",
    "warning": "Early stages of development",
    "wiki_url": "https://github.com/djiamnot/SATIE-OSC",
    "description": "Author SATIE audio scenes with Blender",
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
