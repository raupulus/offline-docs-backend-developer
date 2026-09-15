---
title: ADCBlock
description: control ADC peripherals
source_url: https://docs.micropython.org/en/latest/library/machine.ADCBlock.html
source_repo: https://github.com/micropython/micropython.git
source_ref: master
source_commit: 52b5fbcb4
source_path: library/machine.ADCBlock.rst
technology: micropython-pico
version: master
license: MIT
retrieved_at: '2026-09-15'
section: library-machine
order: 260
---

# class ADCBlock -- control ADC peripherals

The ADCBlock class provides access to an ADC peripheral which has a number of channels that can be used to sample analog values. It allows finer control over configuration of `machine.ADC <machine.ADC>` objects, which do the actual sampling.

This class is not always available.

Example usage:

    from machine import ADCBlock

    block = ADCBlock(id, bits=12)  # create an ADCBlock with 12-bit resolution
    adc = block.connect(4, pin)    # connect channel 4 to the given pin
    val = adc.read_uv()            # read an analog value

## Constructors

Access the ADC peripheral identified by *id*, which may be an integer or string.

The *bits* argument, if given, sets the resolution in bits of the conversion process. If not specified then the previous or default resolution is used.

## Methods

ADCBlock.init(\*, bits)

Configure the ADC peripheral. *bits* will set the resolution of the conversion process.

ADCBlock.connect(channel, *, ...) ADCBlock.connect(source,*, ...) ADCBlock.connect(channel, source, \*, ...)

Connect up a channel on the ADC peripheral so it is ready for sampling, and return an `ADC <machine.ADC>` object that represents that connection.

The *channel* argument must be an integer, and *source* must be an object (for example a `Pin <machine.Pin>`) which can be connected up for sampling.

If only *channel* is given then it is configured for sampling.

If only *source* is given then that object is connected to a default channel ready for sampling.

If both *channel* and *source* are given then they are connected together and made ready for sampling.

Any additional keyword arguments are used to configure the returned ADC object, via its `init <machine.ADC.init>` method.
