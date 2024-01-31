from kms import *

set_global_fn(20)

screenSize = [400, 231, 4]
activeSize = [382, 215, 4]

bracketSize = [15, 8.56, 0.3]
bracketPos = [screenSize[0] / 2 - 20, (screenSize[1] + bracketSize[1]) / 2, screenSize[2] - 0.8 - bracketSize[2]]
bracketHolePos = [4, 3.1 / 2]
bracketHoleDiameter = 2.4
pcbSize = [290.5, 11.5]
pcbPos = [0, (screenSize[1] + pcbSize[1]) / 2]

screenArea = sq(screenSize[0], screenSize[1])
activeArea = center(sq(activeSize[0], activeSize[1]), activeSize, screenSize)
activeBox = activeArea.linear_extrude(10).up(screenSize[2])

pcbArea = center(sq(pcbSize[0], pcbSize[1]), pcbSize, screenSize).back(pcbPos[1] - 0.01)
screenArea += pcbArea
screenBox = screenArea.linear_extrude(screenSize[2])

screenArea += pcbArea.back(6)
__cbr = center(sq(bracketSize[0], bracketSize[1]), bracketSize, screenSize)
screenArea += __cbr.translate( bracketPos[0],  bracketPos[1] - 0.01, 0.0) + __cbr.translate(-bracketPos[0],  bracketPos[1] - 0.01, 0.0) + __cbr.translate( bracketPos[0], -bracketPos[1] + 0.01, 0.0) + __cbr.translate(-bracketPos[0], -bracketPos[1] + 0.01, 0.0) 

bracketArea = sq(bracketSize[0], bracketSize[1]) \
                - ccr(cr(bracketHoleDiameter / 2), bracketSize) \
                    .left(bracketHolePos[0]).fwd(bracketHolePos[1]) \
                - ccr(cr(bracketHoleDiameter / 2), bracketSize) \
                    .right(bracketHolePos[0]).fwd(bracketHolePos[1])

cBracketArea = center(bracketArea, bracketSize, screenSize)
cBracketAreaR = center(rsq(bracketArea, 180, bracketSize), bracketSize, screenSize)
cBracketBox = cBracketArea.linear_extrude(bracketSize[2])
cBracketBoxR = cBracketAreaR.linear_extrude(bracketSize[2])
screenBox += cBracketBox.translate( bracketPos[0],  bracketPos[1], bracketPos[2])
screenBox += cBracketBox.translate(-bracketPos[0],  bracketPos[1], bracketPos[2])
screenBox += cBracketBoxR.translate( bracketPos[0], -bracketPos[1], bracketPos[2])
screenBox += cBracketBoxR.translate(-bracketPos[0], -bracketPos[1], bracketPos[2])

coverYMargins = [10 + bracketSize[1], 
                 10 + pcbSize[1]]
coverMargin = [10, coverYMargins[0] + coverYMargins[1], 0]
coverSize = [screenSize[0] + coverMargin[0] * 2, 
             screenSize[1] + coverMargin[1], 
             screenSize[2] + 2, 10]
coverPos = [0, (coverYMargins[0] - coverYMargins[1]) / 2, 0]
coverArea = center(sq(coverSize[0], coverSize[1]), coverSize, screenSize).translate(coverPos[0], coverPos[1], coverPos[2])

screenFullBox = screenArea.linear_extrude(screenSize[2])
coverBoxTop = coverArea.linear_extrude(coverSize[2]) - screenFullBox - activeBox
coverBoxBot = coverArea.linear_extrude(coverSize[3]).down(coverSize[3]) - screenArea.linear_extrude(coverSize[3] - 1).down(coverSize[3] - 1)

ccubS = [21, 28, 29]
ccub = chc(ccubS, 45, 3, type=0b110)
final = coverBoxBot 
final.save_as_scad("lp.scad")
