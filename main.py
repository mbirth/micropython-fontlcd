# main.py -- put your code here!

import fontlcd
import mpr121

LED_RED = 0
LED_GREEN = 1
LED_YELLOW = 2
LED_BLUE = 3

BTN_Y = 0
BTN_X = 1
BTN_B = 2
BTN_A = 3

leds = [pyb.LED(i) for i in range(1, 5)]
for l in leds:
    l.off()

lcd = fontlcd.FontLCD('X')
lcd.light(True)
lcd.loadFont('fourpx')
#lcd.write('Hello Master!\n')

m = mpr121.MPR121(pyb.I2C(1, pyb.I2C.MASTER))

def blob(x, y, w, h, fill):
    for i in range(w):
        for j in range(h):
            if pyb.rng() & 0xff < fill:
                lcd.pixel(x+i, y+j, 1)

btn_down = [False]*4
try:
    while True:
        t = m.touch_status()
#        lcd.write("%4.2f -- %s\n" % (float(m.elec_voltage(3))/100, t))
#        lcd.fill(0)
#        for y in range(32):
#            lcd.pixel(64, y, 1)
#        for x in range(128):
#            lcd.pixel(x, 16, 1)

        # Button "Y"
        if t & (2**BTN_Y):
            if not btn_down[BTN_Y]:
                leds[LED_RED].toggle()
                lcd.write("You pressed Y!\n")
#            blob(90, 20, 10, 10, 316 - m.elec_voltage(BTN_Y))
            btn_down[BTN_Y] = True
        else:
            btn_down[BTN_Y] = False

        # Button "X"
        if t & (2**BTN_X):
            if not btn_down[BTN_X]:
                leds[LED_YELLOW].toggle()
                lcd.write("You pressed X!\n")
#            blob(30, 20, 10, 10, 316 - m.elec_voltage(BTN_X))
            btn_down[BTN_X] = True
        else:
            btn_down[BTN_X] = False

        # Button "B"
        if t & (2**BTN_B):
            if not btn_down[BTN_B]:
                leds[LED_GREEN].toggle()
                lcd.write("You pressed B!\n")
#            blob(90, 5, 10, 10, 316 - m.elec_voltage(BTN_B))
            btn_down[BTN_B] = True
        else:
            btn_down[BTN_B] = False

        # Button "A"
#        if t & 8:
#            blob(30, 5, 10, 10, 316 - m.elec_voltage(BTN_A))
#        lcd.show()
        leds[LED_BLUE].intensity(345 - m.elec_voltage(BTN_A))
        pyb.delay(20)
finally:
    for l in leds:
        l.off()
