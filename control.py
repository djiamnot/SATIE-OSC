import bpy
from . import properties as props
from . import satie_synth as ss

def instanceHandler():
    synths = [obj.id for obj in props.synths]
    print("############## synths #########", synths)
    visibleObjs = bpy.context.visible_objects 
    if len(visibleObjs) > 0:
        for o in visibleObjs:
            if o.useSatie:
                if o.satieID in synths:
                    print("-- {} in synths, passing.........".format(o.satieID))
                    pass
                else:
                    print("acting on ", o.name)
                    props.synths.append(ss.SatieSynth(o, o.satieID, o.satieSynth))
                    print("current synths", props.synths)
            else:
                if o.satieID in synths:
                    print(">>>>>> removing {} ".format(o.satieID) )
                    toRemove = [x for x in props.synths if x.id == o.satieID]
                    for i in toRemove:
                        i.deleteNode()
                        props.synths.remove(i)

    print("<<<<<< synths ", props.synths)

def instanceCb(scene):
    instanceHandler()
    [synth.updateAED() for synth in props.synths]
    
def cleanCallbackQueue():
    if instanceCb in bpy.app.handlers.scene_update_post:
        bpy.app.handlers.scene_update_post.remove(instanceCb)

def getSatieSendCtl(self):
    print(props.active)
    return props.active

def setSatieSendCtl(self, value):
    props.active = value
    print(props.active)

def setSatieHP(self, value):
    print("HighPass ", self.satieID, value)
