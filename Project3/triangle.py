import numpy as np
import matplotlib.pyplot as plt
from math import sin, pi

#Creates an array with the points of an equilateral triangle
corners = np.array([(0,0), (1,0), (0.5, sin(pi/3))])

plt.axis('equal')
plt.scatter(*zip(*corners))
plt.show()

def triangle(n):
    #Returns a list of points within the equilateral triangle "corners"
    x0 = []
    w = []
    for i in range(0, n):
        r = np.random.random(3)
        w += [r/(sum(r))]
        x0 += [corners[0]*w[i][0] + corners[1]*w[i][1] + corners[2]*w[i][2]]
    return x0
    print(sum(w))

plt.scatter(*zip(*triangle(1000)))
plt.axis('equal')
plt.show()

def corner(n):
    #Creates a list of points based on the number of iterations n
    Xi = []
    Xi += triangle(1)
    for i in range(1, n+6):
        j = np.random.randint(3)
        Xi += [(Xi[i-1] + corners[j])/2]
    return Xi[4:]


plt.scatter(*zip(*corner(10000)), s=0.1)
plt.axis('equal')
plt.axis('off')
marker = '.'
plt.show()

def adding_color(n):
    Xi = []
    col = []
    Xi += triangle(1)
    for i in range(n+3):
        j = np.random.randint(3)
        col += [j]
        Xi += [(Xi[i] + corners[j])/2]
    return Xi[4:], col[3:]


points, colors = adding_color(10000)

red = []
blue = []
green = []
for i in range(len(points)):
	if colors[i] == 0:
		red += [points[i]]
	elif colors[i] == 1:
		blue += [points[i]]
	else:
		green += [points[i]]

plt.scatter(*zip(*red), s=0.1, color="red")
plt.scatter(*zip(*green), s=0.1, color="blue")
plt.scatter(*zip(*blue), s=0.1, color="green")
plt.axis('equal')
plt.axis('off')
marker = '.'
plt.show()

# col = []
# col += [np.zeros(3)]
# for i in range(len(points)-1):
# 	col += [(col[i] + colors[i+1])/2]
    
# col = np.asarray(col)
plt.scatter(*zip(*points), c=colors, s=0.2)
plt.axis('equal')
plt.axis('off')
marker = '.'
plt.show()
 