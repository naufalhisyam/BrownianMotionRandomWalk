import time
import vpython as vp
from calculations import *
from objects import Molecule, Container

"""Canvas Initialization"""
display = vp.canvas(width=500, height=550, background=vp.color.black, resizeable=True) # Initialize canvas object
title = vp.label(pos=vp.vector(0,113,0), text="<b>2D Brownian Motion</b>", box=False, height=25) # Set title


"""Objects Initalization"""
# ----------------------------------------------------------------------------
container = Container(200, 200, 4) # Initialize container
border_up, border_down, border_left, border_right = container.create() # Container borders

# ----------------------------------------------------------------------------
n = 100 # number of molecules
initial_pos = [0,0,0] # molecule initial position
size = 1.2 # molecule size

mols = [Molecule(size, initial_pos) for _ in range(n)]
for mol in mols:
    mol.create() # Initialize molecules

# ----------------------------------------------------------------------------
time_counter = vp.label(pos=vp.vector(70,-115,0), text="t = 0 s", box=False, height=20) # Set time counter
count_mol = vp.label(pos=vp.vector(-50,-115,0),
                     text=f"Number of molecules = {n}", box=False, height=20) # Show number of molecules


"""Simulation"""
# ----------------------------------------------------------------------------
if __name__ == "__main__":
    t = 0
    end_time = 1000
    
    while t < end_time: # Start simulation
        vp.rate(100)
        display.autoscale = False
        ts = time.process_time()
        for mol in mols: # Calculate position of each molecule
            if hit_up(mol, border_up):
                mol.instance.pos = mol.instance.pos - vp.vector(0,border_up.height,0) + delta_x()
            elif hit_down(mol, border_down):
                mol.instance.pos = mol.instance.pos + vp.vector(0,border_down.height,0) + delta_x()
            elif hit_left(mol, border_left):
                mol.instance.pos = mol.instance.pos + vp.vector(border_left.length,0,0) + delta_y()
            elif hit_right(mol, border_right):
                mol.instance.pos = mol.instance.pos - vp.vector(border_right.length,0,0) + delta_y()
            else:
                mol.instance.pos = mol.instance.pos + delta_x() + delta_y() 
        dt = time.process_time() - ts
        t += dt
        time_counter.text = "t = {:0.1f} s".format(t)
