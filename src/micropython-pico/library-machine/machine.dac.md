---
title: DAC
description: digital to analog conversion
source_url: https://docs.micropython.org/en/latest/library/machine.DAC.html
source_repo: https://github.com/micropython/micropython.git
source_ref: master
source_commit: 52b5fbcb4
source_path: library/machine.DAC.rst
technology: micropython-pico
version: master
license: MIT
retrieved_at: '2026-09-15'
section: library-machine
order: 300
---

# class DAC -- digital to analog conversion

The DAC is used to output an analog voltage based on a digital value.

The output voltage will be between 0 and 3.3V.

DAC is currently supported on ESP32[^1], SAMD and Renesas RA.

> [!NOTE]
> The STM32 port has similar functionality to `machine.DAC`. See `pyb.DAC <pyb.DAC>` for details.

Example usage (ESP32):

    from machine import DAC

    dac = DAC(pin)    # create a DAC object acting on a pin
    dac.write(128)    # write a value to the DAC
    dac.write(255)    # output maximum value, 3.3V

## Constructors

Construct a new DAC object.

`id` is a pin object (ESP32 and Renesas RA) or an index to a DAC resource (SAMD).

> [!NOTE]
> On the ESP32, DAC functionality is available on pins 25 and 26. On the ESP32-S2, pins 17 and 18. See `ESP32 Quickref <esp32_quickref>` for more details.

> [!NOTE]
> SAMD21 has one DAC resource, SAMD51 has two. See `SAMD Quickref <samd_quickref>` for more details.

## Methods

DAC.write(value)

Output an analog voltage to the pin connected to the DAC.

`value` is a representation of the desired output; a linear interpolation of 0-3.3V, though the range differs depending on the port and micro, see below:

| *Port/micro* | Bits | Range  |
|--------------|------|--------|
| ESP32        | 8    | 0-255  |
| SAMD21       | 10   | 0-1023 |
| SAMD51       | 12   | 0-4095 |
| Renesas RA   | 12   | 0-4095 |

**Footnotes**

[^1]: The original ESP32 and ESP32-S2 *only*, since DAC hardware is not present on other microcontrollers in the family.
