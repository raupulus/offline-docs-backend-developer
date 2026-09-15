---
title: Reset and Boot Sequence
source_url: https://docs.micropython.org/en/latest/reference/reset_boot.html
source_repo: https://github.com/micropython/micropython.git
source_ref: master
source_commit: 52b5fbcb4
source_path: reference/reset_boot.rst
technology: micropython-pico
version: master
license: MIT
retrieved_at: '2026-09-15'
section: reference
order: 1350
---

# Reset and Boot Sequence

A device running MicroPython follows a particular boot sequence to start up and initialise itself after a reset.

## Hard reset

Booting from hard reset is what happens when a board is first powered up, a cold boot. This is a complete reset of the MCU hardware.

The MicroPython port code initialises all essential hardware (including embedded clocks and power regulators, internal serial UART, etc), and then starts the MicroPython environment. Existing `RTC </library/machine.RTC>` configuration may be retained after a hard reset, but all other hardware state is cleared.

The same hard reset boot sequence can be triggered by a number of events such as:

- Python code executing `machine.reset()`.
- User presses a physical Reset button on the board (where applicable).
- Waking from deep sleep (on most ports).
- MCU hardware watchdog reset.
- MCU hardware brown out detector.

The details of hardware-specific reset triggers depend on the port and associated hardware. The `machine.reset_cause()` function can be used to further determine the cause of a reset.

## Soft Reset

When MicroPython is already running, it's possible to trigger a soft reset by `typing Ctrl-D in the REPL <repl_soft_reset>` or executing `machine.soft_reset()`.

A soft reset clears the Python interpreter, frees all Python memory, and starts the MicroPython environment again.

State which is cleared by a soft reset includes:

- All Python variables, objects, imported modules, etc.
- Most peripherals configured using the `machine module
  </library/machine>`. There are very limited exceptions, for example `machine.Pin </library/machine.Pin>` modes (i.e. if a pin is input or output, high or low) are not reset on most ports. More advanced configuration such as `Pin.irq()` is always reset.
- Bluetooth.
- Network sockets. Open TCP sockets are closed cleanly with respect to the other party.
- Open files. The filesystem is left in a valid state.

Some system state remains the same after a soft reset, including:

- Any existing network connections (Ethernet, Wi-Fi, etc) remain active at the IP Network layer. Querying the `network interface from code
  </library/network>` may indicate the network interface is still active with a configured IP address, etc.
- An active `REPL <repl>` appears continuous before and after soft reset, except in some unusual cases:
  - If the `machine.USBDevice <machine.USBDevice>` class has been used to create a custom USB interface then any built-in USB serial device will appear to disconnect and reconnect as the custom USB interface must be cleared during reset.
  - A serial UART REPL will restore its default hardware configuration (baud rate, etc).
- CPU clock speed is usually not changed by a soft reset.
- `RTC </library/machine.RTC>` configuration (i.e. setting of the current time) is not changed by soft reset.

## Boot Sequence

When MicroPython boots following either a hard or soft reset, it follows this boot sequence in order:

### <span id="boot.py">boot.py</span>

This is an internal script `frozen into the MicroPython firmware
<manifest>`. It is provided by MicroPython on many ports to do essential initialisation.

For example, on most ports `_boot.py` will detect the first boot of a new device and format the `internal flash filesystem <filesystem>` ready for use.

Unless you're creating a custom MicroPython build or adding a new port then you probably don't need to worry about `_boot.py`. It's best not to change the contents unless you really know what you're doing.

### boot.py

