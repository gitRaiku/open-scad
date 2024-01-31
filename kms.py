import solid2 as S
import seaborn as sns
import random

def set_global_fn(fn):
    S.set_global_fn(fn)

max_colours = 10
cpalletes = sns.color_palette("husl", max_colours)
random.seed(2)
def gcol():
    return cpalletes[random.randrange(0, max_colours)]

def gc(x):
    return x.color(gcol())

def sq(sx, sy):
    return S.square(sx, sy, center=False).color(gcol())

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
    rc = zc
    if type & 0b001:
        rc -= zc.rotate([0, 0, 45]).translate([0, size[1] - depth, 0]) + \
              zc.rotate([0, 0, 135]).translate([depth, 0, 0]) + \
              zc.rotate([0, 0, 225]).translate([size[0], depth, 0]) + \
              zc.rotate([0, 0, 315]).translate([size[0] - depth, size[1], 0])
    if type & 0b010:
        rc -= zc.rotate([0, 45, 0]).translate([size[0] - depth, 0, 0]) + \
              zc.rotate([0, 135, 0]).translate([0, 0, depth]) + \
              zc.rotate([0, 225, 0]).translate([depth, 0, size[2]]) + \
              zc.rotate([0, 315, 0]).translate([size[0], 0, size[2] - depth])
    if type & 0b100:
        rc -= zc.rotate([45, 0, 0]).translate([0, size[1], size[2] - depth]) + \
              zc.rotate([135, 0, 0]).translate([0, depth, size[2]]) + \
              zc.rotate([225, 0, 0]).translate([0, 0, depth]) + \
              zc.rotate([315, 0, 0]).translate([0, size[1] - depth, 0])
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


