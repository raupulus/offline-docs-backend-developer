---
title: Libro de recetas de Logging
source_url: https://docs.python.org/es/3
source_path: howto/logging-cookbook.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: howto
order: 1310
---

# Libro de recetas de Logging

Autor:
   Vinay Sajip <vinay_sajip at red-dove dot com>

Esta página contiene un número de recetas sobre *logging*, que han
sido útiles en el pasado. Para obtener enlaces al tutorial e
información de referencia, consulte Otros recursos.

## Usar logging en múltiples módulos

Múltiples llamadas a "logging.getLogger('someLogger')" retornan una
referencia al mismo objeto logger. Esto es cierto no solo dentro del
mismo módulo, sino también en todos los módulos siempre que estén
ejecutándose en el mismo proceso del intérprete de Python. Es válido
para las referencias al mismo objeto. Además, el código de la
aplicación puede definir y configurar un logger primario en un módulo
y crear (pero no configurar) un logger secundario en un módulo
separado, y todas las llamadas al secundario pasarán al principal. A
continuación un módulo principal:

   import logging
   import auxiliary_module

   # create logger with 'spam_application'
   logger = logging.getLogger('spam_application')
   logger.setLevel(logging.DEBUG)
   # create file handler which logs even debug messages
   fh = logging.FileHandler('spam.log')
   fh.setLevel(logging.DEBUG)
   # create console handler with a higher log level
   ch = logging.StreamHandler()
   ch.setLevel(logging.ERROR)
   # create formatter and add it to the handlers
   formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
   fh.setFormatter(formatter)
   ch.setFormatter(formatter)
   # add the handlers to the logger
   logger.addHandler(fh)
   logger.addHandler(ch)

   logger.info('creating an instance of auxiliary_module.Auxiliary')
   a = auxiliary_module.Auxiliary()
   logger.info('created an instance of auxiliary_module.Auxiliary')
   logger.info('calling auxiliary_module.Auxiliary.do_something')
   a.do_something()
   logger.info('finished auxiliary_module.Auxiliary.do_something')
   logger.info('calling auxiliary_module.some_function()')
   auxiliary_module.some_function()
   logger.info('done with auxiliary_module.some_function()')

Y aquí un módulo auxiliar:

   import logging

   # create logger
   module_logger = logging.getLogger('spam_application.auxiliary')

   class Auxiliary:
       def __init__(self):
           self.logger = logging.getLogger('spam_application.auxiliary.Auxiliary')
           self.logger.info('creating an instance of Auxiliary')

       def do_something(self):
           self.logger.info('doing something')
           a = 1 + 1
           self.logger.info('done doing something')

   def some_function():
       module_logger.info('received a call to "some_function"')

El resultado se ve así:

   2005-03-23 23:47:11,663 - spam_application - INFO -
      creating an instance of auxiliary_module.Auxiliary
   2005-03-23 23:47:11,665 - spam_application.auxiliary.Auxiliary - INFO -
      creating an instance of Auxiliary
   2005-03-23 23:47:11,665 - spam_application - INFO -
      created an instance of auxiliary_module.Auxiliary
   2005-03-23 23:47:11,668 - spam_application - INFO -
      calling auxiliary_module.Auxiliary.do_something
   2005-03-23 23:47:11,668 - spam_application.auxiliary.Auxiliary - INFO -
      doing something
   2005-03-23 23:47:11,669 - spam_application.auxiliary.Auxiliary - INFO -
      done doing something
   2005-03-23 23:47:11,670 - spam_application - INFO -
      finished auxiliary_module.Auxiliary.do_something
   2005-03-23 23:47:11,671 - spam_application - INFO -
      calling auxiliary_module.some_function()
   2005-03-23 23:47:11,672 - spam_application.auxiliary - INFO -
      received a call to 'some_function'
   2005-03-23 23:47:11,673 - spam_application - INFO -
      done with auxiliary_module.some_function()

## Logging desde múltiples hilos

Realizar *logging* desde múltiples hilos (*threads*) no requiere
ningún esfuerzo especial. El siguiente ejemplo muestra el logging
desde el hilo principal (inicial) y otro hilo:

   import logging
   import threading
   import time

   def worker(arg):
       while not arg['stop']:
           logging.debug('Hi from myfunc')
           time.sleep(0.5)

   def main():
       logging.basicConfig(level=logging.DEBUG, format='%(relativeCreated)6d %(threadName)s %(message)s')
       info = {'stop': False}
       thread = threading.Thread(target=worker, args=(info,))
       thread.start()
       while True:
           try:
               logging.debug('Hello from main')
               time.sleep(0.75)
           except KeyboardInterrupt:
               info['stop'] = True
               break
       thread.join()

   if __name__ == '__main__':
       main()

Cuando se ejecuta, el script debe imprimir algo como lo siguiente:

      0 Thread-1 Hi from myfunc
      3 MainThread Hello from main
    505 Thread-1 Hi from myfunc
    755 MainThread Hello from main
   1007 Thread-1 Hi from myfunc
   1507 MainThread Hello from main
   1508 Thread-1 Hi from myfunc
   2010 Thread-1 Hi from myfunc
   2258 MainThread Hello from main
   2512 Thread-1 Hi from myfunc
   3009 MainThread Hello from main
   3013 Thread-1 Hi from myfunc
   3515 Thread-1 Hi from myfunc
   3761 MainThread Hello from main
   4017 Thread-1 Hi from myfunc
   4513 MainThread Hello from main
   4518 Thread-1 Hi from myfunc

Esto muestra la salida de logging intercalada como cabría esperar. Por
supuesto, este enfoque funciona para más hilos de lo que se muestran
aquí.

## Múltiples gestores y formateadores

Los *loggers* son simples objetos Python. El método "addHandler()" no
tiene una cuota mínima o máxima para la cantidad de gestores
(*handlers*) que puede agregar. A veces será beneficioso para una
aplicación registrar todos los mensajes de todas las prioridades en un
archivo de texto mientras se registran simultáneamente los errores o
más en la consola. Para configurar esto, simplemente configure los
gestores apropiados. Las llamadas de logging en el código de la
aplicación permanecerán sin cambios. Aquí hay una ligera modificación
al ejemplo de configuración simple anterior basado en módulo:

   import logging

   logger = logging.getLogger('simple_example')
   logger.setLevel(logging.DEBUG)
   # create file handler which logs even debug messages
   fh = logging.FileHandler('spam.log')
   fh.setLevel(logging.DEBUG)
   # create console handler with a higher log level
   ch = logging.StreamHandler()
   ch.setLevel(logging.ERROR)
   # create formatter and add it to the handlers
   formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
   ch.setFormatter(formatter)
   fh.setFormatter(formatter)
   # add the handlers to logger
   logger.addHandler(ch)
   logger.addHandler(fh)

   # 'application' code
   logger.debug('debug message')
   logger.info('info message')
   logger.warning('warn message')
   logger.error('error message')
   logger.critical('critical message')

Tenga en cuenta que el código de la 'aplicación' no se preocupa por
los gestores múltiples. Todo lo que cambió fue la adición y
configuración de un nuevo gestor llamado *fh*.

La capacidad de crear nuevos gestores con filtros de mayor o menor
prioridad puede ser muy útil al escribir y probar una aplicación. En
lugar de usar muchas declaraciones "print" para la depuración, use
"logger.debug": a diferencia de las declaraciones de impresión, que
tendrá que eliminar o comentar más tarde, las declaraciones de
*logger.debug* pueden permanecer intactas en el código fuente y
permanecen inactivas hasta que las necesite nuevamente. En ese
momento, el único cambio que debe realizar es modificar el nivel de
prioridad del *logger* y/o gestor para depurar.

## Logging en múltiples destinos

Supongamos que desea que la consola y un archivo tengan diferentes
formatos de mensaje y salida de log para diferentes situaciones. Por
ejemplo, desea registrar mensajes con un nivel DEBUG y superiores en
un archivo y enviar mensajes con nivel INFO y superior a la consola.
Además, suponga que desea grabar una marca de tiempo en el archivo y
no imprimirlo en la consola. Puede lograr este comportamiento haciendo
lo siguiente:

   import logging

   # set up logging to file - see previous section for more details
   logging.basicConfig(level=logging.DEBUG,
                       format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                       datefmt='%m-%d %H:%M',
                       filename='/tmp/myapp.log',
                       filemode='w')
   # define a Handler which writes INFO messages or higher to the sys.stderr
   console = logging.StreamHandler()
   console.setLevel(logging.INFO)
   # set a format which is simpler for console use
   formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
   # tell the handler to use this format
   console.setFormatter(formatter)
   # add the handler to the root logger
   logging.getLogger().addHandler(console)

   # Now, we can log to the root logger, or any other logger. First the root...
   logging.info('Jackdaws love my big sphinx of quartz.')

   # Now, define a couple of other loggers which might represent areas in your
   # application:

   logger1 = logging.getLogger('myapp.area1')
   logger2 = logging.getLogger('myapp.area2')

   logger1.debug('Quick zephyrs blow, vexing daft Jim.')
   logger1.info('How quickly daft jumping zebras vex.')
   logger2.warning('Jail zesty vixen who grabbed pay from quack.')
   logger2.error('The five boxing wizards jump quickly.')

Cuando ejecute esto, en la consola verá

   root        : INFO     Jackdaws love my big sphinx of quartz.
   myapp.area1 : INFO     How quickly daft jumping zebras vex.
   myapp.area2 : WARNING  Jail zesty vixen who grabbed pay from quack.
   myapp.area2 : ERROR    The five boxing wizards jump quickly.

y en el archivo verá algo como

   10-22 22:19 root         INFO     Jackdaws love my big sphinx of quartz.
   10-22 22:19 myapp.area1  DEBUG    Quick zephyrs blow, vexing daft Jim.
   10-22 22:19 myapp.area1  INFO     How quickly daft jumping zebras vex.
   10-22 22:19 myapp.area2  WARNING  Jail zesty vixen who grabbed pay from quack.
   10-22 22:19 myapp.area2  ERROR    The five boxing wizards jump quickly.

Como se puede ver, el mensaje DEBUG sólo se muestra en el archivo. Los
otros mensajes se envían a los dos destinos.

Este ejemplo usa gestores de consola y archivos, pero puede usar
cualquier número y combinación de los gestores que elija.

Tenga en cuenta que la elección anterior del nombre del archivo de
registro "/tmp/myapp.log" implica el uso de una ubicación estándar
para los archivos temporales en los sistemas POSIX. En Windows, es
posible que tenga que elegir un nombre de directorio diferente para el
registro - sólo asegúrese de que el directorio existe y que tiene los
permisos para crear y actualizar archivos en él.

## Gestión personalizada de niveles

A veces, es posible que desee hacer algo ligeramente diferente del
manejo estándar de niveles, donde todos los niveles por encima de un
umbral son procesados por un gestor. Para ello, es necesario utilizar
filtros. Veamos un escenario en el que se desea organizar las cosas de
la siguiente manera:

* Enviar mensajes de gravedad "INFO" y "WARNING" a "sys.stdout"

* Enviar mensajes de gravedad "ERROR" y superiores a "sys.stderr"

* Envía los mensajes de gravedad "DEBUG" y superiores al archivo
  "app.log"

Supongamos que se configura el registro con el siguiente JSON:

   {
       "version": 1,
       "disable_existing_loggers": false,
       "formatters": {
           "simple": {
               "format": "%(levelname)-8s - %(message)s"
           }
       },
       "handlers": {
           "stdout": {
               "class": "logging.StreamHandler",
               "level": "INFO",
               "formatter": "simple",
               "stream": "ext://sys.stdout"
           },
           "stderr": {
               "class": "logging.StreamHandler",
               "level": "ERROR",
               "formatter": "simple",
               "stream": "ext://sys.stderr"
           },
           "file": {
               "class": "logging.FileHandler",
               "formatter": "simple",
               "filename": "app.log",
               "mode": "w"
           }
       },
       "root": {
           "level": "DEBUG",
           "handlers": [
               "stderr",
               "stdout",
               "file"
           ]
       }
   }

This configuration does *almost* what we want, except that
"sys.stdout" would show messages of severity "ERROR" and only events
of this severity and higher will be tracked as well as "INFO" and
"WARNING" messages. To prevent this, we can set up a filter which
excludes those messages and add it to the relevant handler. This can
be configured by adding a "filters" section parallel to "formatters"
and "handlers":

   {
       "filters": {
           "warnings_and_below": {
               "()" : "__main__.filter_maker",
               "level": "WARNING"
           }
       }
   }

y cambiando la sección del gestor "stdout" para añadirlo:

   {
       "stdout": {
           "class": "logging.StreamHandler",
           "level": "INFO",
           "formatter": "simple",
           "stream": "ext://sys.stdout",
           "filters": ["warnings_and_below"]
       }
   }

Un filtro no es más que una función, por lo que podemos definir el
"filter_maker" (una función de fábrica) como sigue:

   def filter_maker(level):
       level = getattr(logging, level)

       def filter(record):
           return record.levelno <= level

       return filter

Esto convierte el argumento de la cadena de caracteres pasada en un
nivel numérico, y retorna una función que sólo retorna "True" si el
nivel del registro pasado está en o por debajo del nivel especificado.
Ten en cuenta que en este ejemplo se ha definido el "filter_maker" en
un script de prueba "main.py" que se ejecuta desde la línea de
comandos, por lo que su módulo será "__main__" - de ahí el
"__main__.filter_maker" en la configuración del filtro. Tendrás que
cambiar eso si lo defines en un módulo diferente.

Con el filtro añadido, podemos ejecutar "main.py", que en su totalidad
es:

   import json
   import logging
   import logging.config

   CONFIG = '''
   {
       "version": 1,
       "disable_existing_loggers": false,
       "formatters": {
           "simple": {
               "format": "%(levelname)-8s - %(message)s"
           }
       },
       "filters": {
           "warnings_and_below": {
               "()" : "__main__.filter_maker",
               "level": "WARNING"
           }
       },
       "handlers": {
           "stdout": {
               "class": "logging.StreamHandler",
               "level": "INFO",
               "formatter": "simple",
               "stream": "ext://sys.stdout",
               "filters": ["warnings_and_below"]
           },
           "stderr": {
               "class": "logging.StreamHandler",
               "level": "ERROR",
               "formatter": "simple",
               "stream": "ext://sys.stderr"
           },
           "file": {
               "class": "logging.FileHandler",
               "formatter": "simple",
               "filename": "app.log",
               "mode": "w"
           }
       },
       "root": {
           "level": "DEBUG",
           "handlers": [
               "stderr",
               "stdout",
               "file"
           ]
       }
   }
   '''

   def filter_maker(level):
       level = getattr(logging, level)

       def filter(record):
           return record.levelno <= level

       return filter

   logging.config.dictConfig(json.loads(CONFIG))
   logging.debug('A DEBUG message')
   logging.info('An INFO message')
   logging.warning('A WARNING message')
   logging.error('An ERROR message')
   logging.critical('A CRITICAL message')

Y después de ejecutarlo de esta manera:

   python main.py 2>stderr.log >stdout.log

Podemos ver que los resultados son los esperados:

   $ more *.log
   ::::::::::::::
   app.log
   ::::::::::::::
   DEBUG    - A DEBUG message
   INFO     - An INFO message
   WARNING  - A WARNING message
   ERROR    - An ERROR message
   CRITICAL - A CRITICAL message
   ::::::::::::::
   stderr.log
   ::::::::::::::
   ERROR    - An ERROR message
   CRITICAL - A CRITICAL message
   ::::::::::::::
   stdout.log
   ::::::::::::::
   INFO     - An INFO message
   WARNING  - A WARNING message

## Ejemplo de servidor de configuración

Aquí hay un ejemplo de un módulo que usa el servidor de configuración
logging:

   import logging
   import logging.config
   import time
   import os

   # read initial config file
   logging.config.fileConfig('logging.conf')

   # create and start listener on port 9999
   t = logging.config.listen(9999)
   t.start()

   logger = logging.getLogger('simpleExample')

   try:
       # loop through logging calls to see the difference
       # new configurations make, until Ctrl+C is pressed
       while True:
           logger.debug('debug message')
           logger.info('info message')
           logger.warning('warn message')
           logger.error('error message')
           logger.critical('critical message')
           time.sleep(5)
   except KeyboardInterrupt:
       # cleanup
       logging.config.stopListening()
       t.join()

Y aquí hay un script que toma un nombre de archivo y envía ese archivo
al servidor, precedido adecuadamente con la longitud codificada en
binario, como la nueva configuración de logging:

   #!/usr/bin/env python
   import socket, sys, struct

   with open(sys.argv[1], 'rb') as f:
       data_to_send = f.read()

   HOST = 'localhost'
   PORT = 9999
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   print('connecting...')
   s.connect((HOST, PORT))
   print('sending config...')
   s.send(struct.pack('>L', len(data_to_send)))
   s.send(data_to_send)
   s.close()
   print('complete')

## Tratar con gestores que bloquean

A veces tiene que hacer que sus gestores de registro hagan su trabajo
sin bloquear el hilo desde el que está iniciando sesión. Esto es común
en las aplicaciones web, aunque, por supuesto, también ocurre en otros
escenarios.

Un responsable habitual que ejemplifica un comportamiento lento es la
"SMTPHandler": el envío de correos electrónicos puede llevar mucho
tiempo, por varias razones fuera del control del desarrollador (por
ejemplo, una infraestructura de red o correo de bajo rendimiento).
Pero casi cualquier controlador basado en red puede bloquear: incluso
una operación "SocketHandler" puede estar haciendo a bajo nivel una
consulta DNS  que es demasiado lenta (y esta consulta puede estar en
el código de la biblioteca de socket, debajo de la capa de Python, y
fuera de su control).

Una solución es utilizar un enfoque de dos partes. Para la primera
parte, adjunte solo una "QueueHandler" a los loggers que se acceden
desde subprocesos críticos de rendimiento. Simplemente escriben en su
cola, que puede dimensionarse a una capacidad lo suficientemente
grande o inicializarse sin límite superior a su tamaño. La escritura
en la cola generalmente se aceptará rápidamente, aunque es probable
que deba atrapar la excepción "queue.Full" como precaución en su
código. Si usted es un desarrollador de bibliotecas que tiene
subprocesos críticos de rendimiento en su código, asegúrese de
documentar esto (junto con una sugerencia de adjuntar solo
"QueueHandlers" a sus loggers) para el beneficio de otros
desarrolladores que usarán su código.

