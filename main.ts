radio.setGroup(1)
radio.setTransmitPower(7)
radio.setTransmitSerialNumber(true)
let my_serial = control.deviceSerialNumber()
let learn = 0
let alarm = 0
let list = [my_serial]
// alarm_sound_off
input.onButtonPressed(Button.B, function alarm_off() {
    radio.sendValue("alarm", 0)
    music.stopAllSounds()
})
// alarm_sound_on
input.onButtonPressed(Button.A, function alarm_on() {
    radio.sendValue("alarm", 1)
})
// prepinani_learn_on/off
input.onLogoEvent(TouchButtonEvent.LongPressed, function learn_function() {
    
    if (learn == 0) {
        learn = 1
    } else {
        learn = 0
    }
    
})
// posilani_learn
input.onLogoEvent(TouchButtonEvent.Pressed, function send_learn() {
    radio.sendValue("learn", 1)
})
// recevied_data
function received_data(name: any, value: any) {
    
    let remote_serial = radio.receivedPacket(RadioPacketProperty.SerialNumber)
    if (name == "learn" && value == 1) {
        if (list.indexOf(remote_serial) < 0) {
            list.push(remote_serial)
        }
        
    }
    
}

