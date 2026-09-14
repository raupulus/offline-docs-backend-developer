---
title: Comunicación en redes y entre procesos
source_url: https://docs.python.org/es/3
source_path: library/ipc.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 3050
---

# Comunicación en redes y entre procesos

Los módulos descritos en este capítulo proveen los mecanismos para la
comunicación en red y entre procesos.

Algunos módulos solo funcionan para dos procesos que están en una
misma máquina, e.g. "signal" y "mmap". Otros módulos soportan
protocolos de red que dos o mas procesos pueden utilizar para
comunicarse entre máquinas.

La lista de módulos descritos en este capítulo es:

* "asyncio" --- Asynchronous I/O

* "socket" --- Low-level networking interface

* "ssl" --- TLS/SSL wrapper for socket objects

* "select" --- Waiting for I/O completion

* "selectors" --- High-level I/O multiplexing

* "signal" --- Set handlers for asynchronous events

* "mmap" --- Memory-mapped file support