La segunda parte de la solución es "QueueListener", que fue designado
como la contraparte de "QueueHandler". Un "QueueListener" es muy
simple: ha pasado una cola y algunos gestores, y activa un hilo
interno que escucha su cola para *LogRecords* enviados desde
"QueueHandlers" (o cualquier otra fuente de "LogRecords", para el
caso). Los "LogRecords" se eliminan de la cola y se pasan a los
gestores para su procesamiento.

La ventaja de tener una clase separada "QueueListener" es que puede
usar la misma instancia para dar servicio a múltiples "QueueHandlers".
Esto es más amigable con los recursos que, por ejemplo, tener
versiones enhebradas de las clases de gestores existentes, que
consumirían un hilo por gestor sin ningún beneficio particular.

Un ejemplo del uso de estas dos clases a continuación (se omiten
*imports*):

   que = queue.Queue(-1)  # no limit on size
   queue_handler = QueueHandler(que)
   handler = logging.StreamHandler()
   listener = QueueListener(que, handler)
   root = logging.getLogger()
   root.addHandler(queue_handler)
   formatter = logging.Formatter('%(threadName)s: %(message)s')
   handler.setFormatter(formatter)
   listener.start()
   # The log output will display the thread which generated
   # the event (the main thread) rather than the internal
   # thread which monitors the internal queue. This is what
   # you want to happen.
   root.warning('Look out!')
   listener.stop()

que, cuando se ejecuta, producirá:

   MainThread: Look out!

Nota:

  Aunque la discusión anterior no se refería específicamente al código
  asíncrono, sino más bien a los gestores de logging lentos, hay que
  tener en cuenta que cuando se realiza logging desde código
  asíncrono, los gestores de red e incluso de archivos podrían dar
  problemas (bloqueo del bucle de eventos) porque parte del logging se
  realiza desde los internos de "asyncio". Podría ser mejor, si se
  utiliza cualquier código asíncrono en una aplicación, utilizar el
  enfoque anterior para el logging, de modo que cualquier código de
  bloqueo se ejecute sólo en el hilo "QueueListener".

Distinto en la versión 3.5: Antes de Python 3.5, "QueueListener"
siempre pasaba cada mensaje recibido de la cola a cada controlador con
el que se inicializaba. (Esto se debió a que se asumió que el filtrado
de nivel se realizó en el otro lado, donde se llena la cola). A partir
de 3.5, este comportamiento se puede cambiar pasando un argumento de
palabra clave "respect_handler_level=True" al constructor del oyente .
Cuando se hace esto, el oyente compara el nivel de cada mensaje con el
nivel del controlador y solo pasa un mensaje a un controlador si es
apropiado hacerlo.

Distinto en la versión 3.14: The "QueueListener" can be started (and
stopped) via the "with" statement. For example:

   with QueueListener(que, handler) as listener:
       # The queue listener automatically starts
       # when the 'with' block is entered.
       pass
   # The queue listener automatically stops once
   # the 'with' block is exited.

## Enviar y recibir eventos logging a través de una red

Supongamos que desea enviar eventos de registro a través de una red y
gestionarlos en el extremo receptor. Una forma sencilla de hacer esto
es adjuntar una instancia de "SocketHandler" al registrador raíz en el
extremo de envío:

   import logging, logging.handlers

   rootLogger = logging.getLogger()
   rootLogger.setLevel(logging.DEBUG)
   socketHandler = logging.handlers.SocketHandler('localhost',
                       logging.handlers.DEFAULT_TCP_LOGGING_PORT)
   # don't bother with a formatter, since a socket handler sends the event as
   # an unformatted pickle
   rootLogger.addHandler(socketHandler)

   # Now, we can log to the root logger, or any other logger. First the root...
   logging.info('Jackdaws love my big sphinx of quartz.')

   # Now, define a couple of other loggers which might represent areas in your
   # application:

   logger1 = logging.getLogger('myapp.area1')
   logger2 = logging.getLogger('myapp.area2')

   logger1.debug('Quick zephyrs blow, vexing daft Jim.')
   logger1.info('How quickly daft jumping zebras vex.')
   logger2.warning('Jail zesty vixen who grabbed pay from quack.')
   logger2.error('The five boxing wizards jump quickly.')

En el extremo receptor, puede configurar un receptor usando el módulo
"socketserver". Aquí hay un ejemplo básico de trabajo:

   import pickle
   import logging
   import logging.handlers
   import socketserver
   import struct

   class LogRecordStreamHandler(socketserver.StreamRequestHandler):
       """Handler for a streaming logging request.

       This basically logs the record using whatever logging policy is
       configured locally.
       """

       def handle(self):
           """
           Handle multiple requests - each expected to be a 4-byte length,
           followed by the LogRecord in pickle format. Logs the record
           according to whatever policy is configured locally.
           """
           while True:
               chunk = self.connection.recv(4)
               if len(chunk) < 4:
                   break
               slen = struct.unpack('>L', chunk)[0]
               chunk = self.connection.recv(slen)
               while len(chunk) < slen:
                   chunk = chunk + self.connection.recv(slen - len(chunk))
               obj = self.unPickle(chunk)
               record = logging.makeLogRecord(obj)
               self.handleLogRecord(record)

       def unPickle(self, data):
           return pickle.loads(data)

       def handleLogRecord(self, record):
           # if a name is specified, we use the named logger rather than the one
           # implied by the record.
           if self.server.logname is not None:
               name = self.server.logname
           else:
               name = record.name
           logger = logging.getLogger(name)
           # N.B. EVERY record gets logged. This is because Logger.handle
           # is normally called AFTER logger-level filtering. If you want
           # to do filtering, do it at the client end to save wasting
           # cycles and network bandwidth!
           logger.handle(record)

   class LogRecordSocketReceiver(socketserver.ThreadingTCPServer):
       """
       Simple TCP socket-based logging receiver suitable for testing.
       """

       allow_reuse_address = True

       def __init__(self, host='localhost',
                    port=logging.handlers.DEFAULT_TCP_LOGGING_PORT,
                    handler=LogRecordStreamHandler):
           socketserver.ThreadingTCPServer.__init__(self, (host, port), handler)
           self.abort = 0
           self.timeout = 1
           self.logname = None

       def serve_until_stopped(self):
           import select
           abort = 0
           while not abort:
               rd, wr, ex = select.select([self.socket.fileno()],
                                          [], [],
                                          self.timeout)
               if rd:
                   self.handle_request()
               abort = self.abort

   def main():
       logging.basicConfig(
           format='%(relativeCreated)5d %(name)-15s %(levelname)-8s %(message)s')
       tcpserver = LogRecordSocketReceiver()
       print('About to start TCP server...')
       tcpserver.serve_until_stopped()

   if __name__ == '__main__':
       main()

Primero ejecuta el servidor, y luego el cliente. Del lado del cliente,
nada se imprime en la consola; del lado del servidor, se debería ver
algo como esto:

   About to start TCP server...
      59 root            INFO     Jackdaws love my big sphinx of quartz.
      59 myapp.area1     DEBUG    Quick zephyrs blow, vexing daft Jim.
      69 myapp.area1     INFO     How quickly daft jumping zebras vex.
      69 myapp.area2     WARNING  Jail zesty vixen who grabbed pay from quack.
      69 myapp.area2     ERROR    The five boxing wizards jump quickly.

Note that there are some security issues with pickle in some
scenarios. If these affect you, you can use an alternative
serialization scheme by overriding the "makePickle()" method and
implementing your alternative there, as well as adapting the above
script to use your alternative serialization.

### Ejecutando un logging de socket oyente en producción

To run a logging listener in production, you may need to use a
process-management tool such as Supervisor. Here is a Gist which
provides the bare-bones files to run the above functionality using
Supervisor. It consists of the following files:

+---------------------------+------------------------------------------------------+
| File                      | Purpose                                              |
|===========================|======================================================|
## | "prepare.sh"              | A Bash script to prepare the environment for testing |

| "supervisor.conf"         | The Supervisor configuration file, which has entries |
## |                           | for the listener and a multi-process web application |

| "ensure_app.sh"           | A Bash script to ensure that Supervisor is running   |
## |                           | with the above configuration                         |

| "log_listener.py"         | The socket listener program which receives log       |
## |                           | events and records them to a file                    |

| "main.py"                 | A simple web application which performs logging via  |
## |                           | a socket connected to the listener                   |

## | "webapp.json"             | A JSON configuration file for the web application    |

## | "client.py"               | A Python script to exercise the web application      |

The web application uses Gunicorn, which is a popular web application
server that starts multiple worker processes to handle requests. This
example setup shows how the workers can write to the same log file
without conflicting with one another --- they all go through the
socket listener.

To test these files, do the following in a POSIX environment:

1. Download the Gist as a ZIP archive using the Download ZIP button.

2. Unzip the above files from the archive into a scratch directory.

3. In the scratch directory, run "bash prepare.sh" to get things
   ready. This creates a "run" subdirectory to contain Supervisor-
   related and log files, and a "venv" subdirectory to contain a
   virtual environment into which "bottle", "gunicorn" and
   "supervisor" are installed.

4. Run "bash ensure_app.sh" to ensure that Supervisor is running with
   the above configuration.

5. Run "venv/bin/python client.py" to exercise the web application,
   which will lead to records being written to the log.

6. Inspect the log files in the "run" subdirectory. You should see the
   most recent log lines in files matching the pattern "app.log*".
   They won't be in any particular order, since they have been handled
   concurrently by different worker processes in a non-deterministic
   way.

7. You can shut down the listener and the web application by running
   "venv/bin/supervisorctl -c supervisor.conf shutdown".

You may need to tweak the configuration files in the unlikely event
that the configured ports clash with something else in your test
environment.

The default configuration uses a TCP socket on port 9020. You can use
a Unix Domain socket instead of a TCP socket by doing the following:

1. In "listener.json", add a "socket" key with the path to the domain
   socket you want to use. If this key is present, the listener
   listens on the corresponding domain socket and not on a TCP socket
   (the "port" key is ignored).

2. In "webapp.json", change the socket handler configuration
   dictionary so that the "host" value is the path to the domain
   socket, and set the "port" value to "null".

## Agregar información contextual a su salida de logging

A veces, desea que la salida de logging contenga información
contextual además de los parámetros pasados a la llamada del logging.
Por ejemplo, en una aplicación en red, puede ser conveniente registrar
información específica del cliente en el logging (por ejemplo, el
nombre de usuario del cliente remoto o la dirección IP). Aunque puede
usar el parámetro *extra* para lograr esto, no siempre es conveniente
pasar la información de esta manera. Si bien puede resultar tentador
crear instancias "Logger" por conexión, esta no es una buena idea
porque estas instancias no se liberan de memoria vía el recolector de
basura (*garbage collector*). Si bien esto no es un problema en la
práctica, cuando el número de instancias de "Logger" depende del nivel
de granularidad que desea usar para hacer el logging de una
aplicación, podría ser difícil de administrar si el número de
instancias "Logger" se vuelven efectivamente ilimitadas.

### Uso de LoggerAdapters para impartir información contextual

Una manera fácil de pasar información contextual para que se genere
junto con la información de eventos logging es usar la clase
"LoggerAdapter". Esta clase está diseñada para parecerse a "Logger",
de modo que pueda llamar "debug()", "info()", "warning()", "error()",
"excepción()", "critical()" y "log()". Estos métodos tienen las mismas
signaturas que sus contrapartes en "Logger", por lo que puede usar los
dos tipos de instancias indistintamente.

Cuando creas una instancia de "LoggerAdapter", le pasas una instancia
de "Logger" y un objeto similar a un dict que contiene tu información
contextual. Cuando llamas a uno de los métodos de registro en una
instancia de "LoggerAdapter", delega la llamada a la instancia
subyacente de "Logger" pasada a su constructor, y se arregla para
pasar la información contextual en la llamada delegada . Aquí hay un
fragmento del código de "LoggerAdapter":

   def debug(self, msg, /, *args, **kwargs):
       """
       Delegate a debug call to the underlying logger, after adding
       contextual information from this adapter instance.
       """
       msg, kwargs = self.process(msg, kwargs)
       self.logger.debug(msg, *args, **kwargs)

El método "process()" de "LoggerAdapter" es donde la información
contextual se agrega a la salida del logging. Se pasa el mensaje y los
argumentos de palabra clave de la llamada logging, y retorna versiones
(potencialmente) modificadas de estos para usar en la llamada al
logging subyacente. La implementación predeterminada de este método
deja el mensaje solo, pero inserta una clave 'extra' en el argumento
de palabra clave cuyo valor es el objeto tipo dict pasado al
constructor. Por supuesto, si ha pasado un argumento de palabra clave
'extra' en la llamada al adaptador, se sobrescribirá silenciosamente.

La ventaja de usar 'extra' es que los valores en el objeto dict se
combinan en la instancia "LogRecord" __dict__, lo que le permite usar
cadenas personalizadas con sus instancias "Formatter" que conocen las
claves del objeto dict. Si necesita un método diferente, por ejemplo,
si desea anteponer o agregar la información contextual a la cadena del
mensaje, solo necesita la subclase "LoggerAdapter" y anular
"process()" para hacer lo que necesita. Aquí hay un ejemplo simple:

   class CustomAdapter(logging.LoggerAdapter):
       """
       This example adapter expects the passed in dict-like object to have a
       'connid' key, whose value in brackets is prepended to the log message.
       """
       def process(self, msg, kwargs):
           return '[%s] %s' % (self.extra['connid'], msg), kwargs

que puede usar así:

   logger = logging.getLogger(__name__)
   adapter = CustomAdapter(logger, {'connid': some_conn_id})

Luego, cualquier evento que registre en el adaptador tendrá el valor
de "some_conn_id" antepuesto a los mensajes de logging.

#### Usar objetos distintos a los diccionarios para transmitir información contextual

No es necesario pasar un diccionario real a la "LoggerAdapter" -
puedes pasar una instancia de una clase que implemente "__getitem__" y
"__iter__" de modo que parezca un diccionario para el logging. Esto es
útil si quieres generar valores dinámicamente (mientras que los
valores en un diccionario son constantes).

### Usar filtros para impartir información contextual

También puedes agregar información contextual a la salida del log
utilizando un "Filter" definido por el usuario. Las instancias de
"Filter" pueden modificar los "LogRecords" que se les pasan, incluido
el agregado de atributos adicionales que luego se pueden generar
utilizando cadena de caracteres con el formato adecuado, o si es
necesario, un "Formatter" personalizado.

Por ejemplo, en una aplicación web, la solicitud que se está
procesando (o al menos, las partes interesantes de la misma) se pueden
almacenar en una variable *threadlocal* ("threading.local") y luego se
puede acceder a ella desde "Filter" para agregar información de la
solicitud, - digamos, la dirección IP remota y el nombre de usuario-,
al "LogRecord", usando los nombres de atributo 'ip' y 'user' como en
el ejemplo anterior de "LoggerAdapter". En ese caso, se puede usar el
mismo formato de cadena de caracteres para obtener un resultado
similar al que se muestra arriba. Aquí hay un script de ejemplo:

   import logging
   from random import choice

   class ContextFilter(logging.Filter):
       """
       This is a filter which injects contextual information into the log.

       Rather than use actual contextual information, we just use random
       data in this demo.
       """

       USERS = ['jim', 'fred', 'sheila']
       IPS = ['123.231.231.123', '127.0.0.1', '192.168.0.1']

       def filter(self, record):

           record.ip = choice(ContextFilter.IPS)
           record.user = choice(ContextFilter.USERS)
           return True

   if __name__ == '__main__':
       levels = (logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL)
       logging.basicConfig(level=logging.DEBUG,
                           format='%(asctime)-15s %(name)-5s %(levelname)-8s IP: %(ip)-15s User: %(user)-8s %(message)s')
       a1 = logging.getLogger('a.b.c')
       a2 = logging.getLogger('d.e.f')

       f = ContextFilter()
       a1.addFilter(f)
       a2.addFilter(f)
       a1.debug('A debug message')
       a1.info('An info message with %s', 'some parameters')
       for x in range(10):
           lvl = choice(levels)
           lvlname = logging.getLevelName(lvl)
           a2.log(lvl, 'A message at %s level with %d %s', lvlname, 2, 'parameters')

que cuando se ejecuta, produce algo como:

   2010-09-06 22:38:15,292 a.b.c DEBUG    IP: 123.231.231.123 User: fred     A debug message
   2010-09-06 22:38:15,300 a.b.c INFO     IP: 192.168.0.1     User: sheila   An info message with some parameters
   2010-09-06 22:38:15,300 d.e.f CRITICAL IP: 127.0.0.1       User: sheila   A message at CRITICAL level with 2 parameters
   2010-09-06 22:38:15,300 d.e.f ERROR    IP: 127.0.0.1       User: jim      A message at ERROR level with 2 parameters
   2010-09-06 22:38:15,300 d.e.f DEBUG    IP: 127.0.0.1       User: sheila   A message at DEBUG level with 2 parameters
   2010-09-06 22:38:15,300 d.e.f ERROR    IP: 123.231.231.123 User: fred     A message at ERROR level with 2 parameters
   2010-09-06 22:38:15,300 d.e.f CRITICAL IP: 192.168.0.1     User: jim      A message at CRITICAL level with 2 parameters
   2010-09-06 22:38:15,300 d.e.f CRITICAL IP: 127.0.0.1       User: sheila   A message at CRITICAL level with 2 parameters
   2010-09-06 22:38:15,300 d.e.f DEBUG    IP: 192.168.0.1     User: jim      A message at DEBUG level with 2 parameters
   2010-09-06 22:38:15,301 d.e.f ERROR    IP: 127.0.0.1       User: sheila   A message at ERROR level with 2 parameters
   2010-09-06 22:38:15,301 d.e.f DEBUG    IP: 123.231.231.123 User: fred     A message at DEBUG level with 2 parameters
   2010-09-06 22:38:15,301 d.e.f INFO     IP: 123.231.231.123 User: fred     A message at INFO level with 2 parameters

## Uso de "contextvars"

Desde la versión 3.7 de Python, el módulo "contextvars" ha
proporcionado almacenamiento local de contexto que funciona tanto para
las necesidades de procesamiento de "threading" como de "asyncio".
Este tipo de almacenamiento puede ser, por tanto, preferible a los
hilos locales. El siguiente ejemplo muestra cómo, en un entorno
multihilo, los logs pueden rellenarse con información contextual como,
por ejemplo, los atributos de las peticiones gestionadas por las
aplicaciones web.

