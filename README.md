# micropython-stepper-motor-library
Een <a href="http://micropython.readthedocs.io/" target="_blank">Micropython</a> bibliotheek om een <a href="https://github.com/gavinlyonsrepo/RpiMotorLib/blob/master/Documentation/28BYJ.md"   target="_blank">28BYJ-48</a> 5V stepper motor te kunnen gebruiken met ESP8266 of ESP32.

# Installatie
 - Optie 1: gebruik python <a href="https://pypi.org/project/mpfshell/">MPFshell</a> om die lib te upload naar jouw Micropython apparaat

```console
foo@bar:~$ git clone https://github.com/pappavis/micropython-stepper-motor-library
foo@bar:~$ pip3 install mpfshell
foo@bar:~$ mpfshell /dev/ttyUSB0
mpfs [/]> mkdir lib
mpfs [/]> cd lib
mpfs [/]> put uln2003_e4k.py
mpfs [/]> exit
foo@bar:~$
```

- Optie 2: Upload middels <a href="https://thonny.org/">Thonny</a> IDE voor Micropython.

# Gebruik
s1 = Stepper(mode, in1, in2, in3, in4, delay)

mode: MODE_ACHTERUIT|MODE_VOORUIT
in1 tot in4:    pinnen om te gebruiken
delay:          vertraging milliseconden.

## Voorbeeld:
```python
import machine
import micropython
import uln2003_e4k
import esp
esp.osdebug(None)
import gc
gc.collect()

def main():
    # easy Wemos D1 mini pin lookup.
    wemosPinsDict = {"D4":2, "D3":0, "D2":4, "D1":5, "RX":3, "TX":1, "D8":15, "D7":13, "D6":12, "D5":14, "D0":16}

    # run forward once for 1/8th revolution.
    s1 = Stepper(mode=MODE_ACHTERUIT,in1=wemosPinsDict["D1"], in2=wemosPinsDict["D2"], in3=wemosPinsDict["D3"], in4=wemosPinsDict["D4"], delay=0.01)
    runner.run([Command(stepper=s1, steps=FULL_ROTATION/8)])  # run forward


print("App start")
main()
print("App eind")

```

# Meer weten?
Contact mij bij #Easylab4kids  #e4k

