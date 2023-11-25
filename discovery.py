#!/usr/bin/env python3

from time import sleep
import pychromecast
import zeroconf

zconf = zeroconf.Zeroconf()

browser = pychromecast.CastBrowser(
    pychromecast.SimpleCastListener(
        lambda uuid,
        service: print("Device: {}\nUuid: {}\n".format(browser.devices[uuid].friendly_name, uuid))
    ),
    zconf
)

browser.start_discovery()
sleep(5)
pychromecast.discovery.stop_discovery(browser)
