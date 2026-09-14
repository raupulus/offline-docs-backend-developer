---
title: Unix-specific services
source_url: https://docs.python.org/es/3
source_path: library/unix.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 4390
---

# Unix-specific services

Los módulos descritos en este capítulo proporcionan interfaces para
las características exclusivas del sistema operativo Unix o, en
algunos casos, para algunas o muchas variantes del mismo.  He aquí una
visión general:

* "shlex" --- Simple lexical analysis

  * objetos "shlex"

  * Reglas de análisis

  * Compatibilidad mejorada con intérprete de comandos

* "posix" --- The most common POSIX system calls

  * Soporte de archivos grandes

  * Contenido notable del módulo

* "pwd" --- The password database

* "grp" --- The group database

* "termios" --- POSIX style tty control

  * Ejemplo

* "tty" --- Terminal control functions

* "pty" --- Pseudo-terminal utilities

  * Ejemplo

* "fcntl" --- The "fcntl" and "ioctl" system calls

* "resource" --- Resource usage information

  * Límites de recursos

  * Utilización de recursos

* "syslog" --- Unix syslog library routines

  * Ejemplos

    * Ejemplo sencillo
