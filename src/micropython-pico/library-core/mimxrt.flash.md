---
title: Flash
description: access to built-in flash storage
source_url: https://docs.micropython.org/en/latest/library/mimxrt.Flash.html
source_repo: https://github.com/micropython/micropython.git
source_ref: master
source_commit: 52b5fbcb4
source_path: library/mimxrt.Flash.rst
technology: micropython-pico
version: master
license: MIT
retrieved_at: '2026-09-15'
section: library-core
order: 510
---

# class Flash -- access to built-in flash storage

This class gives access to the SPI flash memory.

In most cases, to store persistent data on the device, you'll want to use a higher-level abstraction, for example the filesystem via Python's standard file API, but this interface is useful to `customise the filesystem
configuration <filesystem>` or implement a low-level storage system for your application.

## Constructors

Gets the singleton object for accessing the SPI flash memory.

## Methods

Flash.readblocks(block_num, buf) Flash.readblocks(block_num, buf, offset)

Flash.writeblocks(block_num, buf) Flash.writeblocks(block_num, buf, offset)

Flash.ioctl(cmd, arg)

These methods implement the simple and extended `block protocol <block-device-interface>` defined by `vfs.AbstractBlockDev`.

The block size can be queried by calling `ioctl(5, 0)`. Block numbers are relative to the start of the user flash storage area, not the physical start of flash memory.
