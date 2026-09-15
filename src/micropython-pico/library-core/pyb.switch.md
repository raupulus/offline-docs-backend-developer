---
title: Switch
description: switch object
source_url: https://docs.micropython.org/en/latest/library/pyb.Switch.html
source_repo: https://github.com/micropython/micropython.git
source_ref: master
source_commit: 52b5fbcb4
source_path: library/pyb.Switch.rst
technology: micropython-pico
version: master
license: MIT
retrieved_at: '2026-09-15'
section: library-core
order: 770
---

# class Switch -- switch object

A Switch object is used to control a push-button switch.

Usage:

    sw = pyb.Switch()       # create a switch object
    sw.value()              # get state (True if pressed, False otherwise)
    sw()                    # shorthand notation to get the switch state
    sw.callback(f)          # register a callback to be called when the
                            #   switch is pressed down
    sw.callback(None)       # remove the callback

Example:

    pyb.Switch().callback(lambda: pyb.LED(1).toggle())

## Constructors

Create and return a switch object.

## Methods

Switch.\_\_call\_\_()

Call switch object directly to get its state: `True` if pressed down, `False` otherwise.

Switch.value()

Get the switch state. Returns `True` if pressed down, otherwise `False`.

Switch.callback(fun)

Register the given function to be called when the switch is pressed down. If `fun` is `None`, then it disables the callback.
