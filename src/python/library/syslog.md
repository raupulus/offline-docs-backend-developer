---
title: '"syslog" --- Unix syslog library routines'
source_url: https://docs.python.org/es/3
source_path: library/syslog.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 4040
---

# "syslog" --- Unix syslog library routines

======================================================================

Este módulo ofrece una interfaz a las rutinas de la biblioteca
"syslog" de Unix. Consulte las páginas del manual de Unix para una
descripción detallada de la *facility* (es así como se llama en la
documentación a un subsistema de aplicaciones) "syslog".

Availability: Unix, not WASI, not iOS.

This module wraps the system "syslog" family of routines.  A pure
Python library that can speak to a syslog server is available in the
"logging.handlers" module as "SysLogHandler".

El módulo define las siguientes funciones:

syslog.syslog(message)
syslog.syslog(priority, message)

   Envía la cadena de caracteres *message* al registrador del sistema.
   Se añade un final de línea si es necesario. Cada mensaje se
   etiqueta con una prioridad compuesta por una *facility* y un
   *nivel*. El argumento opcional *priority*, que por defecto es
   "LOG_INFO", determina la prioridad del mensaje. Si la *facility* no
   está codificada en *priority* usando un OR lógico ("LOG_INFO |
   LOG_USER"), se usará el valor con el que se llama a "openlog()".

   Si "openlog()" no se ha llamado antes de la llamada a "syslog()",
   entonces "openlog()" se llamará sin argumentos.

   Lanza un evento de auditoría "syslog.syslog" con los argumentos
   "priority", "message".

   Distinto en la versión 3.2: En versiones anteriores, "openlog()" no
   sería llamado automáticamente si no fuera un llamado previo de la
   llamada a la función "syslog()", postergando la implementación de
   syslog para llamar a "openlog()".

   Distinto en la versión 3.12: Esta función está restringida en
   subintérpretes. (Solo el código que se ejecuta en múltiples
   intérpretes se ve afectado y la restricción no es relevante para la
   mayoría de los usuarios.) "openlog()" debe ser llamada en el
   intérprete principal antes de que "syslog()" pueda ser utilizada en
   un subintérprete. De lo contrario, lanzará "RuntimeError".

syslog.openlog([ident[, logoption[, facility]]])

   Las opciones de registro de las llamadas a "syslog()" pueden
   establecerse llamando a la función "openlog()". "syslog()" llamará
   a "openlog()" sin argumentos si el registro no está abierto
   actualmente.

   El argumento por palabra clave opcional *ident* es una cadena de
   caracteres que precede a cada mensaje, y por defecto es
   "sys.argv[0]" retirando los componentes delanteros de la ruta. El
   argumento nombrado opcional *logoption* (por defecto es 0) es un
   campo de tipo bit -- véanse a continuación los posibles valores que
   pueden combinarse. El argumento nombrado opcional *facility* (por
   defecto es "LOG_USER") establece una *facility* por defecto para
   mensajes que no tienen una *facility* explícitamente codificada.

   Lanza un evento de auditoría "syslog.openlog" con los argumentos
   "ident", "logoption", "facility".

   Distinto en la versión 3.2: En versiones anteriores, argumentos por
   palabras llave no eran permitidos, y la *ident* era obligatoria.

   Distinto en la versión 3.12: Esta función está restringida en
   subintérpretes. (Solo el código que se ejecuta en múltiples
   intérpretes se ve afectado y la restricción no es relevante para la
   mayoría de los usuarios.) Esta solo puede ser llamada en el
   intérprete principal. Lanzará "RuntimeError" si se llama en un
   subintérprete.

syslog.closelog()

   Reinicia los valores del módulo syslog y llama a la librería del
   sistema "closelog()".

   Esto provoca que el módulo actúe como lo hacía cuando fue importado
   inicialmente. Por ejemplo, se llamará a "openlog()" en la primera
   llamada a "syslog()" (si no se ha llamado a "openlog()" ya), e
   *ident* y otros parámetros de "openlog()" se reiniciarán a sus
   valores por defecto.

   Lanza un evento de auditoría "syslog.closelog" sin argumentos.

   Distinto en la versión 3.12: Esta función está restringida en
   subintérpretes. (Solo el código que se ejecuta en múltiples
   intérpretes se ve afectado y la restricción no es relevante para la
   mayoría de los usuarios.) Esta solo puede ser llamada en el
   intérprete principal. Lanzará "RuntimeError" si se llama en un
   subintérprete.

syslog.setlogmask(maskpri)

   Asigna la máscara de prioridad a *maskpri* y retorna el valor
   anterior de la máscara. Las llamadas a "syslog()" con un nivel de
   prioridad no asignado en *maskpri* se ignoran. El comportamiento
   por defecto es registrar todas las prioridades. La función
   "LOG_MASK(pri)" calcula la máscara para la prioridad individual
   *pri*. La función "LOG_UPTO(pri)" calcula la máscara para todas las
   prioridades mayores o iguales que *pri*.

   Lanza un evento de auditoría "syslog.setlogmask" con argumento
   "maskpri".

El módulo define las siguientes constantes:

syslog.LOG_EMERG
syslog.LOG_ALERT
syslog.LOG_CRIT
syslog.LOG_ERR
syslog.LOG_WARNING
syslog.LOG_NOTICE
syslog.LOG_INFO
syslog.LOG_DEBUG

   Priority levels (high to low).

syslog.LOG_AUTH
syslog.LOG_AUTHPRIV
syslog.LOG_CRON
syslog.LOG_DAEMON
syslog.LOG_FTP
syslog.LOG_INSTALL
syslog.LOG_KERN
syslog.LOG_LAUNCHD
syslog.LOG_LPR
syslog.LOG_MAIL
syslog.LOG_NETINFO
syslog.LOG_NEWS
syslog.LOG_RAS
syslog.LOG_REMOTEAUTH
syslog.LOG_SYSLOG
syslog.LOG_USER
syslog.LOG_UUCP
syslog.LOG_LOCAL0
syslog.LOG_LOCAL1
syslog.LOG_LOCAL2
syslog.LOG_LOCAL3
syslog.LOG_LOCAL4
syslog.LOG_LOCAL5
syslog.LOG_LOCAL6
syslog.LOG_LOCAL7

   Facilities, depending on availability in "<syslog.h>" for
   "LOG_AUTHPRIV", "LOG_FTP", "LOG_NETINFO", "LOG_REMOTEAUTH",
   "LOG_INSTALL" and "LOG_RAS".

   Distinto en la versión 3.13: Added "LOG_FTP", "LOG_NETINFO",
   "LOG_REMOTEAUTH", "LOG_INSTALL", "LOG_RAS", and "LOG_LAUNCHD".

syslog.LOG_PID
syslog.LOG_CONS
syslog.LOG_NDELAY
syslog.LOG_ODELAY
syslog.LOG_NOWAIT
syslog.LOG_PERROR

   Log options, depending on availability in "<syslog.h>" for
   "LOG_ODELAY", "LOG_NOWAIT" and "LOG_PERROR".

## Ejemplos

### Ejemplo sencillo

Un conjunto sencillo de ejemplos:

   import syslog

   syslog.syslog('Processing started')
   if error:
       syslog.syslog(syslog.LOG_ERR, 'Processing started')

Un ejemplo de configuración de varias opciones de registro, que
incluirán el identificador del proceso en los mensajes registrados, y
escribirán los mensajes a la facility de destino usada para el
registro de correo:

   syslog.openlog(logoption=syslog.LOG_PID, facility=syslog.LOG_MAIL)
   syslog.syslog('E-mail processing initiated...')
