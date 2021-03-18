import numpy as np
from numpy.random import random
import sys
import os

def gen3d():
	# Gerar dados 3D
	max_x = 10.0
	max_y = 10.0
	max_z = 10.0
	factor = 3.0

	n_points = 30

	'''
	points_3d = []
	ranges = []
	for i in range(20):
		points_3d.append(np.array([max_x*random(), max_y*random(), max_z*random()]))
		ranges.append(factor*random())
	'''

	data = np.zeros((n_points,n_points,n_points,3)) # vector data
	for i in range(n_points):
		for j in range(n_points):
			for k in range(n_points):
				position = np.array([i*max_y/n_points, j*max_x/n_points, k*max_z/n_points])
				value = np.sin(position[0])*(1+np.sin(position[2]))
				data[i,j,k] = np.array([np.cos(position[2]),1,np.sin(position[0])])

	with open("stream.vtk","w") as f:
		f.write("# vtk DataFile Version 3.0\nvtk output\nASCII\nDATASET STRUCTURED_GRID\n")
		f.write("DIMENSIONS %d %d %d\n"%(n_points,n_points,n_points))
		f.write("POINTS %d float\n"%(n_points**3))
		for i in range(n_points):
			for j in range(n_points):
				for k in range(n_points):
					position = np.array([i*max_y/n_points, j*max_x/n_points, k*max_z/n_points])
					f.write("%f %f %f\n"%(position[0], position[1], position[2]))
		f.write("POINT_DATA %d\nSCALARS cellData float 3\nLOOKUP_TABLE default\n"%(n_points**3))
		for i in range(n_points):
			for j in range(n_points):
				for k in range(n_points):
					f.write("%f %f %f\n"%(data[i,j,k][0],data[i,j,k][1],data[i,j,k][2]))

gen3d()