# micropython-stepper-motor-library
Een <a href="http://micropython.readthedocs.io/" target="_blank">Micropython</a> bibliotheek om een 28BYJ-48 5V stepper motor te kunnen gebruiken op met ESP8266 of ESP32.

# Installatie
 - Optie 1: gebruik <a href="https://pypi.org/project/mpfshell/">MPFshell</a> om die lib te upload naar jouw Micropython apparaat
 > mpfshell COM3

 > mkdir lib

 > cd lib

 > put uln2003_e4k.py

- Optie 2: Upload middels <a href="https://thonny.org/">Thonny</a> IDE voor Micropython.

# Gebruik
 s1 = Stepper(mode, in1, in2, in3, in4, delay)

mode: MODE_ACHTERUIT|MODE_VOORUIT
in1 tot in4:    pinnen om te gebruiken
delay:          vertraging milliseconden.

## Voorbeeld:
```python
    s1 = Stepper(mode=MODE_ACHTERUIT,in1=wemosPinsDict["D1"], in2=wemosPinsDict["D2"], in3=wemosPinsDict["D3"], in4=wemosPinsDict["D4"], delay=0.01)
    runner.run([Command(stepper=s1, steps=FULL_ROTATION/8)])  # run forward

.
