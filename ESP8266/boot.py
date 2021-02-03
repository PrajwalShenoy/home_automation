import network  # ip is 192.168.0.102
import machine
import time


def toggle(pin):
    pin.value(not pin.value())

def connect_to_wifi(uid, pwd, pin):
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.active():
        sta_if.active(True)
    sta_if.connect(uid, pwd)
    while not sta_if.isconnected():
        toggle(pin)
        time.sleep(0.1)
    pin.off()
    time.sleep(2)
    pin.on()

if __name__ == "__main__":
    pin = machine.Pin(2, machine.Pin.OUT)
    connect_to_wifi(<<UID>>, <<PWD>>, pin)
