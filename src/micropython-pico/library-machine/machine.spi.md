---
title: SPI
description: a Serial Peripheral Interface bus protocol (controller side)
source_url: https://docs.micropython.org/en/latest/library/machine.SPI.html
source_repo: https://github.com/micropython/micropython.git
source_ref: master
source_commit: 52b5fbcb4
source_path: library/machine.SPI.rst
technology: micropython-pico
version: master
license: MIT
retrieved_at: '2026-09-15'
section: library-machine
order: 400
---

# class SPI -- a Serial Peripheral Interface bus protocol (controller side)

SPI is a synchronous serial protocol that is driven by a controller. At the physical level, a bus consists of 3 lines: SCK, MOSI, MISO. Multiple devices can share the same bus. Each device should have a separate, 4th signal, CS (Chip Select), to select a particular device on a bus with which communication takes place. Management of a CS signal should happen in user code (via machine.Pin class).

Both hardware and software SPI implementations exist via the `machine.SPI <machine.SPI>` and `machine.SoftSPI` classes. Hardware SPI uses underlying hardware support of the system to perform the reads/writes and is usually efficient and fast but may have restrictions on which pins can be used. Software SPI is implemented by bit-banging and can be used on any pin but is not as efficient. These classes have the same methods available and differ primarily in the way they are constructed.

Example usage:

    from machine import SPI, Pin

    spi = SPI(0, baudrate=400000)           # Create SPI peripheral 0 at frequency of 400kHz.
                                            # Depending on the use case, extra parameters may be required
                                            # to select the bus characteristics and/or pins to use.
    cs = Pin(4, mode=Pin.OUT, value=1)      # Create chip-select on pin 4.

    try:
        cs(0)                               # Select peripheral.
        spi.write(b"12345678")              # Write 8 bytes, and don't care about received data.
    finally:
        cs(1)                               # Deselect peripheral.

    try:
        cs(0)                               # Select peripheral.
        rxdata = spi.read(8, 0x42)          # Read 8 bytes while writing 0x42 for each byte.
    finally:
        cs(1)                               # Deselect peripheral.

    rxdata = bytearray(8)
    try:
        cs(0)                               # Select peripheral.
        spi.readinto(rxdata, 0x42)          # Read 8 bytes inplace while writing 0x42 for each byte.
    finally:
        cs(1)                               # Deselect peripheral.

    txdata = b"12345678"
    rxdata = bytearray(len(txdata))
    try:
        cs(0)                               # Select peripheral.
        spi.write_readinto(txdata, rxdata)  # Simultaneously write and read bytes.
    finally:
        cs(1)                               # Deselect peripheral.

## Constructors

Construct an SPI object on the given bus, *id*. Values of *id* depend on a particular port and its hardware. Values 0, 1, etc. are commonly used to select hardware SPI block \#0, \#1, etc.

With no additional parameters, the SPI object is created but not initialised (it has the settings from the last initialisation of the bus, if any). If extra arguments are given, the bus is initialised. See `init` for parameters of initialisation.

> Construct a new software SPI object. Additional parameters must be given, usually at least *sck*, *mosi* and *miso*, and these are used to initialise the bus. See `SPI.init` for a description of the parameters.

## Methods

SPI.init(baudrate=1000000, \*, polarity=0, phase=0, bits=8, firstbit=SPI.MSB, sck=None, mosi=None, miso=None, pins=(SCK, MOSI, MISO))

Initialise the SPI bus with the given parameters:

> - `baudrate` is the SCK clock rate.
> - `polarity` can be 0 or 1, and is the level the idle clock line sits at.
> - `phase` can be 0 or 1 to sample data on the first or second clock edge respectively.
> - `bits` is the width in bits of each transfer. Only 8 is guaranteed to be supported by all hardware.
> - `firstbit` can be `SPI.MSB` or `SPI.LSB`.
> - `sck`, `mosi`, `miso` are pins (machine.Pin) objects to use for bus signals. For most hardware SPI blocks (as selected by `id` parameter to the constructor), pins are fixed and cannot be changed. In some cases, hardware blocks allow 2-3 alternative pin sets for a hardware SPI block. Arbitrary pin assignments are possible only for a bitbanging SPI driver (`id` = -1).
> - `pins` - WiPy port doesn't `sck`, `mosi`, `miso` arguments, and instead allows to specify them as a tuple of `pins` parameter.

In the case of hardware SPI the actual clock frequency may be lower than the requested baudrate. This is dependent on the platform hardware. The actual rate may be determined by printing the SPI object.

SPI.deinit()

Turn off the SPI bus.

SPI.read(nbytes, write=0x00)

Read a number of bytes specified by `nbytes` while continuously writing the single byte given by `write`. Returns a `bytes` object with the data that was read.

SPI.readinto(buf, write=0x00)

Read into the buffer specified by `buf` while continuously writing the single byte given by `write`. Returns `None`.

Note: on WiPy this function returns the number of bytes read.

SPI.write(buf)

Write the bytes contained in `buf`. Returns `None`.

Note: on WiPy this function returns the number of bytes written.

SPI.write_readinto(write_buf, read_buf)

Write the bytes from `write_buf` while reading into `read_buf`. The buffers can be the same or different, but both buffers must have the same length. Returns `None`.

Note: on WiPy this function returns the number of bytes written.

## Constants

SPI.CONTROLLER

for initialising the SPI bus to controller; this is only used for the WiPy

SPI.MSB SoftSPI.MSB

set the first bit to be the most significant bit

SPI.LSB SoftSPI.LSB

set the first bit to be the least significant bit
