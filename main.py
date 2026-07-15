def moveright(spd: number):
    mecanumRobotV2.set_servo(0)
    if mecanumRobotV2.ultra() < SaftyDistance:
        mecanumRobotV2.state()
    else:
        mecanumRobotV2.motor(LR.UPPER_LEFT, MD.FORWARD, spd)
        mecanumRobotV2.motor(LR.LOWER_LEFT, MD.BACK, spd)
        mecanumRobotV2.motor(LR.UPPER_RIGHT, MD.BACK, spd)
        mecanumRobotV2.motor(LR.LOWER_RIGHT, MD.FORWARD, spd)
        mecanumRobotV2.set_led(LedCount.LEFT, LedState.ON)
        mecanumRobotV2.set_led(LedCount.RIGHT, LedState.ON)
def Forward(spd3: number):
    mecanumRobotV2.set_servo(80)
    if mecanumRobotV2.ultra() < SaftyDistance:
        mecanumRobotV2.state()
    else:
        mecanumRobotV2.motor(LR.UPPER_LEFT, MD.FORWARD, spd3)
        mecanumRobotV2.motor(LR.LOWER_LEFT, MD.FORWARD, spd3)
        mecanumRobotV2.motor(LR.UPPER_RIGHT, MD.FORWARD, spd3)
        mecanumRobotV2.motor(LR.LOWER_RIGHT, MD.FORWARD, spd3)
        mecanumRobotV2.set_led(LedCount.LEFT, LedState.ON)
        mecanumRobotV2.set_led(LedCount.RIGHT, LedState.ON)
def Turn_right(spd4: number):
    mecanumRobotV2.motor(LR.UPPER_LEFT, MD.FORWARD, spd4)
    mecanumRobotV2.motor(LR.LOWER_LEFT, MD.FORWARD, spd4)
    mecanumRobotV2.motor(LR.UPPER_RIGHT, MD.BACK, spd4)
    mecanumRobotV2.motor(LR.LOWER_RIGHT, MD.BACK, spd4)
def Turn_left(spd2: number):
    mecanumRobotV2.motor(LR.UPPER_LEFT, MD.BACK, spd2)
    mecanumRobotV2.motor(LR.LOWER_LEFT, MD.BACK, spd2)
    mecanumRobotV2.motor(LR.UPPER_RIGHT, MD.FORWARD, spd2)
    mecanumRobotV2.motor(LR.LOWER_RIGHT, MD.FORWARD, spd2)
def reverse_beep():
    global LastBeepTime, BeepOn
    if input.running_time() - LastBeepTime >= 300:
        LastBeepTime = input.running_time()
        BeepOn = not (BeepOn)
        if BeepOn:
            music.ring_tone(700)
        else:
            music.stop_all_sounds()
def backwards(spd5: number):
    mecanumRobotV2.motor(LR.UPPER_LEFT, MD.BACK, spd5)
    mecanumRobotV2.motor(LR.LOWER_LEFT, MD.BACK, spd5)
    mecanumRobotV2.motor(LR.UPPER_RIGHT, MD.BACK, spd5)
    mecanumRobotV2.motor(LR.LOWER_RIGHT, MD.BACK, spd5)
def moveLeft(spd6: number):
    mecanumRobotV2.set_servo(170)
    if mecanumRobotV2.ultra() < SaftyDistance:
        mecanumRobotV2.state()
    else:
        mecanumRobotV2.motor(LR.UPPER_LEFT, MD.BACK, spd6)
        mecanumRobotV2.motor(LR.LOWER_LEFT, MD.FORWARD, spd6)
        mecanumRobotV2.motor(LR.UPPER_RIGHT, MD.FORWARD, spd6)
        mecanumRobotV2.motor(LR.LOWER_RIGHT, MD.BACK, spd6)
        mecanumRobotV2.set_led(LedCount.LEFT, LedState.ON)
        mecanumRobotV2.set_led(LedCount.RIGHT, LedState.ON)
def setspeed(spd7: number):
    global Speed, TurnSpeed
    Speed = spd7
    TurnSpeed = spd7 / 3
    if TurnSpeed < 20:
        TurnSpeed = 20
    basic.show_number(spd7)
IRVal = 0
TurnSpeed = 0
Speed = 0
BeepOn = False
LastBeepTime = 0
SaftyDistance = 0
serial.redirect_to_usb()
irRemote.connect_infrared(DigitalPin.P0)
setspeed(20)
Time = 1000
SaftyDistance = 50

def on_forever():
    global IRVal, BeepOn
    IRVal = irRemote.return_ir_button()
    mecanumRobotV2.state()
    serial.write_line("btn" + str(IRVal) + "     " + "X" + str(input.acceleration(Dimension.X)) + "     " + "Y" + str(input.acceleration(Dimension.Y)) + "     " + "Z" + str(input.acceleration(Dimension.Z)) + "     " + "North finder" + str(input.compass_heading()))
    if IRVal == 70:
        Forward(Speed)
    elif IRVal == 67:
        Turn_right(TurnSpeed)
    elif IRVal == 68:
        Turn_left(TurnSpeed)
    elif IRVal == 21:
        backwards(Speed)
        reverse_beep()
    elif IRVal == 74:
        moveright(Speed)
    elif IRVal == 66:
        moveLeft(Speed)
    else:
        mecanumRobotV2.state()
        mecanumRobotV2.set_led(LedCount.LEFT, LedState.OFF)
        mecanumRobotV2.set_led(LedCount.RIGHT, LedState.OFF)
        music.stop_all_sounds()
        BeepOn = False
    if IRVal == 22:
        setspeed(20)
    elif IRVal == 25:
        setspeed(40)
    elif IRVal == 13:
        setspeed(60)
    elif IRVal == 12:
        setspeed(80)
    elif IRVal == 24:
        setspeed(100)
    elif IRVal == 82:
        setspeed(0)
    basic.pause(1000)
basic.forever(on_forever)
