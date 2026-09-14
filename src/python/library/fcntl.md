---
title: '"fcntl" --- The "fcntl" and "ioctl" system calls'
source_url: https://docs.python.org/es/3
source_path: library/fcntl.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 2590
---

# "fcntl" --- The "fcntl" and "ioctl" system calls

======================================================================

This module performs file and I/O control on file descriptors. It is
an interface to the "fcntl()" and "ioctl()" Unix routines. See the
*fcntl(2)* and *ioctl(2)* Unix manual pages for full details.

Availability: Unix, not WASI.

Todas las funciones de este módulo toman un descriptor de fichero *fd*
como su primer argumento.  Puede ser un descriptor de fichero entero,
como el retornado por "sys.stdin.fileno()", o un objeto "io.IOBase",
como "sys.stdin", que proporciona un "fileno()" que retorna un
descriptor de fichero original.

Distinto en la versión 3.3: Las operaciones en este módulo solían
lanzar un "IOError" donde ahora lanzan un "OSError".

Distinto en la versión 3.8: The "fcntl" module now contains
"F_ADD_SEALS", "F_GET_SEALS", and "F_SEAL_*" constants for sealing of
"os.memfd_create()" file descriptors.

Distinto en la versión 3.9: On macOS, the "fcntl" module exposes the
"F_GETPATH" constant, which obtains the path of a file from a file
descriptor. On Linux(>=3.15), the "fcntl" module exposes the
"F_OFD_GETLK", "F_OFD_SETLK" and "F_OFD_SETLKW" constants, which are
used when working with open file description locks.

Distinto en la versión 3.10: On Linux >= 2.6.11, the "fcntl" module
exposes the "F_GETPIPE_SZ" and "F_SETPIPE_SZ" constants, which allow
to check and modify a pipe's size respectively.

Distinto en la versión 3.11: On FreeBSD, the "fcntl" module exposes
the "F_DUP2FD" and "F_DUP2FD_CLOEXEC" constants, which allow to
duplicate a file descriptor, the latter setting "FD_CLOEXEC" flag in
addition.

Distinto en la versión 3.12: On Linux >= 4.5, the "fcntl" module
exposes the "FICLONE" and "FICLONERANGE" constants, which allow to
share some data of one file with another file by reflinking on some
filesystems (e.g., btrfs, OCFS2, and XFS). This behavior is commonly
referred to as "copy-on-write".

Distinto en la versión 3.13: On Linux >= 2.6.32, the "fcntl" module
exposes the "F_GETOWN_EX", "F_SETOWN_EX", "F_OWNER_TID",
"F_OWNER_PID", "F_OWNER_PGRP" constants, which allow to direct I/O
availability signals to a specific thread, process, or process group.
On Linux >= 4.13, the "fcntl" module exposes the "F_GET_RW_HINT",
"F_SET_RW_HINT", "F_GET_FILE_RW_HINT", "F_SET_FILE_RW_HINT", and
"RWH_WRITE_LIFE_*" constants, which allow to inform the kernel about
the relative expected lifetime of writes on a given inode or via a
particular open file description. On Linux >= 5.1 and NetBSD, the
"fcntl" module exposes the "F_SEAL_FUTURE_WRITE" constant for use with
"F_ADD_SEALS" and "F_GET_SEALS" operations. On FreeBSD, the "fcntl"
module exposes the "F_READAHEAD", "F_ISUNIONSTACK", and "F_KINFO"
constants. On macOS and FreeBSD, the "fcntl" module exposes the
"F_RDAHEAD" constant. On NetBSD and AIX, the "fcntl" module exposes
the "F_CLOSEM" constant. On NetBSD, the "fcntl" module exposes the
"F_MAXFD" constant. On macOS and NetBSD, the "fcntl" module exposes
the "F_GETNOSIGPIPE" and "F_SETNOSIGPIPE" constant.

Distinto en la versión 3.14: On Linux >= 6.1, the "fcntl" module
exposes the "F_DUPFD_QUERY" to query a file descriptor pointing to the
same file.

El módulo define las siguientes funciones:

fcntl.fcntl(fd, cmd, arg=0, /)

   Perform the operation *cmd* on file descriptor *fd* (file objects
   providing a "fileno()" method are accepted as well).  The values
   used for *cmd* are operating system dependent, and are available as
   constants in the "fcntl" module, using the same names as used in
   the relevant C header files. The argument *arg* can either be an
   integer value, a *bytes-like object*, or a string. The type and
   size of *arg* must match the type and size of the argument of the
   operation as specified in the relevant C documentation.

   When *arg* is an integer, the function returns the integer return
   value of the C "fcntl()" call.

   When the argument is bytes-like object, it represents a binary
   structure, for example, created by "struct.pack()". A string value
   is encoded to binary using the UTF-8 encoding. The binary data is
   copied to a buffer whose address is passed to the C "fcntl()" call.
   The return value after a successful call is the contents of the
   buffer, converted to a "bytes" object. The length of the returned
   object will be the same as the length of the *arg* argument. This
   is limited to 1024 bytes.

   If the "fcntl()" call fails, an "OSError" is raised.

   Nota:

     If the type or the size of *arg* does not match the type or size
     of the argument of the operation (for example, if an integer is
     passed when a pointer is expected, or the information returned in
     the buffer by the operating system is larger than 1024 bytes),
     this is most likely to result in a segmentation violation or a
     more subtle data corruption.

   Lanza un evento de auditoria "fcntl.fcntl" con argumentos "fd",
   "cmd", "arg".

   Distinto en la versión 3.14: Add support of arbitrary *bytes-like
   objects*, not only "bytes".

