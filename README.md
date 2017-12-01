# ArduinoLGServiceRemote
Python and arduino based service remote for LG devices (smart TV, beamer, etc.). Tested and developed on PH550g beamer.

**What you need**

Hardware:

1. An Arduino card (http://arduino.cc)
2. A USB cable
3. A 100 Ohm resistor
4. An IR led emitter
5. A PC with USB port

Software:

1. Arduino software (http://arduino.cc/en/Main/Software)
2. Excellent IR remote library written by Ken Shirriff (https://github.com/z3t0/Arduino-IRremote)
3. Python 2.7 (https://www.python.org/downloads/) 
4. Python menu version <3.0.3. Higher versions don't work. pip install MySQL_python==3.0.3 (https://pypi.python.org/pypi/Menu/3.0.3)

**Wiring things**

As described on Ken Shirriff's blog (http://www.arcfn.com/2009/08/multi-protocol-infrared-remote-library.html), you need to connect one led leg through the resistor to pin 3 of the Arduino, and the other leg to Ground. Connect the Arduino to your PC using the USB cable.

![](http://openlgtv.org.ru/wiki/images/e/ef/Arduino-IR-emiter.png)

**Upload script to Arduino** 

Open the 'LG_service_remote.ino' file in your favorite Arduino IDE and save the project to your arduino folder (in Windows 'Documents/Arduino'). Create a folder 'libraries' in 'Documents/Arduino' and extract the IR remote files in a folder IRremote. Upload the script to the Arduino.

**Starting Python control**

Now turn on the LG device and direct the IR led towards the LG device. Launch the 'lgRemoteMenu.py' and set the correct COM port [e.g. 'COM1']. Now you can control the LG device using the python menu.





> Written with [StackEdit](https://stackedit.io/).