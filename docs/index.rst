.. Mini PCs documentation master file, created by
   sphinx-quickstart on Sun Jul 14 08:11:23 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

========
Mini PCs
========

pcDuino
=======

blink.py
--------

::

    import time

    GPIO_PATH = '/sys/devices/virtual/misc/gpio/'

    OUTPUT_MODE = "1"
    ON = "1"
    OFF = "0"

    DEBUG = True

    def pin_mode(pin, mode):
        with open(GPIO_PATH+'mode/gpio%s' % pin, 'w') as f:
            f.write(mode)

    def digital_write(pin, value):
        with open(GPIO_PATH+'pin/gpio%s' % pin, 'w') as f:
            f.write(str(value))

    def setup():
        pin_mode(3, OUTPUT_MODE)

    setup()
    while True:
        digital_write(3, ON)
        time.sleep(1)
        digital_write(3, OFF)
        time.sleep(1)


pcDuino7seg.py
-----------------

::

    #!/usr/bin/env python

    """
    Segunda versao do Dojo com pcDuino programada por Luciano Ramalho no TDC 2013
    """

    # fonte:
    # https://learn.sparkfun.com/tutorials/programming-the-pcduino/accessing-gpio-pins
    # https://learn.sparkfun.com/tutorials/programming-the-pcduino/analog-input-and-output

    import time, os

    GPIO_PATH = os.path.normpath('/sys/devices/virtual/misc/gpio/')
    ADC_PATH = os.path.normpath('/proc/')

    INPUT = "0"
    OUTPUT = "1"
    HIGH = "1"
    LOW =  "0"

    def pin_mode(pin, mode):
        with open(GPIO_PATH+'mode/gpio%s' % pin, 'w') as f:
            f.write(mode)

    def digital_write(pin, value):
        with open(GPIO_PATH+'pin/gpio%s' % pin, 'w') as f:
            f.write(str(value))

    def analog_read(pin):
        with open(ADC_PATH+'adc%d' % pin) as f:
            f.seek(0)
            return int(f.read(16).split(':')[1])

    def setup():
        for i in range(18):
            pin_mode(i, OUTPUT)
            digital_write(i, LOW)

    setup()
    while True:
        for i in [0, 1, 7, 5, 4, 2]:
            digital_write(i, 1)
            delay = analog_read(5)/4096.0
            time.sleep(delay)
            digital_write(i, 0)


rpi7seg.py
-----------

::

    import atexit
    import time
    import RPi.GPIO as GPIO
    import spi

    atexit.register(GPIO.cleanup)  # chamar na saida do script

    GPIO.setmode(GPIO.BCM)

    DISPLAY = [17, 4, 9, 11, 7, 27, 22, 10]

    SPI_CLK = 18
    SPI_MISO = 23
    SPI_MOSI = 24
    SPI_CS = 25
    conversor_ad = spi.Mcp3008(SPI_CLK, SPI_MISO, SPI_MOSI, SPI_CS)

    CANAL_POTENCIOMETRO = 1

    for led in DISPLAY[:6]:
        GPIO.setup(led, GPIO.OUT)
        GPIO.output(led, 0)

    while True:
        for led in DISPLAY[:6]:
            GPIO.output(led, 1)
            atraso = conversor_ad.read(CANAL_POTENCIOMETRO)/1000.0
            time.sleep(atraso)
            GPIO.output(led, 0)

anima.js
--------

.. code-block:: javascript

    var b = require('bonescript');

    var tempo = 0;
    var i_pino = 0;
    var pinos = [16, 21, 22, 13, 12, 11];

    /* setup */
    for (var i=0; i<pinos.length; i++ ) {
        var p = pinos[i];
        var pin = "P9_" + p;
        b.pinMode(pin, b.OUTPUT);
        b.digitalWrite(pin, 0);
    }

    function desligar() {
        b.digitalWrite("P9_" + pinos[i_pino], 0);
        i_pino++;
        if (i_pino == pinos.length) {
            i_pino = 0;
        }
        setTimeout(ligar, 0);
    };

    function ligar() {
        console.log(i_pino);
        b.digitalWrite("P9_" + pinos[i_pino], 1);
        setTimeout(desligar, tempo);
    }

    function ler() {
        b.analogRead('P9_39', function (p) {
            tempo = p.value * 1000;
        });
    }

    ligar();
    setInterval(ler, 100);





