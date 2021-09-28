from machine import SPI, Pin, TouchPad
import tinypico as TinyPICO
from dotstar import DotStar
import time

spi = SPI(sck=Pin( TinyPICO.DOTSTAR_CLK ), mosi=Pin( TinyPICO.DOTSTAR_DATA ), miso=Pin( TinyPICO.SPI_MISO) ) 
# Create a DotStar instance
dotstar = DotStar(spi, 1, brightness = 0.5 ) # Just one DotStar, half brightness
# Turn on the power to the DotStar
TinyPICO.set_dotstar_power( False )




pin = Pin(5, Pin.OUT)

for i in range (2):
    pin.on()
    time.sleep_ms(200)
    pin.off()
    time.sleep_ms(200)
print("Hello")

touchPad = TouchPad(Pin(27))
while True:
    touchVal = touchPad.read()
    if (touchVal < 100):
        pin.on()
    else:
        pin.off()


