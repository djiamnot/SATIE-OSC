import bpy
import liblo
import os

class SatieSynth():
    """Object representing a synth in SATIE"""
    def __init__(self, parent, id, plugin):
        """
        Parems:
        parent - bpy_types.Object
        id - parent's satieID
        plugin - SATIE plusgin (parent's satieURI property)
        """
        print("instantiated a synth object")
        self.id = id
        self.synth = None
        self.oscaddress = liblo.Address("localhost", 18032)
        self.oscbaseurl = "/spatosc/core"
        self.sourceOSCuri = None
        self.connection = None
        self.listener = "ear"
        self.myParent = parent
        self.selected = False
        self.playing = False
        self.createSource()
        self.setURIplugin(plugin)
        self.play()

    def createSource(self):
        liblo.send(self.oscaddress, self.oscbaseurl, "createSoundSource", self.id)
        self.sourceOSCuri = os.path.join(self.oscbaseurl, "source", self.id)

    def setURIplugin(self, plugin):
        """
        A plugin in this blender addon must include the type (i.e. plugin, file, etc.)
        """
        self.synth = plugin
        plugin = plugin
        path = os.path.join(self.sourceOSCuri, "uri")
        liblo.send(self.oscaddress, path, plugin)
        liblo.send(self.oscaddress, self.oscbaseurl, "connect", self.id, self.listener)
        self.connection = os.path.join(self.oscbaseurl, "connection", self.id + "->" + self.listener)

    def deleteNode(self):
        liblo.send(self.oscaddress, self.oscbaseurl, "deleteNode", self.id)

    def setState(self, val):
        if not val:
            self.playing = False
        else:
            self.playing = True
        uri = os.path.join(self.sourceOSCuri, "state")
        liblo.send(self.oscaddress, uri, val)

    def play(self):
        uri = os.path.join(self.sourceOSCuri, "state")
        liblo.send(self.oscaddress, uri, 1)
        if "zkarpluck" in self.synth:
            print("using plugin: {}".format(self.synth))
            uri = os.path.join(self.sourceOSCuri, "event")
            liblo.send(self.oscaddress, uri, "t_trig", 1)
                
    def sendUpdate(self):
        uri = os.path.join(self.connection, "update")
        msg = self._getAED()
        msg.append(0)
        msg.append(22050)
        print(msg)
        liblo.send(self.oscaddress, uri, *msg)
        
        
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
        aed = xyz_to_aed(distance)
        # print("---------> aed {}".format(aed))
        gain = math.log(distance_to_attenuation(aed[2])) * 20
        aed[2] = gain
        return aed
