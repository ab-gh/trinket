import board
import busio
import time
dotstar = busio.SPI(board.APA102_SCK, board.APA102_MOSI)
colors = [0, 0, 0]
print("INIT") ## REPL
def setPixel(red, green, blue):
    if not dotstar.try_lock():
        return
    #print("setting pixel to: %d %d %d" % (red, green, blue))
    dotstar.write(bytearray([0x00, 0x00, 0x00, 0x00, 0xff, blue, green, red, 0xff, 0xff, 0xff, 0xff]))
    dotstar.unlock()
    time.sleep(0.01)

while True:
    for i in range(0,255):
        colors[1] += 1
        print(colors)
        time.sleep(0.01)
        setPixel(colors[0], colors[1], colors[2])
    for i in range(255,0,-1):
        colors[1] -= 1
        print(colors)
        time.sleep(0.03)
        setPixel(colors[0], colors[1], colors[2])
