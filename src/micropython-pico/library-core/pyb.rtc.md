---
title: RTC
description: real time clock
source_url: https://docs.micropython.org/en/latest/library/pyb.RTC.html
source_repo: https://github.com/micropython/micropython.git
source_ref: master
source_commit: 52b5fbcb4
source_path: library/pyb.RTC.rst
technology: micropython-pico
version: master
license: MIT
retrieved_at: '2026-09-15'
section: library-core
order: 740
---

# class RTC -- real time clock

The RTC is an independent clock that keeps track of the date and time.

Example usage:

    rtc = pyb.RTC()
    rtc.datetime((2014, 5, 1, 4, 13, 0, 0, 0))
    print(rtc.datetime())

## Constructors

Create an RTC object.

## Methods

RTC.datetime(\[datetimetuple\])

Get or set the date and time of the RTC.

With no arguments, this method returns an 8-tuple with the current date and time. With 1 argument (being an 8-tuple) it sets the date and time (and `subseconds` is reset to 255).

The 8-tuple has the following format:

> (year, month, day, weekday, hours, minutes, seconds, subseconds)

`weekday` is 1-7 for Monday through Sunday.

`subseconds` counts down from 255 to 0

RTC.wakeup(timeout, callback=None)

Set the RTC wakeup timer to trigger repeatedly at every `timeout` milliseconds. This trigger can wake the pyboard from both the sleep states: `pyb.stop` and `pyb.standby`.

If `timeout` is `None` then the wakeup timer is disabled.

If `callback` is given then it is executed at every trigger of the wakeup timer. `callback` must take exactly one argument.

RTC.info()

Get information about the startup time and reset source.

> - The lower 0xffff are the number of milliseconds the RTC took to start up.
> - Bit 0x10000 is set if a power-on reset occurred.
> - Bit 0x20000 is set if an external reset occurred

RTC.calibration(cal)

Get or set RTC calibration.

With no arguments, `calibration()` returns the current calibration value, which is an integer in the range \[-511 : 512\]. With one argument it sets the RTC calibration.

The RTC Smooth Calibration mechanism adjusts the RTC clock rate by adding or subtracting the given number of ticks from the 32768 Hz clock over a 32 second period (corresponding to 2^20 clock ticks.) Each tick added will speed up the clock by 1 part in 2^20, or 0.954 ppm; likewise the RTC clock it slowed by negative values. The usable calibration range is: (-511 \* 0.954) ~= -487.5 ppm up to (512 \* 0.954) ~= 488.5 ppm
