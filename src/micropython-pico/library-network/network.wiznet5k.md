---
title: WIZNET5K
description: control WIZnet5x00 Ethernet modules
source_url: https://docs.micropython.org/en/latest/library/network.WIZNET5K.html
source_repo: https://github.com/micropython/micropython.git
source_ref: master
source_commit: 52b5fbcb4
source_path: library/network.WIZNET5K.rst
technology: micropython-pico
version: master
license: MIT
retrieved_at: '2026-09-15'
section: library-network
order: 570
---

# class WIZNET5K -- control WIZnet5x00 Ethernet modules

This class allows you to control WIZnet5x00 Ethernet adaptors based on the W5200 and W5500 chipsets. The particular chipset that is supported by the firmware is selected at compile-time via the MICROPY_PY_NETWORK_WIZNET5K option.

> [!NOTE]
> The esp32 port also supports WIZnet W5500 chipsets, but this port uses the `network.LAN interface <esp32_spi_ethernet>`.

Example usage:

    import network
    nic = network.WIZNET5K(pyb.SPI(1), pyb.Pin.board.X5, pyb.Pin.board.X4)
    print(nic.ipconfig("addr4"))

    # now use socket as usual
    ...

For this example to work the WIZnet5x00 module must have the following connections:

> - MOSI connected to X8
> - MISO connected to X7
> - SCLK connected to X6
> - nSS connected to X5
> - nRESET connected to X4

It is possible to use other SPI buses and other pins for nSS and nRESET.

## Constructors

Create a WIZNET5K driver object, initialise the WIZnet5x00 module using the given SPI bus and pins, and return the WIZNET5K object.

Arguments are:

> - *spi* is an `SPI object <pyb.SPI>` which is the SPI bus that the WIZnet5x00 is connected to (the MOSI, MISO and SCLK pins).
> - *pin_cs* is a `Pin object <pyb.Pin>` which is connected to the WIZnet5x00 nSS pin.
> - *pin_rst* is a `Pin object <pyb.Pin>` which is connected to the WIZnet5x00 nRESET pin.

All of these objects will be initialised by the driver, so there is no need to initialise them yourself. For example, you can use:

    nic = network.WIZNET5K(pyb.SPI(1), pyb.Pin.board.X5, pyb.Pin.board.X4)

## Methods

This class implements most methods from `AbstractNIC \<AbstractNIC\>`, which are documented there. Additional methods are:

WIZNET5K.regs()

Dump the WIZnet5x00 registers. Useful for debugging.
