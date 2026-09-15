---
title: SD
description: secure digital memory card (cc3200 port only)
source_url: https://docs.micropython.org/en/latest/library/machine.SD.html
source_repo: https://github.com/micropython/micropython.git
source_ref: master
source_commit: 52b5fbcb4
source_path: library/machine.SD.rst
technology: micropython-pico
version: master
license: MIT
retrieved_at: '2026-09-15'
section: library-machine
order: 380
---

# class SD -- secure digital memory card (cc3200 port only)

> [!WARNING]
> This is a non-standard class and is only available on the cc3200 port.

The SD card class allows to configure and enable the memory card module of the WiPy and automatically mount it as `/sd` as part of the file system. There are several pin combinations that can be used to wire the SD card socket to the WiPy and the pins used can be specified in the constructor. Please check the [pinout and alternate functions table.](https://raw.githubusercontent.com/wipy/wipy/master/docs/PinOUT.png) for more info regarding the pins which can be remapped to be used with a SD card.

Example usage:

    from machine import SD
    import vfs
    # clk cmd and dat0 pins must be passed along with
    # their respective alternate functions
    sd = machine.SD(pins=('GP10', 'GP11', 'GP15'))
    vfs.mount(sd, '/sd')
    # do normal file operations

## Constructors

Create a SD card object. See `init()` for parameters if initialization.

## Methods

SD.init(id=0, pins=('GP10', 'GP11', 'GP15'))

Enable the SD card. In order to initialize the card, give it a 3-tuple: `(clk_pin, cmd_pin, dat0_pin)`.

SD.deinit()

Disable the SD card.
