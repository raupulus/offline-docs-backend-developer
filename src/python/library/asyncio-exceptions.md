---
title: Excepciones
source_url: https://docs.python.org/es/3
source_path: library/asyncio-exceptions.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 1610
---

# Excepciones

**Código Fuente** Lib/asyncio/exceptions.py

======================================================================

exception asyncio.TimeoutError

   Un alias obsoleto de "TimeoutError", lanzado cuando la operación ha
   superado el plazo establecido.

   Distinto en la versión 3.11: Esta clase es un alias de
   "TimeoutError".

exception asyncio.CancelledError

   La operación ha sido cancelada.

   Esta excepción se puede capturar para realizar operaciones
   personalizadas cuando se cancelan las tareas de asyncio. En casi
   todas las situaciones, la excepción debe volver a lanzarse.

   Distinto en la versión 3.8: "CancelledError" es ahora una subclase
   de "BaseException" en lugar de "Exception".

exception asyncio.InvalidStateError

   Estado Interno no válido de "Task" o "Future".

   Se puede lanzar en situaciones como establecer un valor de
   resultado para un objeto *Future* que ya tiene un valor de
   resultado establecido.

exception asyncio.SendfileNotAvailableError

   La llamada al sistema "sendfile" no esta disponible desde el
   *socket* o tipo de archivo dado.

   Una subclase de "RuntimeError".

exception asyncio.IncompleteReadError

   La operación de lectura solicitada no se completó completamente.

   Lanzado por la asyncio stream APIs.

   La excepción es una subclase de "EOFError".

   expected

      El número total ("int") de bytes esperados.

   partial

      Un cadena de "bytes" leída antes de que alcance al final del
      flujo.

exception asyncio.LimitOverrunError

   Alcanzó el límite de tamaño del búfer mientras buscaba un
   separador.

   Lanzado por asyncio stream APIs.

   consumed

      El número total de bytes que se consumirán.
