# Program to read flow sensor and display flow rate in Serial Monitor.
from machine import Pin, I2C
import time
from ssd1306 import SSD1306_I2C
sda1=machine.Pin(6)
scl1=machine.Pin(7)
i2c=I2C(1,sda=sda1, scl=scl1, freq=400000)
oled = SSD1306_I2C(128, 64, i2c)
oled.init_display()
flow_frequency=0
flow_rate=0
lastcallTime=0
print("\n=====================\nKaira's Flow Meter\n=====================\n")
pin = Pin(21,Pin.IN,Pin.PULL_UP)
def callback(pin):
    global flow_frequency
    flow_frequency=flow_frequency+1
pin.irq(trigger=Pin.IRQ_RISING, handler=callback)
    
while True:
    if ((time.ticks_ms()-lastcallTime) > 1000):  #if time interval is more a than 1 second
        flow_rate = (flow_frequency * 60 / 7.5)  #flowrate in L/hour= (Pulse frequency x 60 min) / 7.5 
        flow_frequency = 0                       # Reset Counter
        lastcallTime=time.ticks_ms()
        print("Flow Rate={} Litres/Hour".format(flow_rate))   #print(flow_rate)
        oled.fill(0)
        oled.text("KD SMART METER", 0, 0)
        oled.text("FR:"+str(flow_rate)+str(" L/Hr"),0,50)
        oled.show()