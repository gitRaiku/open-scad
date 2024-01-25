# import openscad
import sys
sys.path.append('/home/raiku')
from kms import *

set_global_fn(200)

sS = [102, 138.5, 1]
aS = [90.7, 122.5, 1]

screen = sq(sS[0], sS[1]).down(2)
activeArea = sq(aS[0], aS[1]).translate((sS[0] - aS[0]) / 2, (sS[1] - aS[1]) / 2, 0)
activeAreaBox = activeArea.linear_extrude(12)
final = activeArea + activeAreaBox
'''
ch = 10
fpc = ctop(84.5, 20.0, 0.5).translate(0, 79, 0).down(2)
cover = ((ctop(104, 166, ch).fwd(13) - screen) - activeAreaBox) - screen
coverUp = cover - ctop(300, 300, 300).down(3.001) - activeAreaBox.down(5) - ctop(90.7, 122.5, 100).fwd(28).down(2)

coverDownHollow = cbot(90.7, 145, 10).fwd(9.25).down(9)
coverDown = (cover - cbot(300, 300, 300).down(3.001)) - coverDownHollow

final = coverDown
'''


final.save_as_scad("epd.scad")
