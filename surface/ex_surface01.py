#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Examples for the NURBS-Python Package
    Released under MIT License
    Developed by Onur Rauf Bingol (c) 2016-2018
"""

import os
from geomdl import BSpline
from geomdl import control_points
from geomdl import exchange
from geomdl.visualization import VisVTK as vis
from netCDF4 import Dataset
import numpy as np
# Fix file path
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Create a BSpline surface instance
#surf = BSpline.Surface()

# Set degrees

# Set control points
nc=Dataset('C:/Users/HANBIT/Downloads/2014082500.nc')
prmsl=nc['INPUTDATA'].variables['PRMSL'][0][:]
lat=np.arange(419)
lon=np.arange(491)
XX,YY=np.meshgrid(lon,lat)
print(XX,YY)
u=XX.flatten()
v=YY.flatten()
p=prmsl.flatten()
print(u,v,p)
ctr=np.c_[v,u,p]
print(ctr)
print(ctr)
print(len(ctr))
print(419*491)
#surf.set_ctrlpts(ctr, 419,491)

size_u = 419
size_v = 491
# Number of control points in all parametric dimensions

# Create control points manager
points = control_points.SurfaceManager(size_u, size_v)

# Set control points
for u in range(size_u):
    for v in range(size_v):
        # 'pt' is the control point, e.g. [10, 15, 12]
        points.set_ctrlpt(list(ctr[491*u+v]), u, v)

# # Create spline geometry
# Create spline geometry
surf = BSpline.Surface()

# Set control points
surf.degree_v = 3
surf.degree_u = 3
surf.ctrlpts_size_u=size_u
surf.ctrlpts_size_v=size_v
surf.ctrlpts = points.ctrlpts


#
# # Set control points
# surf.ctrlpts_size_u=size_u
# surf.ctrlpts_size_v=size_v
# surf.ctrlpts = ctr
#
# # surf.set_ctrlpts(*exchange.import_txt("ex_surface01.cpt", two_dimensional=True))
#
# Set knot vectors
knot_u=[float(x) for x in range(415)]
knot_u=[0.0,0.0,0.0,0.0]+knot_u+[415.0,415.0,415.0,415.0]
knot_v=[float(x) for x in range(487)]
knot_v=[0.0,0.0,0.0,0.0]+knot_v+[487.0,487.0,487.0,487.0]

surf.knotvector_u=knot_u
surf.knotvector_v=knot_v

# surf.knotvector_u = [0.0, 0.0, 0.0, 0.0, 1.0, 2.0, 3.0, 3.0, 3.0, 3.0]
# surf.knotvector_v = [0.0, 0.0, 0.0, 0.0, 1.0, 2.0, 3.0, 3.0, 3.0, 3.0]

# Set evaluation delta
surf.delta = 0.025

# Evaluate surface points
surf.evaluate()

# Import and use Matplotlib's colormaps
from matplotlib import cm

# Plot the control point grid and the evaluated surface
vis_comp = vis.VisSurface()
vis_config = vis.VisConfig(legend=False, axes=True, figure_dpi=120)
vis_obj = VisMPL.VisCurve2D(vis_config)
surf.vis = vis_comp.VisConfig()
surf.render(colormap=cm.cool)

# Good to have something here to put a breakpoint
pass