A modo de ilustración, digamos que tienes diferentes aplicaciones web,
cada una de ellas independiente de la otra, pero que se ejecutan en el
mismo proceso de Python y utilizan una biblioteca común a todas ellas.
¿Cómo puede cada una de estas aplicaciones tener su propio registro,
donde todos los mensajes de logging de la biblioteca (y otro código de
procesamiento de solicitudes) se dirigen al archivo de registro de la
aplicación apropiada, mientras se incluye en el registro información
contextual adicional como la IP del cliente, el método de solicitud
HTTP y el nombre de usuario del cliente?

Supongamos que la biblioteca se puede simular con el siguiente código:

   # webapplib.py
   import logging
   import time

   logger = logging.getLogger(__name__)

   def useful():
       # Just a representative event logged from the library
       logger.debug('Hello from webapplib!')
       # Just sleep for a bit so other threads get to run
       time.sleep(0.01)

Podemos simular las aplicaciones web múltiples mediante dos clases
simples, "Request" y "WebApp". Éstas simulan cómo funcionan las
aplicaciones web reales con hilos, cada petición es manejada por un
hilo:

   # main.py
   import argparse
   from contextvars import ContextVar
   import logging
   import os
   from random import choice
   import threading
   import webapplib

   logger = logging.getLogger(__name__)
   root = logging.getLogger()
   root.setLevel(logging.DEBUG)

   class Request:
       """
       A simple dummy request class which just holds dummy HTTP request method,
       client IP address and client username
       """
       def __init__(self, method, ip, user):
           self.method = method
           self.ip = ip
           self.user = user

   # A dummy set of requests which will be used in the simulation - we'll just pick
   # from this list randomly. Note that all GET requests are from 192.168.2.XXX
   # addresses, whereas POST requests are from 192.16.3.XXX addresses. Three users
   # are represented in the sample requests.

   REQUESTS = [
       Request('GET', '192.168.2.20', 'jim'),
       Request('POST', '192.168.3.20', 'fred'),
       Request('GET', '192.168.2.21', 'sheila'),
       Request('POST', '192.168.3.21', 'jim'),
       Request('GET', '192.168.2.22', 'fred'),
       Request('POST', '192.168.3.22', 'sheila'),
   ]

   # Note that the format string includes references to request context information
   # such as HTTP method, client IP and username

   formatter = logging.Formatter('%(threadName)-11s %(appName)s %(name)-9s %(user)-6s %(ip)s %(method)-4s %(message)s')

   # Create our context variables. These will be filled at the start of request
   # processing, and used in the logging that happens during that processing

   ctx_request = ContextVar('request')
   ctx_appname = ContextVar('appname')

   class InjectingFilter(logging.Filter):
       """
       A filter which injects context-specific information into logs and ensures
       that only information for a specific webapp is included in its log
       """
       def __init__(self, app):
           self.app = app

       def filter(self, record):
           request = ctx_request.get()
           record.method = request.method
           record.ip = request.ip
           record.user = request.user
           record.appName = appName = ctx_appname.get()
           return appName == self.app.name

   class WebApp:
       """
       A dummy web application class which has its own handler and filter for a
       webapp-specific log.
       """
       def __init__(self, name):
           self.name = name
           handler = logging.FileHandler(name + '.log', 'w')
           f = InjectingFilter(self)
           handler.setFormatter(formatter)
           handler.addFilter(f)
           root.addHandler(handler)
           self.num_requests = 0

       def process_request(self, request):
           """
           This is the dummy method for processing a request. It's called on a
           different thread for every request. We store the context information into
           the context vars before doing anything else.
           """
           ctx_request.set(request)
           ctx_appname.set(self.name)
           self.num_requests += 1
           logger.debug('Request processing started')
           webapplib.useful()
           logger.debug('Request processing finished')

   def main():
       fn = os.path.splitext(os.path.basename(__file__))[0]
       adhf = argparse.ArgumentDefaultsHelpFormatter
       ap = argparse.ArgumentParser(formatter_class=adhf, prog=fn,
                                    description='Simulate a couple of web '
                                                'applications handling some '
                                                'requests, showing how request '
                                                'context can be used to '
                                                'populate logs')
       aa = ap.add_argument
       aa('--count', '-c', type=int, default=100, help='How many requests to simulate')
       options = ap.parse_args()

       # Create the dummy webapps and put them in a list which we can use to select
       # from randomly
       app1 = WebApp('app1')
       app2 = WebApp('app2')
       apps = [app1, app2]
       threads = []
       # Add a common handler which will capture all events
       handler = logging.FileHandler('app.log', 'w')
       handler.setFormatter(formatter)
       root.addHandler(handler)

       # Generate calls to process requests
       for i in range(options.count):
           try:
               # Pick an app at random and a request for it to process
               app = choice(apps)
               request = choice(REQUESTS)
               # Process the request in its own thread
               t = threading.Thread(target=app.process_request, args=(request,))
               threads.append(t)
               t.start()
           except KeyboardInterrupt:
               break

       # Wait for the threads to terminate
       for t in threads:
           t.join()

       for app in apps:
           print('%s processed %s requests' % (app.name, app.num_requests))

   if __name__ == '__main__':
       main()

Si ejecuta lo anterior, debería encontrar que aproximadamente la mitad
de las peticiones van a "app1.log" y el resto a "app2.log", y las
todas las peticiones se registran en "app.log". Cada registro
específico de la aplicación web contendrá únicamente entradas de log
para esa aplicación web, y la información de las peticiones se
mostrará de forma consistente en el registro (es decir, la información
de cada petición ficticia aparecerá siempre junta en una línea de
log). Esto se ilustra con la siguiente salida del shell:

   ~/logging-contextual-webapp$ python main.py
   app1 processed 51 requests
   app2 processed 49 requests
   ~/logging-contextual-webapp$ wc -l *.log
     153 app1.log
     147 app2.log
     300 app.log
     600 total
   ~/logging-contextual-webapp$ head -3 app1.log
   Thread-3 (process_request) app1 __main__  jim    192.168.3.21 POST Request processing started
   Thread-3 (process_request) app1 webapplib jim    192.168.3.21 POST Hello from webapplib!
   Thread-5 (process_request) app1 __main__  jim    192.168.3.21 POST Request processing started
   ~/logging-contextual-webapp$ head -3 app2.log
   Thread-1 (process_request) app2 __main__  sheila 192.168.2.21 GET  Request processing started
   Thread-1 (process_request) app2 webapplib sheila 192.168.2.21 GET  Hello from webapplib!
   Thread-2 (process_request) app2 __main__  jim    192.168.2.20 GET  Request processing started
   ~/logging-contextual-webapp$ head app.log
   Thread-1 (process_request) app2 __main__  sheila 192.168.2.21 GET  Request processing started
   Thread-1 (process_request) app2 webapplib sheila 192.168.2.21 GET  Hello from webapplib!
   Thread-2 (process_request) app2 __main__  jim    192.168.2.20 GET  Request processing started
   Thread-3 (process_request) app1 __main__  jim    192.168.3.21 POST Request processing started
   Thread-2 (process_request) app2 webapplib jim    192.168.2.20 GET  Hello from webapplib!
   Thread-3 (process_request) app1 webapplib jim    192.168.3.21 POST Hello from webapplib!
   Thread-4 (process_request) app2 __main__  fred   192.168.2.22 GET  Request processing started
   Thread-5 (process_request) app1 __main__  jim    192.168.3.21 POST Request processing started
   Thread-4 (process_request) app2 webapplib fred   192.168.2.22 GET  Hello from webapplib!
   Thread-6 (process_request) app1 __main__  jim    192.168.3.21 POST Request processing started
   ~/logging-contextual-webapp$ grep app1 app1.log | wc -l
   153
   ~/logging-contextual-webapp$ grep app2 app2.log | wc -l
   147
   ~/logging-contextual-webapp$ grep app1 app.log | wc -l
   153
   ~/logging-contextual-webapp$ grep app2 app.log | wc -l
   147

## Impartir información contextual en los gestores

Cada "Handler" tiene su propia cadena de filtros. Si quieres añadir
información contextual a una "LogRecord" sin filtrarla a otros
gestores, puedes utilizar un filtro que retorna una nueva "LogRecord"
en lugar de modificarlo in situ, como se muestra en el siguiente
script:

   import copy
   import logging

   def filter(record: logging.LogRecord):
       record = copy.copy(record)
       record.user = 'jim'
       return record

   if __name__ == '__main__':
       logger = logging.getLogger()
       logger.setLevel(logging.INFO)
       handler = logging.StreamHandler()
       formatter = logging.Formatter('%(message)s from %(user)-8s')
       handler.setFormatter(formatter)
       handler.addFilter(filter)
       logger.addHandler(handler)

       logger.info('A log message')

## Logging a un sólo archivo desde múltiples procesos

Aunque logging es seguro para hilos, y el logging a un solo archivo
desde múltiples hilos en un solo proceso *es* compatible, el logging
en un solo archivo desde *múltiples procesos* *no* es compatible,
porque no existe una forma estándar de serializar el acceso a un solo
archivo en múltiples procesos en Python. Si necesita hacer esto
último, una forma de abordarlo es hacer que todos los procesos se
registren en una "SocketHandler", y tener un proceso separado que
implemente un servidor de socket que lee del socket y los loggings
para archivar. (Si lo prefiere, puede dedicar un hilo en uno de los
procesos existentes para realizar esta función.) Esta sección
documenta este enfoque con más detalle e incluye un receptor socket
que funciona que se puede utilizar como punto de partida para que se
adapte a sus propias aplicaciones.

You could also write your own handler which uses the "Lock" class from
the "multiprocessing" module to serialize access to the file from your
processes. The stdlib "FileHandler" and subclasses do not make use of
"multiprocessing".

Alternativamente, puede usar una "Queue" y "QueueHandler" para enviar
todos los logging a uno de los procesos en su aplicación multi-
proceso. El siguiente script de ejemplo demuestra cómo puede hacer
esto; en el ejemplo, un proceso de escucha independiente escucha los
eventos enviados por otros procesos y los registra de acuerdo con su
propia configuración de logging. Aunque el ejemplo solo demuestra una
forma de hacerlo (por ejemplo, es posible que desee utilizar un hilo
de escucha en lugar de un proceso de escucha separado; la
implementación sería análoga), permite configuraciones de logging
completamente diferentes para el oyente y los otros procesos en su
aplicación. Y se puede utilizar como base para el código que cumpla
con sus propios requisitos específicos:

   # You'll need these imports in your own code
   import logging
   import logging.handlers
   import multiprocessing

   # Next two import lines for this demo only
   from random import choice, random
   import time

   #
   # Because you'll want to define the logging configurations for listener and workers, the
   # listener and worker process functions take a configurer parameter which is a callable
   # for configuring logging for that process. These functions are also passed the queue,
   # which they use for communication.
   #
   # In practice, you can configure the listener however you want, but note that in this
   # simple example, the listener does not apply level or filter logic to received records.
   # In practice, you would probably want to do this logic in the worker processes, to avoid
   # sending events which would be filtered out between processes.
   #
   # The size of the rotated files is made small so you can see the results easily.
   def listener_configurer():
       root = logging.getLogger()
       h = logging.handlers.RotatingFileHandler('mptest.log', 'a', 300, 10)
       f = logging.Formatter('%(asctime)s %(processName)-10s %(name)s %(levelname)-8s %(message)s')
       h.setFormatter(f)
       root.addHandler(h)

   # This is the listener process top-level loop: wait for logging events
   # (LogRecords)on the queue and handle them, quit when you get a None for a
   # LogRecord.
   def listener_process(queue, configurer):
       configurer()
       while True:
           try:
               record = queue.get()
               if record is None:  # We send this as a sentinel to tell the listener to quit.
                   break
               logger = logging.getLogger(record.name)
               logger.handle(record)  # No level or filter logic applied - just do it!
           except Exception:
               import sys, traceback
               print('Whoops! Problem:', file=sys.stderr)
               traceback.print_exc(file=sys.stderr)

   # Arrays used for random selections in this demo

   LEVELS = [logging.DEBUG, logging.INFO, logging.WARNING,
             logging.ERROR, logging.CRITICAL]

   LOGGERS = ['a.b.c', 'd.e.f']

   MESSAGES = [
       'Random message #1',
       'Random message #2',
       'Random message #3',
   ]

   # The worker configuration is done at the start of the worker process run.
   # Note that on Windows you can't rely on fork semantics, so each process
   # will run the logging configuration code when it starts.
   def worker_configurer(queue):
       h = logging.handlers.QueueHandler(queue)  # Just the one handler needed
       root = logging.getLogger()
       root.addHandler(h)
       # send all messages, for demo; no other level or filter logic applied.
       root.setLevel(logging.DEBUG)

   # This is the worker process top-level loop, which just logs ten events with
   # random intervening delays before terminating.
   # The print messages are just so you know it's doing something!
   def worker_process(queue, configurer):
       configurer(queue)
       name = multiprocessing.current_process().name
       print('Worker started: %s' % name)
       for i in range(10):
           time.sleep(random())
           logger = logging.getLogger(choice(LOGGERS))
           level = choice(LEVELS)
           message = choice(MESSAGES)
           logger.log(level, message)
       print('Worker finished: %s' % name)

   # Here's where the demo gets orchestrated. Create the queue, create and start
   # the listener, create ten workers and start them, wait for them to finish,
   # then send a None to the queue to tell the listener to finish.
   def main():
       queue = multiprocessing.Queue(-1)
       listener = multiprocessing.Process(target=listener_process,
                                          args=(queue, listener_configurer))
       listener.start()
       workers = []
       for i in range(10):
           worker = multiprocessing.Process(target=worker_process,
                                            args=(queue, worker_configurer))
           workers.append(worker)
           worker.start()
       for w in workers:
           w.join()
       queue.put_nowait(None)
       listener.join()

   if __name__ == '__main__':
       main()

Una variante del script anterior mantiene el logging en el proceso
principal, en un hilo separado:

   import logging
   import logging.config
   import logging.handlers
   from multiprocessing import Process, Queue
   import random
   import threading
   import time

   def logger_thread(q):
       while True:
           record = q.get()
           if record is None:
               break
           logger = logging.getLogger(record.name)
           logger.handle(record)

   def worker_process(q):
       qh = logging.handlers.QueueHandler(q)
       root = logging.getLogger()
       root.setLevel(logging.DEBUG)
       root.addHandler(qh)
       levels = [logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR,
                 logging.CRITICAL]
       loggers = ['foo', 'foo.bar', 'foo.bar.baz',
                  'spam', 'spam.ham', 'spam.ham.eggs']
       for i in range(100):
           lvl = random.choice(levels)
           logger = logging.getLogger(random.choice(loggers))
           logger.log(lvl, 'Message no. %d', i)

   if __name__ == '__main__':
       q = Queue()
       d = {
           'version': 1,
           'formatters': {
               'detailed': {
                   'class': 'logging.Formatter',
                   'format': '%(asctime)s %(name)-15s %(levelname)-8s %(processName)-10s %(message)s'
               }
           },
           'handlers': {
               'console': {
                   'class': 'logging.StreamHandler',
                   'level': 'INFO',
               },
               'file': {
                   'class': 'logging.FileHandler',
                   'filename': 'mplog.log',
                   'mode': 'w',
                   'formatter': 'detailed',
               },
               'foofile': {
                   'class': 'logging.FileHandler',
                   'filename': 'mplog-foo.log',
                   'mode': 'w',
                   'formatter': 'detailed',
               },
               'errors': {
                   'class': 'logging.FileHandler',
                   'filename': 'mplog-errors.log',
                   'mode': 'w',
                   'level': 'ERROR',
                   'formatter': 'detailed',
               },
           },
           'loggers': {
               'foo': {
                   'handlers': ['foofile']
               }
           },
           'root': {
               'level': 'DEBUG',
               'handlers': ['console', 'file', 'errors']
           },
       }
       workers = []
       for i in range(5):
           wp = Process(target=worker_process, name='worker %d' % (i + 1), args=(q,))
           workers.append(wp)
           wp.start()
       logging.config.dictConfig(d)
       lp = threading.Thread(target=logger_thread, args=(q,))
       lp.start()
       # At this point, the main process could do some useful work of its own
       # Once it's done that, it can wait for the workers to terminate...
       for wp in workers:
           wp.join()
       # And now tell the logging thread to finish up, too
       q.put(None)
       lp.join()

Esta variante muestra cómo puede, por ejemplo, aplicar la
configuración para logging particulares: el registrador "foo" tiene un
gestor especial que almacena todos los eventos en el subsistema "foo"
en un archivo "mplog-foo.log". Esto será utilizado por la maquinaria
de logging en el proceso principal (aunque los eventos logging se
generen en los procesos de trabajo) para dirigir los mensajes a los
destinos apropiados.

### Usando concurrent.futures.ProcessPoolExecutor

Si desea utilizar "concurrent.futures.ProcessPoolExecutor" para
iniciar sus procesos de trabajo, debe crear la cola de manera
ligeramente diferente. En vez de

   queue = multiprocessing.Queue(-1)

debería usar

   queue = multiprocessing.Manager().Queue(-1)  # also works with the examples above

y luego puede reemplazar la creación del trabajador de esto:

   workers = []
   for i in range(10):
       worker = multiprocessing.Process(target=worker_process,
                                        args=(queue, worker_configurer))
       workers.append(worker)
       worker.start()
   for w in workers:
       w.join()

a esto (recuerda el primer *import* "concurrent.futures"):

   with concurrent.futures.ProcessPoolExecutor(max_workers=10) as executor:
       for i in range(10):
           executor.submit(worker_process, queue, worker_configurer)

### Deploying web applications using Gunicorn and uWSGI

When deploying web applications using Gunicorn or uWSGI (or similar),
multiple worker processes are created to handle client requests. In
such environments, avoid creating file-based handlers directly in your
web application. Instead, use a "SocketHandler" to log from the web
application to a listener in a separate process. This can be set up
using a process management tool such as Supervisor - see Running a
logging socket listener in production for more details.

## Usando rotación de archivos

