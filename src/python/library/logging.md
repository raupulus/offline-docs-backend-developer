---
title: '"logging" --- Logging facility for Python'
source_url: https://docs.python.org/es/3
source_path: library/logging.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 3140
---

# "logging" --- Logging facility for Python

**Source code:** Lib/logging/__init__.py

##### Important

Esta página contiene la información de referencia de la API. Para
información sobre tutorial y discusión de temas más avanzados, ver

* Tutorial básico

* Tutorial avanzado

* Libro de recetas de Logging

======================================================================

Este módulo define funciones y clases que implementan un sistema
flexible de logging de eventos para aplicaciones y bibliotecas.

El beneficio clave de tener la API de logging proporcionada por un
módulo de la biblioteca estándar es que todos los módulos de Python
pueden participar en el logging, por lo que el registro de su
aplicación puede incluir sus propios mensajes integrados con mensajes
de módulos de terceros.

Here's a simple example of idiomatic usage:

   # myapp.py
   import logging
   import mylib
   logger = logging.getLogger(__name__)

   def main():
       logging.basicConfig(filename='myapp.log', level=logging.INFO)
       logger.info('Started')
       mylib.do_something()
       logger.info('Finished')

   if __name__ == '__main__':
       main()

   # mylib.py
   import logging
   logger = logging.getLogger(__name__)

   def do_something():
       logger.info('Doing something')

If you run *myapp.py*, you should see this in *myapp.log*:

   INFO:__main__:Started
   INFO:mylib:Doing something
   INFO:__main__:Finished

The key feature of this idiomatic usage is that the majority of code
is simply creating a module level logger with "getLogger(__name__)",
and using that logger to do any needed logging. This is concise, while
allowing downstream code fine-grained control if needed. Logged
messages to the module-level logger get forwarded to handlers of
loggers in higher-level modules, all the way up to the highest-level
logger known as the root logger; this approach is known as
hierarchical logging.

For logging to be useful, it needs to be configured: setting the
levels and destinations for each logger, potentially changing how
specific modules log, often based on command-line arguments or
application configuration. In most cases, like the one above, only the
root logger needs to be so configured, since all the lower level
loggers at module level eventually forward their messages to its
handlers.  "basicConfig()" provides a quick way to configure the root
logger that handles many use cases.

El módulo proporciona mucha funcionalidad y flexibilidad. Si no está
familiarizado con logging, la mejor manera de familiarizarse con él es
ver los tutoriales (**vea los enlaces arriba a la derecha**).

The basic classes defined by the module, together with their
attributes and methods, are listed in the sections below.

* Los loggers exponen la interfaz que el código de la aplicación usa
  directamente.

* Los gestores envían los registros (creados por los loggers) al
  destino apropiado.

* Los filtros proporcionan una facilidad de ajuste preciso para
  determinar que registros generar.

* Los formateadores especifican el diseño de los registros en el
  resultado final.

## Objetos logger

Los loggers tienen los siguientes atributos y métodos. Tenga en cuenta
que los loggers *NUNCA* deben ser instanciados directamente, siempre a
través de la función de nivel de módulo "logging.getLogger(name)".
Múltiples llamadas a "getLogger()" con el mismo nombre siempre
retornarán una referencia al mismo objeto Logger.

The "name" is potentially a period-separated hierarchical value, like
"foo.bar.baz" (though it could also be just plain "foo", for example).
Loggers that are further down in the hierarchical list are children of
loggers higher up in the list.  For example, given a logger with a
name of "foo", loggers with names of "foo.bar", "foo.bar.baz", and
"foo.bam" are all descendants of "foo".  In addition, all loggers are
descendants of the root logger. The logger name hierarchy is analogous
to the Python package hierarchy, and identical to it if you organise
your loggers on a per-module basis using the recommended construction
"logging.getLogger(__name__)".  That's because in a module, "__name__"
is the module's name in the Python package namespace.

