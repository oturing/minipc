#!/usr/bin/env python

"""
Primeira versao do Dojo com pcDuino programada por Luciano Ramalho na
Noite do Mini PC em 29/mai/2013 no Garoa Hacker Clube
"""

# fonte:
# https://learn.sparkfun.com/tutorials/programming-the-pcduino/accessing-gpio-pins
# https://learn.sparkfun.com/tutorials/programming-the-pcduino/analog-input-and-output

import time, os

GPIO_MODE_PATH= os.path.normpath('/sys/devices/virtual/misc/gpio/mode/')
GPIO_PIN_PATH=os.path.normpath('/sys/devices/virtual/misc/gpio/pin/')
ADC_PATH= os.path.normpath('/proc/')

pinMode = []
pinData = []
adcFiles = []

HIGH = "1"
LOW =  "0"
INPUT = "0"
OUTPUT = "1"

def setup():
    for i in range(18):
        pinMode.append(os.path.join(GPIO_MODE_PATH, 'gpio'+str(i)))
        pinData.append(os.path.join(GPIO_PIN_PATH, 'gpio'+str(i)))

    for i in range(6):
        adcFiles.append(os.path.join(ADC_PATH, 'adc'+str(i)))

    for pin in pinMode:
        with open(pin, 'r+') as f: ## open the file in r/w mode
            f.write(OUTPUT)        ## set the mode of the pin

    for pin in pinData:
        with open(pin, 'r+') as f: ## open the file in r/w mode
            f.write(LOW)

def set(pin, value):
    with open(pinData[pin], 'r+') as pin_file:
        pin_file.write(str(value))

def analog(pin):
    with open(adcFiles[pin], 'r') as pin_file:
        pin_file.seek(0)
        return int(pin_file.read(16).split(':')[1])

setup()
while True:
    for i in [0, 1, 7, 5, 4, 2]:
        set(i, 1)
        delay = float(analog(5))/4096
        time.sleep(delay)
        set(i, 0)
