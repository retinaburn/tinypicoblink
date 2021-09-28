import bluetooth
from bleuart import *
from machine import Pin, SPI
import tinypico as TinyPICO
from dotstar import DotStar
import time

spi = SPI(sck=Pin( TinyPICO.DOTSTAR_CLK ), mosi=Pin( TinyPICO.DOTSTAR_DATA ), miso=Pin( TinyPICO.SPI_MISO) ) 
dotstar = DotStar(spi, 1, brightness = 0.5 ) # Just one DotStar, half brightness
TinyPICO.set_dotstar_power( True )

lightPin = Pin(5, mode=Pin.OUT)

ble = bluetooth.BLE()
uart = BLEUART(ble)

def on_rx():
    received = uart.read()
    print("Received: ", received)
    try:
        receivedString = received.decode().strip()
        receivedString = receivedString.lower()
        if (receivedString == "on"):
            lightPin.on()
            print("Light: ON")
            uart.write("ON")
        elif (receivedString == "off"):
            lightPin.off()
            print("Light: OFF")
            uart.write("OFF")    
    except UnicodeError:
        mybytes = bytes(received)
        for mybyte in mybytes:
            print("Byte: ", mybyte)
        dotStar[0] = (mybytes(2), mybytes(3), mybytes(4))

        

uart.irq(handler=on_rx)
nums = [4, 8, 15, 16, 23, 42]
i = 0

#try:
#    while True:
        #uart.write(str(nums[i]) + "\n")
        #i = (i + 1) % len(nums)
        #time.sleep_ms(1000)
#except KeyboardInterrupt:
#    pass

uart.close()