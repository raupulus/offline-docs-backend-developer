---
title: Accel
description: accelerometer control
source_url: https://docs.micropython.org/en/latest/library/pyb.Accel.html
source_repo: https://github.com/micropython/micropython.git
source_ref: master
source_commit: 52b5fbcb4
source_path: library/pyb.Accel.rst
technology: micropython-pico
version: master
license: MIT
retrieved_at: '2026-09-15'
section: library-core
order: 650
---

# class Accel -- accelerometer control

Accel is an object that controls the accelerometer. Example usage:

    accel = pyb.Accel()
    for i in range(10):
        print(accel.x(), accel.y(), accel.z())

Raw values are between -32 and 31.

## Constructors

Create and return an accelerometer object.

## Methods

Accel.filtered_xyz()

Get a 3-tuple of filtered x, y and z values.

Implementation note: this method is currently implemented as taking the sum of 4 samples, sampled from the 3 previous calls to this function along with the sample from the current call. Returned values are therefore 4 times the size of what they would be from the raw x(), y() and z() calls.

Accel.tilt()

Get the tilt register.

Accel.x()

Get the x-axis value.

Accel.y()

Get the y-axis value.

Accel.z()

Get the z-axis value.

## Hardware Note

The accelerometer uses I2C bus 1 to communicate with the processor. Consequently when readings are being taken pins X9 and X10 should be unused (other than for I2C). Other devices using those pins, and which therefore cannot be used concurrently, are UART 1 and Timer 4 channels 1 and 2.
