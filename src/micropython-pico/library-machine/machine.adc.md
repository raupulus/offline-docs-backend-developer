---
title: ADC
description: analog to digital conversion
source_url: https://docs.micropython.org/en/latest/library/machine.ADC.html
source_repo: https://github.com/micropython/micropython.git
source_ref: master
source_commit: 52b5fbcb4
source_path: library/machine.ADC.rst
technology: micropython-pico
version: master
license: MIT
retrieved_at: '2026-09-15'
section: library-machine
order: 250
---

# class ADC -- analog to digital conversion

The ADC class provides an interface to analog-to-digital converters, and represents a single endpoint that can sample a continuous voltage and convert it to a discretised value.

For extra control over ADC sampling see `machine.ADCBlock <machine.ADCBlock>`.

Example usage:

    from machine import ADC

    adc = ADC(pin)        # create an ADC object acting on a pin
    val = adc.read_u16()  # read a raw analog value in the range 0-65535
    val = adc.read_uv()   # read an analog value in microvolts

## Constructors

Access the ADC associated with a source identified by *id*. This *id* may be an integer (usually specifying a channel number), a `Pin <machine.Pin>` object, or other value supported by the underlying machine.

If additional keyword-arguments are given then they will configure various aspects of the ADC. If not given, these settings will take previous or default values. The settings are:

> - *sample_ns* is the sampling time in nanoseconds.
> - *atten* specifies the input attenuation.

## Methods

ADC.init(\*, sample_ns, atten)

Apply the given settings to the ADC. Only those arguments that are specified will be changed. See the ADC constructor above for what the arguments are.

ADC.block()

Return the `ADCBlock <machine.ADCBlock>` instance associated with this ADC object.

This method only exists if the port supports the `ADCBlock <machine.ADCBlock>` class.

ADC.read_u16()

Take an analog reading and return an integer in the range 0-65535. The return value represents the raw reading taken by the ADC, scaled such that the minimum value is 0 and the maximum value is 65535.

ADC.read_uv()

Take an analog reading and return an integer value with units of microvolts. It is up to the particular port whether or not this value is calibrated, and how calibration is done.
