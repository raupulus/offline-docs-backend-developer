---
title: File objects
source_url: https://docs.python.org/es/3
source_path: c-api/file.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: c-api
order: 270
---

# File objects

These APIs are a minimal emulation of the Python 2 C API for built-in
file objects, which used to rely on the buffered I/O (FILE*) support
from the C standard library.  In Python 3, files and streams use the
new "io" module, which defines several layers over the low-level
unbuffered I/O of the operating system.  The functions described below
are convenience C wrappers over these new APIs, and meant mostly for
internal error reporting in the interpreter; third-party code is
advised to access the "io" APIs instead.

PyObject *PyFile_FromFd(int fd, const char *name, const char *mode, int buffering, const char *encoding, const char *errors, const char *newline, int closefd)
    *Return value: New reference.** Part of the Stable ABI.*

   Crea un objeto archivo Python a partir del descriptor de archivo de
   un archivo ya abierto *fd*. Los argumentos *name*, *encoding*,
   *errors* y *newline* pueden ser "NULL" para usar los valores
   predeterminados; *buffering* puede ser *-1* para usar el valor
   predeterminado. *name* se ignora y se mantiene por compatibilidad
   con versiones anteriores. Retorna "NULL" en caso de error. Para
   obtener una descripción más completa de los argumentos, consulte la
   documentación de la función "io.open()".

   Advertencia:

     Dado que las transmisiones (*streams*) de Python tienen su propia
     capa de almacenamiento en búfer, combinarlas con descriptores de
     archivos a nivel del sistema operativo puede producir varios
     problemas (como un pedido inesperado de datos).

   Distinto en la versión 3.2: Ignora el atributo *name*.

int PyObject_AsFileDescriptor(PyObject *p)
    * Part of the Stable ABI.*

   Return the file descriptor associated with *p* as an int.  If the
   object is an integer, its value is returned.  If not, the object's
   "fileno()" method is called if it exists; the method must return an
   integer, which is returned as the file descriptor value.  Sets an
   exception and returns "-1" on failure.

PyObject *PyFile_GetLine(PyObject *p, int n)
    *Return value: New reference.** Part of the Stable ABI.*

   Equivalente a "p.readline([n])", esta función lee una línea del
   objeto *p*. *p* puede ser un objeto archivo o cualquier objeto con
   un método "readline()". Si *n* es "0", se lee exactamente una
   línea, independientemente de la longitud de la línea. Si *n* es
   mayor que "0", no se leerán más de *n* bytes del archivo; se puede
   retornar una línea parcial. En ambos casos, se retorna una cadena
   de caracteres vacía si se llega al final del archivo de inmediato.
   Si *n* es menor que "0", sin embargo, se lee una línea
   independientemente de la longitud, pero "EOFError" se lanza si se
   llega al final del archivo de inmediato.

int PyFile_SetOpenCodeHook(Py_OpenCodeHookFunction handler)

   Sobrescribe el comportamiento normal de "io.open_code()" para pasar
   su parámetro a través del controlador proporcionado.

   The *handler* is a function of type:

   typedef PyObject *(*Py_OpenCodeHookFunction)(PyObject*, void*)

      Equivalent of PyObject *(*)(PyObject *path, void *userData),
      where *path* is guaranteed to be "PyUnicodeObject".

   El puntero *userData* se pasa a la función de enlace. Dado que las
   funciones de enlace pueden llamarse desde diferentes tiempos de
   ejecución, este puntero no debe referirse directamente al estado de
   Python.

   Como este *hook* se usa intencionalmente durante la importación,
   evite importar nuevos módulos durante su ejecución a menos que se
   sepa que están congelados o disponibles en "sys.modules".

   Una vez que se ha establecido un *hook*, no se puede quitar ni
   reemplazar, y luego llamadas a "PyFile_SetOpenCodeHook()" fallarán.
   En caso de error, la función retorna -1 y establece una excepción
   si el intérprete se ha inicializado.

   Es seguro llamar a esta función antes de "Py_Initialize()".

   Genera un evento de auditoría "setopencodehook" sin argumentos.

   Added in version 3.8.

PyObject *PyFile_OpenCodeObject(PyObject *path)

   Open *path* with the mode "'rb'". *path* must be a Python "str"
   object. The behavior of this function may be overridden by
   "PyFile_SetOpenCodeHook()" to allow for some preprocessing of the
   text.

   This is analogous to "io.open_code()" in Python.

   On success, this function returns a *strong reference* to a Python
   file object. On failure, this function returns "NULL" with an
   exception set.

   Added in version 3.8.

PyObject *PyFile_OpenCode(const char *path)

   Similar to "PyFile_OpenCodeObject()", but *path* is a UTF-8 encoded
   const char*.

   Added in version 3.8.

int PyFile_WriteObject(PyObject *obj, PyObject *p, int flags)
    * Part of the Stable ABI.*

   Write object *obj* to file object *p*.  The only supported flag for
   *flags* is "Py_PRINT_RAW"; if given, the "str()" of the object is
   written instead of the "repr()".

   If *obj* is "NULL", write the string ""<NULL>"".

   Return "0" on success or "-1" on failure; the appropriate exception
   will be set.

int PyFile_WriteString(const char *s, PyObject *p)
    * Part of the Stable ABI.*

   Escribe la cadena *s* en el objeto archivo *p*. Retorna "0" en caso
   de éxito o "-1" en caso de error; se establecerá la excepción
   apropiada.

## Soft-deprecated API

Soft deprecated since version 3.15.

These are APIs that were included in Python's C API by mistake. They
are documented solely for completeness; use other "PyFile*" APIs
instead.

PyObject *PyFile_NewStdPrinter(int fd)

   Use "PyFile_FromFd()" with defaults ("fd, NULL, "w", -1, NULL,
   NULL, NULL, 0") instead.

PyTypeObject PyStdPrinter_Type

   Type of file-like objects used internally at Python startup when
   "io" is not yet available. Use Python "open()" or "PyFile_FromFd()"
   to create file objects instead.
