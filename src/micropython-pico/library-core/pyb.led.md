---
title: LED
description: LED object
source_url: https://docs.micropython.org/en/latest/library/pyb.LED.html
source_repo: https://github.com/micropython/micropython.git
source_ref: master
source_commit: 52b5fbcb4
source_path: library/pyb.LED.rst
technology: micropython-pico
version: master
license: MIT
retrieved_at: '2026-09-15'
section: library-core
order: 720
---

# class LED -- LED object

The LED object controls an individual LED (Light Emitting Diode).

## Constructors

Create an LED object associated with the given LED:

> - `id` is the LED number, 1-4.

## Methods

LED.intensity(\[value\])

Get or set the LED intensity. Intensity ranges between 0 (off) and 255 (full on). If no argument is given, return the LED intensity. If an argument is given, set the LED intensity and return `None`.

*Note:* Only LED(3) and LED(4) can have a smoothly varying intensity, and they use timer PWM to implement it. LED(3) uses Timer(2) and LED(4) uses Timer(3). These timers are only configured for PWM if the intensity of the relevant LED is set to a value between 1 and 254. Otherwise the timers are free for general purpose use.

LED.off()

Turn the LED off.

LED.on()

Turn the LED on, to maximum intensity.

LED.toggle()

Toggle the LED between on (maximum intensity) and off. If the LED is at non-zero intensity then it is considered "on" and toggle will turn it off.
