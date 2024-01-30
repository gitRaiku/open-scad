from kms import *

set_global_fn(20)

activeSize = [382, 215, 4]
screenSize = [400, 231, 4]
bracketSize = [15, 8.56, 0.3]
bracketPos = [screenSize[0] / 2 - 20, (screenSize[1] + bracketSize[1]) / 2, screenSize[2] - 0.8 - bracketSize[2]]
bracketHolePos = [4, 3.1 / 2]
bracketHoleDiameter = 2.4
pcbSize = [290.5, 11.5]
pcbPos = [0, (screenSize[1] + pcbSize[1]) / 2]

def getScreen():
    screenArea = sq(screenSize[0], screenSize[1]).down(1)
    activeArea = center(sq(activeSize[0], activeSize[1]), activeSize, screenSize)

    pcbArea = center(sq(pcbSize[0], pcbSize[1]), pcbSize, screenSize).back(pcbPos[1])
    screenArea += pcbArea
    screenBox = screenArea.linear_extrude(screenSize[2])


    bracketArea = sq(bracketSize[0], bracketSize[1]) \
                    - ccr(cr(bracketHoleDiameter / 2), bracketSize) \
                        .left(bracketHolePos[0]).fwd(bracketHolePos[1]) \
                    - ccr(cr(bracketHoleDiameter / 2), bracketSize) \
                        .right(bracketHolePos[0]).fwd(bracketHolePos[1])

    cBracketArea = center(bracketArea, bracketSize, screenSize)
    cBracketBox = cBracketArea.linear_extrude(bracketSize[2])
    screenBox += cBracketBox.translate( bracketPos[0],  bracketPos[1], bracketPos[2])
    screenBox += cBracketBox.translate(-bracketPos[0],  bracketPos[1], bracketPos[2])
    screenBox += cBracketBox.translate( bracketPos[0], -bracketPos[1], bracketPos[2])
    screenBox += cBracketBox.translate(-bracketPos[0], -bracketPos[1], bracketPos[2])
    return screenBox

screenBox = getScreen()
final = screenBox
final.save_as_scad("lp.scad")
