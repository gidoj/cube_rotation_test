from Tkinter import *
from numpy import matrix
from math import cos, sin, pi
from random import randint

root = Tk()

canvasW = 500
canvasH = 500
canvasSize = str(canvasW) + "x" + str(canvasH)

root.title("Rotation Test")
root.geometry(canvasSize)

c = Canvas(root, height=canvasH, width=canvasW, bg="black")
c.pack()

offs = 250	#offset from origin
scale = 100	#scale factor
theta = 0.1;#how much to rotate by

#shapes to manipulate in '3D' space
squares = [matrix([[-1,  1,  1, -1],
				   [-1, -1,  1,  1],
				   [ 1,  1,  1,  1]]),
		   matrix([[-1, -1, -1, -1],
				   [-1, -1,  1,  1],
				   [-1,  1,  1, -1]]),
		   matrix([[-1,  1,  1, -1],
				   [ 1,  1,  1,  1],
				   [-1, -1,  1,  1]]),
		   matrix([[-1,  1,  1, -1],
				   [-1, -1,  1,  1],
				   [ -1,  -1,  -1,  -1]]),
		   matrix([[1, 1, 1, 1],
				   [-1, -1,  1,  1],
				   [-1,  1,  1, -1]]),
		   matrix([[-1,  1,  1, -1],
				   [ -1,  -1,  -1,  -1],
				   [-1, -1,  1,  1]])]

triangles = [matrix([[ 0,  1, -1],
					 [-1,  1,  1],
					 [ 0,  1,  1]]),
			 matrix([[ 0,  1,  0],
					 [-1,  1,  1],
					 [ 0,  1, -1]]),
			 matrix([[ 0, -1,  0],
					 [-1,  1,  1],
					 [ 0,  1, -1]]),
		     matrix([[ 1, -1,  0],
					 [ 1,  1,  1],
					 [ 1,  1, -1]])]

squares2 = [matrix([[-1,  1,  1, -1],
				   [-1, -1,  1,  1],
				   [ 1,  1,  1,  1]]),
		   matrix([[-1,  1,  1, -1],
				   [-1, -1,  1,  1],
				   [ -1,  -1,  -1,  -1]])]

squares3 = [matrix([[-1,  1,  1, -1],
				   [-1, -1,  1,  1],
				   [ 1.2,  1.2,  1.2,  1.2]]),
		   matrix([[-1.2, -1.2, -1.2, -1.2],
				   [-1, -1,  1,  1],
				   [-1,  1,  1, -1]]),
		   matrix([[-1,  1,  1, -1],
				   [ 1.2,  1.2,  1.2,  1.2],
				   [-1, -1,  1,  1]]),
		   matrix([[-1,  1,  1, -1],
				   [-1, -1,  1,  1],
				   [ -1.2,  -1.2,  -1.2,  -1.2]]),
		   matrix([[1.2, 1.2, 1.2, 1.2],
				   [-1, -1,  1,  1],
				   [-1,  1,  1, -1]]),
		   matrix([[-1,  1,  1, -1],
				   [ -1.2,  -1.2,  -1.2,  -1.2],
				   [-1, -1,  1,  1]])]

squares_rot = [matrix([[-1,  1,  1, -1],
				   [-1, -1,  1,  1],
				   [ 1,  1,  1,  1]]),
		   matrix([[ 1.14412281,  0.83125388, -1.14412281, -0.83125388],
        		   [-0.83125388,  1.14412281,  0.83125388, -1.14412281],
				   [ 0.8, 0.8, 0.8, 0.8]]),
		   matrix([[ 1.26007351,  0.64203952, -1.26007351, -0.64203952],
        		   [-0.64203952,  1.26007351,  0.64203952, -1.26007351],
				   [ 0.6, 0.6, 0.6, 0.6]]),
		   matrix([[ 1.34499702,  0.43701602, -1.34499702, -0.43701602],
        		   [-0.43701602,  1.34499702,  0.43701602, -1.34499702],
				   [ 0.4, 0.4, 0.4, 0.4]]),
		   matrix([[ 1.39680225,  0.22123174, -1.39680225, -0.22123174],
        		   [-0.22123174,  1.39680225,  0.22123174, -1.39680225],
				   [ 0.2, 0.2, 0.2, 0.2]]),
		   matrix([[  1.41421356e+00,   1.66533454e-16,  -1.41421356e+00,
          -1.66533454e-16],
        			[ -1.66533454e-16,   1.41421356e+00,   1.66533454e-16,
          -1.41421356e+00],
				   [ 0, 0, 0, 0]]),
		   matrix([[ 1.39680225, -0.22123174, -1.39680225,  0.22123174],
        		   [ 0.22123174,  1.39680225, -0.22123174, -1.39680225],
				   [ -0.2, -0.2, -0.2, -0.2]]),
		   matrix([[ 1.34499702, -0.43701602, -1.34499702,  0.43701602],
        		   [ 0.43701602,  1.34499702, -0.43701602, -1.34499702],
				   [ -0.4, -0.4, -0.4, -0.4]]),
		   matrix([[ 1.26007351, -0.64203952, -1.26007351,  0.64203952],
       		  	   [ 0.64203952,  1.26007351, -0.64203952, -1.26007351],
				   [ -0.6, -0.6, -0.6, -0.6]]),
		   matrix([[ 1.14412281, -0.83125388, -1.14412281,  0.83125388],
        		   [ 0.83125388,  1.14412281, -0.83125388, -1.14412281],
				   [ -0.8, -0.8, -0.8, -0.8]]),
		   matrix([[-1,  1,  1, -1],
				   [-1, -1,  1,  1],
				   [ -1,  -1,  -1,  -1]]),]


