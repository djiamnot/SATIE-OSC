import bpy

bl_info = {
    "name": "SATIE OSC",
    "author": "Michal Seta",
    "version": (0, 1, 1),
    "blender": (2, 75, 0),
    "warning": "Preliminary version. You should have SATIE up and running to use this functionnality. It might work.",
    "wiki_url": "http://code.sat.qc.ca/redmine/projects/sc-basic-renderer/wiki",
    "description": "Connect a blender object with SATIE sound engine and author sound spacialisation.",
    "category": "User",
}

from . import properties as SatieProperties
from . import satie_object as so

addon_keymaps = []

def register():
    print("registering SatieSynth")
    bpy.utils.register_class(SatieProperties.SatieProperties)
    bpy.utils.register_class(so.SatieObject)

    bpy.types.Object.useSatie = bpy.props.BoolProperty(
                name = "Use SATIE",
                description = "Make object interact with SATIE",
                default = False
            )
    bpy.types.Object.satieID = bpy.props.StringProperty(
                name = "ID",
                description = "Sound source ID",
                default = "mySource"
            )
    bpy.types.Object.satieSynth = bpy.props.StringProperty(
                name = "Synth",
                description = "SATIE plugin to use",
                default = "default"
            )
    bpy.types.Object.satieGroup = bpy.props.StringProperty(
                name = "Group",
                description = "instrument/FX group",
                default = "default"
            )
    bpy.types.Object.sendToSATIE = bpy.props.BoolProperty(
                name = "Send to SATIE",
                description = "Send data to SATIE",
                default = False
            )
    bpy.types.Object.state = bpy.props.BoolProperty(
                name = "Source playing state",
                description = "Playing state (on, off)",
                default = False
    )

    # handle the keymap
    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps.new(name='Object Mode', space_type='EMPTY')
    kmi = km.keymap_items.new(so.SatieObject.bl_idname, 'SPACE', 'PRESS', ctrl=True, shift=True)
    addon_keymaps.append((km, kmi))
#end register

def unregister():
    print("unregistering SatieSynth")
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()
    bpy.utils.unregister_class(SatieProperties.SatieProperties)
    bpy.utils.unregister_class(so.SatieObject)
    so.cleanCallbackQueue()
    bpy.types.Object.useSatie
    bpy.types.Object.satieID
    bpy.types.Object.satieSynth
    bpy.types.Object.satieGroup
    bpy.types.Object.sendToSATIE
    bpy.types.Object.state


if __name__ == "__main__":
    register()
