def moveTower(height,fromPole,withPole,toPole):
    if height >= 1:
        moveTower(height-1,fromPole,toPole,withPole)
        moveDisk(fromPole,toPole)
        moveTower(height-1,withPole,toPole,fromPole)

def moveDisk(fromPole, toPole):
    print("moving disk from",fromPole,"to",toPole)

moveTower(2,"left","Middle","Right")