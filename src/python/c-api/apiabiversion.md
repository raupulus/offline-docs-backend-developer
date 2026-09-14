---
title: Versiones de API y ABI
source_url: https://docs.python.org/es/3
source_path: c-api/apiabiversion.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: c-api
order: 50
---

# Versiones de API y ABI

## Build-time version constants

CPython exposes its version number in the following macros. Note that
these correspond to the version code is **built** with. See
"Py_Version" for the version used at **run time**.

Consulte Estabilidad de la API en C para obtener una discusión sobre
la estabilidad de API y ABI en todas las versiones.

PY_MAJOR_VERSION

   El "3" en "3.4.1a2".

PY_MINOR_VERSION

   El "4" en "3.4.1a2".

PY_MICRO_VERSION

   El "1" en "3.4.1a2".

PY_RELEASE_LEVEL

   La "a" en "3.4.1a2". Puede ser "0xA" para la versión alfa, "0xB"
   para la versión beta, "0xC" para la versión candidata o "0xF" para
   la versión final.

PY_RELEASE_SERIAL

   El "2" en "3.4.1a2", cero para lanzamientos finales.

PY_VERSION_HEX

   The Python version number encoded in a single integer. See
   "Py_PACK_FULL_VERSION()" for the encoding details.

   Use this for numeric comparisons, for example, "#if PY_VERSION_HEX
   >= ...".

These macros are defined in Include/patchlevel.h.

## Run-time version

const unsigned long Py_Version
    * Part of the Stable ABI since version 3.11.*

   The Python runtime version number encoded in a single constant
   integer. See "Py_PACK_FULL_VERSION()" for the encoding details.
   This contains the Python version used at run time.

   Use this for numeric comparisons, for example, "if (Py_Version >=
   ...)".

   Added in version 3.11.

## Bit-packing macros

uint32_t Py_PACK_FULL_VERSION(int major, int minor, int micro, int release_level, int release_serial)
    * Part of the Stable ABI since version 3.14.*

   Return the given version, encoded as a single 32-bit integer with
   the following structure:

   +--------------------+---------+------------------+-------------+---------------+--------------+
   | Argument           | No. of  | Bit mask         | Bit shift   | Example values               |
   |                    | bits    |                  |             |                              |
   |                    |         |                  |             +---------------+--------------+
   |                    |         |                  |             | "3.4.1a2"     | "3.10.0"     |
   |                    |         |                  |             |               |              |
   |====================|=========|==================|=============|===============|==============|
   | *major*            | 8       | "0xFF000000"     | 24          | "0x03"        | "0x03"       |
   +--------------------+---------+------------------+-------------+---------------+--------------+
   | *minor*            | 8       | "0x00FF0000"     | 16          | "0x04"        | "0x0A"       |
   +--------------------+---------+------------------+-------------+---------------+--------------+
   | *micro*            | 8       | "0x0000FF00"     | 8           | "0x01"        | "0x00"       |
   +--------------------+---------+------------------+-------------+---------------+--------------+
   | *release_level*    | 4       | "0x000000F0"     | 4           | "0xA"         | "0xF"        |
   +--------------------+---------+------------------+-------------+---------------+--------------+
   | *release_serial*   | 4       | "0x0000000F"     | 0           | "0x2"         | "0x0"        |
   +--------------------+---------+------------------+-------------+---------------+--------------+

   For example:

   +---------------+--------------------------------------+-------------------+
   | Version       | "Py_PACK_FULL_VERSION" arguments     | Encoded version   |
   |===============|======================================|===================|
   | "3.4.1a2"     | "(3, 4, 1, 0xA, 2)"                  | "0x030401a2"      |
   +---------------+--------------------------------------+-------------------+
   | "3.10.0"      | "(3, 10, 0, 0xF, 0)"                 | "0x030a00f0"      |
   +---------------+--------------------------------------+-------------------+

   Out-of range bits in the arguments are ignored. That is, the macro
   can be defined as:

      #ifndef Py_PACK_FULL_VERSION
      #define Py_PACK_FULL_VERSION(X, Y, Z, LEVEL, SERIAL) ( \
         (((X) & 0xff) << 24) |                              \
         (((Y) & 0xff) << 16) |                              \
         (((Z) & 0xff) << 8) |                               \
         (((LEVEL) & 0xf) << 4) |                            \
         (((SERIAL) & 0xf) << 0))
      #endif

   "Py_PACK_FULL_VERSION" is primarily a macro, intended for use in
   "#if" directives, but it is also available as an exported function.

   Added in version 3.14.

uint32_t Py_PACK_VERSION(int major, int minor)
    * Part of the Stable ABI since version 3.14.*

   Equivalent to "Py_PACK_FULL_VERSION(major, minor, 0, 0, 0)". The
   result does not correspond to any Python release, but is useful in
   numeric comparisons.

   Added in version 3.14.
