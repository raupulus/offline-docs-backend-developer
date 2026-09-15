---
title: USB_HID
description: USB Human Interface Device (HID)
source_url: https://docs.micropython.org/en/latest/library/pyb.USB_HID.html
source_repo: https://github.com/micropython/micropython.git
source_ref: master
source_commit: 52b5fbcb4
source_path: library/pyb.USB_HID.rst
technology: micropython-pico
version: master
license: MIT
retrieved_at: '2026-09-15'
section: library-core
order: 800
---

# class USB_HID -- USB Human Interface Device (HID)

The USB_HID class allows creation of an object representing the USB Human Interface Device (HID) interface. It can be used to emulate a peripheral such as a mouse or keyboard.

Before you can use this class, you need to use `pyb.usb_mode()` to set the USB mode to include the HID interface.

## Constructors

Create a new USB_HID object.

## Methods

USB_HID.recv(data, \*, timeout=5000)

Receive data on the bus:

> - `data` can be an integer, which is the number of bytes to receive, or a mutable buffer, which will be filled with received bytes.
> - `timeout` is the timeout in milliseconds to wait for the receive.

Return value: if `data` is an integer then a new buffer of the bytes received, otherwise the number of bytes read into `data` is returned.

USB_HID.send(data)

Send data over the USB HID interface:

> - `data` is the data to send (a tuple/list of integers, or a bytearray).
