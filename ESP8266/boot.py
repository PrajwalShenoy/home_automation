import network
import machine
import time
import os
import socket
import html_files

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
ap_if = network.WLAN(network.AP_IF)
ap_if.active(True)
led_pin = machine.Pin(2, machine.Pin.OUT) # D4
led_pin.value(1)


def toggle(pin):
    pin.value(not pin.value())

def connect_to_wifi():
    print("Connecting to WiFi")
    uid, pwd = read_creds()
    sta_if = network.WLAN(network.STA_IF)
    sta_if.connect(uid, pwd)
    while not sta_if.isconnected():
        toggle(led_pin)
        time.sleep(0.1)
    led_pin.off()
    time.sleep(2)
    led_pin.on()

def get_new_creds():
    sta_if.disconnect()
    print("Setting up webpage to get new credentials")
    addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
    soc = socket.socket()
    soc.bind(addr)
    soc.listen(5)
    print("Listening on", addr)
    while True:
        client, addr = soc.accept()
        print("Client connected from", addr)
        request = client.recv(1024)
        request = request.decode().split()
        uid, pwd = '', ''
        if 'uid' in request[1]:
            uid = request[1].split('&')[0].split('=')[1]
            pwd = request[1].split('&')[1].split('=')[1]
            write_new_creds(uid, pwd)
            connect_to_wifi()
            print("The UID is", uid, "and the Password is", pwd)
            client.send('HTTP/1.1 200 OK\r\nContent-type: text/html\r\n\r\n')
            client.send(html_files.connection_response.format(sta_if.ifconfig()[0]))
            return uid, pwd
        print(request)
        client.send('HTTP/1.1 200 OK\r\nContent-type: text/html\r\n\r\n')
        client.send(html_files.cred_prompt)
        client.close()

def check_button(pin):
    print("Checking if button is pressed...")
    start_time = time.time()
    temp_power = machine.Pin(13, machine.Pin.OUT) # D7
    temp_power.value(1)
    while time.time() < start_time + 2:
        if pin.value() == 1:
            temp_power.value(0)
            return True
    temp_power.value(0)
    return False

def write_new_creds(uid, pwd):
    print("Writing new credentials to wifi_cred.txt")
    cred_file = open("wifi_cred.txt", "w")
    cred_file.write("UID="+uid+"\n")
    cred_file.write("PASSWORD="+pwd)
    cred_file.close()

def read_creds():
    print("Reading credentials from wifi_cred.txt")
    if "wifi_cred.txt" in os.listdir():
        cred_file = open("wifi_cred.txt", 'r')
        for line in cred_file:
            if "UID" in line.split('='):
                uid = line.strip().split('=')[1]
            if "PASSWORD"in line.split('='):
                pwd = line.strip().split('=')[1]
        return uid, pwd
    else:
        uid, pwd = get_new_creds()
        return uid, pwd

def main():
    print("\nStarting booting sequence")
    button = machine.Pin(4, machine.Pin.IN) # D2
    if check_button(button):
        print("Button is pressed, getting new credentials...")
        uid, pwd = get_new_creds()
        write_new_creds(uid, pwd)
    connect_to_wifi()

main()
