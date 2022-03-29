radio.set_group(1)
radio.set_transmit_power(7)
radio.set_transmit_serial_number(True)
my_serial = control.device_serial_number()

learn = 0
alarm = 0
list = [my_serial]


#alarm_sound_off
def alarm_off():
    radio.sendValue("alarm", 0)
    music.stop_all_sounds()
input.on_button_pressed(Button.B, alarm_off)

#alarm_sound_on
def alarm_on():
    radio.sendValue("alarm", 1)
input.on_button_pressed(Button.A, alarm_on)

#prepinani_learn_on/off
def learn_function():
    global learn
    if learn == 0:
        learn = 1
    else:
        learn = 0
input.on_logo_event(TouchButtonEvent.LONG_PRESSED, learn_function)

#posilani_learn
def send_learn():
    radio.sendValue("learn", 1)
input.on_logo_event(TouchButtonEvent.PRESSED, send_learn)

#recevied_data
def received_data(name, value):
    global alarm, list
    remote_serial = radio.received_packet(RadioPacketProperty.SERIAL_NUMBER)
    if name == "learn" and value == 1:
        if remote_serial not in list:
            list.append(remote_serial)
           if name == "learn" and value == 1:
            music.play_melody("C", 120)
           if name == "learn" and value == 0:
            music.stop_all_sounds()
