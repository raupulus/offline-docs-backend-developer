---
title: Display
description: access to Zephyr Displays
source_url: https://docs.micropython.org/en/latest/library/zephyr.Display.html
source_repo: https://github.com/micropython/micropython.git
source_ref: master
source_commit: 52b5fbcb4
source_path: library/zephyr.Display.rst
technology: micropython-pico
version: master
license: MIT
retrieved_at: '2026-09-15'
section: library-core
order: 1040
---

# class Display -- access to Zephyr Displays

Uses the [Zephyr Display API](https://docs.zephyrproject.org/latest/doxygen/html/group__display__interface.html).

This class allows access to Zephyr-provided Displays ([zephyr,display chosen Node](https://docs.zephyrproject.org/latest/build/dts/api/api.html#zephyr-specific-chosen-nodes) and [zephyr,displays Node](https://docs.zephyrproject.org/latest/build/dts/api/bindings/display/zephyr%2Cdisplays.html)) via an API reproducing the Zephyr one.

## Constructors

Gets an object for accessing a Display identified by `id`.

`id` can be an integer (`0`, `1`...) or a string (`"ssd1306@3c"`) identifying a display node by its position or by its node identifiers.

## Methods

Display.write(buf\[, x\[, y\[, size_x\[, size_y\]\]\]\])

Write a buffer-protocol object in the Display's Pixel Format to the display.

Optionally x and y position, x size, and y size can be specified.

Display.rgb(r, g, b)

Convert a RGB color to the Display's Pixel Format.

Display.capabilities()

Retrieve a tuple describing the display in the format:

`(X Size, Y Size, Supported PFs, Current PF, Current Orientation, Misc Characteristics, Current PF as framebuf format)`

Display.format(\[format\])

Get and set the Pixel Format of the Display.

Display.blanking(value)

Enable or disable blanking.

Display.clear()

Clear the Display.

Display.set_brightness(value)

Set the Display's brightness from `0` to `255`.

Display.set_contrast(value)

Set the Display's contrast from `0` to `255`.

Display.orientation(\[orientation\])

Get and set the Orientation of the Display.

Display.as_framebuf()

If `framebuf` is enabled, generate a `framebuf.FrameBuffer` instance augmented with a `show()` function that directly maps to the display with the currently configured settings.