Sometimes you want to let a log file grow to a certain size, then open
a new file and log to that. You may want to keep a certain number of
these files, and when that many files have been created, rotate the
files so that the number of files and the size of the files both
remain bounded. For this usage pattern, the logging package provides a
"RotatingFileHandler":

   import glob
   import logging
   import logging.handlers

   LOG_FILENAME = 'logging_rotatingfile_example.out'

   # Set up a specific logger with our desired output level
   my_logger = logging.getLogger('MyLogger')
   my_logger.setLevel(logging.DEBUG)

   # Add the log message handler to the logger
   handler = logging.handlers.RotatingFileHandler(
                 LOG_FILENAME, maxBytes=20, backupCount=5)

   my_logger.addHandler(handler)

   # Log some messages
   for i in range(20):
       my_logger.debug('i = %d' % i)

   # See what files are created
   logfiles = glob.glob('%s*' % LOG_FILENAME)

   for filename in logfiles:
       print(filename)

El resultado debe ser 6 archivos separados, cada uno con parte del
historial de log de la aplicación:

   logging_rotatingfile_example.out
   logging_rotatingfile_example.out.1
   logging_rotatingfile_example.out.2
   logging_rotatingfile_example.out.3
   logging_rotatingfile_example.out.4
   logging_rotatingfile_example.out.5

El archivo más actual siempre es "logging_rotatingfile_example.out", y
cada vez que alcanza el límite de tamaño, se le cambia el nombre con
el sufijo ".1". Se cambia el nombre de cada uno de los archivos de
respaldo existentes para incrementar el sufijo (".1" se convierte en
".2", etc.) y se borra el archivo ".6".

Obviamente, este ejemplo establece la longitud del log demasiado
pequeña como un ejemplo extremo. Se querrá establecer *maxBytes* en un
valor apropiado.

## Uso de estilos de formato alternativos

Cuando se agregó logging a la biblioteca estándar de Python, la única
forma de formatear mensajes con contenido variable era usar el método
de formateo %. Desde entonces, Python ha ganado dos nuevos enfoques de
formato: "string.Template" (agregado en Python 2.4) y "str.format()"
(agregado en Python 2.6).

Logging (a partir de la versión 3.2) proporciona un soporte mejorado
para estos dos estilos de formato adicionales. La clase "Formatter" ha
sido mejorada para tomar un parámetro de palabra clave adicional
llamado "style". El valor predeterminado es "'%'", pero otros valores
posibles son "'{'" y "'$'", que corresponden a los otros dos estilos
de formato. La compatibilidad con versiones anteriores se mantiene de
forma predeterminada (como era de esperar), pero al especificar
explícitamente un parámetro de estilo, tiene la capacidad de
especificar cadenas de formato que funcionan con "str.format()" o
"string.Template". Aquí hay una sesión de consola de ejemplo para
mostrar las posibilidades:

   >>> import logging
   >>> root = logging.getLogger()
   >>> root.setLevel(logging.DEBUG)
   >>> handler = logging.StreamHandler()
   >>> bf = logging.Formatter('{asctime} {name} {levelname:8s} {message}',
   ...                        style='{')
   >>> handler.setFormatter(bf)
   >>> root.addHandler(handler)
   >>> logger = logging.getLogger('foo.bar')
   >>> logger.debug('This is a DEBUG message')
   2010-10-28 15:11:55,341 foo.bar DEBUG    This is a DEBUG message
   >>> logger.critical('This is a CRITICAL message')
   2010-10-28 15:12:11,526 foo.bar CRITICAL This is a CRITICAL message
   >>> df = logging.Formatter('$asctime $name ${levelname} $message',
   ...                        style='$')
   >>> handler.setFormatter(df)
   >>> logger.debug('This is a DEBUG message')
   2010-10-28 15:13:06,924 foo.bar DEBUG This is a DEBUG message
   >>> logger.critical('This is a CRITICAL message')
   2010-10-28 15:13:11,494 foo.bar CRITICAL This is a CRITICAL message
   >>>

Tenga en cuenta que el formato de logging para la salida final a los
logs es completamente independiente de cómo se construye un mensaje de
logging individual. Para eso todavía puede usar el formateo %, como se
muestra aquí:

   >>> logger.error('This is an%s %s %s', 'other,', 'ERROR,', 'message')
   2010-10-28 15:19:29,833 foo.bar ERROR This is another, ERROR, message
   >>>

Las llamadas de Logging ("logger.debug()", "logger.info()", etc.) solo
toman parámetros posicionales para el mensaje de logging real en sí,
los parámetros de palabras clave se usan solo para determinar opciones
sobre cómo gestionar la llamada propiamente a Logging (por ejemplo, el
parámetro de palabra clave "exc_info" para indicar que la información
de rastreo debe registrarse, o el parámetro de palabra clave "extra"
para indicar información contextual adicional que se agregará al log).
Por lo tanto, no puede realizar llamadas de logging directamente
usando la sintaxis "str.format()" o "string.Template", porque
internamente el paquete de logging usa formato % para fusionar la
cadena de formato y los argumentos de las variables. No habría ningún
cambio en esto mientras se conserva la compatibilidad con versiones
anteriores, ya que todas las llamadas de logging que están en el
código existente usarán cadenas de formato %.

Sin embargo, existe una forma en la que puede usar el formato {} - y $
- para construir sus mensajes de log individuales. Recuerde que para
un mensaje puede usar un objeto arbitrario como una cadena de
caracteres de formato de mensaje, y que el paquete logging llamará a
"str()" en ese objeto para obtener la cadena de caracteres de formato
real. Considere las siguientes dos clases:

   class BraceMessage:
       def __init__(self, fmt, /, *args, **kwargs):
           self.fmt = fmt
           self.args = args
           self.kwargs = kwargs

       def __str__(self):
           return self.fmt.format(*self.args, **self.kwargs)

   class DollarMessage:
       def __init__(self, fmt, /, **kwargs):
           self.fmt = fmt
           self.kwargs = kwargs

       def __str__(self):
           from string import Template
           return Template(self.fmt).substitute(**self.kwargs)

Cualquiera de estos puede usarse en lugar de una cadena de formato,
para permitir que se use el formato {} - o $ - para construir la parte
del "mensaje" real que aparece en la salida del log en lugar de
"%(message)s" o "{message}" o "$message". Es un poco difícil de
manejar usar los nombres de las clases siempre que quieras registrar
algo, pero es bastante aceptable si usas un alias como __ (doble
subrayado --- no confundir con _, el subrayado simple usado como
sinónimo/alias para "gettext.gettext()" o sus hermanos).

Las clases anteriores no están incluidas en Python, aunque son
bastante fáciles de copiar y pegar en su propio código. Se pueden usar
de la siguiente manera (asumiendo que están declaradas en un módulo
llamado "wherever"):

   >>> from wherever import BraceMessage as __
   >>> print(__('Message with {0} {name}', 2, name='placeholders'))
   Message with 2 placeholders
   >>> class Point: pass
   ...
   >>> p = Point()
   >>> p.x = 0.5
   >>> p.y = 0.5
   >>> print(__('Message with coordinates: ({point.x:.2f}, {point.y:.2f})',
   ...       point=p))
   Message with coordinates: (0.50, 0.50)
   >>> from wherever import DollarMessage as __
   >>> print(__('Message with $num $what', num=2, what='placeholders'))
   Message with 2 placeholders
   >>>

Si bien los ejemplos anteriores usan "print()" para mostrar cómo
funciona el formateo, por supuesto usaría "logger.debug()" o similar
para realmente registrar usando este enfoque.

One thing to note is that you pay no significant performance penalty
with this approach: the actual formatting happens not when you make
the logging call, but when (and if) the logged message is actually
about to be output to a log by a handler. So the only slightly unusual
thing which might trip you up is that the parentheses go around the
format string and the arguments, not just the format string. That's
because the __ notation is just syntax sugar for a constructor call to
one of the "*XXX*Message" classes.

Si lo prefiere, puede usar "LoggerAdapter" para lograr un efecto
similar al anterior, como en el siguiente ejemplo:

   import logging

   class Message:
       def __init__(self, fmt, args):
           self.fmt = fmt
           self.args = args

       def __str__(self):
           return self.fmt.format(*self.args)

   class StyleAdapter(logging.LoggerAdapter):
       def log(self, level, msg, /, *args, stacklevel=1, **kwargs):
           if self.isEnabledFor(level):
               msg, kwargs = self.process(msg, kwargs)
               self.logger.log(level, Message(msg, args), **kwargs,
                               stacklevel=stacklevel+1)

   logger = StyleAdapter(logging.getLogger(__name__))

   def main():
       logger.debug('Hello, {}', 'world!')

   if __name__ == '__main__':
       logging.basicConfig(level=logging.DEBUG)
       main()

The above script should log the message "Hello, world!" when run with
Python 3.8 or later.

## Personalización de "LogRecord"

Cada evento logging está representado por una instancia "LogRecord".
Cuando se registra un evento y no se filtra por el nivel de un
registrador, se crea "LogRecord", se llena con información sobre el
evento y luego se pasa a los gestores de ese registrador (y sus
antepasados, hasta (e incluyéndolo) el registrador donde se
deshabilita una mayor propagación en la jerarquía). Antes de Python
3.2, solo había dos lugares donde se realizaba esta creación:

* "Logger.makeRecord()", que se llama en el proceso normal de logging
  de un evento. Esto invoca "LogRecord" directamente para crear una
  instancia.

* "makeLogRecord()", que se llama con un diccionario que contiene
  atributos que se agregarán al *LogRecord*. Esto se suele invocar
  cuando se ha recibido un diccionario adecuado a través de la red
  (por ejemplo, en forma de *pickle* a través de "SocketHandler", o en
  formato JSON a través de "HTTPHandler").

Por lo general, esto significa que si necesita hacer algo especial con
"LogRecord", debe hacer una de las siguientes cosas.

* Cree su propia subclase "Logger", que anula "Logger.makeRecord()", y
  configúrelo usando "setLoggerClass()" antes de que se creen
  instancias de los registradores que le interesan.

* Agrega un "Filter" a un registrador o gestor, que realiza la
  manipulación especial necesaria que necesita cuando se llama a su
  método "filter()".

El primer enfoque sería un poco difícil de manejar en el escenario en
el que (digamos) varias bibliotecas diferentes quisieran hacer cosas
diferentes. Cada uno intentaría establecer su propia subclase
"Logger", y el que hiciera esto último ganaría.

El segundo enfoque funciona razonablemente bien en muchos casos, pero
no le permite, por ejemplo, usar una subclase especializada de
"LogRecord". Los desarrolladores de bibliotecas pueden establecer un
filtro adecuado en sus registradores, pero tendrían que recordar
hacerlo cada vez que introduzcan un nuevo registrador (lo que harían
simplemente agregando nuevos paquetes o módulos y haciendo

   logger = logging.getLogger(__name__)

a nivel de módulo). Probablemente sean demasiadas cosas en las que
pensar. Los desarrolladores también podrían agregar el filtro a
"NullHandler" adjunto a su registrador de nivel superior, pero esto no
se invocaría si un desarrollador de aplicaciones adjuntara un
controlador a un registrador de biblioteca de nivel inferior --- así
que la salida de ese gestor no reflejaría las intenciones del
desarrollador de la biblioteca.

En Python 3.2 y posteriores, la creación de "LogRecord" se realiza a
través de una fábrica, que puede especificar. La fábrica es
simplemente un invocable que puede configurar con
"setLogRecordFactory()", e interrogar con "getLogRecordFactory()". La
fábrica se invoca con la misma firma que el constructor "LogRecord",
ya que "LogRecord" es la configuración predeterminada de la fábrica.

Este enfoque permite que una fábrica personalizada controle todos los
aspectos de la creación de *LogRecord*. Por ejemplo, podría devolver
una subclase, o simplemente agregar algunos atributos adicionales al
registro una vez creado, usando un patrón similar a este:

   old_factory = logging.getLogRecordFactory()

   def record_factory(*args, **kwargs):
       record = old_factory(*args, **kwargs)
       record.custom_attribute = 0xdecafbad
       return record

   logging.setLogRecordFactory(record_factory)

Este patrón permite que diferentes bibliotecas encadenen fábricas
juntas, y siempre que no sobrescriban los atributos de las demás o
sobrescriban involuntariamente los atributos proporcionados como
estándar, no debería haber sorpresas. Sin embargo, debe tenerse en
cuenta que cada eslabón de la cadena agrega una sobrecarga de tiempo
de ejecución a todas las operaciones de logging, y la técnica solo
debe usarse cuando el uso de "Filter" no proporciona el resultado
deseado.

## Subclassing QueueHandler and QueueListener- a ZeroMQ example

### Subclass "QueueHandler"

Puede usar una subclase "QueueHandler" para enviar mensajes a otros
tipos de colas, por ejemplo, un socket de 'publicación' ZeroMQ. En el
siguiente ejemplo, el socket se crea por separado y se pasa al gestor
(como su 'cola'):

   import zmq   # using pyzmq, the Python binding for ZeroMQ
   import json  # for serializing records portably

   ctx = zmq.Context()
   sock = zmq.Socket(ctx, zmq.PUB)  # or zmq.PUSH, or other suitable value
   sock.bind('tcp://*:5556')        # or wherever

   class ZeroMQSocketHandler(QueueHandler):
       def enqueue(self, record):
           self.queue.send_json(record.__dict__)

   handler = ZeroMQSocketHandler(sock)

Por supuesto, hay otras formas de organizar esto, por ejemplo, pasando
los datos que necesita el gestor para crear el socket:

   class ZeroMQSocketHandler(QueueHandler):
       def __init__(self, uri, socktype=zmq.PUB, ctx=None):
           self.ctx = ctx or zmq.Context()
           socket = zmq.Socket(self.ctx, socktype)
           socket.bind(uri)
           super().__init__(socket)

       def enqueue(self, record):
           self.queue.send_json(record.__dict__)

       def close(self):
           self.queue.close()

### Subclass "QueueListener"

También puede subclasificar "QueueListener" para obtener mensajes de
otros tipos de colas, por ejemplo, un socket de 'suscripción' de
ZeroMQ. Aquí tienes un ejemplo:

   class ZeroMQSocketListener(QueueListener):
       def __init__(self, uri, /, *handlers, **kwargs):
           self.ctx = kwargs.get('ctx') or zmq.Context()
           socket = zmq.Socket(self.ctx, zmq.SUB)
           socket.setsockopt_string(zmq.SUBSCRIBE, '')  # subscribe to everything
           socket.connect(uri)
           super().__init__(socket, *handlers, **kwargs)

       def dequeue(self):
           msg = self.queue.recv_json()
           return logging.makeLogRecord(msg)

## Subclassing QueueHandler and QueueListener- a "pynng" example

In a similar way to the above section, we can implement a listener and
handler using pynng, which is a Python binding to NNG, billed as a
spiritual successor to ZeroMQ. The following snippets illustrate --
you can test them in an environment which has "pynng" installed. Just
for variety, we present the listener first.

### Subclass "QueueListener"

   # listener.py
   import json
   import logging
   import logging.handlers

   import pynng

   DEFAULT_ADDR = "tcp://localhost:13232"

   interrupted = False

   class NNGSocketListener(logging.handlers.QueueListener):

       def __init__(self, uri, /, *handlers, **kwargs):
           # Have a timeout for interruptibility, and open a
           # subscriber socket
           socket = pynng.Sub0(listen=uri, recv_timeout=500)
           # The b'' subscription matches all topics
           topics = kwargs.pop('topics', None) or b''
           socket.subscribe(topics)
           # We treat the socket as a queue
           super().__init__(socket, *handlers, **kwargs)

       def dequeue(self, block):
           data = None
           # Keep looping while not interrupted and no data received over the
           # socket
           while not interrupted:
               try:
                   data = self.queue.recv(block=block)
                   break
               except pynng.Timeout:
                   pass
               except pynng.Closed:  # sometimes happens when you hit Ctrl-C
                   break
           if data is None:
               return None
           # Get the logging event sent from a publisher
           event = json.loads(data.decode('utf-8'))
           return logging.makeLogRecord(event)

       def enqueue_sentinel(self):
           # Not used in this implementation, as the socket isn't really a
           # queue
           pass

   logging.getLogger('pynng').propagate = False
   listener = NNGSocketListener(DEFAULT_ADDR, logging.StreamHandler(), topics=b'')
   listener.start()
   print('Press Ctrl-C to stop.')
   try:
       while True:
           pass
   except KeyboardInterrupt:
       interrupted = True
   finally:
       listener.stop()

### Subclass "QueueHandler"

   # sender.py
   import json
   import logging
   import logging.handlers
   import time
   import random

   import pynng

   DEFAULT_ADDR = "tcp://localhost:13232"

   class NNGSocketHandler(logging.handlers.QueueHandler):

       def __init__(self, uri):
           socket = pynng.Pub0(dial=uri, send_timeout=500)
           super().__init__(socket)

       def enqueue(self, record):
           # Send the record as UTF-8 encoded JSON
           d = dict(record.__dict__)
           data = json.dumps(d)
           self.queue.send(data.encode('utf-8'))

       def close(self):
           self.queue.close()

   logging.getLogger('pynng').propagate = False
   handler = NNGSocketHandler(DEFAULT_ADDR)
   # Make sure the process ID is in the output
   logging.basicConfig(level=logging.DEBUG,
                       handlers=[logging.StreamHandler(), handler],
                       format='%(levelname)-8s %(name)10s %(process)6s %(message)s')
   levels = (logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR,
             logging.CRITICAL)
   logger_names = ('myapp', 'myapp.lib1', 'myapp.lib2')
   msgno = 1
   while True:
       # Just randomly select some loggers and levels and log away
       level = random.choice(levels)
       logger = logging.getLogger(random.choice(logger_names))
       logger.log(level, 'Message no. %5d' % msgno)
       msgno += 1
       delay = random.random() * 2 + 0.5
       time.sleep(delay)

You can run the above two snippets in separate command shells. If we
run the listener in one shell and run the sender in two separate
shells, we should see something like the following. In the first
sender shell:

   $ python sender.py
   DEBUG         myapp    613 Message no.     1
   WARNING  myapp.lib2    613 Message no.     2
   CRITICAL myapp.lib2    613 Message no.     3
   WARNING  myapp.lib2    613 Message no.     4
   CRITICAL myapp.lib1    613 Message no.     5
   DEBUG         myapp    613 Message no.     6
   CRITICAL myapp.lib1    613 Message no.     7
   INFO     myapp.lib1    613 Message no.     8
   (and so on)

In the second sender shell:

   $ python sender.py
   INFO     myapp.lib2    657 Message no.     1
   CRITICAL myapp.lib2    657 Message no.     2
   CRITICAL      myapp    657 Message no.     3
   CRITICAL myapp.lib1    657 Message no.     4
   INFO     myapp.lib1    657 Message no.     5
   WARNING  myapp.lib2    657 Message no.     6
   CRITICAL      myapp    657 Message no.     7
   DEBUG    myapp.lib1    657 Message no.     8
   (and so on)

