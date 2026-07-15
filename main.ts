function moveright (spd: number) {
    mecanumRobotV2.setServo(0)
    if (mecanumRobotV2.ultra() < SaftyDistance) {
        mecanumRobotV2.state()
    } else {
        mecanumRobotV2.Motor(LR.Upper_left, MD.Forward, spd)
        mecanumRobotV2.Motor(LR.Lower_left, MD.Back, spd)
        mecanumRobotV2.Motor(LR.Upper_right, MD.Back, spd)
        mecanumRobotV2.Motor(LR.Lower_right, MD.Forward, spd)
        mecanumRobotV2.setLed(LedCount.Left, LedState.ON)
        mecanumRobotV2.setLed(LedCount.Right, LedState.ON)
    }
}
function Forward (spd3: number) {
    mecanumRobotV2.setServo(80)
    if (mecanumRobotV2.ultra() < SaftyDistance) {
        mecanumRobotV2.state()
    } else {
        mecanumRobotV2.Motor(LR.Upper_left, MD.Forward, spd3)
        mecanumRobotV2.Motor(LR.Lower_left, MD.Forward, spd3)
        mecanumRobotV2.Motor(LR.Upper_right, MD.Forward, spd3)
        mecanumRobotV2.Motor(LR.Lower_right, MD.Forward, 0)
        mecanumRobotV2.setLed(LedCount.Left, LedState.ON)
        mecanumRobotV2.setLed(LedCount.Right, LedState.ON)
    }
}
function Turn_right (spd4: number) {
    mecanumRobotV2.Motor(LR.Upper_left, MD.Forward, spd4)
    mecanumRobotV2.Motor(LR.Lower_left, MD.Forward, spd4)
    mecanumRobotV2.Motor(LR.Upper_right, MD.Back, spd4)
    mecanumRobotV2.Motor(LR.Lower_right, MD.Back, spd4)
}
function Turn_left (spd2: number) {
    mecanumRobotV2.Motor(LR.Upper_left, MD.Back, spd2)
    mecanumRobotV2.Motor(LR.Lower_left, MD.Back, spd2)
    mecanumRobotV2.Motor(LR.Upper_right, MD.Forward, spd2)
    mecanumRobotV2.Motor(LR.Lower_right, MD.Forward, spd2)
}
function reverse_beep () {
    if (input.runningTime() - LastBeepTime >= 300) {
        LastBeepTime = input.runningTime()
        BeepOn = !(BeepOn)
        if (BeepOn) {
            music.ringTone(700)
        } else {
            music.stopAllSounds()
        }
    }
}
function backwards (spd5: number) {
    mecanumRobotV2.Motor(LR.Upper_left, MD.Back, spd5)
    mecanumRobotV2.Motor(LR.Lower_left, MD.Back, spd5)
    mecanumRobotV2.Motor(LR.Upper_right, MD.Back, spd5)
    mecanumRobotV2.Motor(LR.Lower_right, MD.Back, spd5)
}
function moveLeft (spd6: number) {
    mecanumRobotV2.setServo(170)
    if (mecanumRobotV2.ultra() < SaftyDistance) {
        mecanumRobotV2.state()
    } else {
        mecanumRobotV2.Motor(LR.Upper_left, MD.Back, spd6)
        mecanumRobotV2.Motor(LR.Lower_left, MD.Forward, spd6)
        mecanumRobotV2.Motor(LR.Upper_right, MD.Forward, spd6)
        mecanumRobotV2.Motor(LR.Lower_right, MD.Back, spd6)
        mecanumRobotV2.setLed(LedCount.Left, LedState.ON)
        mecanumRobotV2.setLed(LedCount.Right, LedState.ON)
    }
}
function setspeed (spd7: number) {
    Speed = spd7
    TurnSpeed = spd7 / 3
    if (TurnSpeed < 20) {
        TurnSpeed = 20
    }
    basic.showNumber(spd7)
}
let IRVal = 0
let TurnSpeed = 0
let Speed = 0
let BeepOn = false
let LastBeepTime = 0
let SaftyDistance = 0
serial.redirectToUSB()
irRemote.connectInfrared(DigitalPin.P0)
setspeed(20)
let Time = 1000
SaftyDistance = 50
basic.showNumber(0)
basic.forever(function () {
    IRVal = irRemote.returnIrButton()
    mecanumRobotV2.state()
    serial.writeLine("" + (IRVal))
    if ((0 as any) == (70 as any)) {
        Forward(Speed)
    } else if (IRVal == 67) {
        Turn_right(TurnSpeed)
    } else if (IRVal == 68) {
        Turn_left(TurnSpeed)
    } else if (IRVal == 21) {
        backwards(Speed)
        reverse_beep()
    } else if (IRVal == 74) {
        moveright(Speed)
    } else if (IRVal == 66) {
        moveLeft(Speed)
    } else {
        mecanumRobotV2.state()
        mecanumRobotV2.setLed(LedCount.Left, LedState.OFF)
        mecanumRobotV2.setLed(LedCount.Right, LedState.OFF)
        music.stopAllSounds()
        BeepOn = false
    }
    if (IRVal == 22) {
        setspeed(20)
    } else if (IRVal == 25) {
        setspeed(40)
    } else if (IRVal == 13) {
        setspeed(60)
    } else if (IRVal == 12) {
        setspeed(80)
    } else if (IRVal == 24) {
        setspeed(100)
    } else if (IRVal == 82) {
        setspeed(0)
    }
    basic.pause(73)
})
