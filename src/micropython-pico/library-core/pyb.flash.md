---
title: Flash
description: access to built-in flash storage
source_url: https://docs.micropython.org/en/latest/library/pyb.Flash.html
source_repo: https://github.com/micropython/micropython.git
source_ref: master
source_commit: 52b5fbcb4
source_path: library/pyb.Flash.rst
technology: micropython-pico
version: master
license: MIT
retrieved_at: '2026-09-15'
section: library-core
order: 690
---

# class Flash -- access to built-in flash storage

The Flash class allows direct access to the primary flash device on the pyboard.

In most cases, to store persistent data on the device, you'll want to use a higher-level abstraction, for example the filesystem via Python's standard file API, but this interface is useful to `customise the filesystem
configuration <filesystem>` or implement a low-level storage system for your application.

## Constructors

Create and return a block device that represents the flash device presented to the USB mass storage interface.

It includes a virtual partition table at the start, and the actual flash starts at block `0x100`.

This constructor is deprecated and will be removed in a future version of MicroPython.

Create and return a block device that accesses the flash at the specified offset. The length defaults to the remaining size of the device.

The *start* and *len* offsets are in bytes, and must be a multiple of the block size (typically 512 for internal flash).

## Methods

Flash.readblocks(block_num, buf) Flash.readblocks(block_num, buf, offset)

Flash.writeblocks(block_num, buf) Flash.writeblocks(block_num, buf, offset)

Flash.ioctl(cmd, arg)

These methods implement the simple and `extended
<block-device-interface>` block protocol defined by `vfs.AbstractBlockDev`.

## Hardware Note

On boards with external spiflash (e.g. Pyboard D), the MicroPython firmware will be configured to use that as the primary flash storage. On all other boards, the internal flash inside the `MCU` will be used.