In the listener shell:

   $ python listener.py
   Press Ctrl-C to stop.
   DEBUG         myapp    613 Message no.     1
   WARNING  myapp.lib2    613 Message no.     2
   INFO     myapp.lib2    657 Message no.     1
   CRITICAL myapp.lib2    613 Message no.     3
   CRITICAL myapp.lib2    657 Message no.     2
   CRITICAL      myapp    657 Message no.     3
   WARNING  myapp.lib2    613 Message no.     4
   CRITICAL myapp.lib1    613 Message no.     5
   CRITICAL myapp.lib1    657 Message no.     4
   INFO     myapp.lib1    657 Message no.     5
   DEBUG         myapp    613 Message no.     6
   WARNING  myapp.lib2    657 Message no.     6
   CRITICAL      myapp    657 Message no.     7
   CRITICAL myapp.lib1    613 Message no.     7
   INFO     myapp.lib1    613 Message no.     8
   DEBUG    myapp.lib1    657 Message no.     8
   (and so on)

As you can see, the logging from the two sender processes is
interleaved in the listener's output.

## Una configuración de ejemplo basada en diccionario

A continuación se muestra un ejemplo de un diccionario de
configuración de logging, tomado de la documentación del proyecto
Django. Este diccionario se pasa a "dictConfig()" para poner en efecto
la configuración:

   LOGGING = {
       'version': 1,
       'disable_existing_loggers': False,
       'formatters': {
           'verbose': {
               'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
               'style': '{',
           },
           'simple': {
               'format': '{levelname} {message}',
               'style': '{',
           },
       },
       'filters': {
           'special': {
               '()': 'project.logging.SpecialFilter',
               'foo': 'bar',
           },
       },
       'handlers': {
           'console': {
               'level': 'INFO',
               'class': 'logging.StreamHandler',
               'formatter': 'simple',
           },
           'mail_admins': {
               'level': 'ERROR',
               'class': 'django.utils.log.AdminEmailHandler',
               'filters': ['special']
           }
       },
       'loggers': {
           'django': {
               'handlers': ['console'],
               'propagate': True,
           },
           'django.request': {
               'handlers': ['mail_admins'],
               'level': 'ERROR',
               'propagate': False,
           },
           'myproject.custom': {
               'handlers': ['console', 'mail_admins'],
               'level': 'INFO',
               'filters': ['special']
           }
       }
   }

Para obtener más información sobre esta configuración, puede ver la
sección correspondiente de la documentación de Django.

## Usar un rotador y un nombre para personalizar el procesamiento de rotación de log

An example of how you can define a namer and rotator is given in the
following runnable script, which shows gzip compression of the log
file:

   import gzip
   import logging
   import logging.handlers
   import os
   import shutil

   def namer(name):
       return name + ".gz"

   def rotator(source, dest):
       with open(source, 'rb') as f_in:
           with gzip.open(dest, 'wb') as f_out:
               shutil.copyfileobj(f_in, f_out)
       os.remove(source)

   rh = logging.handlers.RotatingFileHandler('rotated.log', maxBytes=128, backupCount=5)
   rh.rotator = rotator
   rh.namer = namer

   root = logging.getLogger()
   root.setLevel(logging.INFO)
   root.addHandler(rh)
   f = logging.Formatter('%(asctime)s %(message)s')
   rh.setFormatter(f)
   for i in range(1000):
       root.info(f'Message no. {i + 1}')

After running this, you will see six new files, five of which are
compressed:

   $ ls rotated.log*
   rotated.log       rotated.log.2.gz  rotated.log.4.gz
   rotated.log.1.gz  rotated.log.3.gz  rotated.log.5.gz
   $ zcat rotated.log.1.gz
   2023-01-20 02:28:17,767 Message no. 996
   2023-01-20 02:28:17,767 Message no. 997
   2023-01-20 02:28:17,767 Message no. 998

## Un ejemplo de multiprocesamiento más elaborado

El siguiente ejemplo de trabajo muestra cómo logging se puede usar con
multiprocesamiento usando archivos de configuración. Las
configuraciones son bastante simples, pero sirven para ilustrar cómo
se podrían implementar las más complejas en un escenario real de
multiprocesamiento.

En el ejemplo, el proceso principal genera un proceso de escucha y
algunos procesos de trabajo. Cada uno de los procesos principales, el
oyente y los trabajadores tienen tres configuraciones separadas (todos
los trabajadores comparten la misma configuración). Podemos ver el
registro en el proceso principal, cómo los trabajadores se registran
en un QueueHandler y cómo el oyente implementa un QueueListener y una
configuración de registro más compleja, y organiza el envío de eventos
recibidos a través de la cola a los controladores especificados en la
configuración. Tenga en cuenta que estas configuraciones son puramente
ilustrativas, pero debería poder adaptar este ejemplo a su propio
escenario.

Aquí está el script, el docstrings y los comentarios, esperemos,
expliquen cómo funciona:

   import logging
   import logging.config
   import logging.handlers
   from multiprocessing import Process, Queue, Event, current_process
   import os
   import random
   import time

   class MyHandler:
       """
       A simple handler for logging events. It runs in the listener process and
       dispatches events to loggers based on the name in the received record,
       which then get dispatched, by the logging system, to the handlers
       configured for those loggers.
       """

       def handle(self, record):
           if record.name == "root":
               logger = logging.getLogger()
           else:
               logger = logging.getLogger(record.name)

           if logger.isEnabledFor(record.levelno):
               # The process name is transformed just to show that it's the listener
               # doing the logging to files and console
               record.processName = '%s (for %s)' % (current_process().name, record.processName)
               logger.handle(record)

   def listener_process(q, stop_event, config):
       """
       This could be done in the main process, but is just done in a separate
       process for illustrative purposes.

       This initialises logging according to the specified configuration,
       starts the listener and waits for the main process to signal completion
       via the event. The listener is then stopped, and the process exits.
       """
       logging.config.dictConfig(config)
       listener = logging.handlers.QueueListener(q, MyHandler())
       listener.start()
       if os.name == 'posix':
           # On POSIX, the setup logger will have been configured in the
           # parent process, but should have been disabled following the
           # dictConfig call.
           # On Windows, since fork isn't used, the setup logger won't
           # exist in the child, so it would be created and the message
           # would appear - hence the "if posix" clause.
           logger = logging.getLogger('setup')
           logger.critical('Should not appear, because of disabled logger ...')
       stop_event.wait()
       listener.stop()

   def worker_process(config):
       """
       A number of these are spawned for the purpose of illustration. In
       practice, they could be a heterogeneous bunch of processes rather than
       ones which are identical to each other.

       This initialises logging according to the specified configuration,
       and logs a hundred messages with random levels to randomly selected
       loggers.

       A small sleep is added to allow other processes a chance to run. This
       is not strictly needed, but it mixes the output from the different
       processes a bit more than if it's left out.
       """
       logging.config.dictConfig(config)
       levels = [logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR,
                 logging.CRITICAL]
       loggers = ['foo', 'foo.bar', 'foo.bar.baz',
                  'spam', 'spam.ham', 'spam.ham.eggs']
       if os.name == 'posix':
           # On POSIX, the setup logger will have been configured in the
           # parent process, but should have been disabled following the
           # dictConfig call.
           # On Windows, since fork isn't used, the setup logger won't
           # exist in the child, so it would be created and the message
           # would appear - hence the "if posix" clause.
           logger = logging.getLogger('setup')
           logger.critical('Should not appear, because of disabled logger ...')
       for i in range(100):
           lvl = random.choice(levels)
           logger = logging.getLogger(random.choice(loggers))
           logger.log(lvl, 'Message no. %d', i)
           time.sleep(0.01)

   def main():
       q = Queue()
       # The main process gets a simple configuration which prints to the console.
       config_initial = {
           'version': 1,
           'handlers': {
               'console': {
                   'class': 'logging.StreamHandler',
                   'level': 'INFO'
               }
           },
           'root': {
               'handlers': ['console'],
               'level': 'DEBUG'
           }
       }
       # The worker process configuration is just a QueueHandler attached to the
       # root logger, which allows all messages to be sent to the queue.
       # We disable existing loggers to disable the "setup" logger used in the
       # parent process. This is needed on POSIX because the logger will
       # be there in the child following a fork().
       config_worker = {
           'version': 1,
           'disable_existing_loggers': True,
           'handlers': {
               'queue': {
                   'class': 'logging.handlers.QueueHandler',
                   'queue': q
               }
           },
           'root': {
               'handlers': ['queue'],
               'level': 'DEBUG'
           }
       }
       # The listener process configuration shows that the full flexibility of
       # logging configuration is available to dispatch events to handlers however
       # you want.
       # We disable existing loggers to disable the "setup" logger used in the
       # parent process. This is needed on POSIX because the logger will
       # be there in the child following a fork().
       config_listener = {
           'version': 1,
           'disable_existing_loggers': True,
           'formatters': {
               'detailed': {
                   'class': 'logging.Formatter',
                   'format': '%(asctime)s %(name)-15s %(levelname)-8s %(processName)-10s %(message)s'
               },
               'simple': {
                   'class': 'logging.Formatter',
                   'format': '%(name)-15s %(levelname)-8s %(processName)-10s %(message)s'
               }
           },
           'handlers': {
               'console': {
                   'class': 'logging.StreamHandler',
                   'formatter': 'simple',
                   'level': 'INFO'
               },
               'file': {
                   'class': 'logging.FileHandler',
                   'filename': 'mplog.log',
                   'mode': 'w',
                   'formatter': 'detailed'
               },
               'foofile': {
                   'class': 'logging.FileHandler',
                   'filename': 'mplog-foo.log',
                   'mode': 'w',
                   'formatter': 'detailed'
               },
               'errors': {
                   'class': 'logging.FileHandler',
                   'filename': 'mplog-errors.log',
                   'mode': 'w',
                   'formatter': 'detailed',
                   'level': 'ERROR'
               }
           },
           'loggers': {
               'foo': {
                   'handlers': ['foofile']
               }
           },
           'root': {
               'handlers': ['console', 'file', 'errors'],
               'level': 'DEBUG'
           }
       }
       # Log some initial events, just to show that logging in the parent works
       # normally.
       logging.config.dictConfig(config_initial)
       logger = logging.getLogger('setup')
       logger.info('About to create workers ...')
       workers = []
       for i in range(5):
           wp = Process(target=worker_process, name='worker %d' % (i + 1),
                        args=(config_worker,))
           workers.append(wp)
           wp.start()
           logger.info('Started worker: %s', wp.name)
       logger.info('About to create listener ...')
       stop_event = Event()
       lp = Process(target=listener_process, name='listener',
                    args=(q, stop_event, config_listener))
       lp.start()
       logger.info('Started listener')
       # We now hang around for the workers to finish their work.
       for wp in workers:
           wp.join()
       # Workers all done, listening can now stop.
       # Logging in the parent still works normally.
       logger.info('Telling listener to stop ...')
       stop_event.set()
       lp.join()
       logger.info('All done.')

   if __name__ == '__main__':
       main()

## Insertar BOM en mensajes enviados a SysLogHandler

**RFC 5424** requiere que se envíe un mensaje Unicode a un demonio
syslog como un conjunto de bytes que tienen la siguiente estructura:
un componente opcional ASCII puro, seguido de una marca de orden de
bytes UTF-8 (BOM), seguida de Codificado en Unicode usando UTF-8. (Ver
sección relevante de la especificación **RFC 5424 Section 6**.)

En Python 3.1, se agregó código a "SysLogHandler" para insertar BOM en
el mensaje, pero desafortunadamente, se implementó incorrectamente,
BOM aparece al principio del mensaje y, por lo tanto, no permite
ningún componente ASCII puro para que aparezca antes.

Como este comportamiento no funciona, el código de inserción BOM
incorrecto se elimina de Python 3.2.4 y versiones posteriores. Sin
embargo, no se está reemplazando, y si desea producir mensajes
compatibles con **RFC 5424** que incluyan BOM, una secuencia opcional
de ASCII puro antes y Unicode arbitrario después, codificados usando
UTF-8; entonces necesita hacer lo siguiente:

1. Adjunte una instancia de "Formatter" a su instancia
   "SysLogHandler", con una cadena de caracteres de formato como:

      'ASCII section\ufeffUnicode section'

   El punto de código Unicode U+ FEFF, cuando se codifica usando
   UTF-8, se codificará como una BOM UTF-8, la cadena de bytes
   "b'\xef\xbb\xbf'".

2. Reemplace la sección ASCII con los marcadores de posición que
   desee, pero asegúrese de que los datos que aparecen allí después de
   la sustitución sean siempre ASCII (de esa manera, permanecerán sin
   cambios después de la codificación UTF-8).

3. Reemplace la sección Unicode con los marcadores de posición que
   desee; si los datos que aparecen allí después de la sustitución
   contienen caracteres fuera del rango ASCII, está bien: se
   codificarán usando UTF-8.

El mensaje formateado *se* codificará utilizando la codificación UTF-8
por "SysLogHandler". Si sigue las reglas anteriores, debería poder
producir mensajes compatibles con **RFC 5424**. Si no lo hace, es
posible que el logging no se queje, pero sus mensajes no serán
compatibles con RFC 5424 y su demonio syslog puede quejarse.

## Implementar logging estructurado

Aunque la mayoría de los mensajes de registro están destinados a ser
leídos por humanos y, por lo tanto, no se pueden analizar fácilmente
mediante una máquina, puede haber circunstancias en las que desee
generar mensajes en un formato estructurado que *sea* capaz de ser
analizado por un programa (sin necesidad de expresiones regulares
complejas para analizar el mensaje de registro). Esto es sencillo de
lograr utilizando el paquete de registro. Hay varias formas de lograr
esto, pero el siguiente es un enfoque simple que usa JSON para
serializar el evento de una manera analizable por máquina:

   import json
   import logging

   class StructuredMessage:
       def __init__(self, message, /, **kwargs):
           self.message = message
           self.kwargs = kwargs

       def __str__(self):
           return '%s >>> %s' % (self.message, json.dumps(self.kwargs))

   _ = StructuredMessage   # optional, to improve readability

   logging.basicConfig(level=logging.INFO, format='%(message)s')
   logging.info(_('message 1', foo='bar', bar='baz', num=123, fnum=123.456))

Si se ejecuta el script anterior, se imprime:

   message 1 >>> {"fnum": 123.456, "num": 123, "bar": "baz", "foo": "bar"}

Tenga en cuenta que el orden de los elementos puede ser diferente
según la versión de Python utilizada.

Si necesita un procesamiento más especializado, puede utilizar un
codificador JSON personalizado, como en el siguiente ejemplo completo:

   import json
   import logging

   class Encoder(json.JSONEncoder):
       def default(self, o):
           if isinstance(o, set):
               return tuple(o)
           elif isinstance(o, str):
               return o.encode('unicode_escape').decode('ascii')
           return super().default(o)

   class StructuredMessage:
       def __init__(self, message, /, **kwargs):
           self.message = message
           self.kwargs = kwargs

       def __str__(self):
           s = Encoder().encode(self.kwargs)
           return '%s >>> %s' % (self.message, s)

   _ = StructuredMessage   # optional, to improve readability

   def main():
       logging.basicConfig(level=logging.INFO, format='%(message)s')
       logging.info(_('message 1', set_value={1, 2, 3}, snowman='\u2603'))

   if __name__ == '__main__':
       main()

Cuando se ejecuta el script anterior, se imprime:

   message 1 >>> {"snowman": "\u2603", "set_value": [1, 2, 3]}

Tenga en cuenta que el orden de los elementos puede ser diferente
según la versión de Python utilizada.

## Personalización de gestores con "dictConfig()"

Hay ocasiones en las que desea personalizar los gestores de logging de
formas particulares, y si usa "dictConfig()" puede hacerlo sin
subclases. Como ejemplo, considere que es posible que desee establecer
la propiedad de un archivo de log. En POSIX, esto se hace fácilmente
usando "shutil.chown()", pero los gestores de archivos en stdlib no
ofrecen soporte integrado. Puede personalizar la creación de gestores
usando una función simple como:

   def owned_file_handler(filename, mode='a', encoding=None, owner=None):
       if owner:
           if not os.path.exists(filename):
               open(filename, 'a').close()
           shutil.chown(filename, *owner)
       return logging.FileHandler(filename, mode, encoding)

Luego puede especificar, en una configuración de logging pasada a
"dictConfig()", que se cree un gestor de logging llamando a esta
función:

   LOGGING = {
       'version': 1,
       'disable_existing_loggers': False,
       'formatters': {
           'default': {
               'format': '%(asctime)s %(levelname)s %(name)s %(message)s'
           },
       },
       'handlers': {
           'file':{
               # The values below are popped from this dictionary and
               # used to create the handler, set the handler's level and
               # its formatter.
               '()': owned_file_handler,
               'level':'DEBUG',
               'formatter': 'default',
               # The values below are passed to the handler creator callable
               # as keyword arguments.
               'owner': ['pulse', 'pulse'],
               'filename': 'chowntest.log',
               'mode': 'w',
               'encoding': 'utf-8',
           },
       },
       'root': {
           'handlers': ['file'],
           'level': 'DEBUG',
       },
   }

En este ejemplo, se establece la propiedad utilizando el usuario y el
grupo "pulse", solo con fines ilustrativos. Poniéndolo junto en un
script de trabajo, "chowntest.py":

   import logging, logging.config, os, shutil

   def owned_file_handler(filename, mode='a', encoding=None, owner=None):
       if owner:
           if not os.path.exists(filename):
               open(filename, 'a').close()
           shutil.chown(filename, *owner)
       return logging.FileHandler(filename, mode, encoding)

   LOGGING = {
       'version': 1,
       'disable_existing_loggers': False,
       'formatters': {
           'default': {
               'format': '%(asctime)s %(levelname)s %(name)s %(message)s'
           },
       },
       'handlers': {
           'file':{
               # The values below are popped from this dictionary and
               # used to create the handler, set the handler's level and
               # its formatter.
               '()': owned_file_handler,
               'level':'DEBUG',
               'formatter': 'default',
               # The values below are passed to the handler creator callable
               # as keyword arguments.
               'owner': ['pulse', 'pulse'],
               'filename': 'chowntest.log',
               'mode': 'w',
               'encoding': 'utf-8',
           },
       },
       'root': {
           'handlers': ['file'],
           'level': 'DEBUG',
       },
   }

   logging.config.dictConfig(LOGGING)
   logger = logging.getLogger('mylogger')
   logger.debug('A debug message')

