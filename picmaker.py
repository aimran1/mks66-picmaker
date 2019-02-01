import random
width = 500
height = 500
maxval = 255 

header = "P3 " + "\n" + str(width) + " " + str(height) + "\n" + str(maxval) + "\n"
r = 225#random.randint(0,maxval)
g = 200#random.randint(0,maxval)
b = 255#random.randint(0,maxval)

mypic = open("mypic.ppm", "w")
mypic.write(header)

def drawRow(red,gre,blu):
    for i in range(width):
        mypic.write(str(red) + " " + str(gre) + " " + str(blu) + " ")

for j in range(height):
    if g > 0:
        g-=1
    if r > 0: 
        r-=1
    if g == 0:
        g = 0
        r = 0
        b -= 1
    drawRow(r,g,b)
mypic.write("\n")

mypic.close()
