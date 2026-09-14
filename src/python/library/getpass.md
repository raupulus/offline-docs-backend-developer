---
title: '"getpass" --- Portable password input'
source_url: https://docs.python.org/es/3
source_path: library/getpass.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 2730
---

# "getpass" --- Portable password input

**Código fuente:** Lib/getpass.py

======================================================================

Availability: not WASI.

This module does not work or is not available on WebAssembly. See
Plataformas WebAssembly for more information.

The "getpass" module provides two functions:

getpass.getpass(prompt='Password: ', stream=None, *, echo_char=None)

   Solicita al usuario una contraseña sin hacer eco. Se solicita al
   usuario mediante la cadena *prompt*, que por defecto es "'Password:
   '". En Unix, el indicador se escribe en el objeto similar a un
   archivo *stream* usando el controlador de errores de reemplazo si
   es necesario. *stream* toma por defecto el terminal de control
   ("/dev/tty") o si no está disponible para "sys.stderr" (este
   argumento se ignora en Windows).

   The *echo_char* argument controls how user input is displayed while
   typing. If *echo_char* is "None" (default), input remains hidden.
   Otherwise, *echo_char* must be a single printable ASCII character
   and each typed character is replaced by it. For example,
   "echo_char='*'" will display asterisks instead of the actual input.

   Si la entrada sin *echo* no está disponible, getpass() recurre a
   imprimir un mensaje de advertencia en *stream* y leer de
   "sys.stdin" y lanza un "GetPassWarning".

   Nota:

     Si llama a getpass desde IDLE, la entrada puede realizarse en la
     terminal desde la que inició IDLE en lugar de en la ventana
     inactiva en sí.

   Nota:

     On Unix systems, when *echo_char* is set, the terminal will be
     configured to operate in *noncanonical mode*. In particular, this
     means that line editing shortcuts such as "Ctrl"+"U" will not
     work and may insert unexpected characters into the input.

   Distinto en la versión 3.14: Added the *echo_char* parameter for
   keyboard feedback.

exception getpass.GetPassWarning

   Una subclase "UserWarning" lanzada cuando la entrada de la
   contraseña puede repetirse.

getpass.getuser()

   Retorna el "nombre de inicio de sesión" del usuario.

   This function checks the environment variables "LOGNAME", "USER",
   "LNAME" and "USERNAME", in order, and returns the value of the
   first one which is set to a non-empty string.  If none are set, the
   login name from the password database is returned on systems which
   support the "pwd" module, otherwise, an "OSError" is raised.

   In general, this function should be preferred over "os.getlogin()".

   Distinto en la versión 3.13: Previously, various exceptions beyond
   just "OSError" were raised.
