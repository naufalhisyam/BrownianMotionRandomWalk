import vpython as vp
from scipy import stats

#Direction vectors
vy = vp.vector(0,0.5,0)
vx = vp.vector(0.5,0,0)
minvy = vp.vector(0,-0.5,0)
minvx = vp.vector(-0.5,0,0)

# ----------------------------------------------------------------------------
"""Random Walk"""
def displacement():
    return stats.norm.rvs(size=4)

#X-axis displacement
def delta_x():
    return displacement()[0]*vx + displacement()[2]*minvx

#Y-axis displacement
def delta_y():
    return displacement()[1]*vy + displacement()[3]*minvy

# ----------------------------------------------------------------------------
"""Container Collision Detector"""
def hit_right(mol, border_right):
    if (mol.instance.pos.x >= (border_right.pos.x - border_right.length)):
        return True
    else:
        return False
    
def hit_left(mol, border_left):
    if (mol.instance.pos.x <= (border_left.pos.x + border_left.length)):
        return True
    else:
        return False
    
def hit_up(mol, border_up):
    if (mol.instance.pos.y >= (border_up.pos.y - border_up.height)):
        return True
    else:
        return False
    
def hit_down(mol, border_down):
    if (mol.instance.pos.y <= (border_down.pos.y + border_down.height)):
        return True
    else:
        return False