fcntl.ioctl(fd, request, arg=0, mutate_flag=True, /)

   Esta función es idéntica a la función "fcntl()", excepto por el
   manejo de los argumentos que es aún más complicado.

   The *request* parameter is limited to values that can fit in
   32-bits or 64-bits, depending on the platform. Additional constants
   of interest for use as the *request* argument can be found in the
   "termios" module, under the same names as used in the relevant C
   header files.

   The parameter *arg* can be an integer, a *bytes-like object*, or a
   string. The type and size of *arg* must match the type and size of
   the argument of the operation as specified in the relevant C
   documentation.

   If *arg* does not support the read-write buffer interface or the
   *mutate_flag* is false, behavior is as for the "fcntl()" function.

   If *arg* supports the read-write buffer interface (like
   "bytearray") and *mutate_flag* is true (the default), then the
   buffer is (in effect) passed to the underlying "ioctl()" system
   call, the latter's return code is passed back to the calling
   Python, and the buffer's new contents reflect the action of the
   "ioctl()".  This is a slight simplification, because if the
   supplied buffer is less than 1024 bytes long it is first copied
   into a static buffer 1024 bytes long which is then passed to
   "ioctl()" and copied back into the supplied buffer.

   If the "ioctl()" call fails, an "OSError" exception is raised.

   Nota:

     If the type or size of *arg* does not match the type or size of
     the operation's argument (for example, if an integer is passed
     when a pointer is expected, or the information returned in the
     buffer by the operating system is larger than 1024 bytes, or the
     size of the mutable bytes-like object is too small), this is most
     likely to result in a segmentation violation or a more subtle
     data corruption.

   Un ejemplo:

      >>> import array, fcntl, struct, termios, os
      >>> os.getpgrp()
      13341
      >>> struct.unpack('h', fcntl.ioctl(0, termios.TIOCGPGRP, "  "))[0]
      13341
      >>> buf = array.array('h', [0])
      >>> fcntl.ioctl(0, termios.TIOCGPGRP, buf, 1)
      0
      >>> buf
      array('h', [13341])

   Lanza un evento de auditoria "fcntl.ioctl" con argumentos "fd",
   "request", "arg".

   Distinto en la versión 3.14: The GIL is always released during a
   system call. System calls failing with EINTR are automatically
   retried.

fcntl.flock(fd, operation, /)

   Realiza la operación de bloqueo *operation* sobre el descriptor de
   fichero *fd* (también se aceptan objetos de fichero que
   proporcionen un método "fileno()"). Ver el manual de Unix
   *flock(2)* para más detalles. (En algunos sistemas, esta función es
   emulada usando "fcntl()".)

   If the "flock()" call fails, an "OSError" exception is raised.

   Lanza un evento de auditoria "fcntl.flock" con argumentos "fd",
   "operation".

fcntl.lockf(fd, cmd, len=0, start=0, whence=0, /)

   Esto es esencialmente un "wrapper" de las llamadas de bloqueo
   "fcntl()". *fd* es el descriptor de fichero (también se aceptan
   objetos de fichero que proporcionen un método "fileno()") del
   archivo para bloquear o desbloquear, y *cmd* es uno de los
   siguientes valores:

   fcntl.LOCK_UN

      Release an existing lock.

   fcntl.LOCK_SH

      Acquire a shared lock.

   fcntl.LOCK_EX

      Acquire an exclusive lock.

   fcntl.LOCK_NB

      Bitwise OR with any of the other three "LOCK_*" constants to
      make the request non-blocking.

   If "LOCK_NB" is used and the lock cannot be acquired, an "OSError"
   will be raised and the exception will have an *errno* attribute set
   to "EACCES" or "EAGAIN" (depending on the operating system; for
   portability, check for both values).  On at least some systems,
   "LOCK_EX" can only be used if the file descriptor refers to a file
   opened for writing.

   *len* es el número de bytes a bloquear, *start* es el
   desplazamiento de bytes en el que comienza el bloqueo, relativo a
   *whence*, y *whence* es como con "io.IOBase.seek()",
   específicamente:

   * "0" -- relativo al inicio del archivo ("os.SEEK_SET")

   * "1" -- relativo a la posición actual del buffer ("os.SEEK_CUR")

   * "2" -- relativo al final del archivo ("os.SEEK_END")

   El valor por defecto de*start* es 0, lo que significa que comienza
   al inicio del archivo. El valor por defecto para *len* es 0 lo que
   significa bloquear hasta el final del archivo. El valor por defecto
   para *whence* también es 0.

   Lanza un evento de auditoria "fcntl.lockf" con argumentos "fd",
   "cmd", "len", "start", "whence".

Ejemplos (todos en un sistema compatible con SVR4):

   import struct, fcntl, os

   f = open(...)
   rv = fcntl.fcntl(f, fcntl.F_SETFL, os.O_NDELAY)

   lockdata = struct.pack('hhllhh', fcntl.F_WRLCK, 0, 0, 0, 0, 0)
   rv = fcntl.fcntl(f, fcntl.F_SETLKW, lockdata)

Tenga en cuenta que en el primer ejemplo, el valor de la variable
retornada *rv* contendrá un valor entero; en el segundo ejemplo
contendrá un objeto "bytes". La estructura para la variable *lockdata*
depende del sistema --- por lo tanto, usar la llamada "flock()" puede
ser mejor.

Ver también:

  Módulo  "os"
     Si los indicadores de bloqueo "O_SHLOCK" y "O_EXLOCK" están
     presentes en el módulo "os" (sólo en BSD), la función "os.open()"
     proporciona una alternativa a las funciones "lockf()" y
     "flock()".
