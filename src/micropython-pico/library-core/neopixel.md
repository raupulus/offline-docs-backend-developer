---
title: '`neopixel`'
description: control of WS2812 / NeoPixel LEDs
source_url: https://docs.micropython.org/en/latest/library/neopixel.html
source_repo: https://github.com/micropython/micropython.git
source_ref: master
source_commit: 52b5fbcb4
source_path: library/neopixel.rst
technology: micropython-pico
version: master
license: MIT
retrieved_at: '2026-09-15'
section: library-core
order: 530
---

# `neopixel` --- control of WS2812 / NeoPixel LEDs

neopixel

This module provides a driver for WS2818 / NeoPixel LEDs.

> [!NOTE]
> This module is only included by default on the ESP8266, ESP32 and RP2 ports. On STM32 / Pyboard and others, you can either install the `neopixel` package using `mip`, or you can download the module directly from `micropython-lib` and copy it to the filesystem.

## class NeoPixel

This class stores pixel data for a WS2812 LED strip connected to a pin. The application should set pixel data and then call `NeoPixel.write` when it is ready to update the strip.

For example:

    import neopixel

    # 32 LED strip connected to X8.
    p = machine.Pin.board.X8
    n = neopixel.NeoPixel(p, 32)

    # Draw a red gradient.
    for i in range(32):
        n[i] = (i * 8, 0, 0)

    # Update the strip.
    n.write()

## Constructors

Construct an NeoPixel object. The parameters are:

> - *pin* is a machine.Pin instance.
> - *n* is the number of LEDs in the strip.
> - *bpp* is 3 for RGB LEDs, and 4 for RGBW LEDs.
> - *timing* is 0 for 400KHz, and 1 for 800kHz LEDs (most are 800kHz). You may also supply a timing tuple as accepted by `machine.bitstream()`.

## Pixel access methods

NeoPixel.fill(pixel)

Sets the value of all pixels to the specified *pixel* value (i.e. an RGB/RGBW tuple).

NeoPixel.\_\_len\_\_()

Returns the number of LEDs in the strip.

NeoPixel.\_\_setitem\_\_(index, val)

Set the pixel at *index* to the value, which is an RGB/RGBW tuple.

NeoPixel.\_\_getitem\_\_(index)

Returns the pixel at *index* as an RGB/RGBW tuple.

## Output methods

NeoPixel.write()

Writes the current pixel data to the strip.
