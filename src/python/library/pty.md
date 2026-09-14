---
title: '"pty" --- Pseudo-terminal utilities'
source_url: https://docs.python.org/es/3
source_path: library/pty.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 3540
---

# "pty" --- Pseudo-terminal utilities

**Código Fuente:** Lib/pty.py

======================================================================

The "pty" module defines operations for handling the pseudo-terminal
concept: starting another process and being able to write to and read
from its controlling terminal programmatically.

Availability: Unix.

El manejo de pseudo-terminales depende en gran medida de la
plataforma. Este código se prueba principalmente en Linux, FreeBSD y
macOS (se supone que funciona en otras plataformas POSIX, pero no se
ha probado a fondo).

The "pty" module defines the following functions:

pty.fork()

   Bifurcación. Conectar en su propia terminal (terminal hijo) una
   pseudo-terminal. El valor de retorno es "(pid, fd)". Tener en
   cuenta que la terminal hijo tiene como valor *pid* 0 y *fd* es
   *invalid*. El valor de retorno del padre es el *pid* del hijo, y
   *fd* es un descriptor de archivo conectado a la terminal hijo
   (también a la salida y entrada estándar de la terminal hijo)

   Advertencia:

     On macOS the use of this function is unsafe when mixed with using
     higher-level system APIs, and that includes using
     "urllib.request".

pty.openpty()

   Abre un nuevo par de pseudo-terminales, usando "os.openpty()", o
   código de emulación para sistemas genéricos de Unix. Retorna un par
   de descriptores de archivo "(master, slave)", para el *master* y el
   *slave* respectivamente.

pty.spawn(argv[, master_read[, stdin_read]])

   Genera un proceso conectado a su terminal con el io estándar del
   proceso actual. Esto se usa a frecuentemente para confundir
   programas que insisten en leer desde la terminal de control. Se
   espera que el proceso generado detrás de pty sea finalizado y
   cuando lo haga *spawn* se retornará.

   Un bucle copia STDIN del proceso actual al hijo y los datos
   recibidos del niño a STDOUT del proceso actual. No se le indica al
   hijo si STDIN del proceso actual se cierra.

   A las funciones *master_read* y *stdin_read* se les pasa un
   descriptor de archivo del cual deben leer, y siempre deben retornar
   una cadena de bytes. Para forzar el retorno de spawn antes de que
   el proceso hijo salga, se debe retornar un arreglo de bytes vacía
   para señalar el final del archivo.

   La implementación predeterminada para ambas funciones retornará
   hasta 1024 bytes cada vez que se llamen. El dato retornado de
   *master_read* se pasa al descriptor de archivo maestro para leer la
   salida del proceso hijo, y *stdin_read* pasa el descriptor de
   archivo 0, para leer desde la entrada del proceso padre.

   Retornando una cadena de bytes vacía de cualquier llamado es
   interpretado como una condición de fin de archivo (EOF), y el
   llamado no se realizará después de eso. Si *stdin_read* retorna EOF
   la terminal de control ya no puede comunicarse con el proceso padre
   o el proceso hijo. A menos que el proceso hijo se cierre sin
   ninguna entrada *spawn* se repetirá para siempre. Si *master_read*
   retorna EOF se produce el mismo comportamiento (al menos en Linux)

   Retorna el valor del estado de salida de "os.waitpid()" en el
   proceso hijo.

   "os.waitstatus_to_exitcode()" se puede utilizar para convertir el
   estado de salida en un código de salida.

   Lanza un evento de auditoria "pty.spawn"  con el argumento "argv".

   Distinto en la versión 3.4: "spawn()" ahora retorna el valor de
   estado de  "os.waitpid()" para los procesos hijos.

## Ejemplo

El siguiente programa actúa como el comando de Unix *script(1)*,
usando una pseudo-terminal para registrar todas las entradas y salidas
de una sesión en "typescript".

   import argparse
   import os
   import pty
   import sys
   import time

   parser = argparse.ArgumentParser()
   parser.add_argument('-a', dest='append', action='store_true')
   parser.add_argument('-p', dest='use_python', action='store_true')
   parser.add_argument('filename', nargs='?', default='typescript')
   options = parser.parse_args()

   shell = sys.executable if options.use_python else os.environ.get('SHELL', 'sh')
   filename = options.filename
   mode = 'ab' if options.append else 'wb'

   with open(filename, mode) as script:
       def read(fd):
           data = os.read(fd, 1024)
           script.write(data)
           return data

       print('Script started, file is', filename)
       script.write(('Script started on %s\n' % time.asctime()).encode())

       pty.spawn(shell, read)

       script.write(('Script done on %s\n' % time.asctime()).encode())
       print('Script done, file is', filename)
