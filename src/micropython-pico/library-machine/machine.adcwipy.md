---
title: ADCWiPy
description: analog to digital conversion
source_url: https://docs.micropython.org/en/latest/library/machine.ADCWiPy.html
source_repo: https://github.com/micropython/micropython.git
source_ref: master
source_commit: 52b5fbcb4
source_path: library/machine.ADCWiPy.rst
technology: micropython-pico
version: master
license: MIT
retrieved_at: '2026-09-15'
section: library-machine
order: 270
---

# class ADCWiPy -- analog to digital conversion

> [!NOTE]
> This class is a non-standard ADC implementation for the WiPy. It is available simply as `machine.ADC` on the WiPy but is named in the documentation below as `machine.ADCWiPy` to distinguish it from the more general `machine.ADC <machine.ADC>` class.

Usage:

    import machine

    adc = machine.ADC()             # create an ADC object
    apin = adc.channel(pin='GP3')   # create an analog pin on GP3
    val = apin()                    # read an analog value

## Constructors

Create an ADC object associated with the given pin. This allows you to then read analog values on that pin. For more info check the [pinout and alternate functions table.](https://raw.githubusercontent.com/wipy/wipy/master/docs/PinOUT.png)

> [!WARNING]
> ADC pin input range is 0-1.4V (being 1.8V the absolute maximum that it can withstand). When GP2, GP3, GP4 or GP5 are remapped to the ADC block, 1.8 V is the maximum. If these pins are used in digital mode, then the maximum allowed input is 3.6V.

## Methods

ADCWiPy.channel(id, \*, pin)

Create an analog pin. If only channel ID is given, the correct pin will be selected. Alternatively, only the pin can be passed and the correct channel will be selected. Examples:

    # all of these are equivalent and enable ADC channel 1 on GP3
    apin = adc.channel(1)
    apin = adc.channel(pin='GP3')
    apin = adc.channel(id=1, pin='GP3')

ADCWiPy.init()

Enable the ADC block.

ADCWiPy.deinit()

Disable the ADC block.

# class ADCChannel --- read analog values from internal or external sources

ADC channels can be connected to internal points of the MCU or to GPIO pins. ADC channels are created using the ADC.channel method.

adcchannel()

Fast method to read the channel value.

adcchannel.value()

Read the channel value.

adcchannel.init()

Re-init (and effectively enable) the ADC channel.

adcchannel.deinit()

Disable the ADC channel.
