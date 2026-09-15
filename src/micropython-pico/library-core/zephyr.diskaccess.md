---
title: DiskAccess
description: access to disk storage
source_url: https://docs.micropython.org/en/latest/library/zephyr.DiskAccess.html
source_repo: https://github.com/micropython/micropython.git
source_ref: master
source_commit: 52b5fbcb4
source_path: library/zephyr.DiskAccess.rst
technology: micropython-pico
version: master
license: MIT
retrieved_at: '2026-09-15'
section: library-core
order: 1030
---

# class DiskAccess -- access to disk storage

Uses [Zephyr Disk Access API](https://docs.zephyrproject.org/latest/reference/storage/disk/access.html).

This class allows access to storage devices on the board, such as support for SD card controllers and interfacing with SD cards via SPI. Disk devices are automatically detected and initialized on boot using Zephyr devicetree data.

The Zephyr disk access class enables the transfer of data between a disk device and an accessible memory buffer given a disk name, buffer, starting disk block, and number of sectors to read. MicroPython reads as many blocks as necessary to fill the buffer, so the number of sectors to read is found by dividing the buffer length by block size of the disk.

## Constructors

Gets an object for accessing disk memory of the specific disk. For accessing an SD card on the mimxrt1050_evk, `disk_name` would be `SDHC`. See board documentation and devicetree for usable disk names for your board (ex. RT boards use style USDHC#).

## Methods

DiskAccess.readblocks(block_num, buf) DiskAccess.readblocks(block_num, buf, offset)

DiskAccess.writeblocks(block_num, buf) DiskAccess.writeblocks(block_num, buf, offset)

DiskAccess.ioctl(cmd, arg)

These methods implement the simple and extended `block protocol <block-device-interface>` defined by `vfs.AbstractBlockDev`.
