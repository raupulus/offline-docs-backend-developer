---
title: RTC
description: real time clock
source_url: https://docs.micropython.org/en/latest/library/machine.RTC.html
source_repo: https://github.com/micropython/micropython.git
source_ref: master
source_commit: 52b5fbcb4
source_path: library/machine.RTC.rst
technology: micropython-pico
version: master
license: MIT
retrieved_at: '2026-09-15'
section: library-machine
order: 370
---

# class RTC -- real time clock

The RTC is an independent clock that keeps track of the date and time.

Example usage:

    rtc = machine.RTC()
    rtc.datetime((2020, 1, 21, 2, 10, 32, 36, 0))
    print(rtc.datetime())

Availability: **Alif, ESP32, ESP8266, MIMXRT, Renesas-RA, RP2, SAMD, STM32**

## Constructors

Create an RTC object. See init for parameters of initialization.

## Methods

RTC.datetime(\[datetimetuple\])

Get or set the date and time of the RTC.

With no arguments, this method returns an 8-tuple with the current date and time. With 1 argument (being an 8-tuple) it sets the date and time.

The 8-tuple has the following format:

> (year, month, day, weekday, hours, minutes, seconds, subseconds)

The meaning of the `subseconds` field is hardware dependent.

RTC.init(datetime)

Initialise the RTC. Datetime is a tuple of the form:

> `(year, month, day, hour, minute, second, microsecond, tzinfo)`

All eight arguments must be present. The `microsecond` and `tzinfo` values are currently ignored but might be used in the future.

Availability: CC3200, ESP32, MIMXRT, SAMD. The rtc.init() method on the stm32 and renesas-ra ports just (re-)starts the RTC and does not accept arguments.

RTC.now()

Get get the current datetime tuple.

Availability: WiPy.

RTC.deinit()

Resets the RTC to the time of January 1, 2015 and starts running it again.

RTC.alarm(id, time, \*, repeat=False)

Set the RTC alarm. Time might be either a millisecond value to program the alarm to current time + time_in_ms in the future, or a datetimetuple. If the time passed is in milliseconds, repeat can be set to `True` to make the alarm periodic.

RTC.alarm_left(alarm_id=0)

Get the number of milliseconds left before the alarm expires.

RTC.alarm_cancel(alarm_id=0)

Cancel a running alarm.

The mimxrt port also exposes this function as `RTC.cancel(alarm_id=0)`, but this is scheduled to be removed in MicroPython 2.0.

RTC.irq(\*, trigger, handler=None, wake=machine.IDLE)

Create an irq object triggered by a real time clock alarm.

> - `trigger` must be `RTC.ALARM0`
> - `handler` is the function to be called when the callback is triggered.
> - `wake` specifies the sleep mode from where this interrupt can wake up the system.

RTC.memory(\[data\])

`RTC.memory(data)` will write *data* to the RTC memory, where *data* is any object which supports the buffer protocol (including `bytes`, `bytearray`, `memoryview` and `array.array`). `RTC.memory()` reads RTC memory and returns a `bytes` object.

Data written to RTC user memory is persistent across restarts, including `soft_reset` and `machine.deepsleep()`.

The maximum length of RTC user memory is 2048 bytes by default on esp32, and 492 bytes on esp8266.

Availability: esp32, esp8266 ports.

> [!NOTE]
> For cross-port persistent storage, see `machine.mem_backup` which is available on more ports and provides direct memoryview access.

> [!WARNING]
> On esp32, `RTC.memory()` and `machine.mem_backup` share the same backing buffer but track length independently. Writes through one API are not reflected in the length seen by the other. Avoid mixing the two in the same application.

## Constants

RTC.ALARM0

irq trigger source
