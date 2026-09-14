---
title: '"errno" --- Standard errno system symbols'
source_url: https://docs.python.org/es/3
source_path: library/errno.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 2560
---

# "errno" --- Standard errno system symbols

======================================================================

Este módulo pone a disposición los símbolos del sistema "errno"
estándar. El valor de cada símbolo es el valor entero correspondiente.
Los nombres y las descripciones se toman prestados de
"linux/include/errno.h", que debería incluir todo.

errno.errorcode

   Diccionario que proporciona un mapeo del valor de errno al nombre
   de la cadena en el sistema subyacente. Por ejemplo,
   "errno.errorcode[errno.EPERM]" se asigna a "'EPERM'".

Para traducir un código de error numérico en un mensaje de error, use
"os.strerror()".

De la siguiente lista, los símbolos que no se utilizan en la
plataforma actual no están definidos por el módulo. La lista
específica de símbolos definidos está disponible como
"errno.errorcode.keys()". Los símbolos disponibles pueden incluir:

errno.EPERM

   Operación no permitida. Este error se asigna a la excepción
   "PermissionError".

errno.ENOENT

   El archivo o directorio no existe. Este error se asigna a la
   excepción "FileNotFoundError".

errno.ESRCH

   No hay tal proceso. Este error se asigna a la excepción
   "ProcessLookupError".

errno.EINTR

   Llamada al sistema interrumpida. Este error se asigna a la
   excepción "InterruptedError".

errno.EIO

   Error de E/S

errno.ENXIO

   No existe tal dispositivo o dirección

errno.E2BIG

   Lista de argumentos demasiado larga

errno.ENOEXEC

   Error de formato de ejecución

errno.EBADF

   Número de archivo incorrecto

errno.ECHILD

   No hay procesos secundarios. Este error se asigna a la excepción
   "ChildProcessError".

errno.EAGAIN

   Intentar otra vez. Este error se asigna a la excepción
   "BlockingIOError".

errno.ENOMEM

   Sin memoria

errno.EACCES

   Permiso denegado. Este error se asigna a la excepción
   "PermissionError".

errno.EFAULT

   Dirección incorrecta

errno.ENOTBLK

   Bloquear dispositivo requerido

errno.EBUSY

   Dispositivo o recurso ocupado

errno.EEXIST

   El archivo existe. Este error se asigna a la excepción
   "FileExistsError".

errno.EXDEV

   Enlace entre dispositivos

errno.ENODEV

   Hay tal dispositivo

errno.ENOTDIR

   No es un directorio. Este error se asigna a la excepción
   "NotADirectoryError".

errno.EISDIR

   Es un directorio. Este error se asigna a la excepción
   "IsADirectoryError".

errno.EINVAL

   Argumento inválido

errno.ENFILE

   Desbordamiento de la tabla de archivos

errno.EMFILE

   Demasiados archivos abiertos

errno.ENOTTY

   No es un typewriter

errno.ETXTBSY

   Archivo de texto ocupado

errno.EFBIG

   Archivo demasiado grande

errno.ENOSPC

   No queda espacio en el dispositivo

errno.ESPIPE

   Búsqueda ilegal

errno.EROFS

   Sistema de archivos de sólo lectura

errno.EMLINK

   Demasiados enlaces

errno.EPIPE

   Tubería rota. Este error se asigna a la excepción
   "BrokenPipeError".

errno.EDOM

   Argumento matemático fuera del dominio de función

errno.ERANGE

   Resultado matemático no representable

errno.EDEADLK

   Podría ocurrir un bloqueo de recursos

errno.ENAMETOOLONG

   Nombre de archivo demasiado largo

errno.ENOLCK

   No hay bloqueos de registro disponibles

errno.ENOSYS

   Función no implementada

errno.ENOTEMPTY

   Directorio no vacío

errno.ELOOP

   Se han encontrado demasiados enlaces simbólicos

errno.EWOULDBLOCK

   La operación se bloquearía. Este error se asigna a la excepción
   "BlockingIOError".

errno.ENOMSG

   Ningún mensaje del tipo deseado

