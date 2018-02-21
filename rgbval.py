import board
import busio
import time
dotstar = busio.SPI(board.APA102_SCK, board.APA102_MOSI)
print("INIT") # REPL
def setPixel(red, green, blue):
    if not dotstar.try_lock():
        return
    print("setting pixel to: %d %d %d" % (red, green, blue))
    data = bytearray([0x00, 0x00, 0x00, 0x00,
                      0xff, blue, green, red,
                      0xff, 0xff, 0xff, 0xff])
    dotstar.write(data)
    dotstar.unlock()
    time.sleep(0.01)
while True:
    setPixel(*(int(c) for c in input("r, g, b: ").split(", ")))

