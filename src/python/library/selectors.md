---
title: '"selectors" --- High-level I/O multiplexing'
source_url: https://docs.python.org/es/3
source_path: library/selectors.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 3750
---

# "selectors" --- High-level I/O multiplexing

Added in version 3.4.

**Código fuente:** Lib/selectors.py

======================================================================

## Introducción

Este módulo permite multiplexación de E/S eficiente y de alto nivel,
basada en los primitivos del módulo "select". Se recomienda a los
usuarios utilizar este módulo en su lugar, a menos que deseen un
control preciso sobre los primitivos a nivel de sistema operativo
utilizados.

It defines a "BaseSelector" abstract base class, along with several
concrete implementations ("KqueueSelector", "EpollSelector"...), that
can be used to wait for I/O readiness notification on multiple file
objects. In the following, "file object" refers to any object with a
"fileno()" method, or a raw file descriptor. See *file object*.

"DefaultSelector" es un alias de la implementación más eficiente
disponible en la plataforma actual: esta debería ser la opción
predeterminada para la mayoría de los usuarios.

Nota:

  El tipo de objetos de archivo admitidos depende de la plataforma: en
  Windows, se admiten sockets, pero no *pipes*, mientras que en Unix,
  ambos son compatibles (también se pueden admitir algunos otros
  tipos, como FIFOs o dispositivos de archivo especiales).

Ver también:

  "select"
     Módulo de multiplexación de E/S de bajo nivel.

Availability: not WASI.

This module does not work or is not available on WebAssembly. See
Plataformas WebAssembly for more information.

## Clases

Jerarquía de clases:

   BaseSelector
   +-- SelectSelector
   +-- PollSelector
   +-- EpollSelector
   +-- DevpollSelector
   +-- KqueueSelector

In the following, *events* is a bitwise mask indicating which I/O
events should be waited for on a given file object. It can be a
combination of the module's constants below:

   +-------------------------+-------------------------------------------------+
   | Constante               | Significado                                     |
   |=========================|=================================================|
   | selectors.EVENT_READ    | Disponible para lectura                         |
   +-------------------------+-------------------------------------------------+
   | selectors.EVENT_WRITE   | Disponible para escritura                       |
   +-------------------------+-------------------------------------------------+

class selectors.SelectorKey

   La clase "SelectorKey" es una "namedtuple" que se utiliza para
   asociar un objeto de archivo a su descriptor de archivo subyacente,
   máscara de evento seleccionada y datos adjuntos. Es retornada por
   varios métodos "BaseSelector".

   fileobj

      Objeto de archivo registrado.

   fd

      Descriptor de archivo subyacente.

   events

      Eventos que se deben esperar en este objeto de archivo.

   data

      Datos opacos opcionales asociados a este objeto de archivo: por
      ejemplo, podría usarse para almacenar un ID de sesión por
      cliente.

