import solid2 as S
import seaborn as sns
import random
from math import sqrt, tan

def set_global_fn(fn):
    S.set_global_fn(fn)

max_colours = 10
cpalletes = sns.color_palette("husl", max_colours)
random.seed(2)

def a2r(x):
    return x * 3.1415 / 180

def ta(x):
    return tan(a2r(x))

def gcol():
    return cpalletes[random.randrange(0, max_colours)]

def gc(x):
    return x.color(gcol())

def sq(*args):
    if len(args) == 2:
        return S.square(args[0], args[1]).color(gcol())
    else:
        return S.square(args[0][0], args[0][1]).color(gcol())

def cr(sx):
    return S.circle(sx).color(gcol())

def rsq(p, ang, sa):
    return p.translate(-sa[0]/2, -sa[1]/2, 0).rotate(ang).translate(sa[0]/2, sa[1]/2, 0)

def center(p, sa, sb):
    return p.translate((sb[0] - sa[0]) / 2, (sb[1] - sa[1]) / 2, 0.0)

def ccr(c, sa):
    return c.translate(sa[0] / 2, sa[1] / 2, 0.0)

def csq(sx, sy):
    return S.square(sx, sy, center=True).color(gcol())

def c(sx, sy, sz):
    return S.cube(sx, sy, sz, center=False).color(gcol())

def ctop(sx, sy, sz):
    return c(sx, sy, sz).up(sz/2)

def cbot(sx, sy, sz):
    return c(sx, sy, sz).down(sz/2)

def cleft(sx, sy, sz):
    return c(sx, sy, sz).left(sx/2)

def cright(sx, sy, sz):
    return c(sx, sy, sz).right(sx/2)

def cfront(sx, sy, sz):
    return c(sx, sy, sz).fwd(sy/2)

def cback(sx, sy, sz):
    return c(sx, sy, sz).back(sy/2)

def cc(sx, sy, sz):
    return S.cube(sx, sy, sz, center=True).color(gcol())

def cctop(sx, sy, sz):
    return cc(sx, sy, sz).down(sz/2)

def ccbot(sx, sy, sz):
    return cc(sx, sy, sz).up(sz/2)

def ccleft(sx, sy, sz):
    return cc(sx, sy, sz).right(sx/2)

def ccright(sx, sy, sz):
    return cc(sx, sy, sz).left(sx/2)

def ccfront(sx, sy, sz):
    return cc(sx, sy, sz).back(sy/2)

def ccback(sx, sy, sz):
    return cc(sx, sy, sz).front(sy/2)

def s(*args):
    if len(args) == 3:
        return S.sphere(args[0], args[1], args[2]).color(gcol())
    else:
        return S.sphere(args[0]).color(gcol())

def chc(size, angle, depth, type = 0b111):
    zc = S.cube(size[0], size[1], size[2])
    rc = S.cube(size[0], size[1], size[2])

    if type & 0b001:
        rc -= zc.rotate([0, 0,  90 - angle]).translate([0, size[1] - depth, 0]) + \
              zc.rotate([0, 0,  90 + angle]).translate([depth * ta(angle), 0, 0]) + \
              zc.rotate([0, 0, 270 - angle]).translate([size[0], depth, 0]) + \
              zc.rotate([0, 0, 270 + angle]).translate([size[0] - depth * ta(angle), size[1], 0])
    if type & 0b010:
        angle = 90 - angle
        rc -= zc.rotate([0,  90 - angle, 0]).translate([size[0] - depth, 0, 0]) + \
              zc.rotate([0,  90 + angle, 0]).translate([0, 0, depth * ta(angle)]) + \
              zc.rotate([0, 270 - angle, 0]).translate([depth, 0, size[2]]) + \
              zc.rotate([0, 270 + angle, 0]).translate([size[0], 0, size[2] - depth * ta(angle)])
        angle = 90 - angle
    if type & 0b100:
        rc -= zc.rotate([ 90 - angle, 0, 0]).translate([0, 0, size[2] - depth]) + \
              zc.rotate([ 90 + angle, 0, 0]).translate([0, depth * ta(angle), 0]) + \
              zc.rotate([270 - angle, 0, 0]).translate([0, size[1], depth]) + \
              zc.rotate([270 + angle, 0, 0]).translate([0, size[1] - depth * ta(angle), size[2]])
    return rc
def s(*args):
    if len(args) == 3:
        return S.sphere(args[0], args[1], args[2]).color(gcol())
    else:
        return S.sphere(args[0]).color(gcol())

def half(s):
    if len(s) == 2:
        return [s[0] / 2, s[1] / 2]
    else:
        return [s[0] / 2, s[1] / 2, s[2] / 2]

def neg(s):
    if len(s) == 2:
        return [-s[0], -s[1]]
    else:
        return [-s[0], -s[1], -s[2]]
            
def rcb(c, *args):
    ang = 0.0
    scale = []
    if len(args) == 2:
        scale = args[0]
        ang = args[1]
    else:
        scale = [args[0], args[1], args[2]]
        ang = args[3]

    return c.translate(neg(half(scale))).rotate(ang).translate(half(scale))

def hex(d):
    return S.circle(d = d, _fn = 6)

def drik(d):
    return S.circle(d = d, _fn = 3)

def schraube(m, h, counterSunk=False, actualHeight=0, topHeight=0, topDiameter=0, headType=0):
    pitch = 0.0
    bore = 0.0
    if topHeight == 0:
        topHeight = m
    if topDiameter == 0:
        topDiameter = m * 2
    if actualHeight == 0:
        actualHeight = h
    if m == 3:
        pitch = 0.5
        bore = 3.2
    elif m == 4:
        pitch = 0.7
        bore = 4.3

    threadHeight = sqrt(3) / 2 * pitch
    centerD = bore - threadHeight
    angel = (h / pitch) * 120
    thread = drik(m).linear_extrude(h, twist=angel)
    centerBore = S.circle(d = centerD).linear_extrude(actualHeight)


    top = S.cylinder(topHeight, d1 = centerD if counterSunk else topDiameter, d2 = topDiameter)

    gauraDepth = 0.8
    if headType == 0:
        phillipsWidth = 0.14
        phillipsLength = 0.8
        top = top - \
            S.square([topDiameter * phillipsWidth, topDiameter * phillipsLength], center=True).linear_extrude(gauraDepth + 1).up(topHeight - gauraDepth) - \
            S.square([topDiameter * phillipsLength, topDiameter * phillipsWidth], center=True).linear_extrude(gauraDepth + 1).up(topHeight - gauraDepth) 
    elif headType == 1:
        phillipsWidth = 0.2
        phillipsLength = 0.8
        top = top - \
            S.square([topDiameter * phillipsLength, topDiameter * phillipsWidth], center=True).linear_extrude(gauraDepth + 1).up(topHeight - gauraDepth)
    elif headType == 2:
        top = top - \
            hex(4).linear_extrude(gauraDepth + 1).up(topHeight - gauraDepth)
            # TODO: This 4 isn't actually what it should be

    return thread + centerBore + top.up(actualHeight)

    # centerThign = S.cylinder(h, m, m)
    

