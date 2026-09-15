---
title: Pin
description: control I/O pins
source_url: https://docs.micropython.org/en/latest/library/pyb.Pin.html
source_repo: https://github.com/micropython/micropython.git
source_ref: master
source_commit: 52b5fbcb4
source_path: library/pyb.Pin.rst
technology: micropython-pico
version: master
license: MIT
retrieved_at: '2026-09-15'
section: library-core
order: 730
---

# class Pin -- control I/O pins

A pin is the basic object to control I/O pins. It has methods to set the mode of the pin (input, output, etc) and methods to get and set the digital logic level. For analog control of a pin, see the ADC class.

Usage Model:

All Board Pins are predefined as pyb.Pin.board.Name:

    x1_pin = pyb.Pin.board.X1

    g = pyb.Pin(pyb.Pin.board.X1, pyb.Pin.IN)

CPU pins which correspond to the board pins are available as `pyb.Pin.cpu.Name`. For the CPU pins, the names are the port letter followed by the pin number. On the PYBv1.0, `pyb.Pin.board.X1` and `pyb.Pin.cpu.A0` are the same pin.

You can also use strings:

    g = pyb.Pin('X1', pyb.Pin.OUT_PP)

Users can add their own names:

    MyMapperDict = { 'LeftMotorDir' : pyb.Pin.cpu.C12 }
    pyb.Pin.dict(MyMapperDict)
    g = pyb.Pin("LeftMotorDir", pyb.Pin.OUT_OD)

and can query mappings:

    pin = pyb.Pin("LeftMotorDir")

Users can also add their own mapping function:

    def MyMapper(pin_name):
       if pin_name == "LeftMotorDir":
           return pyb.Pin.cpu.A0

    pyb.Pin.mapper(MyMapper)

So, if you were to call: `pyb.Pin("LeftMotorDir", pyb.Pin.OUT_PP)` then `"LeftMotorDir"` is passed directly to the mapper function.

To summarise, the following order determines how things get mapped into an ordinal pin number:

1.  Directly specify a pin object
2.  User supplied mapping function
3.  User supplied mapping (object must be usable as a dictionary key)
4.  Supply a string which matches a board pin
5.  Supply a string which matches a CPU port/pin

You can set `pyb.Pin.debug(True)` to get some debug information about how a particular object gets mapped to a pin.

All pin objects go through the pin mapper to come up with one of the gpio pins.

## Constructors

Create a new Pin object associated with the id. If additional arguments are given, they are used to initialise the pin. See `pin.init`.

## Class methods

Pin.debug(\[state\])

Get or set the debugging state (`True` or `False` for on or off).

Pin.dict(\[dict\])

Get or set the pin mapper dictionary.

Pin.mapper(\[fun\])

Get or set the pin mapper function.

## Methods

Pin.init(mode, pull=Pin.PULL_NONE, \*, value=None, alt=-1)

Initialise the pin:

> - *mode* can be one of:
>
>   > - `Pin.IN` - configure the pin for input;
>   > - `Pin.OUT_PP` - configure the pin for output, with push-pull control;
>   > - `Pin.OUT_OD` - configure the pin for output, with open-drain control;
>   > - `Pin.ALT` - configure the pin for alternate function, input or output;
>   > - `Pin.AF_PP` - configure the pin for alternate function, push-pull;
>   > - `Pin.AF_OD` - configure the pin for alternate function, open-drain;
>   > - `Pin.ANALOG` - configure the pin for analog.
>
> - *pull* can be one of:
>
>   > - `Pin.PULL_NONE` - no pull up or down resistors;
>   > - `Pin.PULL_UP` - enable the pull-up resistor;
>   > - `Pin.PULL_DOWN` - enable the pull-down resistor.
>
>   When a pin has the `Pin.PULL_UP` or `Pin.PULL_DOWN` pull-mode enabled, that pin has an effective 40k Ohm resistor pulling it to 3V3 or GND respectively (except pin Y5 which has 11k Ohm resistors).
>
> - *value* if not None will set the port output value before enabling the pin.
>
> - *alt* can be used when mode is `Pin.ALT` , `Pin.AF_PP` or `Pin.AF_OD` to set the index or name of one of the alternate functions associated with a pin. This arg was previously called *af* which can still be used if needed.

Returns: `None`.

Pin.value(\[value\])

Get or set the digital logic level of the pin:

> - With no argument, return 0 or 1 depending on the logic level of the pin.
> - With `value` given, set the logic level of the pin. `value` can be anything that converts to a boolean. If it converts to `True`, the pin is set high, otherwise it is set low.

Pin.\_\_str\_\_()

Return a string describing the pin object.

Pin.af()

Returns the currently configured alternate-function of the pin. The integer returned will match one of the allowed constants for the af argument to the init function.

Pin.af_list()

Returns an array of alternate functions available for this pin.

Pin.gpio()

Returns the base address of the GPIO block associated with this pin.

Pin.mode()

Returns the currently configured mode of the pin. The integer returned will match one of the allowed constants for the mode argument to the init function.

Pin.name()

Get the pin name.

Pin.names()

Returns the cpu and board names for this pin.

Pin.pin()

Get the pin number.

Pin.port()

Get the pin port.

Pin.pull()

Returns the currently configured pull of the pin. The integer returned will match one of the allowed constants for the pull argument to the init function.

## Constants

Pin.ALT

initialise the pin to alternate-function mode for input or output

Pin.AF_OD

initialise the pin to alternate-function mode with an open-drain drive

Pin.AF_PP

initialise the pin to alternate-function mode with a push-pull drive

Pin.ANALOG

initialise the pin to analog mode

Pin.IN

initialise the pin to input mode

Pin.OUT_OD

initialise the pin to output mode with an open-drain drive

Pin.OUT_PP

initialise the pin to output mode with a push-pull drive

Pin.PULL_DOWN

enable the pull-down resistor on the pin

Pin.PULL_NONE

don't enable any pull up or down resistors on the pin

Pin.PULL_UP

enable the pull-up resistor on the pin

# class PinAF -- Pin Alternate Functions

A Pin represents a physical pin on the microprocessor. Each pin can have a variety of functions (GPIO, I2C SDA, etc). Each PinAF object represents a particular function for a pin.

Usage Model:

    x3 = pyb.Pin.board.X3
    x3_af = x3.af_list()

x3_af will now contain an array of PinAF objects which are available on pin X3.

For the pyboard, x3_af would contain:  
\[Pin.AF1_TIM2, Pin.AF2_TIM5, Pin.AF3_TIM9, Pin.AF7_USART2\]

Normally, each peripheral would configure the alternate function automatically, but sometimes the same function is available on multiple pins, and having more control is desired.

To configure X3 to expose TIM2_CH3, you could use:

    pin = pyb.Pin(pyb.Pin.board.X3, mode=pyb.Pin.ALT, alt=pyb.Pin.AF1_TIM2)

or:

    pin = pyb.Pin(pyb.Pin.board.X3, mode=pyb.Pin.ALT, alt=1)

## Methods

pinaf.\_\_str\_\_()

Return a string describing the alternate function.

pinaf.index()

Return the alternate function index.

pinaf.name()

Return the name of the alternate function.

pinaf.reg()

Return the base register associated with the peripheral assigned to this alternate function. For example, if the alternate function were TIM2_CH3 this would return stm.TIM2