class selectors.BaseSelector

   Un "BaseSelector" se usa para esperar a que el evento de E/S esté
   listo en varios objetos de archivo. Admite el registro y la
   cancelación del registro de secuencias de archivos y un método para
   esperar eventos de E/S en esas secuencias, con un tiempo de espera
   opcional. Es una clase base abstracta, por lo que no se puede crear
   una instancia. Use "DefaultSelector" en su lugar, o un
   "SelectSelector", "KqueueSelector", etc. si deseas usar
   específicamente una implementación y su plataforma la admite.
   "BaseSelector" y sus implementaciones concretas soportan el
   protocolo *context manager*.

   abstractmethod register(fileobj, events, data=None)

      Registra un objeto de archivo para su selección y lo monitoriza
      en busca de eventos de E/S.

      *fileobj* es el objeto de archivo a monitorear.  Puede ser un
      descriptor de archivo de tipo entero o un objeto con un método
      "fileno()". *events* es una máscara bit a bit de eventos para
      monitorear. *data* es un objeto opaco.

      Esto retorna una nueva instancia "SelectorKey", o lanza un
      "ValueError" en caso de una máscara de evento o un descriptor de
      archivo no válidos, o "KeyError" si el objeto de archivo ya está
      registrado.

   abstractmethod unregister(fileobj)

      Anula el registro de un objeto de archivo de la selección y lo
      elimina del monitoreo. Se anulará el registro de un objeto de
      archivo antes de cerrarlo.

      *fileobj* debe ser un objeto de archivo previamente registrado.

      Esto retorna la instancia "SelectorKey" asociada, o lanza un
      "KeyError" si *fileobj* no está registrado. Se lanzará un
      "ValueError" si *fileobj* no es válido (por ejemplo, no tiene el
      método "fileno ()" o su método "fileno ()" tiene un valor de
      retorno no válido).

   modify(fileobj, events, data=None)

      Cambia los eventos monitorizados de un objeto de archivo
      registrado o los datos adjuntos.

      Esto es equivalente a *BaseSelector.unregister(fileobj)* seguido
      de *BaseSelector.register(fileobj, events, data)*, excepto que
      se puede implementar de manera más eficiente.

      Esto retorna una nueva instancia de "SelectorKey", o lanza un
      "ValueError" en caso de una máscara de evento o un descriptor de
      archivo no válidos, o "KeyError" si el objeto de archivo no está
      registrado.

   abstractmethod select(timeout=None)

      Espera hasta que algunos objetos de archivo registrados estén
      listos o el tiempo de espera expire.

      Si "timeout > 0", esto especifica el tiempo máximo de espera, en
      segundos. Si "timeout <= 0", la llamada no se bloqueará y
      reportará los objetos de archivo actualmente listos. Si
      *timeout* es "None", la llamada se bloqueará hasta que un objeto
      de archivo monitorizado esté listo.

      Retorna una lista de tuplas "(key, events)", una por cada objeto
      de archivo listo.

      *key* es la instancia "SelectorKey" correspondiente a un objeto
      de archivo listo. *events* es una máscara de bits de eventos
      listos en este objeto de archivo.

      Nota:

        Este método puede regresar antes de que cualquier objeto de
        archivo esté listo o haya transcurrido el tiempo de espera si
        el proceso actual recibe una señal: en este caso, se retornará
        una lista vacía.

      Distinto en la versión 3.5: El selector ahora se reintenta con
      un tiempo de espera recalculado cuando es interrumpido por una
      señal si el gestor de señales no lanzó una excepción (ver **PEP
      475** para la justificación), en lugar de retornar una lista
      vacía de eventos antes del tiempo de espera.

   close()

      Cierra el selector.

      Se debe llamar para asegurarse de que se libera cualquier
      recurso subyacente. El selector no se utilizará una vez cerrado.

   get_key(fileobj)

      Retorna la clave asociada con un objeto de archivo registrado.

      Esto retorna la instancia "SelectorKey" asociada a este objeto
      de archivo, o lanza un "KeyError" si el objeto de archivo no
      está registrado.

   abstractmethod get_map()

      Retorna un mapeo asociando objetos de archivo a las llaves del
      selector.

      Retorna una instancia de "Mapping" mapeando objetos de archivo
      registrados a su instancia "SelectorKey" asociada.

class selectors.DefaultSelector

   La clase de selector predeterminada, utiliza la implementación más
   eficiente disponible en la plataforma actual. Esta debería ser la
   opción predeterminada para la mayoría de los usuarios.

class selectors.SelectSelector

   Selector basado en "select.select()".

class selectors.PollSelector

   Selector basado en "select.poll()".

class selectors.EpollSelector

   Selector basado en "select.epoll()".

   fileno()

      Esto retorna el descriptor de archivo utilizado por el objeto
      "select.epoll()" subyacente.

class selectors.DevpollSelector

   Selector basado en "select.devpoll()".

   fileno()

      Esto retorna el descriptor de archivo utilizado por el objeto
      "select.devpoll()" subyacente.

   Added in version 3.5.

class selectors.KqueueSelector

   Selector basado en "select.kqueue()".

   fileno()

      Esto retorna el descriptor de archivo utilizado por el objeto
      "select.kqueue()" subyacente.

## Ejemplos

Aquí hay una implementación simple de un servidor de eco:

   import selectors
   import socket

   sel = selectors.DefaultSelector()

   def accept(sock, mask):
       conn, addr = sock.accept()  # Should be ready
       print('accepted', conn, 'from', addr)
       conn.setblocking(False)
       sel.register(conn, selectors.EVENT_READ, read)

   def read(conn, mask):
       data = conn.recv(1000)  # Should be ready
       if data:
           print('echoing', repr(data), 'to', conn)
           conn.send(data)  # Hope it won't block
       else:
           print('closing', conn)
           sel.unregister(conn)
           conn.close()

   sock = socket.socket()
   sock.bind(('localhost', 1234))
   sock.listen(100)
   sock.setblocking(False)
   sel.register(sock, selectors.EVENT_READ, accept)

   while True:
       events = sel.select()
       for key, mask in events:
           callback = key.data
           callback(key.fileobj, mask)