errno.EIDRM

   Identificador eliminado

errno.ECHRNG

   Número de canal fuera de rango

errno.EL2NSYNC

   Nivel 2 no sincronizado

errno.EL3HLT

   Nivel 3 detenido

errno.EL3RST

   Nivel 3 restablecido

errno.ELNRNG

   Número de enlace fuera de rango

errno.EUNATCH

   Controlador de protocolo no adjunto

errno.ENOCSI

   No hay estructura CSI disponible

errno.EL2HLT

   Nivel 2 detenido

errno.EBADE

   Intercambio inválido

errno.EBADR

   Descriptor de solicitud inválido

errno.EXFULL

   Intercambio completo

errno.ENOANO

   Sin ánodo

errno.EBADRQC

   Código de solicitud inválido

errno.EBADSLT

   Ranura inválida

errno.EDEADLOCK

   Error de interbloqueo de bloqueo de archivos

errno.EBFONT

   Formato de archivo de fuente incorrecto

errno.ENOSTR

   El dispositivo no es una secuencia

errno.ENODATA

   Datos no disponibles

errno.ETIME

   Temporizador expirado

errno.ENOSR

   Recursos fuera de flujos

errno.ENONET

   La computadora no está en la red

errno.ENOPKG

   Paquete no instalado

errno.EREMOTE

   El objeto es remoto

errno.ENOLINK

   El enlace ha sido cortado

errno.EADV

   Error de publicidad

errno.ESRMNT

   Error de Srmount

errno.ECOMM

   Error de comunicación al enviar

errno.EPROTO

   Error de protocolo

errno.EMULTIHOP

   Intento de salto múltiple

errno.EDOTDOT

   Error específico de RFS (por su significado en inglés *Remote File
   System*)

errno.EBADMSG

   No es un mensaje de datos

errno.EOVERFLOW

   Valor demasiado grande para el tipo de datos definido

errno.ENOTUNIQ

   Nombre no único en la red

errno.EBADFD

   Descriptor de archivo en mal estado

errno.EREMCHG

   La dirección remota cambió

errno.ELIBACC

   No se puede acceder a una biblioteca compartida necesaria

errno.ELIBBAD

   Accediendo a una biblioteca compartida dañada

errno.ELIBSCN

   Sección .lib en a.out corrupta

errno.ELIBMAX

   Intentando vincular demasiadas bibliotecas compartidas

errno.ELIBEXEC

   No se puede ejecutar una biblioteca compartida directamente

errno.EILSEQ

   Secuencia de byte ilegal

errno.ERESTART

   Llamada al sistema interrumpida debe reiniciarse

errno.ESTRPIPE

   Error de tubería de flujos

errno.EUSERS

   Demasiados usuarios

errno.ENOTSOCK

   Operación de socket en no-socket

errno.EDESTADDRREQ

   Dirección de destino requerida

errno.EMSGSIZE

   Mensaje demasiado largo

errno.EPROTOTYPE

   Protocolo de tipo incorrecto para socket

errno.ENOPROTOOPT

   Protocolo no disponible

errno.EPROTONOSUPPORT

   Protocolo no soportado

errno.ESOCKTNOSUPPORT

   Tipo de socket no soportado

errno.EOPNOTSUPP

   Operación no soportada en el endpoint de transporte

errno.ENOTSUP

   Operación no soportada

   Added in version 3.2.

errno.EPFNOSUPPORT

   Familia de protocolo no soportada

errno.EAFNOSUPPORT

   Familia de direcciones no soportada por protocolo

errno.EADDRINUSE

   Dirección ya en uso

errno.EADDRNOTAVAIL

   No se puede asignar la dirección solicitada

errno.ENETDOWN

   Red caída

errno.ENETUNREACH

   Red es inalcanzable

errno.ENETRESET

   Conexión de red interrumpida debido al reinicio

errno.ECONNABORTED

   El software causó falla de conexión. Este error se asigna a la
   excepción "ConnectionAbortedError".

errno.ECONNRESET

   Restablecimiento de la conexión por par. Este error se asigna a la
   excepción "ConnectionResetError".

