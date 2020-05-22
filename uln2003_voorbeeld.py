import uln2003
import machine
import micropython
import time

wemosPinsDict = {"D4":2, "D3":0, "D2":4, "D1":5, "RX":3, "TX":1, "D8":15, "D7":13, "D6":12, "D5":14, "D0":16}
LED_INTERNAL = wemosPinsDict["D4"]
LED_AANUIT = {"AAN":1, "UIT":0}

print("App start")

def main():
    s1 = Stepper(mode=MODE_ACHTERUIT,in1=wemosPinsDict["D1"], in2=wemosPinsDict["D2"], in3=wemosPinsDict["D3"], in4=wemosPinsDict["D4"], delay=0.01)
    
    if(1==2):
        s1.testAllesAan(waarde=1)
        pass

    if(1==2):
        s1.step(count=FULL_ROTATION/2)        
        time.sleep(2)
        #s1.reset()
        pass

    if(1==1):
        runner = Driver()
        aantalLoopjes = 12
        for teller1 in range(0, aantalLoopjes):
            
            print("runner loopje",teller1,"van",aantalLoopjes)        
            s1 = Stepper(mode=MODE_ACHTERUIT,in1=wemosPinsDict["D1"], in2=wemosPinsDict["D2"], in3=wemosPinsDict["D3"], in4=wemosPinsDict["D4"], delay=0.01)
            runner.run([Command(stepper=s1, steps=FULL_ROTATION/8)])  # run forward
            time.sleep(0.5)

            #print("runner: vooruit")
            s1 = Stepper(mode=MODE_VOORUIT,in1=wemosPinsDict["D1"], in2=wemosPinsDict["D2"], in3=wemosPinsDict["D3"], in4=wemosPinsDict["D4"], delay=0.01)
            runner.run([Command(stepper=s1, steps=FULL_ROTATION/2)])  # backwards a bit to remove blockages from cat feeder screw.
            
        print("runner: eind")
        pass

print("main")
main()
print("App eind")
