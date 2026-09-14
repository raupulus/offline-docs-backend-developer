---
title: '"msvcrt" --- Useful routines from the MS VC++ runtime'
source_url: https://docs.python.org/es/3
source_path: library/msvcrt.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 3270
---

# "msvcrt" --- Useful routines from the MS VC++ runtime

======================================================================

These functions provide access to some useful capabilities on Windows
platforms. Some higher-level modules use these functions to build the
Windows implementations of their services. For example, the "getpass"
module uses this in the implementation of the "getpass()" function.

Más información sobre estas funciones se pueden encontrar en la
documentación de la API de la plataforma.

El módulo implementa las variantes tanto de caracteres normales como
amplios de la API E/S de la consola (se codifican en más de 8 bits,
pudiendo llegar hasta 32). La API normal se ocupa solamente de
caracteres ASCII y es de uso limitado a aplicaciones internacionales.
La API para caracteres amplios se recomienda usar siempre que sea
posible.

Availability: Windows.

Distinto en la versión 3.3: Las operaciones en este módulo lanzan
ahora "OSError" donde antes se lanzaba "IOError".

## Operaciones con archivos

msvcrt.locking(fd, mode, nbytes)

   Lock part of a file based on file descriptor *fd* from the C
   runtime. Raises "OSError" on failure. The locked region of the file
   extends from the current file position for *nbytes* bytes, and may
   continue beyond the end of the file. *mode* must be one of the
   "LK_*" constants listed below. Multiple regions in a file may be
   locked at the same time, but may not overlap. Adjacent regions are
   not merged; they must be unlocked individually.

   Lanza un evento de auditoría "msvcrt.locking" con los argumentos
   "fd", "mode", "nbytes".

msvcrt.LK_LOCK
msvcrt.LK_RLCK

   Locks the specified bytes. If the bytes cannot be locked, the
   program immediately tries again after 1 second. If, after 10
   attempts, the bytes cannot be locked, "OSError" is raised.

msvcrt.LK_NBLCK
msvcrt.LK_NBRLCK

   Bloquea los bytes especificados. Si no se pueden bloquear, lanza
   una excepción "OSError".

msvcrt.LK_UNLCK

   Desbloquea los bytes especificados que han sido previamente
   bloqueados.

msvcrt.setmode(fd, flags)

   Establece el modo traducción del final de línea del descriptor de
   un archivo *fd*. Si se establece como modo texto, *flags* debería
   ser "os.O_TEXT"; para establecerlo como modo binario, debería ser
   "os.O_BINARY".

msvcrt.open_osfhandle(handle, flags)

   Create a C runtime file descriptor from the file handle *handle*.
   The *flags* parameter should be a bitwise OR of "os.O_APPEND",
   "os.O_RDONLY", "os.O_TEXT" and "os.O_NOINHERIT". The returned file
   descriptor may be used as a parameter to "os.fdopen()" to create a
   file object.

   The file descriptor is inheritable by default. Pass
   "os.O_NOINHERIT" flag to make it non inheritable.

   Lanza un evento de auditoría "msvcrt.open_osfhandle" con los
   argumentos "handle", "flags".

msvcrt.get_osfhandle(fd)

   Return the file handle for the file descriptor *fd*. Raises
   "OSError" if *fd* is not recognized.

   Lanza un evento de auditoría "msvcrt.get_osfhandle" con el
   argumento "fd".

## Consola E/S

msvcrt.kbhit()

   Returns a nonzero value if a keypress is waiting to be read.
   Otherwise, return 0.

msvcrt.getch()

   Read a keypress and return the resulting character as a byte
   string. Nothing is echoed to the console. This call will block if a
   keypress is not already available, but will not wait for "Enter" to
   be pressed. If the pressed key was a special function key, this
   will return "'\000'" or "'\xe0'"; the next call will return the
   keycode. The "Control"-"C" keypress cannot be read with this
   function.

msvcrt.getwch()

   Variante de carácter amplio de "getch()", retornando un valor
   Unicode.

msvcrt.getche()

   Similar to "getch()", but the keypress will be echoed if it
   represents a printable character.

msvcrt.getwche()

   Variante de carácter amplio de "getche()", retornando un valor
   Unicode.

msvcrt.putch(char)

   Imprime la cadena de caracteres de bytes *char* a la consola sin
   almacenamiento en buffer.

msvcrt.putwch(unicode_char)

   Variante de carácter amplio de "putch()", admitiendo un valor
   Unicode.

msvcrt.ungetch(char)

   Provoca que la cadena de caracteres de bytes *char* sea "colocada
   de nuevo" en el buffer de la consola, será el siguiente carácter
   que lea la función "getch()" o "getche()".

msvcrt.ungetwch(unicode_char)

   Variante de carácter amplio de "ungetch()", admitiendo un valor
   Unicode.

## Otras funciones

msvcrt.heapmin()

   Force the "malloc()" heap to clean itself up and return unused
   blocks to the operating system. On failure, this raises "OSError".

msvcrt.set_error_mode(mode)

   Changes the location where the C runtime writes an error message
   for an error that might end the program. *mode* must be one of the
   "OUT_*" constants listed below  or "REPORT_ERRMODE". Returns the
   old setting or -1 if an error occurs. Only available in debug build
   of Python.

msvcrt.OUT_TO_DEFAULT

   Error sink is determined by the app's type. Only available in debug
   build of Python.

msvcrt.OUT_TO_STDERR

   Error sink is a standard error. Only available in debug build of
   Python.

msvcrt.OUT_TO_MSGBOX

   Error sink is a message box. Only available in debug build of
   Python.

msvcrt.REPORT_ERRMODE

   Report the current error mode value. Only available in debug build
   of Python.

msvcrt.CrtSetReportMode(type, mode)

   Specifies the destination or destinations for a specific report
   type generated by "_CrtDbgReport()" in the MS VC++ runtime. *type*
   must be one of the "CRT_*" constants listed below. *mode* must be
   one of the "CRTDBG_*" constants listed below. Only available in
   debug build of Python.

msvcrt.CrtSetReportFile(type, file)

   After you use "CrtSetReportMode()" to specify "CRTDBG_MODE_FILE",
   you can specify the file handle to receive the message text. *type*
   must be one of the "CRT_*" constants listed below. *file* should be
   the file handle your want specified. Only available in debug build
   of Python.

msvcrt.CRT_WARN

   Warnings, messages, and information that doesn't need immediate
   attention.

msvcrt.CRT_ERROR

   Errors, unrecoverable problems, and issues that require immediate
   attention.

msvcrt.CRT_ASSERT

   Assertion failures.

msvcrt.CRTDBG_MODE_DEBUG

   Writes the message to the debugger's output window.

msvcrt.CRTDBG_MODE_FILE

   Writes the message to a user-supplied file handle.
   "CrtSetReportFile()" should be called to define the specific file
   or stream to use as the destination.

msvcrt.CRTDBG_MODE_WNDW

   Creates a message box to display the message along with the
   "Abort", "Retry", and "Ignore" buttons.

msvcrt.CRTDBG_REPORT_MODE

   Returns current *mode* for the specified *type*.

msvcrt.CRT_ASSEMBLY_VERSION

   The CRT Assembly version, from the "crtassem.h" header file.

msvcrt.VC_ASSEMBLY_PUBLICKEYTOKEN

   The VC Assembly public key token, from the "crtassem.h" header
   file.

msvcrt.LIBRARIES_ASSEMBLY_NAME_PREFIX

   The Libraries Assembly name prefix, from the "crtassem.h" header
   file.