class logging.Logger

   name

      This is the logger's name, and is the value that was passed to
      "getLogger()" to obtain the logger.

      Nota:

        This attribute should be treated as read-only.

   level

      The threshold of this logger, as set by the "setLevel()" method.

      Nota:

        Do not set this attribute directly - always use "setLevel()",
        which has checks for the level passed to it.

   parent

      The parent logger of this logger. It may change based on later
      instantiation of loggers which are higher up in the namespace
      hierarchy.

      Nota:

        This value should be treated as read-only.

   propagate

      Si este atributo se evalúa como verdadero, los eventos
      registrados en este logger se pasarán a los gestores de los
      loggers de nivel superior (ancestro), además de los gestores
      asociados a este logger. Los mensajes se pasan directamente a
      los gestores de los loggers ancestrales; no se consideran ni el
      nivel ni los filtros de los loggers ancestrales en cuestión.

      Si esto se evalúa como falso, los mensajes de registro no se
      pasan a los gestores de los logger ancestrales.

      Explicándolo con un ejemplo: Si el atributo propagado del logger
      llamado "A.B.C" se evalúa a true, cualquier evento registrado en
      "A.B.C" a través de una llamada a un método como
      "logging.getLogger('A.B.C').error(...)" será [sujeto a pasar el
      nivel de ese logger y la configuración del filtro] pasado a su
      vez a cualquier manejador adjunto a los loggers llamados "A.B",
      "A" y al logger raíz, después de ser pasado primero a cualquier
      manejador adjunto a "A.B.C". Si cualquier logger en la cadena
      "A.B.C", "A.B", "A" tiene su atributo "propagate" a false,
      entonces ese es el último logger a cuyos manejadores se les
      ofrece el evento a manejar, y la propagación se detiene en ese
      punto.

      El constructor establece este atributo en "True".

      Nota:

        Si adjunta un gestor a un logger *y* uno o más de sus
        ancestros, puede emitir el mismo registro varias veces. En
        general, no debería necesitar adjuntar un gestor a más de un
        logger; si solo lo adjunta al logger apropiado que está más
        arriba en la jerarquía del logger, verá todos los eventos
        registrados por todos los logger descendientes, siempre que la
        configuración de propagación sea "True". Un escenario común es
        adjuntar gestores solo al logger raíz y dejar que la
        propagación se encargue del resto.

   handlers

      The list of handlers directly attached to this logger instance.

      Nota:

        This attribute should be treated as read-only; it is normally
        changed via the "addHandler()" and "removeHandler()" methods,
        which use locks to ensure thread-safe operation.

   disabled

      This attribute disables handling of any events. It is set to
      "False" in the initializer, and only changed by logging
      configuration code.

      Nota:

        This attribute should be treated as read-only.

   setLevel(level)

      Establece el umbral para este logger en *level*. Los mensajes de
      logging que son menos severos que *level* serán ignorados; los
      mensajes de logging que tengan un nivel de severidad *level* o
      superior serán emitidos por cualquier gestor o gestores que
      atiendan este logger, a menos que el nivel de un gestor haya
      sido configurado en un nivel de severidad más alto que *level*.

      Cuando se crea un logger, el nivel se establece en "NOTSET" (que
      hace que todos los mensajes se procesen cuando el logger es el
      logger raíz, o la delegación al padre cuando el logger no es un
      logger raíz). Tenga en cuenta que el logger raíz se crea con el
      nivel "WARNING".

      El término 'delegación al padre' significa que si un logger
      tiene un nivel de NOTSET, su cadena de logger ancestrales se
      atraviesa hasta que se encuentra un ancestro con un nivel
      diferente a NOTSET o se alcanza la raíz.

      Si se encuentra un antepasado con un nivel distinto de NOTSET,
      entonces el nivel de ese antepasado se trata como el nivel
      efectivo del logger donde comenzó la búsqueda de antepasados, y
      se utiliza para determinar cómo se maneja un evento de registro.

      Si se alcanza la raíz y tiene un nivel de NOTSET, se procesarán
      todos los mensajes. De lo contrario, el nivel de la raíz se
      utilizará como el nivel efectivo.

      Ver Niveles de logging para obtener una lista de niveles.

      Distinto en la versión 3.2: El parámetro *level* ahora acepta
      una representación de cadena del nivel como 'INFO' como
      alternativa a las constantes de enteros como "INFO". Sin
      embargo, tenga en cuenta que los niveles se almacenan
      internamente como e.j. "getEffectiveLevel()" y "isEnabledFor()"
      retornará/esperará que se pasen enteros.

   isEnabledFor(level)

      Indica si este logger procesará un mensaje de gravedad *level*.
      Este método verifica primero el nivel de nivel de módulo
      establecido por "logging.disable(level)" y luego el nivel
      efectivo del logger según lo determinado por
      "getEffectiveLevel()".

   getEffectiveLevel()

      Indica el nivel efectivo para este logger. Si se ha establecido
      un valor distinto de "NOTSET" utilizando "setLevel()", se
      retorna. De lo contrario, la jerarquía se atraviesa hacia la
      raíz hasta que se encuentre un valor que no sea "NOTSET" y se
      retorna ese valor. El valor retornado es un entero, típicamente
      uno de "logging.DEBUG", "logging.INFO" etc.

   getChild(suffix)

      Retorna un logger que es descendiente de este logger, según lo
      determinado por el sufijo. Por lo tanto,
      "logging.getLogger('abc').getChild('def.ghi')" retornaría el
      mismo logger que retornaría "logging.getLogger('abc.def.ghi')".
      Este es un método convenientemente útil cuando el logger
      principal se nombra usando e.j. "__name__" en lugar de una
      cadena literal.

      Added in version 3.2.

   getChildren()

      Retorna un conjunto de loggers que son hijos inmediatos de este
      logger. Así, por ejemplo, "logging.getLogger().getChildren()"
      podría retornar un conjunto que contenga loggers llamados "foo"
      y "bar", pero un logger llamado "foo.bar" no estaría incluido en
      el conjunto. Del mismo modo,
      "logging.getLogger('foo').getChildren()" podría retornar un
      conjunto que incluyera un logger llamado "foo.bar", pero no
      incluiría uno llamado "foo.bar.baz".

      Added in version 3.12.

   debug(msg, *args, **kwargs)

      Registra un mensaje con el nivel "DEBUG" en este logger. El
      *msg* es la cadena de formato del mensaje, y los *args* son los
      argumentos que se fusionan en *msg* utilizando el operador de
      formato de cadena. (Tenga en cuenta que esto significa que puede
      usar palabras clave en la cadena de formato, junto con un solo
      argumento de diccionario). No se realiza ninguna operación de
      formateo mediante % en *msg* cuando no se proporcionan *args*.

      Hay cuatro argumentos de palabras clave *kwargs* que se
      inspeccionan: *exc_info*, *stack_info*, *stacklevel* y *extra*.

      Si *exc_info* no se evalúa como falso, hace que se agregue
      información de excepción al mensaje de registro. Si se
      proporciona una tupla de excepción (en el formato retornado por
      "sys.exc_info()") o se proporciona una instancia de excepción,
      se utiliza; de lo contrario, se llama a "sys.exc_info()" para
      obtener la información de excepción.

      El segundo argumento opcional con la palabra clave *stack_info*,
      que por defecto es "False". Si es verdadero, la información de
      la pila agregara el mensaje de registro, incluida la actual
      llamada del registro. Tenga en cuenta que esta no es la misma
      información de la pila que se muestra al especificar *exc_info*:
      la primera son los cuadros de la pila desde la parte inferior de
      la pila hasta la llamada de registro en el hilo actual, mientras
      que la segunda es la información sobre los cuadros de la pila
      que se han desenrollado, siguiendo una excepción, mientras busca
      gestores de excepción.

      Puede especificar *stack_info* independientemente de *exc_info*,
      por ejemplo solo para mostrar cómo llegaste a cierto punto en tu
      código, incluso cuando no se lanzaron excepciones. Los marcos de
      la pila se imprimen siguiendo una línea de encabezado que dice:

         Stack (most recent call last):

      Esto imita el "Traceback (most recent call last):" que se usa
      cuando se muestran marcos de excepción.

      El tercer argumento opcional con la palabra clave *stacklevel*,
      que por defecto es "1". Si es mayor que 1, se omite el número
      correspondiente de cuadros de pila al calcular el número de
      línea y el nombre de la función establecidos en "LogRecord"
      creado para el evento de registro. Esto se puede utilizar en el
      registro de ayudantes para que el nombre de la función, el
      nombre de archivo y el número de línea registrados no sean la
      información para la función/método auxiliar, sino más bien su
      llamador. El nombre de este parámetro refleja el equivalente en
      el modulo "warnings".

      The fourth keyword argument is *extra* which can be used to pass
      a dictionary which is used to populate the "__dict__" of the
      "LogRecord" created for the logging event with user-defined
      attributes. These custom attributes can then be used as you
      like. For example, they could be incorporated into logged
      messages. For example:

         FORMAT = '%(asctime)s %(clientip)-15s %(user)-8s %(message)s'
         logging.basicConfig(format=FORMAT)
         d = {'clientip': '192.168.0.1', 'user': 'fbloggs'}
         logger = logging.getLogger('tcpserver')
         logger.warning('Protocol problem: %s', 'connection reset', extra=d)

      imprimiría algo como

         2006-02-08 22:20:02,165 192.168.0.1 fbloggs  Protocol problem: connection reset

      Las claves en el diccionario pasado *extra* no deben entrar en
      conflicto con las claves utilizadas por el sistema de registro.
      (Ver la documentación de Atributos LogRecord para obtener más
      información sobre qué claves utiliza el sistema de registro).

      Si elige usar estos atributos en los mensajes registrados, debe
      tener cuidado. En el ejemplo anterior, se ha configurado
      "Formatter" con una cadena de formato que espera *clientip* y
      'usuario' en el diccionario de atributos de "LogRecord". Si
      faltan, el mensaje no se registrará porque se producirá una
      excepción de formato de cadena. En este caso, siempre debe pasar
      el diccionario *extra* con estas teclas.

      Si bien esto puede ser molesto, esta función está diseñada para
      su uso en circunstancias especializadas, como servidores de
      subprocesos múltiples donde el mismo código se ejecuta en muchos
      contextos, y las condiciones interesantes que surgen dependen de
      este contexto (como la dirección IP del cliente remoto y
      autenticado nombre de usuario, en el ejemplo anterior). En tales
      circunstancias, es probable que se especialice "Formatter"s con
      particular "Handler"s.

      If no handler is attached to this logger (or any of its
      ancestors, taking into account the relevant "Logger.propagate"
      attributes), the message will be sent to the handler set on
      "lastResort".

      Distinto en la versión 3.2: Se agregó el parámetro *stack_info*.

      Distinto en la versión 3.5: El parámetro *exc_info* ahora puede
      aceptar instancias de excepción.

      Distinto en la versión 3.8: Se agregó el parámetro *stacklevel*.

   info(msg, *args, **kwargs)

      Registra un mensaje con el nivel "INFO" en este logger. Los
      argumentos se interpretan como "debug()".

   warning(msg, *args, **kwargs)

      Registra un mensaje con el nivel "WARNING" en este logger. Los
      argumentos se interpretan como "debug()".

      Nota:

        Hay un método obsoleto "warn" que es funcionalmente idéntico a
        "warning". Como "warn" está en desuso, no lo use, use
        "warning" en su lugar.

   error(msg, *args, **kwargs)

      Registra un mensaje con nivel "ERROR" en este logger. Los
      argumentos se interpretan como "debug()".

   critical(msg, *args, **kwargs)

      Registra un mensaje con el nivel "CRITICAL" en este logger. Los
      argumentos se interpretan como "debug()".

   log(level, msg, *args, **kwargs)

      Registra un mensaje con nivel entero *level* en este logger. Los
      otros argumentos se interpretan como "debug()".

   exception(msg, *args, **kwargs)

      Registra un mensaje con nivel "ERROR" en este logger. Los
      argumentos se interpretan como "debug()". La información de
      excepción se agrega al mensaje de registro. Este método solo
      debe llamarse desde un gestor de excepciones.

   addFilter(filter)

      Agrega el filtro *filter* especificado a este logger.

   removeFilter(filter)

      Elimina el filtro *filter* especificado de este logger.

   filter(record)

      Aplique los filtros de este logger al registro y retorna "True"
      si se va a procesar el registro. Los filtros se consultan a su
      vez, hasta que uno de ellos retorna un valor falso. Si ninguno
      de ellos retorna un valor falso, el registro será procesado
      (pasado a los gestores). Si se retorna un valor falso, no se
      produce más procesamiento del registro.

   addHandler(hdlr)

      Agrega el gestor especificado *hdlr* a este logger.

   removeHandler(hdlr)

      Elimina el gestor especificado *hdlr* de este logger.

   findCaller(stack_info=False, stacklevel=1)

      Encuentra el nombre de archivo de origen de la invoca y el
      número de línea. Retorna el nombre del archivo, el número de
      línea, el nombre de la función y la información de la pila como
      una tupla de 4 elementos. La información de la pila se retorna
      como "None" a menos que *stack_info* sea "True".

      El parámetro *stacklevel* se pasa del código que llama a
      "debug()" y otras API. Si es mayor que 1, el exceso se utiliza
      para omitir los cuadros de la pila antes de determinar los
      valores que se retornarán. Esto generalmente será útil al llamar
      a las API de registro desde un *helper/wrapper*, de modo que la
      información en el registro de eventos no se refiera al
      *helper/wrapper*, sino al código que lo llama.

   handle(record)

      Gestiona un registro pasándolo a todos los gestores asociados
      con este logger y sus antepasados (hasta que se encuentre un
      valor falso de *propagar*). Este método se utiliza para
      registros no empaquetados recibidos de un socket, así como para
      aquellos creados localmente. El filtrado a nivel de logger se
      aplica usando "filter()".

   makeRecord(name, level, fn, lno, msg, args, exc_info, func=None, extra=None, sinfo=None)

      Este es un método *factory* que se puede sobreescribir en
      subclases para crear instancias especializadas "LogRecord".

   hasHandlers()

      Comprueba si este logger tiene algún gestor configurado. Esto se
      hace buscando gestores en este logger y sus padres en la
      jerarquía del logger. Retorna "True" si se encontró un gestor,
      de lo contrario, "False" . El método deja de buscar en la
      jerarquía cada vez que se encuentra un logger con el atributo
      *propagate* establecido en falso: ese será el último logger que
      verificará la existencia de gestores.

      Added in version 3.2.

   Distinto en la versión 3.7: Los logger ahora se pueden serializar y
   deserializar (*pickled and unpickled*).

