---
title: WDT
description: watchdog timer
source_url: https://docs.micropython.org/en/latest/library/machine.WDT.html
source_repo: https://github.com/micropython/micropython.git
source_ref: master
source_commit: 52b5fbcb4
source_path: library/machine.WDT.rst
technology: micropython-pico
version: master
license: MIT
retrieved_at: '2026-09-15'
section: library-machine
order: 460
---

# class WDT -- watchdog timer

The WDT is used to restart the system when the application crashes and ends up into a non recoverable state. Once started it cannot be stopped or reconfigured in any way. After enabling, the application must "feed" the watchdog periodically to prevent it from expiring and resetting the system.

Example usage:

    from machine import WDT
    wdt = WDT(timeout=2000)  # enable it with a timeout of 2s
    wdt.feed()

Availability: **Alif, ESP32, ESP8266, MIMXRT, RP2, SAMD, STM32, Zephyr**

## Constructors

Create a WDT object and start it. The timeout must be given in milliseconds. Once it is running the timeout cannot be changed and the WDT cannot be stopped either.

Notes:

- On the alif port the HP and HE cores have independent watchdogs, both accessed by the default `id=0`. The maximum timeout on the HP core is 10737ms. The watchdog does not run during deepsleep.
- On the esp8266 port a timeout cannot be specified, it is determined by the underlying system.
- On rp2040 devices the maximum timeout is 8388 ms.
- On the stm32 port the default `id=0` is the IWDG, which can also be specified by an id of `"IWDG"`. Use an id of `"WWDG"` to access the WWDG peripheral. For dual-core STM32H7 MCUs there are also `"IWDG2"` and `"WWDG2"`. The WWDG has a very limited maximum timeout across all MCUs, of around 100ms (but it depends heavily on the APB clock).

## Methods

WDT.feed()

Feed the WDT to prevent it from resetting the system. The application should place this call in a sensible place ensuring that the WDT is only fed after verifying that everything is functioning correctly.
