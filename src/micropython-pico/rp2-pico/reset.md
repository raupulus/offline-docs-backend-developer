---
title: Factory reset
source_url: https://docs.micropython.org/en/latest/rp2/tutorial/reset.html
source_repo: https://github.com/micropython/micropython.git
source_ref: master
source_commit: 52b5fbcb4
source_path: rp2/tutorial/reset.rst
technology: micropython-pico
version: master
license: MIT
retrieved_at: '2026-09-15'
section: rp2-pico
order: 1430
---

# Factory reset

If something unexpected happens and your RP2xxx-based board no longer boots MicroPython, then you may have to factory reset it. For more details, see `soft_bricking`.

Factory resetting the MicroPython rp2 port involves fully erasing the flash and resetting the flash memory, so you will need to re-flash the MicroPython firmware afterwards and copy any Python files to the filesystem again.

1.  Follow the instructions on the Raspberry Pi website for [resetting flash memory](https://www.raspberrypi.com/documentation/microcontrollers/pico-series.html#resetting-flash-memory).
2.  Copy the MicroPython .uf2 firmware file to your board. If needed, this file can be found on the [MicroPython downloads page](https://micropython.org/download/?port=rp2).