## Niveles de logging

Los valores numéricos de los niveles de logging se dan en la siguiente
tabla. Estos son principalmente de interés si desea definir sus
propios niveles y necesita que tengan valores específicos en relación
con los niveles predefinidos. Si define un nivel con el mismo valor
numérico, sobrescribe el valor predefinido; se pierde el nombre
predefinido.

+-------------------------+-----------------+---------------------------------------+
| Nivel                   | Valor numérico  | Qué significa / Cuándo utilizarlo     |
|=========================|=================|=======================================|
| logging.NOTSET          | 0               | Cuando se establece en un logger,     |
|                         |                 | indica que los loggers antecesores    |
|                         |                 | deben ser consultados para determinar |
|                         |                 | el nivel efectivo. Si el resultado    |
|                         |                 | sigue siendo "NOTSET", se registrarán |
|                         |                 | todos los eventos. Cuando se          |
|                         |                 | establece en un gestor, todos los     |
## |                         |                 | eventos son gestionados.              |

| logging.DEBUG           | 10              | Información detallada, normalmente    |
|                         |                 | sólo de interés para un desarrollador |
## |                         |                 | que intenta diagnosticar un problema. |

| logging.INFO            | 20              | Confirmación de que todo funciona     |
## |                         |                 | según lo previsto.                    |