Para ejecutar esto, probablemente se necesite ejecutarlo como "root":

   $ sudo python3.3 chowntest.py
   $ cat chowntest.log
   2013-11-05 09:34:51,128 DEBUG mylogger A debug message
   $ ls -l chowntest.log
   -rw-r--r-- 1 pulse pulse 55 2013-11-05 09:34 chowntest.log

Tenga en cuenta que este ejemplo usa Python 3.3 porque ahí es donde
"shutil.chown()" aparece. Este enfoque debería funcionar con cualquier
versión de Python que admita "dictConfig()", es decir, Python 2.7, 3.2
o posterior. Con las versiones anteriores a 3.3, necesitaría
implementar el cambio de propiedad real usando, por ejemplo,
"os.chown()".

En la práctica, la función de creación de gestores puede estar en un
módulo de utilidad en algún lugar de su proyecto. En lugar de la línea
en la configuración:

   '()': owned_file_handler,

podrías usar, por ejemplo,:

   '()': 'ext://project.util.owned_file_handler',

donde "project.util" se puede reemplazar con el nombre real del
paquete donde reside la función. En el script de trabajo anterior, el
uso de "'ext://__main__.owned_file_handler'" debería funcionar. Aquí,
el invocable real se resuelve mediante "dictConfig()" de la
especificación "ext://".

Por fortuna, este ejemplo también indica el camino hacia cómo podría
implementar otros tipos de cambio de archivo, por ejemplo,
configurando de la misma manera bits de permisos POSIX específicos,
usando "os.chmod()".

Por supuesto, el enfoque también podría extenderse a tipos de gestores
distintos a "FileHandler" - por ejemplo, uno de los gestores de
archivos rotativos, o un tipo diferente por completo.

## Usar estilos de formato particulares en toda su aplicación

En Python 3.2, "Formatter" obtuvo un parámetro de palabra clave
"estilo" que, aunque por defecto era "%" para compatibilidad con
versiones anteriores, permitía la especificación de "{" o "$" para
permitir los enfoques de formato admitidos por "str.format()" y
"string.Template". Tenga en cuenta que esto rige el formato de los
mensajes de logging para la salida final a los logging y es
completamente ortogonal a cómo se construye un mensaje de logging
individual.

Logging calls ("debug()", "info()" etc.) only take positional
parameters for the actual logging message itself, with keyword
parameters used only for determining options for how to handle the
logging call (e.g. the "exc_info" keyword parameter to indicate that
traceback information should be logged, or the "extra" keyword
parameter to indicate additional contextual information to be added to
the log). So you cannot directly make logging calls using
"str.format()" or "string.Template" syntax, because internally the
logging package uses %-formatting to merge the format string and the
variable arguments. There would be no changing this while preserving
backward compatibility, since all logging calls which are out there in
existing code will be using %-format strings.

Ha habido sugerencias para asociar estilos de formato con *loggers*
específicos, pero ese enfoque también tiene problemas de
compatibilidad con versiones anteriores porque cualquier código
existente podría estar usando un nombre de *logger* dado y usando
formato %.

Para que logging funcione de manera interoperable entre cualquier
biblioteca de terceros y su código, las decisiones sobre el formato
deben tomarse a nivel de la llamada de logging individual. Esto abre
un par de formas en las que se pueden acomodar estilos de formato
alternativos.

### Uso de fábricas de LogRecord

En Python 3.2, junto con los cambios de "Formatter" mencionados
anteriormente, el paquete logging ganó la capacidad de permitir a los
usuarios establecer sus propias subclases "LogRecord", usando la
función "setLogRecordFactory()". Puede usar esto para configurar su
propia subclase de "LogRecord", que hace lo correcto al anular el
método "getMessage()". La implementación de la clase base de este
método es donde ocurre el formato "msg % args" y donde puede sustituir
su formato alternativo; sin embargo, debe tener cuidado de admitir
todos los estilos de formato y permitir formato % como predeterminado,
para garantizar la interoperabilidad con otro código. También se debe
tener cuidado de llamar a "str(self.msg)", tal como lo hace la
implementación base.

Consulte la documentación de referencia en "setLogRecordFactory()" y
"LogRecord" para obtener más información.

### Usar objetos de mensaje personalizados

Existe otra forma, quizás más sencilla, de usar el formato {} - y $ -
para construir sus mensajes de log individuales. Al iniciar sesión,
recuerde que puede usar cualquier objeto como una cadena de caracteres
de formato de mensaje (Usando objetos arbitrarios como mensajes) que
al iniciar sesión puede usar un objeto arbitrario como una cadena de
formato de mensaje, y que el paquete de logging llamará "str()" en ese
objeto para obtener el cadena de formato real. Considere las
siguientes dos clases:

   class BraceMessage:
       def __init__(self, fmt, /, *args, **kwargs):
           self.fmt = fmt
           self.args = args
           self.kwargs = kwargs

       def __str__(self):
           return self.fmt.format(*self.args, **self.kwargs)

   class DollarMessage:
       def __init__(self, fmt, /, **kwargs):
           self.fmt = fmt
           self.kwargs = kwargs

       def __str__(self):
           from string import Template
           return Template(self.fmt).substitute(**self.kwargs)

Cualquiera de estos puede usarse en lugar de una cadena de formato,
para permitir que se use el formato {} - o $ - para construir la parte
del "mensaje" real que aparece en la salida del log formateado en
lugar de “%(message)s” or “{message}” or “$message”. Si le resulta un
poco difícil de manejar usar los nombres de las clases cada vez que
desea registrar algo, puede hacerlo más tolerable si usa un alias como
"M" o "_" para el mensaje (o quizás "__", si está utilizando "_" para
localización).

A continuación se dan ejemplos de este enfoque. En primer lugar,
formatear con "str.format()":

   >>> __ = BraceMessage
   >>> print(__('Message with {0} {1}', 2, 'placeholders'))
   Message with 2 placeholders
   >>> class Point: pass
   ...
   >>> p = Point()
   >>> p.x = 0.5
   >>> p.y = 0.5
   >>> print(__('Message with coordinates: ({point.x:.2f}, {point.y:.2f})', point=p))
   Message with coordinates: (0.50, 0.50)

En segundo lugar, formatear con "string.Template":

   >>> __ = DollarMessage
   >>> print(__('Message with $num $what', num=2, what='placeholders'))
   Message with 2 placeholders
   >>>

One thing to note is that you pay no significant performance penalty
with this approach: the actual formatting happens not when you make
the logging call, but when (and if) the logged message is actually
about to be output to a log by a handler. So the only slightly unusual
thing which might trip you up is that the parentheses go around the
format string and the arguments, not just the format string. That’s
because the __ notation is just syntax sugar for a constructor call to
one of the "*XXX*Message" classes shown above.

## Configurar filtros con "dictConfig()"

*Puedes* configurar filtros usando "dictConfig()", aunque a primera
vista es posible que no sea obvio cómo hacerlo (de ahí esta receta).
Dado que "Filter" es la única clase de filtro incluida en la
biblioteca estándar, y es poco probable que satisfaga muchos
requisitos (solo está allí como clase base), normalmente necesitarás
definir tu propia subclase "Filter" con un método "filter()"
sobreescrito. Para hacer esto, especifique la clave "()" en el
diccionario de configuración para el filtro, especificando un
invocable que se usará para crear el filtro (una clase es la más
obvia, pero puede proporcionar cualquier invocable que retorne una
instancia "Filter"). Aquí hay un ejemplo completo:

   import logging
   import logging.config
   import sys

   class MyFilter(logging.Filter):
       def __init__(self, param=None):
           self.param = param

       def filter(self, record):
           if self.param is None:
               allow = True
           else:
               allow = self.param not in record.msg
           if allow:
               record.msg = 'changed: ' + record.msg
           return allow

   LOGGING = {
       'version': 1,
       'filters': {
           'myfilter': {
               '()': MyFilter,
               'param': 'noshow',
           }
       },
       'handlers': {
           'console': {
               'class': 'logging.StreamHandler',
               'filters': ['myfilter']
           }
       },
       'root': {
           'level': 'DEBUG',
           'handlers': ['console']
       },
   }

   if __name__ == '__main__':
       logging.config.dictConfig(LOGGING)
       logging.debug('hello')
       logging.debug('hello - noshow')

Este ejemplo muestra cómo puede pasar datos de configuración al
invocable que construye la instancia, en forma de parámetros de
palabras clave. Cuando se ejecuta, se imprimirá el script anterior:

   changed: hello

que muestra que el filtro está funcionando según lo configurado.

Un par de puntos adicionales a tener en cuenta:

* Si no puede hacer referencia al invocable directamente en la
  configuración (por ejemplo, si vive en un módulo diferente y no
  puede importarlo directamente donde está el diccionario de
  configuración), puede usar el formulario "ext://..." como se
  describe en Acceso a objetos externos. Por ejemplo, podría haber
  usado el texto "'ext://__main__.MyFilter'" en lugar de "MyFilter" en
  el ejemplo anterior.

* Además de los filtros, esta técnica también se puede utilizar para
  configurar gestores y formateadores personalizados. Consultar
  Objetos definidos por el usuario para obtener más información sobre
  cómo logging admite el uso de objetos definidos por el usuario en su
  configuración, y ver arriba la otra receta Personalización de
  gestores con dictConfig().

## Formato de excepción personalizado

Puede haber ocasiones en las que desee personalizar un formato de
excepción; por el bien del argumento, digamos que desea exactamente
una línea por evento registrado, incluso cuando la información de la
excepción está presente. Puede hacer esto con una clase de formateador
personalizada, como se muestra en el siguiente ejemplo:

   import logging

   class OneLineExceptionFormatter(logging.Formatter):
       def formatException(self, exc_info):
           """
           Format an exception so that it prints on a single line.
           """
           result = super().formatException(exc_info)
           return repr(result)  # or format into one line however you want to

       def format(self, record):
           s = super().format(record)
           if record.exc_text:
               s = s.replace('\n', '') + '|'
           return s

   def configure_logging():
       fh = logging.FileHandler('output.txt', 'w')
       f = OneLineExceptionFormatter('%(asctime)s|%(levelname)s|%(message)s|',
                                     '%d/%m/%Y %H:%M:%S')
       fh.setFormatter(f)
       root = logging.getLogger()
       root.setLevel(logging.DEBUG)
       root.addHandler(fh)

   def main():
       configure_logging()
       logging.info('Sample message')
       try:
           x = 1 / 0
       except ZeroDivisionError as e:
           logging.exception('ZeroDivisionError: %s', e)

   if __name__ == '__main__':
       main()

Cuando se ejecuta, esto produce un archivo con exactamente dos líneas:

   28/01/2015 07:21:23|INFO|Sample message|
   28/01/2015 07:21:23|ERROR|ZeroDivisionError: division by zero|'Traceback (most recent call last):\n  File "logtest7.py", line 30, in main\n    x = 1 / 0\nZeroDivisionError: division by zero'|

Si bien el tratamiento anterior es simplista, señala el camino hacia
cómo se puede formatear la información de excepción a su gusto. El
módulo "traceback" puede resultar útil para necesidades más
especializadas.

## Mensajes de logging hablantes

Puede haber situaciones en las que sea deseable que los mensajes de
logging se presenten en un formato audible en lugar de visible. Esto
es fácil de hacer si tiene la funcionalidad de texto a voz (*TTS* por
sus siglas en inglés) disponible en su sistema, incluso si no tiene un
*binding* Python. La mayoría de los sistemas TTS tienen un programa de
línea de comandos que puede ejecutar, y esto puede invocarse desde un
gestor usando "subprocess". Aquí se asume que los programas de línea
de comando TTS no esperarán interactuar con los usuarios o tardarán
mucho en completarse, y que la frecuencia de los mensajes registrados
no será tan alta como para inundar al usuario con mensajes, y que es
aceptable que los mensajes se reproducen uno a la vez en lugar de
todos al mismo tiempo. La implementación de ejemplo a continuación
espera a que se pronuncie un mensaje antes de que se procese el
siguiente, y esto puede hacer que otros gestores se mantengan
esperando. Aquí hay un breve ejemplo que muestra el enfoque, que asume
que el paquete TTS "espeak" está disponible:

   import logging
   import subprocess
   import sys

   class TTSHandler(logging.Handler):
       def emit(self, record):
           msg = self.format(record)
           # Speak slowly in a female English voice
           cmd = ['espeak', '-s150', '-ven+f3', msg]
           p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                                stderr=subprocess.STDOUT)
           # wait for the program to finish
           p.communicate()

   def configure_logging():
       h = TTSHandler()
       root = logging.getLogger()
       root.addHandler(h)
       # the default formatter just returns the message
       root.setLevel(logging.DEBUG)

   def main():
       logging.info('Hello')
       logging.debug('Goodbye')

   if __name__ == '__main__':
       configure_logging()
       sys.exit(main())

Cuando se ejecute, este script debería decir "Hola" y luego "Adiós"
con voz femenina.

El enfoque anterior puede, por supuesto, adaptarse a otros sistemas
TTS e incluso a otros sistemas que pueden procesar mensajes a través
de programas externos ejecutados desde una línea de comando.

## Almacenamiento en búfer de mensajes de logging y su salida condicional

Puede haber situaciones en las que desee registrar mensajes en un área
temporal y solo mostrarlos si se produce una determinada condición.
Por ejemplo, es posible que desee comenzar a registrar eventos de
depuración en una función, y si la función se completa sin errores, no
desea saturar el log con la información de depuración recopilada; pero
si hay un error, desea toda la información de depuración información
así como el error.

Aquí hay un ejemplo que muestra cómo puede hacer esto usando un
decorador para sus funciones donde desea que el logging se comporte de
esta manera. Hace uso de "logging.handlers.MemoryHandler", que permite
el almacenamiento en búfer de eventos registrados hasta que se
produzca alguna condición, momento en el que los eventos almacenados
en búfer se "flushed" y se pasan a otro gestor (el gestor "target")
para su procesamiento. De forma predeterminada, el "MemoryHandler" se
vacía cuando su búfer se llena o se ve un evento cuyo nivel es mayor o
igual a un umbral especificado. Puede usar esta receta con una
subclase más especializada de "MemoryHandler" si desea un
comportamiento de descarga personalizado.

El script de ejemplo tiene una función simple, "foo", que recorre
todos los niveles de logging, escribiendo en "sys.stderr" para decir
en qué nivel está a punto de *loguear* y luego registrar un mensaje en
ese nivel. Puede pasar un parámetro a "foo" que, si es verdadero, se
registrará en los niveles ERROR y CRITICAL; de lo contrario, solo
registrará en los niveles DEBUG, INFO y WARNING.

El script simplemente dispone decorar "foo" con un decorador que hará
el logging condicional que se requiere. El decorador toma un
registrador como parámetro y adjunta un gestor de memoria durante la
duración de la llamada a la función decorada. El decorador se puede
parametrizar adicionalmente utilizando un gestor *target*, un nivel en
el que debe producirse el vaciado y una capacidad para el búfer
(número de registros almacenados en búfer). Estos están
predeterminados a "StreamHandler" que escribe en "sys.stderr",
"logging.ERROR" y "100" respectivamente.

Aquí está el script:

   import logging
   from logging.handlers import MemoryHandler
   import sys

   logger = logging.getLogger(__name__)
   logger.addHandler(logging.NullHandler())

   def log_if_errors(logger, target_handler=None, flush_level=None, capacity=None):
       if target_handler is None:
           target_handler = logging.StreamHandler()
       if flush_level is None:
           flush_level = logging.ERROR
       if capacity is None:
           capacity = 100
       handler = MemoryHandler(capacity, flushLevel=flush_level, target=target_handler)

       def decorator(fn):
           def wrapper(*args, **kwargs):
               logger.addHandler(handler)
               try:
                   return fn(*args, **kwargs)
               except Exception:
                   logger.exception('call failed')
                   raise
               finally:
                   super(MemoryHandler, handler).flush()
                   logger.removeHandler(handler)
           return wrapper

       return decorator

   def write_line(s):
       sys.stderr.write('%s\n' % s)

   def foo(fail=False):
       write_line('about to log at DEBUG ...')
       logger.debug('Actually logged at DEBUG')
       write_line('about to log at INFO ...')
       logger.info('Actually logged at INFO')
       write_line('about to log at WARNING ...')
       logger.warning('Actually logged at WARNING')
       if fail:
           write_line('about to log at ERROR ...')
           logger.error('Actually logged at ERROR')
           write_line('about to log at CRITICAL ...')
           logger.critical('Actually logged at CRITICAL')
       return fail

   decorated_foo = log_if_errors(logger)(foo)

   if __name__ == '__main__':
       logger.setLevel(logging.DEBUG)
       write_line('Calling undecorated foo with False')
       assert not foo(False)
       write_line('Calling undecorated foo with True')
       assert foo(True)
       write_line('Calling decorated foo with False')
       assert not decorated_foo(False)
       write_line('Calling decorated foo with True')
       assert decorated_foo(True)

Cuando se ejecuta este script, se debe observar el siguiente
resultado:

   Calling undecorated foo with False
   about to log at DEBUG ...
   about to log at INFO ...
   about to log at WARNING ...
   Calling undecorated foo with True
   about to log at DEBUG ...
   about to log at INFO ...
   about to log at WARNING ...
   about to log at ERROR ...
   about to log at CRITICAL ...
   Calling decorated foo with False
   about to log at DEBUG ...
   about to log at INFO ...
   about to log at WARNING ...
   Calling decorated foo with True
   about to log at DEBUG ...
   about to log at INFO ...
   about to log at WARNING ...
   about to log at ERROR ...
   Actually logged at DEBUG
   Actually logged at INFO
   Actually logged at WARNING
   Actually logged at ERROR
   about to log at CRITICAL ...
   Actually logged at CRITICAL

Como puede ver, la salida real de logging solo ocurre cuando se
registra un evento cuya gravedad es ERROR o mayor, pero en ese caso,
también se registra cualquier evento anterior con una gravedad menor.

Por supuesto, puede utilizar las formas de decoración convencionales:

   @log_if_errors(logger)
   def foo(fail=False):
       ...

## Enviando mensajes de logging al correo electrónico, con almacenamiento en búfer

