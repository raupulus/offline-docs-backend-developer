---
title: Soporte de plataforma
source_url: https://docs.python.org/es/3
source_path: library/asyncio-platforms.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 1660
---

# Soporte de plataforma

El módulo "asyncio" está diseñado para ser portátil, pero algunas
plataformas tienen diferencias y limitaciones sutiles debido a la
arquitectura y las capacidades subyacentes de las plataformas.

## Todas las plataformas

* "loop.add_reader()" y "loop.add_writer()" no se pueden utilizar para
  supervisar la E/S del archivo.

* "loop.connect_read_pipe()" and "loop.connect_write_pipe()" cannot be
  used with regular files.  See Supported pipe objects for the objects
  that are accepted on each platform.

## Windows

**Código fuente:** Lib/asyncio/proactor_events.py,
Lib/asyncio/windows_events.py, Lib/asyncio/windows_utils.py

======================================================================

Distinto en la versión 3.8: En Windows, "ProactorEventLoop" es ahora
el bucle de eventos predeterminado.

Todos los bucles de eventos en Windows no admiten los métodos
siguientes:

* "loop.create_unix_connection()" y "loop.create_unix_server()" no son
  compatibles. La familia de sockets "socket.AF_UNIX" es específica de
  Unix.

* "loop.add_signal_handler()" y "loop.remove_signal_handler()" no son
  compatibles.

"SelectorEventLoop" tiene las siguientes limitaciones:

* "SelectSelector" se utiliza para esperar los eventos de los sockets:
  soporta los sockets y está limitado a 512 sockets.

* "loop.add_reader()" y "loop.add_writer()" sólo aceptan manejadores
  de sockets (por ejemplo, los descriptores de archivos de tuberías no
  están soportados).

* Las tuberías no están soportadas, por lo que los métodos
  "loop.connect_read_pipe()" y "loop.connect_write_pipe()" no están
  implementados.

* Subprocesos no están soportados, es decir, los métodos
  "loop.subprocess_exec()" y "loop.subprocess_shell()" no están
  implementados.

"ProactorEventLoop" tiene las siguientes limitaciones:

* Los métodos "loop.add_reader()" y "loop.add_writer()" no están
  soportados.

* "loop.connect_read_pipe()" and "loop.connect_write_pipe()" only
  accept a handle opened for overlapped I/O. See Supported pipe
  objects for which objects are supported.

La resolución del reloj monótono de Windows suele ser de unos 15,6
milisegundos. La mejor resolución es de 0,5 milisegundos. La
resolución depende del hardware (disponibilidad de HPET) y de la
configuración de Windows.

### Soporte de sub-procesos en Windows

En Windows, el bucle de eventos por defecto "ProactorEventLoop"
soporta subprocesos, mientras que "SelectorEventLoop" no lo hace.

## macOS

Las versiones modernas de MacOS son totalmente compatibles.

-[ macOS <= 10.8 ]-

En macOS 10.6, 10.7 y 10.8, el bucle de eventos por defecto utiliza
"selectors.KqueueSelector", que no soporta dispositivos de caracteres
en estas versiones. El "SelectorEventLoop" puede ser configurado
manualmente para usar "SelectSelector" o "PollSelector" para soportar
dispositivos de caracteres en estas versiones antiguas de macOS.
Ejemplo:

   import asyncio
   import selectors

   selector = selectors.SelectSelector()
   loop = asyncio.SelectorEventLoop(selector)
   asyncio.set_event_loop(loop)
