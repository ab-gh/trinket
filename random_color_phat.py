import unicornhat as uh
import time
import random
uh.set_layout(uh.PHAT)
uh.brightness(0.5)
uh.set_layout(uh.AUTO)
uh.rotation(0)
uh.brightness(0.5)
width,height=uh.get_shape()
#colors = [1, 128, 244]      # set colors all to 1
colors = [random.randint(3, 240), random.randint(3, 240), random.randint(3, 240), ]     # selects random start color in "safe zone"
steps = [1, 3, 4]       # set wavelength
steps = [random.randint(1, 5), random.randint(1, 5), random.randint(1, 5)]              # selects random step beteween 1 and 5
print("INIT") ## REPL
def getColor(index, colors, steps):
    if colors[index] >= 255 or colors[index] <= 0:      # flip the sign of the step at the max/min
        steps[index] *= -1
    colors[index] += steps[index]                       # increment the value
    if colors[index] > 255: colors[index] = 255         # accounting for stepping over 255
    if colors[index] < 0: colors[index] = 0             # accounting for stepping under 0
    return (colors[index], colors, steps)               # returns colors for index

while True:
    r, colors, steps = getColor(0, colors, steps)       # gets red
    g, colors, steps = getColor(1, colors, steps)       # gets green
    b, colors, steps = getColor(2, colors, steps)       # gets blue
    print("STEP = ", steps, "COLOR = ", colors)         # REPL debug print
    uh.set_all(r, g, b)                                 # calls setPixel
    uh.show()
    time.sleep(random.random())                         # random wait time between 0 and 1
