import math

def distance_to_attenuation(distance):
    """
    A very crude distance to attenuation conversion.
    (we use the abs of the number you give us.)
    @param distance: Absolute distance in meters.
    @type distance: float
    @rtype: float
    """
    d = abs(distance)
    if d <= 1.0:
        return 1.0
    attenuation = 1.0 / d
    return attenuation

def xyz_to_aed(xyz):
    """
    Converts XYZ to AED.
    @param xyz - list of three floats.
    @return: list of three floats.
    """
    aed = []
    x = xyz[0]
    y = xyz[1]
    z = xyz[2]
    distance = math.sqrt((x*x) + (y*y) + (z*z))
    azimuth = math.atan2(y,x)
    # print("----> azimuth {}".format(azimuth))
    # put in range of [-pi, pi]
    if azimuth > math.pi:
        azimuth -= 2 * math.pi
    elif azimuth < -math.pi:
        azimuth += 2 * math.pi
    if distance > 0.00001:
        elevation = math.acos(z/distance)
    else:
        elevation = 0.0

    aed = rads2degs([azimuth, elevation])
    aed.append(distance) 
    return aed

def rads2degs(v):
    ret = map(math.degrees, v)
    ret = list(ret)
    return ret