Para ilustrar cómo puede enviar mensajes de logging por correo
electrónico, de modo que se envíe un número determinado de mensajes,
puede usar la subclase "BufferingHandler". En el siguiente ejemplo,
que puedes adaptar a tus necesidades específicas, se proporciona un
sencillo arnés de pruebas que permite ejecutar el script con
argumentos de línea de comandos especificando lo que normalmente
necesitas para enviar cosas por SMTP. (Ejecute el script descargado
con el argumento "-h" para ver los argumentos necesarios y
opcionales).

   import logging
   import logging.handlers
   import smtplib

   class BufferingSMTPHandler(logging.handlers.BufferingHandler):
       def __init__(self, mailhost, port, username, password, fromaddr, toaddrs,
                    subject, capacity):
           logging.handlers.BufferingHandler.__init__(self, capacity)
           self.mailhost = mailhost
           self.mailport = port
           self.username = username
           self.password = password
           self.fromaddr = fromaddr
           if isinstance(toaddrs, str):
               toaddrs = [toaddrs]
           self.toaddrs = toaddrs
           self.subject = subject
           self.setFormatter(logging.Formatter("%(asctime)s %(levelname)-5s %(message)s"))

       def flush(self):
           if len(self.buffer) > 0:
               try:
                   smtp = smtplib.SMTP(self.mailhost, self.mailport)
                   smtp.starttls()
                   smtp.login(self.username, self.password)
                   msg = "From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n" % (self.fromaddr, ','.join(self.toaddrs), self.subject)
                   for record in self.buffer:
                       s = self.format(record)
                       msg = msg + s + "\r\n"
                   smtp.sendmail(self.fromaddr, self.toaddrs, msg)
                   smtp.quit()
               except Exception:
                   if logging.raiseExceptions:
                       raise
               self.buffer = []

   if __name__ == '__main__':
       import argparse

       ap = argparse.ArgumentParser()
       aa = ap.add_argument
       aa('host', metavar='HOST', help='SMTP server')
       aa('--port', '-p', type=int, default=587, help='SMTP port')
       aa('user', metavar='USER', help='SMTP username')
       aa('password', metavar='PASSWORD', help='SMTP password')
       aa('to', metavar='TO', help='Addressee for emails')
       aa('sender', metavar='SENDER', help='Sender email address')
       aa('--subject', '-s',
          default='Test Logging email from Python logging module (buffering)',
          help='Subject of email')
       options = ap.parse_args()
       logger = logging.getLogger()
       logger.setLevel(logging.DEBUG)
       h = BufferingSMTPHandler(options.host, options.port, options.user,
                                options.password, options.sender,
                                options.to, options.subject, 10)
       logger.addHandler(h)
       for i in range(102):
           logger.info("Info index = %d", i)
       h.flush()
       h.close()

Si ejecuta este script y su servidor SMTP está correctamente
configurado, debería ver que envía once correos electrónicos al
destinatario que usted especifique. Los primeros diez correos
electrónicos tendrán cada uno diez mensajes de log, y el undécimo
tendrá dos mensajes. Eso hace 102 mensajes como se especifica en el
script.

## Formateo de horas usando UTC (GMT) a través de la configuración

A veces desea formatear las horas usando UTC, lo que se puede hacer
usando una clase como "UTCFormatter", como se muestra a continuación:

   import logging
   import time

   class UTCFormatter(logging.Formatter):
       converter = time.gmtime

y luego puede usar el "UTCFormatter" en su código en lugar de
"Formatter". Si desea hacer eso a través de la configuración, puede
usar la API "dictConfig()" con un enfoque ilustrado por el siguiente
ejemplo completo:

   import logging
   import logging.config
   import time

   class UTCFormatter(logging.Formatter):
       converter = time.gmtime

   LOGGING = {
       'version': 1,
       'disable_existing_loggers': False,
       'formatters': {
           'utc': {
               '()': UTCFormatter,
               'format': '%(asctime)s %(message)s',
           },
           'local': {
               'format': '%(asctime)s %(message)s',
           }
       },
       'handlers': {
           'console1': {
               'class': 'logging.StreamHandler',
               'formatter': 'utc',
           },
           'console2': {
               'class': 'logging.StreamHandler',
               'formatter': 'local',
           },
       },
       'root': {
           'handlers': ['console1', 'console2'],
      }
   }

   if __name__ == '__main__':
       logging.config.dictConfig(LOGGING)
       logging.warning('The local time is %s', time.asctime())

Cuando se ejecuta este script, debería imprimir algo como:

   2015-10-17 12:53:29,501 The local time is Sat Oct 17 13:53:29 2015
   2015-10-17 13:53:29,501 The local time is Sat Oct 17 13:53:29 2015

mostrando cómo se formatea la hora como hora local y UTC, una para
cada gestor.

## Usar un administrador de contexto para logging selectivo

Hay ocasiones en las que sería útil cambiar temporalmente la
configuración de logging y revertir esto después de hacer algo. Para
ello, un administrador de contexto es la forma más obvia de guardar y
restaurar el contexto de logging. Aquí hay un ejemplo simple de un
administrador de contexto de este tipo, que le permite cambiar
opcionalmente el nivel de logging y agregar un gestor de logging
exclusivamente en el alcance del administrador de contexto:

   import logging
   import sys

   class LoggingContext:
       def __init__(self, logger, level=None, handler=None, close=True):
           self.logger = logger
           self.level = level
           self.handler = handler
           self.close = close

       def __enter__(self):
           if self.level is not None:
               self.old_level = self.logger.level
               self.logger.setLevel(self.level)
           if self.handler:
               self.logger.addHandler(self.handler)

       def __exit__(self, et, ev, tb):
           if self.level is not None:
               self.logger.setLevel(self.old_level)
           if self.handler:
               self.logger.removeHandler(self.handler)
           if self.handler and self.close:
               self.handler.close()
           # implicit return of None => don't swallow exceptions

Si especifica un valor de nivel, el nivel del registrador se establece
en ese valor en el alcance del bloque *with* cubierto por el
administrador de contexto. Si especifica un gestor, se agrega al
registrador al entrar al bloque y se elimina al salir del bloque.
También puede pedirle al administrador que cierre el gestor por usted
al salir del bloque si ya no lo necesita.

Para ilustrar cómo funciona, podemos agregar el siguiente bloque de
código al anterior:

   if __name__ == '__main__':
       logger = logging.getLogger('foo')
       logger.addHandler(logging.StreamHandler())
       logger.setLevel(logging.INFO)
       logger.info('1. This should appear just once on stderr.')
       logger.debug('2. This should not appear.')
       with LoggingContext(logger, level=logging.DEBUG):
           logger.debug('3. This should appear once on stderr.')
       logger.debug('4. This should not appear.')
       h = logging.StreamHandler(sys.stdout)
       with LoggingContext(logger, level=logging.DEBUG, handler=h, close=True):
           logger.debug('5. This should appear twice - once on stderr and once on stdout.')
       logger.info('6. This should appear just once on stderr.')
       logger.debug('7. This should not appear.')

Inicialmente configuramos el nivel del registrador en "INFO", por lo
que aparece el mensaje #1 y el mensaje #2 no. Luego cambiamos el nivel
a "DEBUG" temporalmente en el siguiente bloque "with", y aparece el
mensaje #3. Una vez que se sale del bloque, el nivel del registrador
se restaura a "INFO" y, por lo tanto, el mensaje #4 no aparece. En el
siguiente bloque "with", configuramos el nivel en "DEBUG" nuevamente,
pero también agregamos un gestor que escribe en "sys.stdout". Por lo
tanto, el mensaje #5 aparece dos veces en la consola (una vez a través
de "stderr" y una vez a través de "stdout"). Después de la
finalización de la declaración "with", se vuelve al estado anterior,
por lo que aparece el mensaje #6 (como el mensaje #1) mientras que el
mensaje #7 no (como el mensaje #2).

Si ejecutamos el script resultante, el resultado es el siguiente:

   $ python logctx.py
   1. This should appear just once on stderr.
   3. This should appear once on stderr.
   5. This should appear twice - once on stderr and once on stdout.
   5. This should appear twice - once on stderr and once on stdout.
   6. This should appear just once on stderr.

Si lo ejecutamos de nuevo, pero dirigimos "stderr" a "/dev/null",
vemos lo siguiente, que es el único mensaje escrito en "stdout":

   $ python logctx.py 2>/dev/null
   5. This should appear twice - once on stderr and once on stdout.

Una vez más, pero canalizando "stdout" a "/dev/null", obtenemos:

   $ python logctx.py >/dev/null
   1. This should appear just once on stderr.
   3. This should appear once on stderr.
   5. This should appear twice - once on stderr and once on stdout.
   6. This should appear just once on stderr.

En este caso, el mensaje #5 impreso en "stdout" no aparece, como se
esperaba.

Por supuesto, el enfoque descrito aquí puede generalizarse, por
ejemplo, para adjuntar filtros de logging temporalmente. Tenga en
cuenta que el código anterior funciona tanto en Python 2 como en
Python 3.

## Una plantilla de inicio de aplicación CLI

Aquí hay un ejemplo que muestra cómo puede:

* Utilizar un nivel de logging basado en argumentos de la línea de
  comandos

* Enviar a varios subcomandos en archivos separados, todos registrando
  en el mismo nivel de forma coherente

* Utilizar una configuración mínima y sencilla

Supongamos que tenemos una aplicación de línea de comandos cuyo
trabajo es detener, iniciar o reiniciar algunos servicios. Esto podría
organizarse con fines ilustrativos como un archivo "app.py" que es el
script principal de la aplicación, con comandos individuales
implementados en "start.py", "stop.py" y "restart.py". Supongamos
además que queremos controlar la verbosidad de la aplicación a través
de un argumento de línea de comandos, por defecto en "logging.INFO".
Aquí hay una forma en que se podría escribir "app.py":

   import argparse
   import importlib
   import logging
   import os
   import sys

   def main(args=None):
       scriptname = os.path.basename(__file__)
       parser = argparse.ArgumentParser(scriptname)
       levels = ('DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL')
       parser.add_argument('--log-level', default='INFO', choices=levels)
       subparsers = parser.add_subparsers(dest='command',
                                          help='Available commands:')
       start_cmd = subparsers.add_parser('start', help='Start a service')
       start_cmd.add_argument('name', metavar='NAME',
                              help='Name of service to start')
       stop_cmd = subparsers.add_parser('stop',
                                        help='Stop one or more services')
       stop_cmd.add_argument('names', metavar='NAME', nargs='+',
                             help='Name of service to stop')
       restart_cmd = subparsers.add_parser('restart',
                                           help='Restart one or more services')
       restart_cmd.add_argument('names', metavar='NAME', nargs='+',
                                help='Name of service to restart')
       options = parser.parse_args()
       # the code to dispatch commands could all be in this file. For the purposes
       # of illustration only, we implement each command in a separate module.
       try:
           mod = importlib.import_module(options.command)
           cmd = getattr(mod, 'command')
       except (ImportError, AttributeError):
           print('Unable to find the code for command \'%s\'' % options.command)
           return 1
       # Could get fancy here and load configuration from file or dictionary
       logging.basicConfig(level=options.log_level,
                           format='%(levelname)s %(name)s %(message)s')
       cmd(options)

   if __name__ == '__main__':
       sys.exit(main())

Y los comandos "start", "stop" y "reiniciar" se pueden implementar en
módulos separados, como para iniciar:

   # start.py
   import logging

   logger = logging.getLogger(__name__)

   def command(options):
       logger.debug('About to start %s', options.name)
       # actually do the command processing here ...
       logger.info('Started the \'%s\' service.', options.name)

y así para detener:

   # stop.py
   import logging

   logger = logging.getLogger(__name__)

   def command(options):
       n = len(options.names)
       if n == 1:
           plural = ''
           services = '\'%s\'' % options.names[0]
       else:
           plural = 's'
           services = ', '.join('\'%s\'' % name for name in options.names)
           i = services.rfind(', ')
           services = services[:i] + ' and ' + services[i + 2:]
       logger.debug('About to stop %s', services)
       # actually do the command processing here ...
       logger.info('Stopped the %s service%s.', services, plural)

y de manera similar para reiniciar:

   # restart.py
   import logging

   logger = logging.getLogger(__name__)

   def command(options):
       n = len(options.names)
       if n == 1:
           plural = ''
           services = '\'%s\'' % options.names[0]
       else:
           plural = 's'
           services = ', '.join('\'%s\'' % name for name in options.names)
           i = services.rfind(', ')
           services = services[:i] + ' and ' + services[i + 2:]
       logger.debug('About to restart %s', services)
       # actually do the command processing here ...
       logger.info('Restarted the %s service%s.', services, plural)

Si ejecutamos esta aplicación con el nivel de log predeterminado,
obtenemos un resultado como este:

   $ python app.py start foo
   INFO start Started the 'foo' service.

   $ python app.py stop foo bar
   INFO stop Stopped the 'foo' and 'bar' services.

   $ python app.py restart foo bar baz
   INFO restart Restarted the 'foo', 'bar' and 'baz' services.

La primera palabra es el nivel de logging y la segunda palabra es el
nombre del módulo o paquete del lugar donde se registró el evento.

Si cambiamos el nivel de logging, podemos cambiar la información
enviada al log. Por ejemplo, si queremos más información:

   $ python app.py --log-level DEBUG start foo
   DEBUG start About to start foo
   INFO start Started the 'foo' service.

   $ python app.py --log-level DEBUG stop foo bar
   DEBUG stop About to stop 'foo' and 'bar'
   INFO stop Stopped the 'foo' and 'bar' services.

   $ python app.py --log-level DEBUG restart foo bar baz
   DEBUG restart About to restart 'foo', 'bar' and 'baz'
   INFO restart Restarted the 'foo', 'bar' and 'baz' services.

Y si queremos menos:

   $ python app.py --log-level WARNING start foo
   $ python app.py --log-level WARNING stop foo bar
   $ python app.py --log-level WARNING restart foo bar baz

En este caso, los comandos no imprimen nada en la consola, ya que no
registran nada en el nivel de "WARNING" o superior.

## Una GUI de Qt para logging

A question that comes up from time to time is about how to log to a
GUI application. The Qt framework is a popular cross-platform UI
framework with Python bindings using PySide2 or PyQt5 libraries.

El siguiente ejemplo muestra cómo iniciar sesión en una GUI de Qt.
Esto introduce una clase simple "QtHandler" que toma un invocable, que
debería ser un slot en el hilo principal que realiza actualizaciones
de la GUI. También se crea un hilo de trabajo para mostrar cómo puede
iniciar sesión en la GUI tanto desde la propia interfaz de usuario (a
través de un botón para el logging manual) como desde un hilo de
trabajo que trabaja en segundo plano (aquí, simplemente registrando
mensajes en niveles aleatorios con aleatorio breves retrasos
intermedios).

El hilo *worker* se implementa usando la clase "QThread" de Qt en
lugar del módulo "threading", ya que hay circunstancias en las que uno
tiene que usar "QThread", que ofrece una mejor integración con otros
componentes "Qt".

