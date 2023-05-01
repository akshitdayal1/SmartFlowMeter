#Smart Flow Meter

Components required:
Connection Diagram:
Code:
Output:
Interfacing the microcontroller and Mobile App
References:






























Components required:
1x RaspberryPi PicoW (Wireless pico)
1x Water Flow Sensor: YF-S201  (Hall Effect Sensor)
1x Breadboard
1x Bidirectional Level Shifter
1x ssd1306 OLED display (To output the flow rate on an OLED Display)
1x NPN Small signal Transistor (Optional, not required if the level shifter is used)
2x 10k Resistors (Optional, not required if the level shifter is used)
Pin Connecting wires of various colors


Connection Diagram:

Connecting the PICO W and the Flow meter



Refer the raspberry pi pico W pinout diagram here
Flow Rate calculations: Refer

Flow rate (L/min)=Frequency (Hz) / 7.5



Connecting OLED to PICO



Picture of the connections (Final result)


Code: 
I will be using python in Thonny IDE to program the picoW
Setup the picoW to be used with thonny


Code to output the flow rate and output





Code to send the flow rate to the Local Server : 
<Work in Progress>





Output:
Note: Output data simulated by blowing air through the flow sensor, it should be similar to flow of water at the same rate.


Interfacing the microcontroller and Mobile App


References:
https://electrocredible.com/raspberry-pi-pico-flow-sensor-yfs201/

