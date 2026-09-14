---
title: '"posix" --- The most common POSIX system calls'
source_url: https://docs.python.org/es/3
source_path: library/posix.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 3510
---

# "posix" --- The most common POSIX system calls

======================================================================

Este módulo proporciona acceso a la funcionalidad del sistema
operativo que está estandarizada por el estándar C y el estándar POSIX
(una interfaz Unix finamente disfrazada).

Availability: Unix.

**Do not import this module directly.**  Instead, import the module
"os", which provides a *portable* version of this interface.  On Unix,
the "os" module provides a superset of the "posix" interface.  On non-
Unix operating systems the "posix" module is not available, but a
subset is always available through the "os" interface.  Once "os" is
imported, there is *no* performance penalty in using it instead of
"posix".  In addition, "os" provides some additional functionality,
such as automatically calling "putenv()" when an entry in "os.environ"
is changed.

Los errores se notifican como excepciones; las excepciones habituales
se proporcionan para los errores de tipo, mientras que los errores
notificados por las llamadas del sistema lanzan "OSError".

## Soporte de archivos grandes

Several operating systems (including AIX and Solaris) provide support
for files that are larger than 2 GiB from a C programming model where
int and long are 32-bit values. This is typically accomplished by
defining the relevant size and offset types as 64-bit values. Such
files are sometimes referred to as *large files*.

Large file support is enabled in Python when the size of an "off_t" is
larger than a long and the long long is at least as large as an
"off_t". It may be necessary to configure and compile Python with
certain compiler flags to enable this mode. For example, with Solaris
2.6 and 2.7 you need to do something like:

   CFLAGS="`getconf LFS_CFLAGS`" OPT="-g -O2 $CFLAGS" \
           ./configure

En sistemas Linux con capacidad para archivos grandes, esto podría
funcionar:

   CFLAGS='-D_LARGEFILE64_SOURCE -D_FILE_OFFSET_BITS=64' OPT="-g -O2 $CFLAGS" \
           ./configure

## Contenido notable del módulo

In addition to many functions described in the "os" module
documentation, "posix" defines the following data item:

posix.environ

   Diccionario que representa el entorno de cadena en el momento en
   que se inició el intérprete. Las claves y los valores son bytes en
   Unix y str en Windows. Por ejemplo, "environ[b'HOME']"
   ("environ['HOME']" en Windows) es el nombre de ruta de acceso de su
   directorio principal, equivalente a "getenv("HOME")" en C.

   La modificación de este diccionario no afecta al entorno de cadena
   que transmite "execv()", "popen()" o "system()"; si necesita
   cambiar el entorno, pase "environ" a "execve()" o agregue
   asignaciones variables y declaraciones de exportación a la cadena
   de comandos para "system()" o "popen()".

   Distinto en la versión 3.2: En Unix, las claves y los valores son
   bytes.

   Nota:

     The "os" module provides an alternate implementation of "environ"
     which updates the environment on modification. Note also that
     updating "os.environ" will render this dictionary obsolete. Use
     of the "os" module version of this is recommended over direct
     access to the "posix" module.
