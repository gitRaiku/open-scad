# import openscad
from kms import *

set_global_fn(20)

sS = [110, 138.5, 1]
coverMargin = 1
coverBotMargin = 30
coverUpMargin = 1
coverDownMargin = 7
cS = [sS[0] + coverMargin, sS[1] + coverMargin + coverBotMargin, 10]
aS = [90.7, 122.5, 1]
fS = [90.7, 35, 1]
buttonMargin = 5
bS = [105, 20, 1]

screen = sq(sS[0], sS[1]).up(2)
screenBox = gc(screen.linear_extrude(1))

activeArea = center(sq(aS[0], aS[1]), aS, sS)
activeAreaBox = gc(activeArea.linear_extrude(30))

fpcArea = center(sq(fS[0], fS[1]), fS, sS).up(10).fwd((sS[1] + fS[1]) / 2 - 10)
fpcAreaBox = gc(fpcArea.linear_extrude(7).down(6))

cover = center(sq(cS[0], cS[1]), cS, sS).fwd(coverBotMargin / 2)

buttonArea = center(sq(bS[0], bS[1]), bS, sS).fwd((sS[1] + bS[1]) / 2 + buttonMargin)
buttonAreaS = buttonArea.linear_extrude(6).down(4)

coverBoxTop = gc(cover.linear_extrude(coverUpMargin + 1) - activeAreaBox.down(5) - screenBox - fpcAreaBox - buttonAreaS)

coverBoxBot = gc(cover.linear_extrude(coverDownMargin).down(coverDownMargin))
coverBoxBot = coverBoxBot - activeAreaBox.down(coverDownMargin - 1) - fpcAreaBox

final = coverBoxTop + coverBoxBot

final.save_as_scad("epd.scad")