The code should work with recent releases of any of "PySide6",
"PyQt6", "PySide2" or "PyQt5". You should be able to adapt the
approach to earlier versions of Qt. Please refer to the comments in
the code snippet for more detailed information.

   import logging
   import random
   import sys
   import time

   # Deal with minor differences between different Qt packages
   try:
       from PySide6 import QtCore, QtGui, QtWidgets
       Signal = QtCore.Signal
       Slot = QtCore.Slot
   except ImportError:
       try:
           from PyQt6 import QtCore, QtGui, QtWidgets
           Signal = QtCore.pyqtSignal
           Slot = QtCore.pyqtSlot
       except ImportError:
           try:
               from PySide2 import QtCore, QtGui, QtWidgets
               Signal = QtCore.Signal
               Slot = QtCore.Slot
           except ImportError:
               from PyQt5 import QtCore, QtGui, QtWidgets
               Signal = QtCore.pyqtSignal
               Slot = QtCore.pyqtSlot

   logger = logging.getLogger(__name__)

   #
   # Signals need to be contained in a QObject or subclass in order to be correctly
   # initialized.
   #
   class Signaller(QtCore.QObject):
       signal = Signal(str, logging.LogRecord)

   #
   # Output to a Qt GUI is only supposed to happen on the main thread. So, this
   # handler is designed to take a slot function which is set up to run in the main
   # thread. In this example, the function takes a string argument which is a
   # formatted log message, and the log record which generated it. The formatted
   # string is just a convenience - you could format a string for output any way
   # you like in the slot function itself.
   #
   # You specify the slot function to do whatever GUI updates you want. The handler
   # doesn't know or care about specific UI elements.
   #
   class QtHandler(logging.Handler):
       def __init__(self, slotfunc, *args, **kwargs):
           super().__init__(*args, **kwargs)
           self.signaller = Signaller()
           self.signaller.signal.connect(slotfunc)

       def emit(self, record):
           s = self.format(record)
           self.signaller.signal.emit(s, record)

   #
   # This example uses QThreads, which means that the threads at the Python level
   # are named something like "Dummy-1". The function below gets the Qt name of the
   # current thread.
   #
   def ctname():
       return QtCore.QThread.currentThread().objectName()

   #
   # Used to generate random levels for logging.
   #
   LEVELS = (logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR,
             logging.CRITICAL)

   #
   # This worker class represents work that is done in a thread separate to the
   # main thread. The way the thread is kicked off to do work is via a button press
   # that connects to a slot in the worker.
   #
   # Because the default threadName value in the LogRecord isn't much use, we add
   # a qThreadName which contains the QThread name as computed above, and pass that
   # value in an "extra" dictionary which is used to update the LogRecord with the
   # QThread name.
   #
   # This example worker just outputs messages sequentially, interspersed with
   # random delays of the order of a few seconds.
   #
   class Worker(QtCore.QObject):
       @Slot()
       def start(self):
           extra = {'qThreadName': ctname() }
           logger.debug('Started work', extra=extra)
           i = 1
           # Let the thread run until interrupted. This allows reasonably clean
           # thread termination.
           while not QtCore.QThread.currentThread().isInterruptionRequested():
               delay = 0.5 + random.random() * 2
               time.sleep(delay)
               try:
                   if random.random() < 0.1:
                       raise ValueError('Exception raised: %d' % i)
                   else:
                       level = random.choice(LEVELS)
                       logger.log(level, 'Message after delay of %3.1f: %d', delay, i, extra=extra)
               except ValueError as e:
                   logger.exception('Failed: %s', e, extra=extra)
               i += 1

   #
   # Implement a simple UI for this cookbook example. This contains:
   #
   # * A read-only text edit window which holds formatted log messages
   # * A button to start work and log stuff in a separate thread
   # * A button to log something from the main thread
   # * A button to clear the log window
   #
   class Window(QtWidgets.QWidget):

       COLORS = {
           logging.DEBUG: 'black',
           logging.INFO: 'blue',
           logging.WARNING: 'orange',
           logging.ERROR: 'red',
           logging.CRITICAL: 'purple',
       }

       def __init__(self, app):
           super().__init__()
           self.app = app
           self.textedit = te = QtWidgets.QPlainTextEdit(self)
           # Set whatever the default monospace font is for the platform
           f = QtGui.QFont('nosuchfont')
           if hasattr(f, 'Monospace'):
               f.setStyleHint(f.Monospace)
           else:
               f.setStyleHint(f.StyleHint.Monospace)  # for Qt6
           te.setFont(f)
           te.setReadOnly(True)
           PB = QtWidgets.QPushButton
           self.work_button = PB('Start background work', self)
           self.log_button = PB('Log a message at a random level', self)
           self.clear_button = PB('Clear log window', self)
           self.handler = h = QtHandler(self.update_status)
           # Remember to use qThreadName rather than threadName in the format string.
           fs = '%(asctime)s %(qThreadName)-12s %(levelname)-8s %(message)s'
           formatter = logging.Formatter(fs)
           h.setFormatter(formatter)
           logger.addHandler(h)
           # Set up to terminate the QThread when we exit
           app.aboutToQuit.connect(self.force_quit)

           # Lay out all the widgets
           layout = QtWidgets.QVBoxLayout(self)
           layout.addWidget(te)
           layout.addWidget(self.work_button)
           layout.addWidget(self.log_button)
           layout.addWidget(self.clear_button)
           self.setFixedSize(900, 400)

           # Connect the non-worker slots and signals
           self.log_button.clicked.connect(self.manual_update)
           self.clear_button.clicked.connect(self.clear_display)

           # Start a new worker thread and connect the slots for the worker
           self.start_thread()
           self.work_button.clicked.connect(self.worker.start)
           # Once started, the button should be disabled
           self.work_button.clicked.connect(lambda : self.work_button.setEnabled(False))

       def start_thread(self):
           self.worker = Worker()
           self.worker_thread = QtCore.QThread()
           self.worker.setObjectName('Worker')
           self.worker_thread.setObjectName('WorkerThread')  # for qThreadName
           self.worker.moveToThread(self.worker_thread)
           # This will start an event loop in the worker thread
           self.worker_thread.start()

       def kill_thread(self):
           # Just tell the worker to stop, then tell it to quit and wait for that
           # to happen
           self.worker_thread.requestInterruption()
           if self.worker_thread.isRunning():
               self.worker_thread.quit()
               self.worker_thread.wait()
           else:
               print('worker has already exited.')

       def force_quit(self):
           # For use when the window is closed
           if self.worker_thread.isRunning():
               self.kill_thread()

       # The functions below update the UI and run in the main thread because
       # that's where the slots are set up

       @Slot(str, logging.LogRecord)
       def update_status(self, status, record):
           color = self.COLORS.get(record.levelno, 'black')
           s = '<pre><font color="%s">%s</font></pre>' % (color, status)
           self.textedit.appendHtml(s)

       @Slot()
       def manual_update(self):
           # This function uses the formatted message passed in, but also uses
           # information from the record to format the message in an appropriate
           # color according to its severity (level).
           level = random.choice(LEVELS)
           extra = {'qThreadName': ctname() }
           logger.log(level, 'Manually logged!', extra=extra)

       @Slot()
       def clear_display(self):
           self.textedit.clear()

   def main():
       QtCore.QThread.currentThread().setObjectName('MainThread')
       logging.getLogger().setLevel(logging.DEBUG)
       app = QtWidgets.QApplication(sys.argv)
       example = Window(app)
       example.show()
       if hasattr(app, 'exec'):
           rc = app.exec()
       else:
           rc = app.exec_()
       sys.exit(rc)

   if __name__=='__main__':
       main()

## Logging en syslog con soporte RFC5424

Although **RFC 5424** dates from 2009, most syslog servers are
configured by default to use the older **RFC 3164**, which hails from
2001. When "logging" was added to Python in 2003, it supported the
earlier (and only existing) protocol at the time. Since RFC 5424 came
out, as there has not been widespread deployment of it in syslog
servers, the "SysLogHandler" functionality has not been updated.

El RFC 5424 contiene algunas características útiles como el soporte
para datos estructurados, y si necesitas poder registrar en un
servidor syslog con soporte para ello, puedes hacerlo con una subclase
*handler* que se parezca a esto:

   import datetime as dt
   import logging.handlers
   import re
   import socket
   import time

   class SysLogHandler5424(logging.handlers.SysLogHandler):

       tz_offset = re.compile(r'([+-]\d{2})(\d{2})$')
       escaped = re.compile(r'([\]"\\])')

       def __init__(self, *args, **kwargs):
           self.msgid = kwargs.pop('msgid', None)
           self.appname = kwargs.pop('appname', None)
           super().__init__(*args, **kwargs)

       def format(self, record):
           version = 1
           asctime = dt.datetime.fromtimestamp(record.created).isoformat()
           m = self.tz_offset.match(time.strftime('%z'))
           has_offset = False
           if m and time.timezone:
               hrs, mins = m.groups()
               if int(hrs) or int(mins):
                   has_offset = True
           if not has_offset:
               asctime += 'Z'
           else:
               asctime += f'{hrs}:{mins}'
           try:
               hostname = socket.gethostname()
           except Exception:
               hostname = '-'
           appname = self.appname or '-'
           procid = record.process
           msgid = '-'
           msg = super().format(record)
           sdata = '-'
           if hasattr(record, 'structured_data'):
               sd = record.structured_data
               # This should be a dict where the keys are SD-ID and the value is a
               # dict mapping PARAM-NAME to PARAM-VALUE (refer to the RFC for what these
               # mean)
               # There's no error checking here - it's purely for illustration, and you
               # can adapt this code for use in production environments
               parts = []

               def replacer(m):
                   g = m.groups()
                   return '\\' + g[0]

               for sdid, dv in sd.items():
                   part = f'[{sdid}'
                   for k, v in dv.items():
                       s = str(v)
                       s = self.escaped.sub(replacer, s)
                       part += f' {k}="{s}"'
                   part += ']'
                   parts.append(part)
               sdata = ''.join(parts)
           return f'{version} {asctime} {hostname} {appname} {procid} {msgid} {sdata} {msg}'

Tendrá que estar familiarizado con el RFC 5424 para entender
completamente el código anterior, y puede ser que tenga necesidades
ligeramente diferentes (por ejemplo, para la forma de pasar los datos
estructurales al log). No obstante, lo anterior debería poder
adaptarse a sus necesidades específicas. Con el gestor anterior, usted
pasaría datos estructurados usando algo como esto:

   sd = {
       'foo@12345': {'bar': 'baz', 'baz': 'bozz', 'fizz': r'buzz'},
       'foo@54321': {'rab': 'baz', 'zab': 'bozz', 'zzif': r'buzz'}
   }
   extra = {'structured_data': sd}
   i = 1
   logger.debug('Message %d', i, extra=extra)

## Cómo tratar un logger como una salida stream

A veces, necesitas interactuar con una API de terceros que espera un
objeto tipo archivo para escribir, pero quieres dirigir la salida de
la API a un logger. Puedes hacer esto usando una clase que envuelva un
logger con una API tipo archivo. Aquí hay un pequeño script que
ilustra tal clase:

   import logging

   class LoggerWriter:
       def __init__(self, logger, level):
           self.logger = logger
           self.level = level

       def write(self, message):
           if message != '\n':  # avoid printing bare newlines, if you like
               self.logger.log(self.level, message)

       def flush(self):
           # doesn't actually do anything, but might be expected of a file-like
           # object - so optional depending on your situation
           pass

       def close(self):
           # doesn't actually do anything, but might be expected of a file-like
           # object - so optional depending on your situation. You might want
           # to set a flag so that later calls to write raise an exception
           pass

   def main():
       logging.basicConfig(level=logging.DEBUG)
       logger = logging.getLogger('demo')
       info_fp = LoggerWriter(logger, logging.INFO)
       debug_fp = LoggerWriter(logger, logging.DEBUG)
       print('An INFO message', file=info_fp)
       print('A DEBUG message', file=debug_fp)

   if __name__ == "__main__":
       main()

Cuando se ejecuta este script, se imprime

   INFO:demo:An INFO message
   DEBUG:demo:A DEBUG message

También puedes usar "LoggerWriter" para redirigir "sys.stdout" y
"sys.stderr" haciendo algo así:

   import sys

   sys.stdout = LoggerWriter(logger, logging.INFO)
   sys.stderr = LoggerWriter(logger, logging.WARNING)

Debería hacer esto *después* de configurar logging para sus
necesidades. En el ejemplo anterior, la llamada "basicConfig()" hace
esto (utilizando el valor de "sys.stderr" *antes* de que sea
sobrescrito por una instancia de "LoggerWriter"). Entonces, obtendrías
este tipo de resultado:

   >>> print('Foo')
   INFO:demo:Foo
   >>> print('Bar', file=sys.stderr)
   WARNING:demo:Bar
   >>>

Por supuesto, los ejemplos anteriores muestran la salida según el
formato utilizado por "basicConfig()", pero puede utilizar un
formateador diferente cuando configure logging.

Ten en cuenta que con el esquema anterior, estás un poco a merced del
buffering y de la secuencia de llamadas de escritura que estás
interceptando. Por ejemplo, con la definición de "LoggerWriter"
anterior, si tienes el fragmento

   sys.stderr = LoggerWriter(logger, logging.WARNING)
   1 / 0

entonces la ejecución del script da como resultado

   WARNING:demo:Traceback (most recent call last):

   WARNING:demo:  File "/home/runner/cookbook-loggerwriter/test.py", line 53, in <module>

   WARNING:demo:
   WARNING:demo:main()
   WARNING:demo:  File "/home/runner/cookbook-loggerwriter/test.py", line 49, in main

   WARNING:demo:
   WARNING:demo:1 / 0
   WARNING:demo:ZeroDivisionError
   WARNING:demo::
   WARNING:demo:division by zero

As you can see, this output isn't ideal. That's because the underlying
code which writes to "sys.stderr" makes multiple writes, each of which
results in a separate logged line (for example, the last three lines
above). To get around this problem, you need to buffer things and only
output log lines when newlines are seen. Let's use a slightly better
implementation of "LoggerWriter":

   class BufferingLoggerWriter(LoggerWriter):
       def __init__(self, logger, level):
           super().__init__(logger, level)
           self.buffer = ''

       def write(self, message):
           if '\n' not in message:
               self.buffer += message
           else:
               parts = message.split('\n')
               if self.buffer:
                   s = self.buffer + parts.pop(0)
                   self.logger.log(self.level, s)
               self.buffer = parts.pop()
               for part in parts:
                   self.logger.log(self.level, part)

Esto sólo almacena cosas hasta que se ve una nueva línea, y luego
registra las líneas completas. Con este enfoque, se obtiene una mejor
salida:

   WARNING:demo:Traceback (most recent call last):
   WARNING:demo:  File "/home/runner/cookbook-loggerwriter/main.py", line 55, in <module>
   WARNING:demo:    main()
   WARNING:demo:  File "/home/runner/cookbook-loggerwriter/main.py", line 52, in main
   WARNING:demo:    1/0
   WARNING:demo:ZeroDivisionError: division by zero

## How to uniformly handle newlines in logging output

Usually, messages that are logged (say to console or file) consist of
a single line of text. However, sometimes there is a need to handle
messages with multiple lines - whether because a logging format string
contains newlines, or logged data contains newlines. If you want to
handle such messages uniformly, so that each line in the logged
message appears uniformly formatted as if it was logged separately,
you can do this using a handler mixin, as in the following snippet:

   # Assume this is in a module mymixins.py
   import copy

   class MultilineMixin:
       def emit(self, record):
           s = record.getMessage()
           if '\n' not in s:
               super().emit(record)
           else:
               lines = s.splitlines()
               rec = copy.copy(record)
               rec.args = None
               for line in lines:
                   rec.msg = line
                   super().emit(rec)

You can use the mixin as in the following script:

   import logging

   from mymixins import MultilineMixin

   logger = logging.getLogger(__name__)

   class StreamHandler(MultilineMixin, logging.StreamHandler):
       pass

   if __name__ == '__main__':
       logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)-9s %(message)s',
                           handlers = [StreamHandler()])
       logger.debug('Single line')
       logger.debug('Multiple lines:\nfool me once ...')
       logger.debug('Another single line')
       logger.debug('Multiple lines:\n%s', 'fool me ...\ncan\'t get fooled again')

The script, when run, prints something like:

   2025-07-02 13:54:47,234 DEBUG     Single line
   2025-07-02 13:54:47,234 DEBUG     Multiple lines:
   2025-07-02 13:54:47,234 DEBUG     fool me once ...
   2025-07-02 13:54:47,234 DEBUG     Another single line
   2025-07-02 13:54:47,234 DEBUG     Multiple lines:
   2025-07-02 13:54:47,234 DEBUG     fool me ...
   2025-07-02 13:54:47,234 DEBUG     can't get fooled again

If, on the other hand, you are concerned about log injection, you can
use a formatter which escapes newlines, as per the following example:

   import logging

   logger = logging.getLogger(__name__)

   class EscapingFormatter(logging.Formatter):
       def format(self, record):
           s = super().format(record)
           return s.replace('\n', r'\n')

   if __name__ == '__main__':
       h = logging.StreamHandler()
       h.setFormatter(EscapingFormatter('%(asctime)s %(levelname)-9s %(message)s'))
       logging.basicConfig(level=logging.DEBUG, handlers = [h])
       logger.debug('Single line')
       logger.debug('Multiple lines:\nfool me once ...')
       logger.debug('Another single line')
       logger.debug('Multiple lines:\n%s', 'fool me ...\ncan\'t get fooled again')

You can, of course, use whatever escaping scheme makes the most sense
for you. The script, when run, should produce output like this:

   2025-07-09 06:47:33,783 DEBUG     Single line
   2025-07-09 06:47:33,783 DEBUG     Multiple lines:\nfool me once ...
   2025-07-09 06:47:33,783 DEBUG     Another single line
   2025-07-09 06:47:33,783 DEBUG     Multiple lines:\nfool me ...\ncan't get fooled again

Escaping behaviour can't be the stdlib default , as it would break
backwards compatibility.

## Patrones para evitar

Aunque las secciones anteriores han descrito formas de hacer las cosas
que podría necesitar hacer o con las que tratar, vale la pena
mencionar algunos patrones de uso que son *inútiles* y que, por lo
tanto, deben evitarse en la mayoría de los casos. Las siguientes
secciones no están en ningún orden en particular.

### Abrir el mismo archivo de registro varias veces

En Windows, por lo general, no podrá abrir el mismo archivo varias
veces, ya que esto lanzará un error de "otro proceso está usando el
archivo". Sin embargo, en las plataformas POSIX no obtendrá ningún
error si abre el mismo archivo varias veces. Esto podría hacerse
accidentalmente, por ejemplo:

* Agregar un controlador de archivos más de una vez que hace
  referencia al mismo archivo (por ejemplo, mediante un error de
  copiar/pegar/olvidar-cambiar).

* Abrir dos archivos que se ven diferentes, ya que tienen diferentes
  nombres, pero son iguales porque uno es un enlace simbólico al otro.

* Bifurcar un proceso, después del cual tanto el padre como el hijo
  tienen una referencia al mismo archivo. Esto podría ser mediante el
  uso del módulo "multiprocessing", por ejemplo.

Abrir un archivo varias veces puede *parecer* que funciona la mayor
parte del tiempo, pero puede dar lugar a una serie de problemas en la
práctica:

* La salida del registro se puede distorsionar porque varios
  subprocesos o procesos intentan escribir en el mismo archivo. Aunque
  el registro se protege de el uso simultáneo de la misma instancia de
  controlador por varios subprocesos, no existe tal protección si dos
  subprocesos diferentes intentan escrituras simultáneas utilizando
  dos instancias de controlador diferentes que apunten al mismo
  archivo.

* Un intento de eliminar un archivo (por ejemplo, durante la rotación
  de archivos) falla silenciosamente, porque hay otra referencia que
  apunta a él. Esto puede generar confusión y una pérdida de tiempo de
  depuración: las entradas del registro terminan en lugares
  inesperados o se pierden por completo. O un archivo que debía ser
  movido permanece en su lugar, y crece en tamaño inesperadamente a
  pesar de que la rotación basada en el tamaño está supuestamente en
  su lugar.

Utilice las técnicas descritas en Logging a un sólo archivo desde
múltiples procesos para evitar estos problemas.

### Usar registradores como atributos en una clase o pasarlos como parámetros

Si bien puede haber casos inusuales en los que deba hacer esto, en
general no tiene sentido porque los registradores son singletons. El
código siempre puede acceder a una instancia de registrador dada por
su nombre usando "logging.getLogger(name)", por lo que pasar
instancias y mantenerlas como atributos de instancia no tiene sentido.
Tenga en cuenta que en otros lenguajes como Java y C#, los
registradores suelen ser atributos de clase estáticos. Sin embargo,
este patrón no tiene sentido en Python, donde el módulo (y no la
clase) es la unidad de descomposición del software.

### Adding handlers other than "NullHandler" to a logger in a library

La configuración del registro agregando controladores, formateadores y
filtros es responsabilidad del desarrollador de la aplicación, no del
desarrollador de la biblioteca. Si mantiene una biblioteca, asegúrese
de no agregar controladores a ninguno de sus registradores que no sean
una instancia "NullHandler".

### Crear muchos registradores (*loggers*)

Los registradores son singletons que nunca se liberan durante la
ejecución de un script, por lo que la creación de muchos registradores
consumirá memoria que luego no se puede liberar. En lugar de crear un
registrador por ej. archivo procesado o conexión de red realizada, use
los mecanismos existentes para pasar información contextual a sus
registros y restringir los registradores creados a aquellos que
describen áreas dentro de su aplicación (generalmente módulos, pero
ocasionalmente un poco más detallado que eso).

## Otros recursos

Ver también:

  Módulo "logging"
     Referencia de API para el módulo logging.

  Módulo "logging.config"
     API de configuración para el módulo logging.

  Módulo "logging.handlers"
     Gestores útiles incluidos con el módulo logging.

  Tutorial Básico

  Tutorial Avanzado
