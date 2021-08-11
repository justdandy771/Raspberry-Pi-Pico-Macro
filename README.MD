Wiring Diagram
![image](https://user-images.githubusercontent.com/86481157/129115380-86042ad6-cea7-449c-89d6-946a6e323791.png)
Connect each of the respective pins you wish to use to the appropriate GPIO Pin placing a switch in between with the gate allowing the pin to pull down to the positive VBUS pin


![PXL_20210811_231413113 MP](https://user-images.githubusercontent.com/86481157/129115540-85f2a19b-2443-4080-956c-7b2c95af845d.jpg)


How to use:

#1 Hold the boot select button then connect to computer

#2 This will initialize the pico and show up as a removable storage device. 

#3 Then copy over the adafruit-circuitpython-raspberry_pi_pico-en_US-6.3.0.uf2 to the pico. This will reboot the pico with the circuit python files installed

#4 Open up the editor of choice ie: thonny in my case and choose your interpreter in the run tab. Select circuit python from the drop down menu

#5 Copy the code directly into thonny and edit accordingly then test with run

#6 Once you are satisfied with the macros or text input save the file directly to the pico as code.py and disconnect

#7 Reconnect the device and you should be good to go.
