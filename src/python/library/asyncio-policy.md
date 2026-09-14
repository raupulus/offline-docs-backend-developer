---
title: Políticas
source_url: https://docs.python.org/es/3
source_path: library/asyncio-policy.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 1670
---

# Políticas

Advertencia:

  Policies are deprecated and will be removed in Python 3.16. Users
  are encouraged to use the "asyncio.run()" function or the
  "asyncio.Runner" with *loop_factory* to use the desired loop
  implementation.

Una política de bucle de eventos es un objeto global que se utiliza
para obtener y establecer el bucle de eventos actual o para crear
nuevos bucles de eventos. La política preestablecida puede ser
reemplazada con alternativas built-in para usar diferentes
implementaciones de bucles de eventos, o sustituida por una política
personalizada la cual puede anular estos comportamientos.

El objeto de política obtiene y establece un bucle de eventos separado
por *contexto*. Por defecto, esto se realiza por hilo, aunque las
políticas personalizadas pueden definir el *contexto* de una forma
diferente.

Las políticas de bucle de eventos personalizadas pueden controlar el
comportamiento de "get_event_loop()", "set_event_loop()", y
"new_event_loop()".

Los objetos de política deberían implementar las APIs definidas en la
clase abstracta base "AbstractEventLoopPolicy".

## Obteniendo y configurando la política

Las siguientes funciones pueden ser usadas para obtener y configurar
la política de los procesos actuales:

asyncio.get_event_loop_policy()

   Retorna la política actual en todo el proceso.

   Obsoleto desde la versión 3.14: The "get_event_loop_policy()"
   function is deprecated and will be removed in Python 3.16.

asyncio.set_event_loop_policy(policy)

   Establece la política actual en todo el proceso a *policy*.

   Si *policy* está configurado a "None", la política por defecto se
   reestablece.

   Obsoleto desde la versión 3.14: The "set_event_loop_policy()"
   function is deprecated and will be removed in Python 3.16.

## Objetos de política

La clase base de política de bucle de eventos abstractos se define de
la siguiente manera:

class asyncio.AbstractEventLoopPolicy

   Una clase base abstracta para políticas asyncio.

   get_event_loop()

      Retorna el bucle de eventos para el contexto actual.

      Retorna un objeto bucle de eventos implementando la interfaz
      "AbstractEventLoop".

      Este método nunca debería retornar "None".

      Distinto en la versión 3.6.

   set_event_loop(loop)

      Establece el bucle de eventos para el contexto a *loop*.

   new_event_loop()

      Crea y retorna un nuevo objeto de bucle de eventos.

      Este método nunca debería retornar "None".

   Obsoleto desde la versión 3.14: The "AbstractEventLoopPolicy" class
   is deprecated and will be removed in Python 3.16.

asyncio se envía con las siguientes políticas integradas:

class asyncio.DefaultEventLoopPolicy

   La política por defecto asyncio.  Usa "SelectorEventLoop" en Unix y
   "ProactorEventLoop" en Windows.

   No hay necesidad de instalar la política por defecto manualmente.
   asyncio está configurado para usar la política por defecto
   automáticamente.

   Distinto en la versión 3.8: En Windows, "ProactorEventLoop" ahora
   se usa por defecto.

   Distinto en la versión 3.14: The "get_event_loop()" method of the
   default asyncio policy now raises a "RuntimeError" if there is no
   set event loop.

   Obsoleto desde la versión 3.14: The "DefaultEventLoopPolicy" class
   is deprecated and will be removed in Python 3.16.

class asyncio.WindowsSelectorEventLoopPolicy

   Una política de bucle de eventos alternativa que usa la
   implementación de bucle de eventos "SelectorEventLoop".

   Availability: Windows.

   Obsoleto desde la versión 3.14: The
   "WindowsSelectorEventLoopPolicy" class is deprecated and will be
   removed in Python 3.16.

class asyncio.WindowsProactorEventLoopPolicy

   Una política de bucle de eventos alternativa que usa la
   implementación de bucle de eventos "ProactorEventLoop".

   Availability: Windows.

   Obsoleto desde la versión 3.14: The
   "WindowsProactorEventLoopPolicy" class is deprecated and will be
   removed in Python 3.16.

## Personalizar Políticas

Para implementar una nueva política de bucle de eventos, se recomienda
heredar "DefaultEventLoopPolicy" y sobreescribir los métodos para los
cuales se desea una conducta personalizada, por ejemplo:

   class MyEventLoopPolicy(asyncio.DefaultEventLoopPolicy):

       def get_event_loop(self):
           """Get the event loop.

           This may be None or an instance of EventLoop.
           """
           loop = super().get_event_loop()
           # Do something with loop ...
           return loop

   asyncio.set_event_loop_policy(MyEventLoopPolicy())
