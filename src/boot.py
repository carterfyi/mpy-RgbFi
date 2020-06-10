# boot.py - - runs on boot-up
import network
from ujson import load

def init_wifi():
    wificonfig = {}
    try:
        f = open("wificonfig.json")
        wificonfig = load(f)
        f.close()
    except OSError:
        print('wifi config file error')
        return None

    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.ifconfig(('192.168.1.186', '255.255.255.0', '192.168.1.1', '8.8.8.8'))
    wlan.connect(wificonfig["ssid"], wificonfig["password"])

    while not wlan.isconnected():
        pass
    print('network config:', wlan.ifconfig())
    return wlan

wlan = init_wifi()