errno.ENOBUFS

   No hay espacio de búfer disponible

errno.EISCONN

   El endpoint de transporte ya está conectado

errno.ENOTCONN

   El endpoint final de transporte no está conectado

errno.ESHUTDOWN

   No se puede enviar después del apagado del endpoint de transporte.
   Este error se asigna a la excepción "BrokenPipeError".

errno.ETOOMANYREFS

   Demasiadas referencias: no se puede empalmar

errno.ETIMEDOUT

   Tiempo de conexión agotado. Este error se asigna a la excepción
   "TimeoutError".

errno.ECONNREFUSED

   Conexión denegada. Este error se asigna a la excepción
   "ConnectionRefusedError".

errno.EHOSTDOWN

   Anfitrión caído

errno.EHOSTUNREACH

   Sin ruta al anfitrión

errno.EHWPOISON

   Memory page has hardware error.

   Added in version 3.14.

errno.EALREADY

   Operación ya en curso. Este error se asigna a la excepción
   "BlockingIOError".

errno.EINPROGRESS

   Operación ahora en curso. Este error se asigna a la excepción
   "BlockingIOError".

errno.ESTALE

   Manejador de archivos NFS (por su significado en inglés *Network
   File System*) obsoleto

errno.EUCLEAN

   La estructura necesita limpieza

errno.ENOTNAM

   No es un archivo de tipo con nombre XENIX

errno.ENAVAIL

   No hay semáforos XENIX disponibles

errno.EISNAM

   Es un archivo de tipo con nombre

errno.EREMOTEIO

   Error de E/S remota

errno.EDQUOT

   Cuota excedida

errno.EQFULL

   La cola de salida de la interfaz está llena

   Added in version 3.11.

errno.ENOMEDIUM

   No medium found

errno.EMEDIUMTYPE

   Wrong medium type

errno.ENOKEY

   Required key not available

errno.EKEYEXPIRED

   Key has expired

errno.EKEYREVOKED

   Key has been revoked

errno.EKEYREJECTED

   Key was rejected by service

errno.ERFKILL

   Operation not possible due to RF-kill

errno.ELOCKUNMAPPED

   Locked lock was unmapped

errno.ENOTACTIVE

   Facility is not active

errno.EAUTH

   Authentication error

   Added in version 3.2.

errno.EBADARCH

   Bad CPU type in executable

   Added in version 3.2.

errno.EBADEXEC

   Bad executable (or shared library)

   Added in version 3.2.

errno.EBADMACHO

   Malformed Mach-o file

   Added in version 3.2.

errno.EDEVERR

   Device error

   Added in version 3.2.

errno.EFTYPE

   Inappropriate file type or format

   Added in version 3.2.

errno.ENEEDAUTH

   Need authenticator

   Added in version 3.2.

errno.ENOATTR

   Attribute not found

   Added in version 3.2.

errno.ENOPOLICY

   Policy not found

   Added in version 3.2.

errno.EPROCLIM

   Too many processes

   Added in version 3.2.

errno.EPROCUNAVAIL

   Bad procedure for program

   Added in version 3.2.

errno.EPROGMISMATCH

   Program version wrong

   Added in version 3.2.

errno.EPROGUNAVAIL

   RPC prog. not avail

   Added in version 3.2.

errno.EPWROFF

   Device power is off

   Added in version 3.2.

errno.EBADRPC

   RPC struct is bad

   Added in version 3.2.

errno.ERPCMISMATCH

   RPC version wrong

   Added in version 3.2.

errno.ESHLIBVERS

   Shared library version mismatch

   Added in version 3.2.

errno.ENOTCAPABLE

   Capacidades insuficientes. Este error se asigna a la excepción
   "PermissionError".

   Availability: WASI, FreeBSD

   Added in version 3.11.1.

errno.ECANCELED

   Operación cancelada

   Added in version 3.2.

errno.EOWNERDEAD

   El propietario murió

   Added in version 3.2.

errno.ENOTRECOVERABLE

   Estado no recuperable

   Added in version 3.2.