A file named `boot.py` can be copied to the board's internal `filesystem
<filesystem>` using `mpremote <mpremote>`.

If `boot.py` is found then it is executed. You can add code in `boot.py` to perform custom one-off initialisation (for example, to configure the board's hardware).

A common practice is to configure a board's network connection in `boot.py` so that it's always available after reset for use with the `REPL <repl>`, `mpremote <mpremote>`, etc.

> [!WARNING]
> boot.py should always exit and not run indefinitely.
>
> Depending on the port, some hardware initialisation is delayed until after `boot.py` exits. This includes initialising USB on the stm32 port and all ports which support `machine.USBDevice <machine.USBDevice>`. On these ports, output printed from `boot.py` may not be visible on the built-in USB serial port until after `boot.py` finishes running.
>
> The purpose of this late initialisation is so that it's possible to pre-configure particular hardware in `boot.py`, and then have it start with the correct configuration.

> [!NOTE]
> It is sometimes simpler to not have a `boot.py` file and place any initialisation code at the top of `main.py` instead.

### main.py

Similar to `boot.py`, a file named `main.py` can be copied to the board's internal `filesystem <filesystem>`. If found then it is executed next in the startup process.

`main.py` is for any Python code that you want to run each time your device starts.

Some tips for `main.py` usage:

- `main.py` doesn't have to exit, feel free to put an infinite `while True` loop in there.

- For complex Python applications then you don't need to put all your code in `main.py`. `main.py` can be a simple entry point that imports your application and starts execution:

      import my_app
      my_app.main()

  This can help keep the structure of your application clear. It also makes it easy to install multiple applications on a board and switch among them.

- It's good practice when writing robust apps to wrap code in `main.py` with an exception handler to take appropriate action if the code crashes. For example:

      import machine, sys
      import my_app
      try:
          my_app.main()
      except Exception as e:
          print("Fatal error in main:")
          sys.print_exception(e)

      # Following a normal Exception or main() exiting, reset the board.
      # Following a non-Exception error such as KeyboardInterrupt (Ctrl-C),
      # this code will drop to a REPL. Place machine.reset() in a finally
      # block to always reset, instead.
      machine.reset()

  Otherwise MicroPython will drop to the REPL following any crash or if main exits (see below).

- Any global variables that were set in `boot.py` will still be set in the global context of `main.py`.

- To fully optimise flash usage and memory consumption, you can copy `pre-compiled <mpyfiles>` `main.mpy` and/or `boot.mpy` files to the filesystem, or even `freeze <manifest>` them into the firmware build instead.

- `main.py` execution is skipped when a soft reset is initiated from `raw
  REPL mode <raw_repl>` (for example, when `mpremote <mpremote>` or another program is interacting directly with MicroPython).

### Interactive Interpreter (REPL)

If `main.py` is not found, or if `main.py` exits, then `repl` will start immediately.

> [!NOTE]
> Even if `main.py` contains an infinite loop, typing Ctrl-C on the REPL serial port will inject a `KeyboardInterrupt`. If no exception handler catches it then `main.py` will exit and the REPL will start.

Any global variables that were set in `boot.py` and `main.py` will still be set in the global context of the REPL.

The REPL continues executing until Python code triggers a hard or soft reset.

## Soft Bricking (failure to boot)

It is rare but possible for MicroPython to become unresponsive during startup, a state sometimes called "soft bricked". For example:

- If `boot.py` execution gets stuck and the native USB serial port never initialises.
- If Python code reconfigures the REPL interface, making it inaccessible.

Rest assured, recovery is possible!

### KeyboardInterrupt

In many cases, opening the REPL serial port and typing `Ctrl-C` will inject `KeyboardInterrupt` and may cause the running script to exit and a REPL to start. From the REPL, you can use `os.remove()` to remove the misbehaving Python file:

    import os
    os.remove('main.py')

To confirm which files are still present in the internal filesystem:

    import os
    os.listdir()

### Safe Mode and Factory Reset

If you're unable to easily access the REPL then you may need to perform one of two processes:

1.  "Safe mode" boot, which skips `boot.py` and `main.py` and immediately starts a REPL, allowing you to clean up. This is only supported on some ports.
2.  Factory Reset to erase the entire contents of the flash filesystem. This may also be necessary if the internal flash filesystem has become corrupted somehow.

The specific process(es) are different on each port:

- `pyboard and stm32 port instructions </pyboard/tutorial/reset>`
- `esp32 port instructions </esp32/tutorial/reset>`
- `renesas-ra port instructions </renesas-ra/tutorial/reset>`
- `rp2 port instructions </rp2/tutorial/reset>`
- `wipy port instructions </wipy/tutorial/reset>`

For ports without specific instructions linked above, the factory reset process involves erasing the board's entire flash and then flashing MicroPython again from scratch. Usually this will involve the same tool(s) that were originally used to install MicroPython. Consult the installation docs for your board, or ask on the [GitHub Discussions](https://github.com/orgs/micropython/discussions) if you're not sure.

> [!WARNING]
> Re-flashing the MicroPython firmware without erasing the entire flash first will usually not recover from soft bricking, as a firmware update usually preserves the contents of the filesystem.