| logging.WARNING         | 30              | Una indicación de que ha ocurrido     |
|                         |                 | algo inesperado o de que podría       |
|                         |                 | producirse un problema en un futuro   |
|                         |                 | próximo (por ejemplo, "espacio en     |
|                         |                 | disco bajo"). El software sigue       |
## |                         |                 | funcionando como se esperaba.         |

| logging.ERROR           | 40              | Debido a un problema más grave, el    |
|                         |                 | software no ha podido realizar alguna |
## |                         |                 | función.                              |

| logging.CRITICAL        | 50              | Un error grave, que indica que es     |
|                         |                 | posible que el propio programa no     |
## |                         |                 | pueda seguir ejecutándose.            |

## Gestor de objetos

Los gestores tienen los siguientes atributos y métodos. Tenga en
cuenta que "Handler" nunca se instancia directamente; esta clase actúa
como base para subclases más útiles. Sin embargo, el método
"__init__()" en las subclases debe llamar a "Handler.__init__()".

class logging.Handler

   __init__(level=NOTSET)

      Inicializa la instancia "Handler" estableciendo su nivel,
      configurando la lista de filtros en la lista vacía y creando un
      bloqueo (usando "createLock()") para serializar el acceso a un
      mecanismo de E/S.

   createLock()

      Inicializa un bloqueo de subprocesos que se puede utilizar para
      serializar el acceso a la funcionalidad de E/S subyacente que
      puede no ser segura para subprocesos.

   acquire()

      Adquiere el bloqueo de hilo creado con "createLock()".

   release()

      Libera el bloqueo de hilo adquirido con "acquire()".

   setLevel(level)

      Establece el umbral para este gestor en *level*. Los mensajes de
      registro que son menos severos que *level* serán ignorados.
      Cuando se crea un gestor, el nivel se establece en "NOTSET" (lo
      que hace que se procesen todos los mensajes).

      Ver Niveles de logging para obtener una lista de niveles.

      Distinto en la versión 3.2: El parámetro *level* ahora acepta
      una representación de cadena del nivel como 'INFO' como
      alternativa a las constantes de enteros como "INFO".

   setFormatter(fmt)

      Sets the formatter for this handler to *fmt*. The *fmt* argument
      must be a "Formatter" instance or "None".

   addFilter(filter)

      Agrega el filtro *filter* especificado a este gestor.

   removeFilter(filter)

      Elimina el filtro especificado *filter* de este gestor.

   filter(record)

      Aplique los filtros de este gestor al registro y retorna "True"
      si se va a procesar el registro. Los filtros se consultan a su
      vez, hasta que uno de ellos retorna un valor falso. Si ninguno
      de ellos retorna un valor falso, se emitirá el registro. Si uno
      retorna un valor falso, el gestor no emitirá el registro.

   flush()

      Asegúrese de que toda la salida de logging se haya vaciado. Esta
      versión no hace nada y está destinada a ser implementada por
      subclases.

   close()

      Tidy up any resources used by the handler. This version does no
      output but removes the handler from an internal map of handlers,
      which is used for handler lookup by name.

      Subclasses should ensure that this gets called from overridden
      "close()" methods.

   handle(record)

      Emite condicionalmente el registro especifico, según los filtros
      que se hayan agregado al gestor. Envuelve la actual emisión del
      registro con *acquisition/release* del hilo de bloqueo E/S.

   handleError(record)

      This method should be called from handlers when an exception is
      encountered during an "emit()" call. If the module-level
      attribute "raiseExceptions" is "False", exceptions get silently
      ignored. This is what is mostly wanted for a logging system -
      most users will not care about errors in the logging system,
      they are more interested in application errors. You could,
      however, replace this with a custom handler if you wish. The
      specified record is the one which was being processed when the
      exception occurred. (The default value of "raiseExceptions" is
      "True", as that is more useful during development).

   format(record)

      Formato para un registro - si se configura un formateador,
      úselo. De lo contrario, use el formateador predeterminado para
      el módulo.

   emit(record)

      Haga lo que sea necesario para registrar de forma especifica el
      registro. Esta versión está destinada a ser implementada por
      subclases y, por lo tanto, lanza un "NotImplementedError".

      Advertencia:

        Este método es llamado después de que un bloqueo a nivel de
        gestor es adquirido, el cual es liberado después de que este
        método retorna. Cuando sobrescriba este método, tenga en
        cuenta que debe tener cuidado al llamar a cualquier cosa que
        invoque a otras partes de la API de registro que puedan
        realizar bloqueos, ya que esto podría provocar un bloqueo.
        Específicamente:

        * Las API de configuración del registro adquieren el bloqueo a
          nivel de módulo y, a continuación, los bloqueos a nivel de
          gestor individual a medida que se configuran dichos
          gestores.

        * Muchas APIs de registro bloquean el bloqueo a nivel de
          módulo. Si se llama a una API de este tipo desde este
          método, podría causar un bloqueo si se realiza una llamada
          de configuración en otro hilo, porque ese hilo intentará
          adquirir el bloqueo a nivel de módulo *antes* del bloqueo a
          nivel de gestor, mientras que este hilo intenta adquirir el
          bloqueo a nivel de módulo *después* del bloqueo a nivel de
          gestor (porque en este método, el bloqueo a nivel de gestor
          ya se ha adquirido).

Para obtener una lista de gestores incluidos como estándar, consulte
"logging.handlers".

## Objetos formateadores

class logging.Formatter(fmt=None, datefmt=None, style='%', validate=True, *, defaults=None)

   Responsable de convertir un "LogRecord" en una cadena de salida
   para ser interpretada por un humano o un sistema externo.

   Parámetros:
      * **fmt** (*str*) -- Una cadena de formato en el *estilo* dado
        para la salida registrada en su conjunto. Las posibles claves
        de mapeo se extraen de Atributos LogRecord del objeto
        "LogRecord". Si no se especifica, se utiliza "'%(message)s'",
        que es sólo el mensaje registrado.

      * **datefmt** (*str*) -- A format string for the date/time
        portion of the logged output. If not specified, the default
        described in "formatTime()" is used.

      * **style** (*str*) -- Can be one of "'%'", "'{'" or "'$'" and
        determines how the format string will be merged with its data:
        using one of Formateo de cadenas al estilo *printf* ("%"),
        "str.format()" ("{") or "string.Template" ("$"). This only
        applies to *fmt* (e.g. "'%(message)s'" versus "'{message}'"),
        not to the actual log messages passed to the logging methods.
        However, there are other ways to use "{"- and "$"-formatting
        for log messages.

      * **validate** (*bool*) -- Si el parámetro *validate* es "True"
        (lo es por defecto), es incorrecto o no coincidente, *fmt* y
        *style* lanzarán un "ValueError"; Por ejemplo,
        "logging.Formatter('%(asctime)s - %(message)s', style='{')".

      * **defaults** (*dict**[**str**, **Any**]*) -- El parámetro
        *defaults* puede ser un diccionario con valores por defecto
        para usar en campos personalizados. Por ejemplo:
        "logging.Formatter('%(ip)s %(message)s', defaults={"ip":
        None})"

   Distinto en la versión 3.2: Added the *style* parameter.

   Distinto en la versión 3.8: Added the *validate* parameter.

   Distinto en la versión 3.10: Added the *defaults* parameter.

   format(record)

      El diccionario de atributos del registro se usa como el operando
      de una operación para formateo de cadenas. Retorna la cadena
      resultante. Antes de formatear el diccionario, se lleva a cabo
      un par de pasos preparatorios. El atributo *message* del
      registro se calcula usando *msg* % *args*. Si el formato de la
      cadena contiene "'(asctime)'", "formatTime()" se llama para dar
      formato al tiempo del evento. Si hay información sobre la
      excepción, se formatea usando "formatException()" y se adjunta
      al mensaje. Tenga en cuenta que la información de excepción
      formateada se almacena en caché en el atributo *exc_text*. Esto
      es útil porque la información de excepción se puede serializar
      con pickle (*pickled*) y propagarse por el cable, pero debe
      tener cuidado si tiene más de una subclase de "Formatter" que
      personaliza el formato de la información de la excepción. En
      este caso, tendrá que borrar el valor almacenado en caché
      (estableciendo el atributo *exc_text* a "None") después de que
      un formateador haya terminado su formateo, para que el siguiente
      formateador que maneje el evento no use el valor almacenado en
      caché, sino que lo recalcule de nuevo.

      Si la información de la pila está disponible, se agrega después
      de la información de la excepción, usando "formatStack()" para
      transformarla si es necesario.

   formatTime(record, datefmt=None)

      Este método debe ser llamado desde "format()" por un formateador
      que espera un tiempo formateado . Este método se puede
      reemplazar en formateadores para proporcionar cualquier
      requisito específico, pero el comportamiento básico es el
      siguiente: if *datefmt* (una cadena), se usa con
      "time.strftime()" para formatear el tiempo de creación del
      registro De lo contrario, se utiliza el formato '%Y-%m-%d
      %H:%M:%S,uuu', donde la parte *uuu* es un valor de milisegundos
      y las otras letras son "time.strftime()" . Un ejemplo de tiempo
      en este formato es "2003-01-23 00:29:50,411". Se retorna la
      cadena resultante.

      Esta función utiliza una función configurable por el usuario
      para convertir el tiempo de creación en una tupla. Por defecto,
      se utiliza "time.localtime()"; Para cambiar esto para una
      instancia de formateador particular, se agrega el atributo
      "converter" en una función con igual firma como
      "time.localtime()" o "time.gmtime()". Para cambiarlo en todos
      los formateadores, por ejemplo, si desea que todos los tiempos
      de registro se muestren en GMT, agregue el atributo "converter"
      en la clase "Formatter".

      Distinto en la versión 3.3: Anteriormente, el formato
      predeterminado estaba codificado como en este ejemplo:
      "2010-09-06 22:38:15,292" donde la parte anterior a la coma es
      manejada por una cadena de formato strptime ("'%Y-%m-%d
      %H:%M:%S'"), y la parte después de la coma es un valor de
      milisegundos. Debido a que strptime no tiene una posición de
      formato para milisegundos, el valor de milisegundos se agrega
      usando otra cadena de formato, "'%s,%03d'"--- ambas cadenas de
      formato se han codificado en este método. Con el cambio, estas
      cadenas se definen como atributos de nivel de clase que pueden
      *overridden* a nivel de instancia cuando se desee. Los nombres
      de los atributos son "default_time_format" (para una cadena de
      formato strptime) y "default_msec_format" (para agregar el valor
      de milisegundos).

      Distinto en la versión 3.9: El formato "default_msec_format"
      puede ser "None".

   formatException(exc_info)

      Formatea la información de una excepción especificada (una
      excepción como una tupla estándar es retornada por
      "sys.exc_info()") como una cadena. Esta implementación
      predeterminada solo usa "traceback.print_exception()". La cadena
      resultantes retornada.

   formatStack(stack_info)

      Formatea la información de una pila especificada (una cadena es
      retornada por "traceback.print_stack()", pero con la ultima
      línea removida) como una cadena. Esta implementación
      predeterminada solo retorna el valor de entrada.

class logging.BufferingFormatter(linefmt=None)

   Una clase base de formateador adecuada para subclasificar cuando se
   desea formatear un número de registros. Puede pasar una instancia
   "Formatter" que desee utilizar para formatear cada línea (que
   corresponde a un único registro). Si no se especifica, el
   formateador por defecto (que sólo muestra el mensaje del evento) se
   utiliza como formateador de línea.

   formatHeader(records)

      Retorna una cabecera para una lista de *registros*. La
      implementación base sólo retorna la cadena vacía. Tendrá que
      anular este método si desea un comportamiento específico, por
      ejemplo, mostrar el recuento de registros, un título o una línea
      separadora.

   formatFooter(records)

      Retorna un pie de página para una lista de *registros*. La
      implementación base sólo retorna la cadena vacía. Tendrá que
      anular este método si desea un comportamiento específico, por
      ejemplo, para mostrar el recuento de registros o una línea
      separadora.

   format(records)

      Retorna el texto formateado de una lista de *registros*. La
      implementación base sólo retorna la cadena vacía si no hay
      registros; en caso contrario, retorna la concatenación de la
      cabecera, cada registro formateado con el formateador de líneas
      y el pie de página.

## Filtro de Objetos

Los "Manejadores" y los "Registradores" pueden usar los "Filtros" para
un filtrado más sofisticado que el proporcionado por los niveles. La
clase de filtro base solo permite eventos que están por debajo de
cierto punto en la jerarquía del logger. Por ejemplo, un filtro
inicializado con 'A.B' permitirá los eventos registrados por los
logger 'A.B', 'A.B.C', 'A.B.C.D', 'A.B.D' etc., pero no 'A.BB',
'B.A.B', etc. Si se inicializa con una cadena vacía, se pasan todos
los eventos.

class logging.Filter(name='')

   Retorna una instancia de la clase "Filter". Si se especifica
   *name*, nombra un logger que, junto con sus hijos, tendrá sus
   eventos permitidos a través del filtro. Si *name* es una cadena
   vacía, permite todos los eventos.

   filter(record)

      ¿Debe registrarse el registro especificado? Retorna 'false' para
      no, 'true' para sí. Los filtros pueden modificar los registros
      en el lugar o retornar una instancia de registro completamente
      diferente que sustituirá al registro original en cualquier
      procesamiento futuro del evento.

Tenga en cuenta que los filtros adjuntos a los gestores se consultan
antes de que el gestor emita un evento, mientras que los filtros
adjuntos a los loggers se consultan cada vez que se registra un evento
(usando "debug()", "info()", etc.), antes de enviar un evento a los
gestores. Esto significa que los eventos que han sido generados por
loggers descendientes no serán filtrados por la configuración del
filtro del logger, a menos que el filtro también se haya aplicado a
esos loggers descendientes.

En realidad, no se necesita la subclase "Filtro": se puede pasar
cualquier instancia que tenga un método de "filter" con la misma
semántica.

Distinto en la versión 3.2: No es necesario crear clases
especializadas de "Filter" ni usar otras clases con un método
"filter": puede usar una función (u otra invocable) como filtro. La
lógica de filtrado verificará si el objeto de filtro tiene un atributo
"filter": si lo tiene, se asume que es un "Filter" y se llama a su
método "filter()". De lo contrario, se supone que es invocable y se
llama con el registro como único parámetro. El valor retornado debe
ajustarse al retornado por "filter()".

Distinto en la versión 3.12: Ahora puedes retornar una instancia de
"LogRecord" desde los filtros para reemplazar el registro en lugar de
modificarlo. Esto permite a los filtros adjuntos a un "Handler"
modificar el registro de log antes de que se emita, sin tener efectos
secundarios en otros gestores.

Aunque los filtros se utilizan principalmente para filtrar registros
basados en criterios más sofisticados que los niveles, son capaces de
ver cada registro que es procesado por el gestor o logger al que están
adjuntos: esto puede ser útil si desea hacer cosas como contar cuántos
registros fueron procesados por un logger o gestor en particular, o
agregando, cambiando o quitando atributos en "LogRecord" que se está
procesando. Obviamente, el cambio de LogRecord debe hacerse con cierto
cuidado, pero permite la inyección de información contextual en los
registros (ver Usar filtros para impartir información contextual).

## Objetos LogRecord

Las instancias "LogRecord" son creadas automáticamente por "Logger"
cada vez que se registra algo, y se pueden crear manualmente a través
de "makeLogRecord()" (por ejemplo, a partir de un evento serializado
(*pickled*) recibido en la transmisión).

class logging.LogRecord(name, level, pathname, lineno, msg, args, exc_info, func=None, sinfo=None)

   Contiene toda la información pertinente al evento que se registra.

   La información principal se pasa en *msg* y *args*, que se combinan
   usando "msg % args" para crear el atributo "message" del registro.

   Parámetros:
      * **name** (*str*) -- El nombre del logger utilizado para
        registrar el evento representado por este "LogRecord". Tenga
        en cuenta que el nombre del logger en el "LogRecord" siempre
        tendrá este valor, aunque puede ser emitido por un gestor
        adjunto a un logger diferente (ancestro).

      * **level** (*int*) -- El numeric level del evento de registro
        (como "10" para "DEBUG", "20" para "INFO", etc). Tenga en
        cuenta que esto se convierte en *dos* atributos del LogRecord:
        "levelno" para el valor numérico y "levelname" para el nombre
        del nivel correspondiente.

      * **pathname** (*str*) -- El nombre de ruta completo del archivo
        de origen donde se realizó la llamada logging.

      * **lineno** (*int*) -- El número de línea en el archivo de
        origen donde se realizó la llamada logging.

      * **msg** (*Any*) -- El mensaje de descripción del evento, que
        puede ser una cadena de formato %, con marcadores de posición
        para datos variables o un objeto arbitrario (para más
        información vea Usando objetos arbitrarios como mensajes).

      * **args** (*tuple** | **dict**[**str**, **Any**]*) -- Datos
        variables para fusionar en el argumento *msg* para obtener la
        descripción del evento.

      * **exc_info** (*tuple**[**type**[**BaseException**]**,
        **BaseException**, **types.TracebackType**] **| **None*) --
        Una tupla de excepción con la información de excepción actual,
        tal como se retorna por "sys.exc_info()" o "None" si no hay
        información de excepción disponible.

      * **func** (*str** | **None*) -- El nombre de la función o
        método desde el que se invocó la llamada de logging.

      * **sinfo** (*str** | **None*) -- Una cadena de texto que
        representa la información de la pila desde la base de la pila
        en el hilo actual, hasta la llamada de logging.

   getMessage()

      Retorna el mensaje para la instancia "LogRecord" después de
      fusionar cualquier argumento proporcionado por el usuario con el
      mensaje. Si el argumento del mensaje proporcionado por el
      usuario para la llamada de logging no es una cadena de
      caracteres, se invoca "str()" para convertirlo en una cadena.
      Esto permite el uso de clases definidas por el usuario como
      mensajes, cuyo método "__str__" puede retornar la cadena de
      formato real que se utilizará.

   Distinto en la versión 3.2: La creación de "LogRecord" se ha hecho
   más configurable al proporcionar una fábrica que se utiliza para
   crear el registro. La fábrica se puede configurar usando
   "getLogRecordFactory()" y "setLogRecordFactory()" (ver esto para la
   firma de la fábrica).

   Esta funcionalidad se puede utilizar para inyectar sus propios
   valores en "LogRecord" en el momento de la creación. Puede utilizar
   el siguiente patrón:

      old_factory = logging.getLogRecordFactory()

      def record_factory(*args, **kwargs):
          record = old_factory(*args, **kwargs)
          record.custom_attribute = 0xdecafbad
          return record

      logging.setLogRecordFactory(record_factory)

   Con este patrón, se podrían encadenar varias fábricas y, siempre
   que no sobrescriban los atributos de las demás o se sobrescriban
   involuntariamente los atributos estándar enumerados anteriormente,
   no debería haber sorpresas.

## Atributos LogRecord

El LogRecord tiene una serie de atributos, la mayoría de los cuales se
derivan de los parámetros del constructor. (Tenga en cuenta que los
nombres no siempre se corresponden exactamente entre los parámetros
del constructor de LogRecord y los atributos de LogRecord). Estos
atributos pueden utilizarse para combinar los datos del registro en la
cadena de formato. La siguiente tabla enumera (en orden alfabético)
los nombres de los atributos, sus significados y el correspondiente
marcador de posición en una cadena de formato %-style.

Si utilizas formato-{} ("str.format()"), puedes usar "{attrname}" como
marcador de posición en la cadena de caracteres de formato. Si está
utilizando formato-$ ("string.Template"), use la forma "${attrname}".
En ambos casos, por supuesto, reemplace "attrname" con el nombre de
atributo real que desea utilizar.

En el caso del formato con {}, puede especificar *flags* de formato
colocándolos después del nombre del atributo, separados con dos
puntos. Por ejemplo: un marcador de posición de "{msecs:03.0f}"
formateará un valor de milisegundos de "4" como "004". Consulte la
documentación "str.format()" para obtener detalles completos sobre las
opciones disponibles.

+------------------+---------------------------+-------------------------------------------------+
| Nombre del       | Formato                   | Descripción                                     |
| atributo         |                           |                                                 |
|==================|===========================|=================================================|
| args             | No debería necesitar      | La tupla de argumentos se fusionó en "msg" para |
|                  | formatear esto usted      | producir un "messsage", o un dict cuyos valores |
|                  | mismo.                    | se utilizan para la fusión (cuando solo hay un  |
## |                  |                           | argumento y es un diccionario).                 |

| asctime          | "%(asctime)s"             | Fecha y Hora en formato legible por humanos     |
|                  |                           | cuando se creó "LogRecord". De forma            |
|                  |                           | predeterminada, tiene el formato '2003-07-08    |
|                  |                           | 16: 49: 45,896' (los números después de la coma |
## |                  |                           | son milisegundos).                              |

| created          | "%(created)f"             | Time when the "LogRecord" was created (as       |
## |                  |                           | returned by "time.time_ns()" / 1e9).            |

| exc_info         | No debería necesitar      | Tupla de excepción (al modo "sys.exc_info") o,  |
|                  | formatear esto usted      | si no se ha producido ninguna excepción,        |
## |                  | mismo.                    | "None".                                         |

| exc_text         | No debería necesitar      | Exception information formatted as a string.    |
|                  | formatear esto usted      | This is set when "Formatter.format()" is        |
|                  | mismo.                    | invoked, or "None" if no exception has          |
## |                  |                           | occurred.                                       |

## | filename         | "%(filename)s"            | Parte del nombre de archivo de "pathname".      |

| funcName         | "%(funcName)s"            | Nombre de la función que contiene la llamada de |
## |                  |                           | logging.                                        |

| levelname        | "%(levelname)s"           | Texto de nivel de logging para el mensaje       |
|                  |                           | ("'DEBUG'", "'INFO'", "'WARNING'", "'ERROR'",   |
## |                  |                           | "'CRITICAL'").                                  |

| levelno          | "%(levelno)s"             | Número de nivel de logging para el mensaje      |
|                  |                           | ("DEBUG", "INFO", "WARNING", "ERROR",           |
## |                  |                           | "CRITICAL").                                    |

| lineno           | "%(lineno)d"              | Número de línea original donde se emitió la     |
## |                  |                           | llamada de logging (si está disponible).        |

| message          | "%(message)s"             | El mensaje registrado, computado como "msg %    |
|                  |                           | args". Esto se establece cuando se invoca       |
## |                  |                           | "Formatter.format()".                           |

## | module           | "%(module)s"              | Módulo (parte del nombre de "filename").        |

| msecs            | "%(msecs)d"               | Porción de milisegundos del tiempo en que se    |
## |                  |                           | creó "LogRecord".                               |

| msg              | No debería necesitar      | La cadena de caracteres de formato pasada en la |
|                  | formatear esto usted      | llamada logging original. Se fusionó con "args" |
|                  | mismo.                    | para producir un "message", o un objeto         |
|                  |                           | arbitrario (ver Usando objetos arbitrarios como |
## |                  |                           | mensajes).                                      |

| name             | "%(name)s"                | Nombre del logger usado para registrar la       |
## |                  |                           | llamada.                                        |

| pathname         | "%(pathname)s"            | Nombre de ruta completo del archivo de origen   |
|                  |                           | donde se emitió la llamada de logging (si está  |
## |                  |                           | disponible).                                    |

## | process          | "%(process)d"             | ID de proceso (si está disponible).             |

## | processName      | "%(processName)s"         | Nombre del proceso (si está disponible).        |

| relativeCreated  | "%(relativeCreated)d"     | Tiempo en milisegundos cuando se creó el        |
|                  |                           | LogRecord, en relación con el tiempo en que se  |
## |                  |                           | cargó el módulo logging.                        |

| stack_info       | No debería necesitar      | Apila la información del marco (si está         |
|                  | formatear esto usted      | disponible) desde la parte inferior de la pila  |
|                  | mismo.                    | en el hilo actual hasta la llamada de registro  |
|                  |                           | que dio como resultado la generación de este    |
## |                  |                           | registro.                                       |

## | thread           | "%(thread)d"              | ID de hilo (si está disponible).                |

## | threadName       | "%(threadName)s"          | Nombre del hilo (si está disponible).           |

## | taskName         | "%(taskName)s"            | nombre de "asyncio.Task" (si está disponible).  |

Distinto en la versión 3.1: *processName* fue agregado.

Distinto en la versión 3.12: *taskName* fue agregado.

## Objetos LoggerAdapter

Las instancias "LoggerAdapter" se utilizan para pasar convenientemente
información contextual en las llamadas de logging. Para ver un ejemplo
de uso, consulte la sección sobre agregar información contextual a su
salida de logging.

class logging.LoggerAdapter(logger, extra=None, merge_extra=False)

   Returns an instance of "LoggerAdapter" initialized with an
   underlying "Logger" instance, an optional dict-like object
   (*extra*), and an optional boolean (*merge_extra*) indicating
   whether or not the *extra* argument of individual log calls should
   be merged with the "LoggerAdapter" extra. The default behavior is
   to ignore the *extra* argument of individual log calls and only use
   the one of the "LoggerAdapter" instance

   process(msg, kwargs)

      Modifica el mensaje y/o los argumentos de palabra clave pasados
      a una llamada de logging para insertar información contextual.
      Esta implementación toma el objeto pasado como *extra* al
      constructor y lo agrega a *kwargs* usando la clave 'extra'. El
      valor de retorno es una tupla (*msg*, *kwargs*) que tiene las
      versiones (posiblemente modificadas) de los argumentos pasados.

   manager

      Delegates to the underlying "manager" on *logger*.

   _log

      Delegates to the underlying "_log()" method on *logger*.

   Además de lo anterior, "LoggerAdapter" admite los siguientes
   métodos de "Logger": "debug()", "info()", "warning()", "error()",
   "exception()", "critical()", "log()", "isEnabledFor()",
   "getEffectiveLevel()", "setLevel()" y "hasHandlers()". Estos
   métodos tienen las mismas firmas que sus contrapartes en "Logger",
   por lo que puede usar los dos tipos de instancias indistintamente.

   Distinto en la versión 3.2: Los métodos "isEnabledFor()",
   "getEffectiveLevel()", "setLevel()" y "hasHandlers()" se agregaron
   a "LoggerAdapter" . Estos métodos se delegan al logger subyacente.

   Distinto en la versión 3.6: Se añadió el atributo "manager" y el
   método "_log()", que delegan al logger subyacente y permiten que
   los adaptadores se aniden.

   Distinto en la versión 3.10: The *extra* argument is now optional.

   Distinto en la versión 3.13: The *merge_extra* parameter was added.

## Seguridad del hilo

The logging module is intended to be thread-safe without any special
work needing to be done by its clients. It achieves this through using
threading locks; there is one lock to serialize access to the module's
shared data, and each handler also creates a lock to serialize access
to its underlying I/O.

Si está implementando gestores de señales asíncronos usando el módulo
"signal", es posible que no pueda usar logging desde dichos gestores.
Esto se debe a que las implementaciones de bloqueo en el módulo
"threading" no siempre son reentrantes y, por lo tanto, no se pueden
invocar desde dichos gestores de señales.

## Funciones a nivel de módulo

Además de las clases descritas anteriormente, hay una serie de
funciones a nivel de módulo.

logging.getLogger(name=None)

   Return a logger with the specified name or, if name is "None",
   return the root logger of the hierarchy. If specified, the name is
   typically a dot-separated hierarchical name like *'a'*, *'a.b'* or
   *'a.b.c.d'*. Choice of these names is entirely up to the developer
   who is using logging, though it is recommended that "__name__" be
   used unless you have a specific reason for not doing that, as
   mentioned in Objetos logger.

   Todas las llamadas a esta función con un nombre dado retornan la
   misma instancia de logger. Esto significa que las instancias del
   logger nunca necesitan pasar entre diferentes partes de una
   aplicación.

logging.getLoggerClass()

   Retorna ya sea la clase estándar "Logger", o la última clase pasada
   a "setLoggerClass()". Esta función se puede llamar desde una nueva
   definición de clase, para garantizar que la instalación de una
   clase personalizada "Logger" no deshaga las *customizaciones* ya
   aplicadas por otro código. Por ejemplo:

      class MyLogger(logging.getLoggerClass()):
          # ... override behaviour here

logging.getLogRecordFactory()

   Retorna un invocable que se usa para crear una "LogRecord".

   Added in version 3.2: Esta función se ha proporcionado, junto con
   "setLogRecordFactory()", para permitir a los desarrolladores un
   mayor control sobre cómo "LogRecord" representa un evento logging
   construido.

   Consulte "setLogRecordFactory()" para obtener más información sobre
   cómo se llama a la fábrica.

logging.debug(msg, *args, **kwargs)

   This is a convenience function that calls "Logger.debug()", on the
   root logger. The handling of the arguments is in every way
   identical to what is described in that method.

   The only difference is that if the root logger has no handlers,
   then "basicConfig()" is called, prior to calling "debug" on the
   root logger.

   For very short scripts or quick demonstrations of "logging"
   facilities, "debug" and the other module-level functions may be
   convenient. However, most programs will want to carefully and
   explicitly control the logging configuration, and should therefore
   prefer creating a module-level logger and calling "Logger.debug()"
   (or other level-specific methods) on it, as described at the
   beginning of this documentation.

logging.info(msg, *args, **kwargs)

   Logs a message with level "INFO" on the root logger. The arguments
   and behavior are otherwise the same as for "debug()".

logging.warning(msg, *args, **kwargs)

   Logs a message with level "WARNING" on the root logger. The
   arguments and behavior are otherwise the same as for "debug()".

   Nota:

     Hay una función obsoleta "warn" que es funcionalmente idéntica a
     "warning". Como "warn" está deprecado, por favor no lo use, use
     "warning" en su lugar.

logging.error(msg, *args, **kwargs)

   Logs a message with level "ERROR" on the root logger. The arguments
   and behavior are otherwise the same as for "debug()".

logging.critical(msg, *args, **kwargs)

   Logs a message with level "CRITICAL" on the root logger. The
   arguments and behavior are otherwise the same as for "debug()".

logging.exception(msg, *args, **kwargs)

   Logs a message with level "ERROR" on the root logger. The arguments
   and behavior are otherwise the same as for "debug()". Exception
   info is added to the logging message. This function should only be
   called from an exception handler.

logging.log(level, msg, *args, **kwargs)

   Logs a message with level *level* on the root logger. The arguments
   and behavior are otherwise the same as for "debug()".

logging.disable(level=CRITICAL)

   Proporciona un nivel superior de *level* para todos los loggers que
   tienen prioridad sobre el propio nivel del logger. Cuando surge la
   necesidad de reducir temporalmente la salida de logging en toda la
   aplicación, esta función puede resultar útil. Su efecto es
   deshabilitar todas las llamadas de gravedad *level* e inferior, de
   modo que si lo llaman con un valor de INFO, todos los eventos INFO
   y DEBUG se descartarán, mientras que los de gravedad WARNING y
   superiores se procesarán de acuerdo con el nivel efectivo del
   logger. Si se llama a "logging.disable(logging.NOTSET)" , elimina
   efectivamente este nivel primordial, de modo que la salida del
   registro depende nuevamente de los niveles efectivos de los loggers
   individuales.

   Tenga en cuenta que si ha definido un nivel de logging
   personalizado superior a "CRITICAL" (esto no es recomendado), no
   podrá confiar en el valor predeterminado para el parámetro *level*,
   pero tendrá que proporcionar explícitamente un valor adecuado.

   Distinto en la versión 3.7: El parámetro *level* se estableció por
   defecto en el nivel "CRITICAL". Consulte el Issue #28524 para
   obtener más información sobre este cambio.

logging.addLevelName(level, levelName)

   Asocia nivel *level* con el texto *levelName* en un diccionario
   interno, que se utiliza para asignar niveles numéricos a una
   representación textual, por ejemplo, cuando "Formatter" formatea un
   mensaje. Esta función también se puede utilizar para definir sus
   propios niveles. Las únicas restricciones son que todos los niveles
   utilizados deben registrarse utilizando esta función, los niveles
   deben ser números enteros positivos y deben aumentar en orden
   creciente de severidad.

   Nota:

     Si está pensando en definir sus propios niveles, consulte la
     sección sobre Niveles personalizados.

logging.getLevelNamesMapping()

   Retorna una correspondencia entre los nombres de nivel y sus
   correspondientes niveles de registro. Por ejemplo, la cadena
   "CRITICAL" corresponde a "CRITICAL". La correspondencia retornada
   se copia de una correspondencia interna en cada llamada a esta
   función.

   Added in version 3.11.

logging.getLevelName(level)

   Retorna la representación textual o numérica del nivel de registro
   *level*.

   Si *level* es uno de los niveles predefinidos "CRITICAL", "ERROR",
   "WARNING", "INFO" o "DEBUG" entonces se obtiene la cadena
   correspondiente. Si has asociado niveles con nombres usando
   "addLevelName()" entonces se retorna el nombre que has asociado con
   *level*. Si se pasa un valor numérico correspondiente a uno de los
   niveles definidos, se retorna la representación de cadena
   correspondiente.

   El parámetro *level* también acepta una representación de cadena
   del nivel como, por ejemplo, "INFO". En estos casos, esta función
   retorna el correspondiente valor numérico del nivel.

   Si no se pasa un valor numérico o de cadena que coincida, se
   retorna el valor de nivel de la cadena 'Level %s'.

   Nota:

     Los niveles internamente son números enteros (ya que deben
     compararse en la lógica de logging). Esta función se utiliza para
     convertir entre un nivel entero y el nombre del nivel que se
     muestra en la salida de logging formateado mediante el
     especificador de formato "%(levelname)s" (ver Atributos
     LogRecord).

   Distinto en la versión 3.4: En las versiones de Python anteriores a
   la 3.4, esta función también podría pasar un nivel de texto y
   retornaría el valor numérico correspondiente del nivel. Este
   comportamiento indocumentado se consideró un error y se eliminó en
   Python 3.4, pero se restableció en 3.4.2 debido a que conserva la
   compatibilidad con versiones anteriores.

logging.getHandlerByName(name)

   Retorna un gestor con el *name* especificado o "None" si no hay un
   gestor con ese nombre.

   Added in version 3.12.

logging.getHandlerNames()

   Retorna un conjunto inmutable del nombre de todos los gestor
   conocidos.

   Added in version 3.12.

logging.makeLogRecord(attrdict)

   Crea y retorna una nueva instancia "LogRecord" cuyos atributos
   están definidos por *attrdict*. Esta función es útil para tomar un
   diccionario de atributos serializado (*pickled*) "LogRecord",
   enviado a través de un socket, y reconstituido como una instancia
   "LogRecord" en el extremo receptor.

logging.basicConfig(**kwargs)

   Realiza una configuración básica para el sistema de logging creando
   una "StreamHandler" con un "Formatter" predeterminado y agregándolo
   al logger raíz. Las funciones "debug()", "info()", "warning()",
   "error()" y "critical()" llamarán "basicConfig()" automáticamente
   si no se definen gestores para el logger raíz.

   Esta función no hace nada si el logger raíz ya tiene gestores
   configurados, a menos que el argumento de palabra clave *force*
   esté establecido como "True".

   Nota:

     Esta función debe llamarse desde el hilo principal antes de que
     se inicien otros hilos. En las versiones de Python anteriores a
     2.7.1 y 3.2, si se llama a esta función desde varios subprocesos,
     es posible (en raras circunstancias) que se agregue un gestor al
     logger raíz más de una vez, lo que genera resultados inesperados
     como mensajes duplicados en el registro.

   Se admiten los siguientes argumentos de palabras clave.

   +----------------+-----------------------------------------------+
   | Formato        | Descripción                                   |
   |================|===============================================|
   | *filename*     | Especifica que se cree un "FileHandler",      |
   |                | utilizando el nombre de archivo especificado, |
   |                | en lugar de "StreamHandler".                  |
   +----------------+-----------------------------------------------+
   | *filemode*     | Si se especifica *filename*, abre el archivo  |
   |                | en mode. Por defecto es "'a'".                |
   +----------------+-----------------------------------------------+
   | *format*       | Utiliza la cadena de caracteres de formato    |
   |                | especificada para el gestor.Los atributos por |
   |                | defecto son "levelname", "name" y "message"   |
   |                | separado por dos puntos.                      |
   +----------------+-----------------------------------------------+
   | *datefmt*      | Utiliza el formato de fecha/hora              |
   |                | especificado, aceptado por "time.strftime()". |
   +----------------+-----------------------------------------------+
   | *style*        | Si *format* es especificado, utilice este     |
   |                | estilo para la cadena de caracteres de        |
   |                | formato. Uno de "'%'", "'{'" o "'$'" para     |
   |                | printf- style, "str.format()" o               |
   |                | "string.Template" respectivamente. El valor   |
   |                | predeterminado es "'%'".                      |
   +----------------+-----------------------------------------------+
   | *level*        | Establece el nivel del logger raíz en el      |
   |                | level especificado.                           |
   +----------------+-----------------------------------------------+
   | *stream*       | Utiliza la secuencia especificada para        |
   |                | inicializar "StreamHandler". Tenga en cuenta  |
   |                | que este argumento es incompatible con        |
   |                | *filename* - si ambos están presentes, se     |
   |                | lanza un "ValueError".                        |
   +----------------+-----------------------------------------------+
   | *handlers*     | Si se especifica, debe ser una iteración de   |
   |                | los gestores ya creados para agregar al       |
   |                | logger raíz. A cualquier gestor que aún no    |
   |                | tenga un formateador configurado se le        |
   |                | asignará el formateador predeterminado creado |
   |                | en esta función. Tenga en cuenta que este     |
   |                | argumento es incompatible con *filename* o    |
   |                | *stream*; si ambos están presentes, se lanza  |
   |                | un "ValueError".                              |
   +----------------+-----------------------------------------------+
   | *force*        | Si este argumento de palabra clave se         |
   |                | especifica como verdadero, los gestores       |
   |                | existentes adjuntos al logger raíz se         |
   |                | eliminan y cierran antes de llevar a cabo la  |
   |                | configuración tal como se especifica en los   |
   |                | otros argumentos.                             |
   +----------------+-----------------------------------------------+
   | *encoding*     | Si este argumento de palabra clave se         |
   |                | especifica junto con *filename*, su valor se  |
   |                | utiliza cuando se crea el "FileHandler", y    |
   |                | por lo tanto se utiliza al abrir el archivo   |
   |                | de salida.                                    |
   +----------------+-----------------------------------------------+
   | *errors*       | Si este argumento de palabra clave se         |
   |                | especifica junto con *filename*, su valor se  |
   |                | utiliza cuando se crea el "FileHandler", y    |
   |                | por lo tanto cuando se abre el archivo de     |
   |                | salida. Si no se especifica, se utiliza el    |
   |                | valor 'backslashreplace'. Tenga en cuenta que |
   |                | si se especifica "None", se pasará como tal a |
   |                | "open()", lo que significa que se tratará     |
   |                | igual que pasar 'errors'.                     |
   +----------------+-----------------------------------------------+

   Distinto en la versión 3.2: Se agregó el argumento *style*.

   Distinto en la versión 3.3: Se agregó el argumento *handlers*. Se
   agregaron verificaciones adicionales para detectar situaciones en
   las que se especifican argumentos incompatibles (por ejemplo,
   *handlers* junto con *stream* o *filename*, o *stream* junto con
   *filename*).

   Distinto en la versión 3.8: Se agregó el argumento *force*.

   Distinto en la versión 3.9: Se han añadido los argumentos
   *encoding* y *errors*.

logging.shutdown()

   Informa al sistema de logging para realizar un apagado ordenado
   descargando y cerrando todos los gestores. Esto se debe llamar al
   salir de la aplicación y no se debe hacer ningún uso posterior del
   sistema de logging después de esta llamada.

   Cuando se importa el módulo de logging, registra esta función como
   un gestor de salida (ver "atexit"), por lo que normalmente no es
   necesario hacerlo manualmente.

logging.setLoggerClass(klass)

   Le dice al sistema de logging que use la clase *klass* al crear una
   instancia de un logger. La clase debe definir "__init__()" tal que
   solo se requiera un argumento de nombre, y "__init__()" debe llamar
   "Logger.__init__()". Por lo general, esta función se llama antes de
   que cualquier logger sea instanciado por las aplicaciones que
   necesitan utilizar un comportamiento de logger personalizado.
   Después de esta llamada, como en cualquier otro momento, no cree
   instancias de loggers directamente usando la subclase: continúe
   usando la API "logging.getLogger()" para obtener sus loggers.

logging.setLogRecordFactory(factory)

   Establece un invocable que se utiliza para crear "LogRecord".

   Parámetros:
      **factory** -- La fábrica invocable que se utilizará para crear
      una instancia de un registro.

   Added in version 3.2: Esta función se ha proporcionado, junto con
   "getLogRecordFactory()", para permitir a los desarrolladores un
   mayor control sobre cómo se construye "LogRecord" que representa un
   evento de logging.

   La fábrica tiene la siguiente firma:

   "factory(name, level, fn, lno, msg, args, exc_info, func=None,
   sinfo=None, **kwargs)"

      name:
         El nombre del logger.

      level:
         El nivel de logging (numérico).

      fn:
         El nombre de ruta completo del archivo donde se realizó la
         llamada de logging.

      lno:
         El número de línea en el archivo donde se realizó la llamada
         de logging.

      msg:
         El mensaje de logging.

      args:
         Los argumentos para el mensaje de logging.

      exc_info:
         Una tupla de excepción o "None".

      func:
         El nombre de la función o método que invocó la llamada de
         logging.

      sinfo:
         Un seguimiento de pila como el que proporciona
         "traceback.print_stack()", que muestra la jerarquía de
         llamadas.

      kwargs:
         Argumentos de palabras clave adicionales.

## Atributos a nivel de módulo

logging.lastResort

   Un "gestor de último recurso" está disponible a través de este
   atributo. Esta es una "StreamHandler" que escribe en "sys.stderr"
   con un nivel "WARNING", y se usa para gestionar eventos de logging
   en ausencia de cualquier configuración de logging. El resultado
   final es simplemente imprimir el mensaje en "sys.stderr". Esto
   reemplaza el mensaje de error anterior que decía que "no se
   pudieron encontrar gestores para el logger XYZ". Si necesita el
   comportamiento anterior por alguna razón, "lastResort" se puede
   configurar en "None".

   Added in version 3.2.

logging.raiseExceptions

   Used to see if exceptions during handling should be propagated.

   Default: "True".

   If "raiseExceptions" is "False", exceptions get silently ignored.
   This is what is mostly wanted for a logging system - most users
   will not care about errors in the logging system, they are more
   interested in application errors.

## Integración con el módulo de advertencias

The "captureWarnings()" function can be used to integrate "logging"
with the "warnings" module.

logging.captureWarnings(capture)

   Esta función se utiliza para activar y desactivar la captura de
   advertencias (*warnings*).

   Si *capture* es "True", las advertencias emitidas por el módulo
   "warnings" serán redirigidas al sistema de logging.
   Específicamente, una advertencia se formateará usando
   "warnings.formatwarning()" y la cadena de caracteres resultante se
   registrará en un logger  llamado "'py.warnings'" con severidad
   "WARNING".

   Si *capture* es "False", la redirección de advertencias al sistema
   de logging se detendrá y las advertencias serán redirigidas a sus
   destinos originales (es decir, aquellos en vigor antes de que se
   llamara a "captureWarnings(True)").

Ver también:

  Módulo "logging.config"
     API de configuración para el módulo logging.

  Módulo "logging.handlers"
     Gestores útiles incluidos con el módulo logging.

  **PEP 282** - A Logging System
     La propuesta que describió esta característica para su inclusión
     en la biblioteca estándar de Python.

  Paquete logging original de Python
     This is the original source for the "logging" package.  The
     version of the package available from this site is suitable for
     use with Python 1.5.2, 2.1.x and 2.2.x, which do not include the
     "logging" package in the standard library.
