import numpy as np
from numpy.random import random
import sys
import os

def gen2d():
	# Gerar dados 2D - blobs
	max_x = 10.0
	max_y = 10.0
	factor = 3.0

	n_points = 100

	points_2d = []
	ranges = []
	for i in range(20):
		points_2d.append(np.array([max_x*random(), max_y*random()]))
		ranges.append(factor*random())

	data = np.zeros((n_points,n_points))
	for i in range(n_points):
		for j in range(n_points):
			position = np.array([i*max_y/n_points, j*max_x/n_points])
			value = 0
			for k in range(len(points_2d)):
				value += ranges[k]/(np.sqrt(np.linalg.norm(position-points_2d[k], 2)))
			data[i,j] = value

	with open("2d_data_ref.vtk","w") as f:
		f.write("# vtk DataFile Version 3.0\nvtk output\nASCII\nDATASET STRUCTURED_GRID\n")
		f.write("DIMENSIONS %d %d 1\n"%(n_points,n_points))
		f.write("POINTS %d float\n"%(n_points**2))
		for i in range(n_points):
			for j in range(n_points):
				position = np.array([i*max_y/n_points, j*max_x/n_points])
				f.write("%f %f 0\n"%(position[0], position[1]))
		f.write("POINT_DATA %d\nSCALARS cellData float 1\nLOOKUP_TABLE default\n"%(n_points**2))
		for i in range(n_points):
			for j in range(n_points):
				f.write("%f\n"%(data[i,j]))

def gen3d():
	# Gerar dados 3D
	max_x = 10.0
	max_y = 10.0
	max_z = 10.0
	factor = 3.0

	n_points = 30

	points_3d = []
	ranges = []
	for i in range(20):
		points_3d.append(np.array([max_x*random(), max_y*random(), max_z*random()]))
		ranges.append(factor*random())

	data = np.zeros((n_points,n_points,n_points))
	for i in range(n_points):
		for j in range(n_points):
			for k in range(n_points):
				position = np.array([i*max_y/n_points, j*max_x/n_points, k*max_z/n_points])
				value = 0
				for l in range(len(points_3d)):
					value += ranges[l]/(np.sqrt(np.linalg.norm(position-points_3d[l], 2)))
				data[i,j,k] = value

	with open("3d_data.vtk","w") as f:
		f.write("# vtk DataFile Version 3.0\nvtk output\nASCII\nDATASET STRUCTURED_GRID\n")
		f.write("DIMENSIONS %d %d %d\n"%(n_points,n_points,n_points))
		f.write("POINTS %d float\n"%(n_points**3))
		for i in range(n_points):
			for j in range(n_points):
				for k in range(n_points):
					position = np.array([i*max_y/n_points, j*max_x/n_points, k*max_z/n_points])
					f.write("%f %f %f\n"%(position[0], position[1], position[2]))
		f.write("POINT_DATA %d\nSCALARS cellData float 1\nLOOKUP_TABLE default\n"%(n_points**3))
		for i in range(n_points):
			for j in range(n_points):
				for k in range(n_points):
					f.write("%f\n"%(data[i,j,k]))

gen3d()