#colors = ["red", "blue", "yellow", "white", "orange", "green"]
#colors = ["#188888", "#199999", "#1aaaaa", "#1bbbbb", "#1ccccc", "#1ddddd"]
colors = ["#188888", "#199999", "#1aaaaa", "#1bbbbb", "#1ccccc", "#1ddddd",
			'#17c7c7', '#1ccccc', '#1bbbbb', '#1aaaaa', '#199999', '#188888']

### CHANGE DEPENDING ON WHICH SHAPES WISH TO DISPLAY
shapes = squares


x = 0
y = 0

### below are mouse listeners

#listen for mouse pressed
def pressed(event):
	global x, y
	x = event.x
	y = event.y

#listen for mouse dragged
def dragged(event):
	global x, y
	dx = x - event.x
	dy = y - event.y
	x = event.x
	y = event.y
	c.delete("all")
	redraw(dy*0.1, -dx*0.1)

### end listeners

#sx, sy determine which direction and to what degree to rotate in x, y directions
def redraw(sx, sy):
	global shapes, theta
	for i, _ in sorted(draw_order().iteritems(), key=lambda (k,v): (v,k)):
		shapes[i] = rotate(shapes[i], theta, sx, sy)
		draw_polygon(flatten(shapes[i]), colors[i])

def draw_order():
	global shapes
	zdict = {}
	for i in range(len(shapes)):
		m = shapes[i]
		zs = 0
		for j in range(m.shape[1]):
			zs += m[2,j]
		zdict[i] = zs
	return zdict

##given matrix m of 2d points (x, y) draw the corresponding polygon
def draw_polygon(m, col):
	pts = []
	for i in range(m.shape[1]):
		pts.append(m[0,i] + offs)
		pts.append(m[1,i] + offs)
	
	c.create_polygon(pts, fill=col)

#given a matrix m, flattens 3d object into 2d representation 
#not sure how to incorporate z at the moment
def flatten(m):
	clist = [[], []]
	for i in range(m.shape[1]):
		dz = m[2,i]/500
		u = m[0,i]*(dz+1)
		v = m[1,i]*(dz+1)
		clist[0].append(u)
		clist[1].append(v)
	return matrix(clist)

#m is matrix to rotate
#sx, sy determine which direction and to what degree to rotate in x, y directions
def rotate(m, theta, sx, sy):
	m = rotm_x(theta*sx)*m
	m = rotm_y(theta*sy)*m
	return m

'''
** below are transformation matrices
**	-x rotation
**	-y rotation
**	-z rotation
**	-scaling
**
'''

#f is scale factor
def scalem(f):
	scalem = matrix([[f, 0, 0],
					[0, f, 0],
					[0, 0, f]])
	return scalem

def rotm_z(theta):
	rotm = matrix([[cos(theta), -sin(theta), 0], 
				   [sin(theta),  cos(theta), 0],
				   [0		  ,  0		   , 1]])
	return rotm

def rotm_y(theta):
	rotm = matrix([[ cos(theta), 	0, sin(theta)], 
				   [    	  0, 	1,  		0],
				   [-sin(theta), 	0, cos(theta)]])
	return rotm

def rotm_x(theta):
	rotm = matrix([[1, 			0, 			 0], 
				   [0, cos(theta), -sin(theta)],
				   [0, sin(theta), cos(theta)]])
	return rotm

### end of transformation matrices
def start():
	for i, _ in sorted(draw_order().iteritems(), key=lambda (k,v): (v,k)):
		shapes[i] = scalem(scale)*shapes[i]
		draw_polygon(flatten(shapes[i]), colors[i])

c.focus_set()
c.bind("<Button-1>", pressed)
c.bind("<B1-Motion>", dragged)

start()

root.mainloop()
