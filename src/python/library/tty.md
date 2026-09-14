---
title: '"tty" --- Terminal control functions'
source_url: https://docs.python.org/es/3
source_path: library/tty.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 4310
---

# "tty" --- Terminal control functions

**Código fuente:** Lib/tty.py

======================================================================

The "tty" module defines functions for putting the tty into cbreak and
raw modes.

Availability: Unix.

Dado que requiere el módulo "termios", solamente funciona en Unix.

The "tty" module defines the following functions:

tty.cfmakeraw(mode)

   Convert the tty attribute list *mode*, which is a list like the one
   returned by "termios.tcgetattr()", to that of a tty in raw mode.

   Added in version 3.12.

tty.cfmakecbreak(mode)

   Convert the tty attribute list *mode*, which is a list like the one
   returned by "termios.tcgetattr()", to that of a tty in cbreak mode.

   This clears the "ECHO" and "ICANON" local mode flags in *mode* as
   well as setting the minimum input to 1 byte with no delay.

   Added in version 3.12.

   Distinto en la versión 3.12.2: The "ICRNL" flag is no longer
   cleared. This matches Linux and macOS "stty cbreak" behavior and
   what "setcbreak()" historically did.

tty.setraw(fd, when=termios.TCSAFLUSH)

   Change the mode of the file descriptor *fd* to raw. If *when* is
   omitted, it defaults to "termios.TCSAFLUSH", and is passed to
   "termios.tcsetattr()". The return value of "termios.tcgetattr()" is
   saved before setting *fd* to raw mode; this value is returned.

   Distinto en la versión 3.12: The return value is now the original
   tty attributes, instead of "None".

tty.setcbreak(fd, when=termios.TCSAFLUSH)

   Change the mode of file descriptor *fd* to cbreak. If *when* is
   omitted, it defaults to "termios.TCSAFLUSH", and is passed to
   "termios.tcsetattr()". The return value of "termios.tcgetattr()" is
   saved before setting *fd* to cbreak mode; this value is returned.

   This clears the "ECHO" and "ICANON" local mode flags as well as
   setting the minimum input to 1 byte with no delay.

   Distinto en la versión 3.12: The return value is now the original
   tty attributes, instead of "None".

   Distinto en la versión 3.12.2: The "ICRNL" flag is no longer
   cleared. This restores the behavior of Python 3.11 and earlier as
   well as matching what Linux, macOS, & BSDs describe in their
   "stty(1)" man pages regarding cbreak mode.

Ver también:

  Módulo "termios"
     Interfaz de control de la terminal de bajo nivel.
