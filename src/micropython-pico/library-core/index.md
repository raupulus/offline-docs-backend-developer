---
title: MicroPython libraries
source_url: https://docs.micropython.org/en/latest/library/index.html
source_repo: https://github.com/micropython/micropython.git
source_ref: master
source_commit: 52b5fbcb4
source_path: library/index.rst
technology: micropython-pico
version: master
license: MIT
retrieved_at: '2026-09-15'
section: library-core
order: 210
---

# MicroPython libraries

> [!WARNING]
> Important summary of this section
>
> - MicroPython provides built-in modules that mirror the functionality of the `Python standard library <micropython_lib_python>` (e.g. `os`, `time`), as well as `MicroPython-specific modules <micropython_lib_micropython>` (e.g. `bluetooth`, `machine`).
> - Most Python standard library modules implement a subset of the functionality of the equivalent Python module, and in a few cases provide some MicroPython-specific extensions (e.g. `array`, `os`)
> - Due to resource constraints or other limitations, some ports or firmware versions may not include all the functionality documented here.
> - To allow for extensibility, some built-in modules can be `extended from Python code <micropython_lib_extending>` loaded onto the device filesystem.

This chapter describes modules (function and class libraries) which are built into MicroPython. This documentation in general aspires to describe all modules and functions/classes which are implemented in the MicroPython project. However, MicroPython is highly configurable, and each port to a particular board/embedded system may include only a subset of the available MicroPython libraries.

With that in mind, please be warned that some functions/classes in a module (or even the entire module) described in this documentation **may be unavailable** in a particular build of MicroPython on a particular system. The best place to find general information of the availability/non-availability of a particular feature is the "General Information" section which contains information pertaining to a specific `MicroPython port`.

On some ports you are able to discover the available, built-in libraries that can be imported by entering the following at the `REPL`:

    help('modules')

Beyond the built-in libraries described in this documentation, many more modules from the Python standard library, as well as further MicroPython extensions to it, can be found in `micropython-lib`.

## Python standard libraries and micro-libraries

The following standard Python libraries have been "micro-ified" to fit in with the philosophy of MicroPython. They provide the core functionality of that module and are intended to be a drop-in replacement for the standard Python library.



## MicroPython-specific libraries

Functionality specific to the MicroPython implementation is available in the following libraries.



The following libraries provide drivers for hardware components.



## Port-specific libraries

In some cases the following port/board-specific libraries have functions or classes similar to those in the `machine` library. Where this occurs, the entry in the port specific library exposes hardware functionality unique to that platform.

To write portable code use functions and classes from the `machine` module. To access platform-specific hardware use the appropriate library, e.g. `pyb` in the case of the Pyboard.

### Libraries specific to the pyboard

The following libraries are specific to the pyboard.



### Libraries specific to the WiPy

The following libraries and classes are specific to the WiPy.



### Libraries specific to the ESP8266 and ESP32

The following libraries are specific to the ESP8266 and ESP32.





### Libraries specific to NXP i.MXRT

The following libraries are specific to the NXP i.MXRT family of microcontrollers.



### Libraries specific to the RP2040

The following libraries are specific to the RP2040, as used in the Raspberry Pi Pico.



### Libraries specific to Zephyr

The following libraries are specific to the Zephyr port.



## Extending built-in libraries from Python

A subset of the built-in modules are able to be extended by Python code by providing a module of the same name in the filesystem. This extensibility applies to the following Python standard library modules which are built-in to the firmware: `array`, `binascii`, `collections`, `errno`, `gzip`, `hashlib`, `heapq`, `io`, `json`, `os`, `platform`, `random`, `re`, `select`, `socket`, `ssl`, `struct`, `time` `zlib`, as well as the MicroPython-specific `machine` module. All other built-in modules cannot be extended from the filesystem.

This allows the user to provide an extended implementation of a built-in library (perhaps to provide additional CPython compatibility or missing functionality). This is used extensively in `micropython-lib`, see `packages` for more information. The filesystem module will typically do a wildcard import of the built-in module in order to inherit all the globals (classes, functions and variables) from the built-in.

In MicroPython v1.21.0 and higher, to prevent the filesystem module from importing itself, it can force an import of the built-in module it by temporarily clearing `sys.path` during the import. For example, to extend the `time` module from Python, a file named `time.py` on the filesystem would do the following:

    _path = sys.path
    sys.path = ()
    try:
      from time import *
    finally:
      sys.path = _path
      del _path

    def extra_method():
      pass

The result is that `time.py` contains all the globals of the built-in `time` module, but adds `extra_method`.

In earlier versions of MicroPython, you can force an import of a built-in module by appending a `u` to the start of its name. For example, `import utime` instead of `import time`. For example, `time.py` on the filesystem could look like:

    from utime import *

    def extra_method():
      pass

This way is still supported, but the `sys.path` method described above is now preferred as the `u`-prefix will be removed from the names of built-in modules in a future version of MicroPython.

*Other than when it specifically needs to force the use of the built-in module, code should always use* `import module` *rather than* `import umodule`.
