import board
import busio
import time
import random
import neopixel
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=.2)
pixels.fill((0,0,0))
pixels.show()
pixels.brightness=1

#colors = [1, 128, 244]      # set colors all to 1
colors = [random.randint(2, 80), random.randint(80, 149), random.randint(150, 200), ]     # selects random start color in "safe zone"
#steps = [1, 3, 4]       # set wavelength
steps = [random.randint(1, 2), random.randint(1, 2), random.randint(1, 2)]              # selects random step beteween 1 and 5
print("INIT") ## REPL
def getColor(index, colors, steps):
    if colors[index] >= 255 or colors[index] <= 0:      # flip the sign of the step at the max/min
        steps[index] *= -1
    colors[index] += steps[index]                       # increment the value
    if colors[index] > 255: colors[index] = 255         # accounting for stepping over 255
    if colors[index] < 0: colors[index] = 0             # accounting for stepping under 0
    return (colors[index], colors, steps)               # returns colors for index

def setPixel(red, green, blue):                         # call setpixel
    if not dotstar.try_lock():                          # see if clock is locked
        return
    #print("setting pixel to: %d %d %d" % (red, green, blue))   # debug
    dotstar.write(bytearray([0x00, 0x00, 0x00, 0x00, 0xff, blue, green, red, 0xff, 0xff, 0xff, 0xff]))
    dotstar.unlock()                                    # pass new color

while True:
    r, colors, steps = getColor(0, colors, steps)       # gets red
    g, colors, steps = getColor(1, colors, steps)       # gets green
    b, colors, steps = getColor(2, colors, steps)       # gets blue
    print("STEP = ", steps, "COLOR = ", colors)         # REPL debug print
    pixels.fill((r,g,b))
    pixels.show()    # calls setPixel
    #time.sleep(random.random())                         # random wait time between 0 and 1
    time.sleep(0.2)
