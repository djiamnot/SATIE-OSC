import bpy
import liblo
import math
import os
from . import utils

print("imported satie synth module")

class SatieSynth():
    """
    Object representing a synth in SATIE
    This implementation uses the satieOSC prorocol
    """
    def __init__(self, parent, id, plugin):
        """
        Parems:
        parent - bpy_types.Object
        id - parent's satieID
        """
        print("instantiated a synth object")
        self.id = id
        self.synth = plugin
        self.group = "default"
        self.oscaddress = liblo.Address("localhost", 18032)
        self.oscbaseurl = "/SATIE"
        self.oscURI = None
        self.myParent = parent
        self.selected = False
        self.playing = False
        self.setURI()
        self.createSource()
        # self.setURIplugin(plugin)
        self.play()

    def setURI(self):
        self.oscURI = os.path.join(self.oscbaseurl, self.group, self.id)

    def createSource(self):
        liblo.send(self.oscaddress, self.oscURI, "create", self.id, self.synth)

    def deleteNode(self):
        liblo.send(self.oscaddress, self.oscURI, "delete")

    def set(self, prop, val):
        if not val:
            self.playing = False
        else:
            self.playing = True
        liblo.send(self.oscaddress, self.oscURI, prop, val)

    def play(self):
        print("play", self)
        liblo.send(self.oscaddress, self.oscURI, "t_trig", 1)
        print("sent play")
        
        # uri = os.path.join(self.sourceOSCuri, "state")
        # liblo.send(self.oscaddress, uri, 1)
        # if "zkarpluck" in self.synth:
        #     print("using plugin: {}".format(self.synth))
        #     uri = os.path.join(self.sourceOSCuri, "event")
        #     liblo.send(self.oscaddress, uri, "t_trig", 1)
                
    def updateAED(self):
        azi, ele, gain = self._getAED()
        liblo.send(self.oscaddress, self.oscURI, "set", "aziDeg", azi, "elevDeg", ele, "gainDB", gain)
        
        
    def _getLocation(self):
        camlocation = bpy.data.objects['Camera'].location

        parent = self._getParent()
        # location = parent.location - camlocation
        location = parent.matrix_world.to_translation()
        # print("-------> location: {}".format(location))
        return location

    def _getParent(self):
        parent = [o for o in bpy.context.selected_objects if o.satieID == self.id]
        if len(parent) is 1:
            return parent[0]
        else:
            print("something went wrong. there are {} parents, should be 1 and they are {} but I am {}".format(len(parent), parent, self.id))
            print([o.satieID for o in parent])

    def _getAED(self):
        distance = self._getLocation()
        # print("----> distance {}".format(distance))
        aed = utils.xyz_to_aed(distance)
        # print("---------> aed {}".format(aed))
        gain = math.log(utils.distance_to_attenuation(aed[2])) * 20
        aed[2] = gain
        return aed
