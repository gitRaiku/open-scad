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
