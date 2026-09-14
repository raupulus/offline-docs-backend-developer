---
title: '"logging.handlers" --- Logging handlers'
source_url: https://docs.python.org/es/3
source_path: library/logging.handlers.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 3130
---

# "logging.handlers" --- Logging handlers

**Código fuente** Lib/logging/handlers.py

##### Important

Esta página contiene solo información de referencia. Para tutoriales
por favor véase

* Tutorial Básico

* Tutorial avanzado

* Libro de cocina de *Logging*

======================================================================

Estos gestores son muy útiles y están provistos en este paquete. Nota
que tres de los gestores de las clases ("StreamHandler", "FileHandler"
and "NullHandler") están definidos en propio módulo "logging" pero
fueron documentados aquí junto con los otros gestores.

## StreamHandler

La clase "StreamHandler" ubicada en el paquete núcleo "logging" envía
la salida del *logging* a un *stream* como *sys.stdout*, *sys.stderr*
o cualquier objeto tipo archivo (o mas precisamente cualquier objeto
que soporte los métodos "write()" y "flush()").

class logging.StreamHandler(stream=None)

   Retorna una nueva instancia de la clase "StreamHandler". Si
   *stream* esta especificado, la instancia lo usará para la salida
   del registro, sino se usará *sys.stderr*.

   emit(record)

      Si se especifica un formateador, se utiliza para formatear el
      registro. Luego, el registro se escribe en el flujo seguido de
      "terminator". Si hay información de excepción, se formatea con
      "traceback.print_exception()" y se agrega al flujo.

   flush()

      Descarga el *stream* llamando a su método "flush()". Nota que el
      método "close()" es heredado de la clase "Handler" y por lo
      tanto no produce ninguna salida. Por eso muchas veces será
      necesario invocar al método explícito "flush()".

   setStream(stream)

      Establece el *stream* de la instancia a un valor especifico, si
      este es diferente. El anterior *stream* es vaciado antes de que
      el nuevo *stream* sea establecido.

      Parámetros:
         **stream** -- El *stream* que el gestor debe usar.

      Devuelve:
         the old stream, if the stream was changed, or "None" if it
         wasn't.

      Added in version 3.7.

   terminator

      Cadena utilizada como terminador al escribir un registro
      formateado en un flujo. El valor por defecto es "'\n'".

      Si no quieres una terminación de nueva línea, puedes establecer
      el atributo "terminator" de la instancia del manejador a la
      cadena vacía.

      En versiones anteriores, el terminador estaba codificado como
      "'\n'".

      Added in version 3.2.

## FileHandler

La clase "FileHandler" está localizada en el paquete núcleo "logging",
envía la salida del *logging* a un archivo de disco. Hereda la
funcionalidad de salida de la clase "StreamHandler".

class logging.FileHandler(filename, mode='a', encoding=None, delay=False, errors=None)

   Retorna una nueva instancia de la clase "FileHandler". El archivo
   especificado se abre y se utiliza como flujo para el registro. Si
   no se especifica *mode*, se utiliza "'a'". Si *encoding* no es
   "None", se utiliza para abrir el archivo con esa codificación. Si
   *delay* es verdadero, la apertura del archivo se pospone hasta la
   primera llamada a "emit()". Por defecto, el archivo crece de manera
   indefinida. Si se especifica *errors*, se usa para determinar cómo
   se manejan los errores de codificación.

   Distinto en la versión 3.6: Así como valores de cadena de
   caracteres, también se aceptan objetos de la clase "Path" para el
   argumento "*filename*".

   Distinto en la versión 3.9: Se agregó el parámetro *errors*.

   close()

      Cierra el archivo.

   emit(record)

      Da la salida del registro al archivo.

      Ten en cuenta que si el archivo se cerró debido al apagado del
      registro al salir y el modo de archivo es 'w', el registro no se
      emitirá (consulta bpo-42378).

## NullHandler

Added in version 3.1.

La clase "NullHandler" está ubicada en el núcleo biblioteca "logging"
. No realiza ningún formateo o salida. Es en esencia un gestor 'no-op'
para uso de desarrolladores de bibliotecas.

class logging.NullHandler

   Retorna una nueva instancia de la clase "NullHandler".

   emit(record)

      Este método no realiza ninguna acción.

   handle(record)

      Este método no realiza ninguna acción.

   createLock()

      Este método retorna "None" para el bloqueo , dado que no hay una
      E/S subyacente cuyo acceso se necesite serializar.

Véase Configurando Logging para una biblioteca para mas información en
como usar la clase "NullHandler".

## WatchedFileHandler

The "WatchedFileHandler" class, located in the "logging.handlers"
module, is a "FileHandler" which watches the file it is logging to. If
the file changes, it is closed and reopened using the file name.

Puede suceder que haya un cambio de archivo por uso de programas como
*newsyslog* y *logrotate* que realizan una rotación del archivo log.
Este gestor destinado para uso bajo Unix/Linux controla el archivo
para ver si hubo cambios desde la última emisión. (Un archivo se
considera que cambió si su dispositivo o nodo índice cambió). Si el
archivo cambió entonces el anterior *stream* de archivo se cerrará, y
se abrirá el nuevo para obtener un nuevo *stream*.

Este gestor no es apropiado para uso bajo Windows porque bajo Windows
los archivos log abiertos no se pueden mover o renombrar. *Logging*
abre los archivos con bloqueos exclusivos y entonces no hay necesidad
de usar el gestor. Por otra parte *ST_INO* no es soportado bajo
Windows. La función "stat()" siempre retorna cero para este valor.

class logging.handlers.WatchedFileHandler(filename, mode='a', encoding=None, delay=False, errors=None)

   Retorna una nueva instancia de la clase "WatchedFileHandler". El
   archivo especificado se abre y se utiliza como flujo para el
   registro. Si no se especifica *mode*, se utiliza "'a'". Si
   *encoding* no es "None", se utiliza para abrir el archivo con esa
   codificación. Si *delay* es verdadero, la apertura del archivo se
   pospone hasta la primera llamada a "emit()". Por defecto, el
   archivo crece de manera indefinida. Si se proporciona *errors*,
   determina cómo se manejan los errores de codificación.

   Distinto en la versión 3.6: Así como valores de cadena de
   caracteres, también se aceptan objetos de la clase "Path" para el
   argumento "*filename*".

   Distinto en la versión 3.9: Se agregó el parámetro *errors*.

   reopenIfNeeded()

      Revisa si el archivo cambió. Si hubo cambio, el *stream*
      existente se vacía y cierra y el archivo se abre nuevamente.
      Típicamente es un precursor para dar salida del registro a un
      archivo.

      Added in version 3.6.

   emit(record)

      Da salida al registro a un archivo, pero primero invoca al
      método "reopenIfNeeded()" para reabrir el archivo si es que
      cambió.

## BaseRotatingHandler

The "BaseRotatingHandler" class, located in the "logging.handlers"
module, is the base class for the rotating file handlers,
"RotatingFileHandler" and "TimedRotatingFileHandler". You should not
need to instantiate this class, but it has attributes and methods you
may need to override.

class logging.handlers.BaseRotatingHandler(filename, mode, encoding=None, delay=False, errors=None)

   Los parámetros son como los de la clase "FileHandler". Los
   atributos son:

   namer

      Si este atributo se establece como invocable, el método
      "rotation_filename()" delega a este invocable. Los parámetros
      pasados al invocable son aquellos pasados al método
      "rotation_filename()".

      Nota:

        La función de nombrado es invocada unas cuantas veces durante
        el volcado (*rollover*) , entonces debe ser tan simple y
        rápida como sea posible. Debe también retornar siempre la
        misma salida para una misma entrada, de otra manera el volcado
        puede no funcionar como se espera.También vale la pena señalar
        que se debe tener cuidado al usar un nombrador para conservar
        ciertos atributos en el nombre de archivo que se usan durante
        la rotación. Por ejemplo, "RotatingFileHandler" espera tener
        un conjunto de archivos de registro cuyos nombres contengan
        números enteros sucesivos, para que la rotación funcione como
        se espera, y "TimedRotatingFileHandler" elimina los archivos
        de registro antiguos (según el parámetro "backupCount" pasado
        al inicializador del controlador), determinando los archivos
        más antiguos para eliminar. Para que esto suceda, los nombres
        de los archivos deben poder ordenarse utilizando la parte de
        fecha/hora del nombre del archivo, y un nombrador debe
        respetar esto. (Si se desea un nombrador que no respete este
        esquema, deberá usarse en una subclase de
        "TimedRotatingFileHandler" que anula el método
        "getFilesToDelete()" para encajar con el esquema de
        denominación personalizada.)

      Added in version 3.3.

   rotator

      Si este atributo se estableció como invocable, el método
      "rotate()" delega a este invocable. Los parámetros pasados al
      invocable son aquellos pasados al método "rotate()".

      Added in version 3.3.

   rotation_filename(default_name)

      Modifica el nombre de un archivo log cuando esta rotando.

      Esto esta previsto para que pueda usarse un nombre de archivo
      personalizado.

      La implementación por defecto llama al atributo 'namer' del
      gestor, si este es invocable, pasando el nombre por defecto a
      él. Si el atributo no es invocable (por defecto es "None") el
      nombre se retorna sin cambios.

      Parámetros:
         **default_name** -- El nombre por defecto para el archivo de
         log.

      Added in version 3.3.

   rotate(source, dest)

      Cuando está rotando, rotar el actual log.

      La implementación por defecto llama al atributo 'rotator' del
      gestor, si es invocable, pasando los argumentos de origen y
      destino a él. Si no se puede invocar (porque el atributo por
      defecto es 'None') el origen es simplemente renombrado al
      destino.

      Parámetros:
         * **source** -- El nombre de archivo origen . Normalmente el
           nombre de archivo base, por ejemplo 'test.log'.

         * **dest** -- El nombre de archivo de destino. Normalmente es
           el nombre al que se rota el archivo origen por ejemplo
           'test.log.1'.

      Added in version 3.3.

La razón de que existen los atributos es para evitar tener que usar
una subclase - puedes usar los mismos invocadores para instancias de
clase "RotatingFileHandler" y "TimedRotatingFileHandler". Si el
rotador invocable o la función de nombrado plantean una excepción esta
se manejará de la misma manera que cualquier otra excepción durante
una llamada al método "emit()" por ejemplo a través del método
"handleError()" del gestor.

Si necesitas hacer cambios mas significativos al proceso de rotación
puedes obviar los métodos.

Para un ejemplo véase Usar un rotador y un nombre para personalizar el
procesamiento de rotación de log.

## RotatingFileHandler

The "RotatingFileHandler" class, located in the "logging.handlers"
module, supports rotation of disk log files.

class logging.handlers.RotatingFileHandler(filename, mode='a', maxBytes=0, backupCount=0, encoding=None, delay=False, errors=None)

   Retorna una nueva instancia de la clase "RotatingFileHandler". El
   archivo especificado se abre y se utiliza como flujo para el
   registro. Si no se especifica *mode*, se utiliza "'a'". Si
   *encoding* no es "None", se utiliza para abrir el archivo con esa
   codificación. Si *delay* es verdadero, la apertura del archivo se
   aplaza hasta la primera llamada a "emit()". De forma
   predeterminada, el archivo crece indefinidamente. Si se proporciona
   *errors*, determina cómo se manejan los errores de codificación.

   Se pueden usar los valores *maxBytes* y *backupCount* para permitir
   que el archivo *rollover* tenga un tamaño predeterminado. Cuando el
   tamaño del archivo está a punto de excederse, se cerrará y un nuevo
   archivo se abrirá silenciosamente para salida. El volcado
   (*rollover*) ocurre cada vez que el actual archivo log esta cerca
   de *maxBytes* en tamaño , pero si cualquiera *maxBytes* o
   *backupCount* es cero, el volcado (*rollover*) no ocurre. Por eso
   generalmente necesitas establecer *backupCount* por lo menos en 1 y
   no tener cero en *maxBytes*. Cuando *backupCount* no es cero, el
   sistema guardará los anteriores archivos log agregando las
   extensiones '.1', '.2' etc. al nombre del archivo. Por ejemplo con
   un *backupCount* de 5 y un nombre de archivo base de "app.log",
   tendrás como nombre de archivo t "app.log", "app.log.1",
   "app.log.2", hasta "app.log.5". El archivo que esta siendo escrito
   es siempre "app.log". Cuando este se completa , se cierra y se
   renombra a "app.log.1" y si ya existen "app.log.1", "app.log.2",
   etc. Entonces se renombrará como "app.log.2", "app.log.3" etc.
   respectivamente.

   Distinto en la versión 3.6: Así como valores de cadena de
   caracteres, también se aceptan objetos de la clase "Path" para el
   argumento "*filename*".

   Distinto en la versión 3.9: Se agregó el parámetro *errors*.

   doRollover()

      Realiza un volcado (*rollover*) como se describe arriba.

   emit(record)

      Da la salida del registro al archivo , dando suministro para el
      volcado (*rollover*) como está descripto anteriormente.

   shouldRollover(record)

      See if the supplied record would cause the file to exceed the
      configured size limit.

## TimedRotatingFileHandler

The "TimedRotatingFileHandler" class, located in the
"logging.handlers" module, supports rotation of disk log files at
certain timed intervals.

class logging.handlers.TimedRotatingFileHandler(filename, when='h', interval=1, backupCount=0, encoding=None, delay=False, utc=False, atTime=None, errors=None)

   Retorna una nueva instancia de la clase "TimedRotatingFileHandler"
   . El archivo especificado es abierto y usado como *stream* para el
   historial de log. En la rotación también establece el sufijo del
   nombre de archivo. La rotación ocurre basada en el producto de
   *when* y *interval*.

   Puedes usar el *when* para especificar el tipo de intervalo
   *interval*. La lista de posibles valores esta debajo. Nota que no
   distingue mayúsculas y minúsculas.

   +------------------+------------------------------+---------------------------+
   | Valor            | Tipo de intervalo            | Si/como *atTime* es usado |
   |==================|==============================|===========================|
   | "'S'"            | Segundos                     | Ignorado                  |
   +------------------+------------------------------+---------------------------+
   | "'M'"            | Minutos                      | Ignorado                  |
   +------------------+------------------------------+---------------------------+
   | "'H'"            | Horas                        | Ignorado                  |
   +------------------+------------------------------+---------------------------+
   | "'D'"            | Días                         | Ignorado                  |
   +------------------+------------------------------+---------------------------+
   | "'W0'-'W6'"      | Día de la semana (0=Lunes)   | Usado para calcular la    |
   |                  |                              | hora inicial del volcado  |
   |                  |                              | *rollover*                |
   +------------------+------------------------------+---------------------------+
   | "'midnight'"     | Volcado (*rollover*) a       | Usado para calcular la    |
   |                  | medianoche , si *atTime* no  | hora inicial del volcado  |
   |                  | está especificado, sino el   | *rollover*                |
   |                  | volcado se hará *atTime*     |                           |
   +------------------+------------------------------+---------------------------+

   Cuando se usa rotación basada en día de la semana, especifica 'W0'
   para Lunes, 'W1' para Martes y así, hasta 'W6' para Domingo. en
   este caso el valor pasado para *Interval* no se usa.

   El sistema guardará los archivos de log anteriores agregándoles
   extensiones al nombre de archivo. Las extensiones están basadas en
   día-hora usando el formato "%Y-%m-%d_%H-%M-%S" o un prefijo
   respecto el intervalo del volcado (*rollover*).

   Cuando se calcula la hora del siguiente volcado (*rollover*) por
   primera vez (cuando el gestor es creado), la última hora de
   modificación de un archivo log existente o sino la hora actual, se
   usa para calcular cuando será la próxima rotación.

   Si el argumento *utc* es *true* se usará la hora en UTC, sino se
   usará la hora local.

   Si *backupCount* no es cero, se conservará como máximo una cantidad
   de archivos especificada en *backupCount*,y si son creados más,
   cuando ocurre el volcado (*rollover*) se borrará el último. La
   lógica de borrado usa el intervalo para determinar que archivos
   borrar, pues entonces cambiando el intervalo puede dejar viejos
   archivos abandonados.

   Si *delay* es *true* entonces la apertura del archivo se demorará
   hasta la primer llamada a "emit()".

   Si *atTime* no es "None", debe haber una instancia "datetime.time"
   que especifica la hora que ocurre el volcado (*rollover*) , para
   los casos en que el volcado esta establecido para ocurrir "a
   medianoche" o "un día en particular". Nótese que en estos casos el
   valor *atTime* se usa para calcular el valor *initial* del volcado
   (*rollover*) y los subsecuentes volcados serán calculados a través
   del calculo normal de intervalos.

   Si se especifica *errors*, se utiliza para determinar cómo se
   manejan los errores de codificación.

   Nota:

     El cálculo de la hora en que se realizara el volcado (*rollover*)
     inicial cuando se inicializa el gestor. El cálculo de la hora de
     los siguientes volcados (*rollovers*) se realiza solo cuando este
     ocurre, y el volcado ocurre solo cuando se emite una salida. Si
     esto no se tiene en cuenta puede generar cierta confusión. Por
     ejemplo si se establece un intervalo de "cada minuto" eso no
     significa que siempre se verán archivos log con hora (en el
     nombre del archivo) separados por un minuto. Si durante la
     ejecución de la aplicación el *logging* se genera con mayor
     frecuencia que un minuto entonces se pueden esperar archivos log
     separados por un minuto. Si por otro lado los mensajes *logging*
     son establecidos cada digamos cinco minutos, entonces habrá
     brechas de tiempo en los archivos correspondientes a los minutos
     que no hubo salida (y no ocurrió por tanto volcado alguno).

   Distinto en la versión 3.4: Se agregó el parámetro *atTime*.

   Distinto en la versión 3.6: Así como valores de cadena de
   caracteres, también se aceptan objetos de la clase "Path" para el
   argumento "*filename*".

   Distinto en la versión 3.9: Se agregó el parámetro *errors*.

   doRollover()

      Realiza un volcado (*rollover*) como se describe arriba.

   emit(record)

      Da la salida del registro a un archivo , proveyendo la
      información para el volcado (*rollover*) como esta descripto
      anteriormente.

   getFilesToDelete()

      Returns a list of filenames which should be deleted as part of
      rollover. These are the absolute paths of the oldest backup log
      files written by the handler.

   shouldRollover(record)

      See if enough time has passed for a rollover to occur and if it
      has, compute the next rollover time.

## SocketHandler

The "SocketHandler" class, located in the "logging.handlers" module,
sends logging output to a network socket. The base class uses a TCP
socket.

class logging.handlers.SocketHandler(host, port)

   Retorna una nueva instancia de la clase "SocketHandler" destinada
   para comunicarse con una terminal remota cuya dirección esta dada
   por *host* y *port*.

   Distinto en la versión 3.4: Si "port" se especifica como "None" se
   crea un socket de dominio Unix, usando el valor en "host" - de otra
   manera se creará un socket TCP.

   close()

      Cierra el socket.

   emit()

      Serializa (*Pickles*) el registro del diccionario de atributos y
      lo escribe en el socket en formato binario. Si hay un error con
      el socket, silenciosamente descarta el paquete. Si la conexión
      se perdió previamente, la restablece. Para deserializar
      (*unpickle*) un registro en el extremo receptor a una clase
      "LogRecord", usa la función "makeLogRecord()".

   handleError()

      Maneja un error que ocurrió durante el método "emit()". La causa
      mas común es una perdida de conexión. Cierra el socket para que
      podamos reintentar en el próximo evento.

   makeSocket()

      Este es un método patrón que permite subclases para definir el
      tipo preciso de socket que se necesita. La implementación por
      defecto crea un socket TCP("socket.SOCK_STREAM").

   makePickle(record)

      Serializa (*pickles*) el registro del diccionario de atributos
      en formato binario con un prefijo de tamaño, y lo retorna listo
      para transmitir a través del socket. Los detalles de esta
      operación son equivalentes a:

         data = pickle.dumps(record_attr_dict, 1)
         datalen = struct.pack('>L', len(data))
         return datalen + data

      Nota que los serializados (*pickles*) no son totalmente seguros.
      Si te preocupa la seguridad desearás evitar este método para
      implementar un mecanismo mas seguro. Por ejemplo puedes firmar
      *pickles* usando HMAC y verificarlos después en el extremo
      receptor. O alternativamente puedes deshabilitar la
      deserialización (*unpickling*) de objetos globales en el extremo
      receptor.

   send(packet)

      Envía un paquete serializado (*pickled*) de cadena de caracteres
      al socket. El formato de la cadena de bytes enviada es tal como
      se describe en la documentación de "makePickle()".

      Esta función permite envíos parciales, que pueden ocurrir cuando
      la red esta ocupada.

   createSocket()

      Intenta crear un socket, si hay una falla usa un algoritmo de
      marcha atrás exponencial. En el fallo inicial el gestor
      desechará el mensaje que intentaba enviar. Cuando los siguientes
      mensajes sean gestionados por la misma instancia no intentará
      conectarse hasta que haya transcurrido cierto tiempo. Los
      parámetros por defecto son tales que el retardo inicial es un
      segundo y si después del retardo la conexión todavía no se puede
      realizar, el gestor doblará el retardo cada vez hasta un máximo
      de 30 segundos.

      Este comportamiento es controlado por los siguientes atributos
      del gestor:

      * "retryStart" (retardo inicial por defecto 1.0 segundos)

      * "retryFactor" (multiplicador por defecto 2.0)

      * "retryMax" (máximo retardo por defecto 30.0 segundos)

      Esto significa que si el oyente remoto (*listener*) comienza
      después de que se usó el gestor , pueden perderse mensajes (dado
      que el gestor no puede siquiera intentar una conexión hasta que
      se haya cumplido el retardo, y silenciosamente desechará los
      mensajes mientras se cumpla el retardo).

## DatagramHandler

The "DatagramHandler" class, located in the "logging.handlers" module,
inherits from "SocketHandler" to support sending logging messages over
UDP sockets.

class logging.handlers.DatagramHandler(host, port)

   Retorna una nueva instancia de la clase "DatagramHandler" destinada
   para comunicarse con la terminal remota cuya dirección es dada por
   *host* y *port*.

   Nota:

     Como UDP no es un protocolo de transmisión, no existe una
     conexión persistente entre una instancia de este controlador y
     *host*. Por esta razón, cuando se usa un socket de red, es
     posible que se deba realizar una búsqueda de DNS cada vez que se
     registra un evento, lo que puede generar cierta latencia en el
     sistema. Si esto te afecta, puedes realizar una búsqueda tu mismo
     e inicializar este controlador utilizando la dirección IP buscada
     en lugar del nombre de host.

   Distinto en la versión 3.4: Si 'port' se especifica como "None", se
   crea un socket de dominio Unix, usando el valor en "host" - de otra
   manera se crea un socket UDP.

   emit()

      Serializa (*pickles*) el registro del diccionario de atributos y
      lo escribe en el socket en formato binario. Si hay un error con
      el socket, silenciosamente desecha el paquete. Para deserializar
      (*unpickle*) el registro en el extremo de recepción a una clase
      "LogRecord", usa la función "makeLogRecord()".

   makeSocket()

      El método original de la clase "SocketHandler" se omite para
      crear un socket UDP ("socket.SOCK_DGRAM").

   send(s)

      Enviar una cadena de caracteres serializada (*pickled*) a un
      socket de red. El formato de la cadena de *bytes* enviado es tal
      como se describe en la documentación para
      "SocketHandler.makePickle()".

## Gestor *SysLog* (*SysLogHandler*)

The "SysLogHandler" class, located in the "logging.handlers" module,
supports sending logging messages to a remote or local Unix syslog.

class logging.handlers.SysLogHandler(address=('localhost', SYSLOG_UDP_PORT), facility=LOG_USER, socktype=socket.SOCK_DGRAM, timeout=None)

   Returns a new instance of the "SysLogHandler" class intended to
   communicate with a remote Unix machine whose address is given by
   *address* in the form of a "(host, port)" tuple.  If *address* is
   not specified, "('localhost', 514)" is used.  The address is used
   to open a socket.  An alternative to providing a "(host, port)"
   tuple is providing an address as a string, for example '/dev/log'.
   In this case, a Unix domain socket is used to send the message to
   the syslog. If *facility* is not specified, "LOG_USER" is used. The
   type of socket opened depends on the *socktype* argument, which
   defaults to "socket.SOCK_DGRAM" and thus opens a UDP socket. To
   open a TCP socket (for use with the newer syslog daemons such as
   rsyslog), specify a value of "socket.SOCK_STREAM". If *timeout* is
   specified, it sets a timeout (in seconds) for the socket
   operations. This can help prevent the program from hanging
   indefinitely if the syslog server is unreachable. By default,
   *timeout* is "None", meaning no timeout is applied.

   Nótese que si el servidor no esta escuchando el puerto UDP 514, la
   clase "SysLogHandler" puede parecer no funcionar. En ese caso
   chequea que dirección deberías usar para un socket de dominio . Es
   sistema-dependiente. Por ejemplo en Linux generalmente es
   '/dev/log' pero en OS/X es '/var/run/syslog'. Será necesario
   chequear tu plataforma y usar la dirección adecuada (quizá sea
   necesario realizar este chequeo mientras corre la aplicación si
   necesita correr en diferentes plataformas). En Windows seguramente
   tengas que usar la opción UDP.

   Nota:

     En macOS 12.x (Monterey), Apple cambió el comportamiento de su
     syslog daemon: ya no escucha en un socket de dominio. Por lo
     tanto, no puedes esperar que "SysLogHandler" funcione en este
     sistema.Ver gh-91070 para más información.

   Distinto en la versión 3.2: Se agregó *socktype*.

   Distinto en la versión 3.14: *timeout* was added.

   close()

      Cierra el socket del host remoto.

   createSocket()

      Tries to create a socket and, if it's not a datagram socket,
      connect it to the other end. This method is called during
      handler initialization, but it's not regarded as an error if the
      other end isn't listening at this point - the method will be
      called again when emitting an event, if there is no socket at
      that point.

      Added in version 3.11.

   emit(record)

      El registro es formateado, y luego enviado al servidor *syslog*.
      Si hay información de excepción presente entonces no se enviará
      al servidor.

      Distinto en la versión 3.2.1: (Véase el bpo-12168.) En versiones
      anteriores , los mensajes enviados a los *daemons syslog*
      siempre terminaban con un byte NUL ya que versiones anteriores
      de estos *daemons* esperaban un mensaje NUL de terminación.
      Incluso a pesar que no es relevante la especificación (**RFC
      5424**). Versiones mas recientes de estos *daemons* no esperan
      el byte NUL pero lo quitan si esta ahí. Versiones aún mas
      recientes que están mas cercanas a la especificación RFC 5424
      pasan el byte NUL como parte del mensaje.Para habilitar una
      gestión mas sencilla de los mensajes *syslog* respecto de todos
      esos *daemons* de diferentes comportamientos el agregado del
      byte NUL es configurable a través del uso del atributo de nivel
      de clase "append_nul". Este es por defecto '"True" (preservando
      el comportamiento ya existente) pero se puede establecer a
      'False' en una instancia "SysLogHandler" como para que esa
      instancia no añada el terminador NUL.

      Distinto en la versión 3.3: (Véase: issue '12419') en versiones
      anteriores, no había posibilidades para un prefijo 'ident' o
      'tag' para identificar el origen del mensaje. Esto ahora se
      puede especificar usando un atributo de nivel de clase, que por
      defecto será "''" para preservar el comportamiento existente ,
      pero puede ser sorteado en una instancia "SysLogHandler" para
      que esta instancia anteponga el *ident* a todos los mensajes
      gestionados. Nótese que el *ident* provisto debe ser texto, no
      bytes y se antepone al mensaje tal como es.

   encodePriority(facility, priority)

      Codifica la funcionalidad y prioridad en un entero. Puedes pasar
      cadenas de caracteres o enteros, si pasas cadenas de caracteres
      se usarán los diccionarios de mapeo interno para convertirlos en
      enteros.

      Los valores simbólicos "LOG_" están definidos en "SysLogHandler"
      e invierten los valores definidos en el archivo de encabezado
      "sys/syslog.h".

      **Prioridades**

      +----------------------------+-----------------+
      | Nombre (cadena de          | Valor simbólico |
      | caracteres)                |                 |
      |============================|=================|
      | "alert"                    | LOG_ALERT       |
      +----------------------------+-----------------+
      | "crit" or "critical"       | LOG_CRIT        |
      +----------------------------+-----------------+
      | "debug"                    | LOG_DEBUG       |
      +----------------------------+-----------------+
      | "emerg" or "panic"         | LOG_EMERG       |
      +----------------------------+-----------------+
      | "err" or "error"           | LOG_ERR         |
      +----------------------------+-----------------+
      | "info"                     | LOG_INFO        |
      +----------------------------+-----------------+
      | "notice"                   | LOG_NOTICE      |
      +----------------------------+-----------------+
      | "warn" o "warning"         | LOG_WARNING     |
      +----------------------------+-----------------+

      **Facilities**

      +-----------------+-----------------+
      | Nombre (cadena  | Valor simbólico |
      | de caracteres)  |                 |
      |=================|=================|
      | "auth"          | LOG_AUTH        |
      +-----------------+-----------------+
      | "authpriv"      | LOG_AUTHPRIV    |
      +-----------------+-----------------+
      | "cron"          | LOG_CRON        |
      +-----------------+-----------------+
      | "daemon"        | LOG_DAEMON      |
      +-----------------+-----------------+
      | "ftp"           | LOG_FTP         |
      +-----------------+-----------------+
      | "kern"          | LOG_KERN        |
      +-----------------+-----------------+
      | "lpr"           | LOG_LPR         |
      +-----------------+-----------------+
      | "mail"          | LOG_MAIL        |
      +-----------------+-----------------+
      | "news"          | LOG_NEWS        |
      +-----------------+-----------------+
      | "syslog"        | LOG_SYSLOG      |
      +-----------------+-----------------+
      | "user"          | LOG_USER        |
      +-----------------+-----------------+
      | "uucp"          | LOG_UUCP        |
      +-----------------+-----------------+
      | "local0"        | LOG_LOCAL0      |
      +-----------------+-----------------+
      | "local1"        | LOG_LOCAL1      |
      +-----------------+-----------------+
      | "local2"        | LOG_LOCAL2      |
      +-----------------+-----------------+
      | "local3"        | LOG_LOCAL3      |
      +-----------------+-----------------+
      | "local4"        | LOG_LOCAL4      |
      +-----------------+-----------------+
      | "local5"        | LOG_LOCAL5      |
      +-----------------+-----------------+
      | "local6"        | LOG_LOCAL6      |
      +-----------------+-----------------+
      | "local7"        | LOG_LOCAL7      |
      +-----------------+-----------------+

   mapPriority(levelname)

      Mapea un nombre de nivel *logging* a un nombre de prioridad
      *syslog*. Puedes necesitar omitir esto si estas usando niveles
      personalizados, o si el algoritmo por defecto no es aplicable a
      tus necesidades. El algoritmo por defecto mapea "DEBUG", "INFO",
      "WARNING", "ERROR" y "CRITICAL" a sus nombres equivalentes
      *syslog*, y todos los demás nombres de nivel a 'warning'.

## Gestor de eventos *NTELog* (NTEventLogHandler)

The "NTEventLogHandler" class, located in the "logging.handlers"
module, supports sending logging messages to a local Windows NT,
Windows 2000 or Windows XP event log. Before you can use it, you need
Mark Hammond's Win32 extensions for Python installed.

class logging.handlers.NTEventLogHandler(appname, dllname=None, logtype='Application')

   Retorna una nueva instancia de la clase "NTEventLogHandler" la
   *appname* se usa para definir el nombre de la aplicación tal como
   aparece en el log de eventos. Se crea una entrada de registro
   apropiada usando este nombre. El *dllname* debe dar la ruta
   completa calificada de un .dll o .exe que contiene definiciones de
   mensaje para conservar en el log. (si no esta especificada, se
   usara "'win32service.pyd'" esto es instalado con las extensiones de
   Win32 y contiene algunas definiciones básicas de mensajes de
   conservación de lugar. Nótese que el uso de estos conservadores de
   lugar harán tu log de eventos extenso, dado que el origen completo
   del mensaje es guardado en el log. Si quieres *logs* menos extensos
   deberás pasar el nombre de tu propio .dll o .exe que contiene la
   definición de mensajes que quieres usar en el log. El *logtype*
   puede ser de "'Application'", "'System'" or "'Security'" y sino por
   defecto será de "'Application'".

   close()

      Llegado a este punto puedes remover el nombre de aplicación del
      registro como origen de entrada de log de eventos. Sin embargo
      si haces esto no te será posible ver los eventos tal como has
      propuesto en el visor del log de eventos - necesita ser capaz de
      acceder al registro para tomar el nombre .dll. Esto no lo hace
      la versión actual.

   emit(record)

      Determina el ID del mensaje, categoría y tipo de evento y luego
      registra el mensaje en el log de eventos NT.

   getEventCategory(record)

      Retorna la categoría de evento del registro. Evita esto si
      quieres especificar tus propias categorías. Esta versión retorna
      0.

   getEventType(record)

      Retorna el tipo de evento del registro. Haz caso omiso de esto
      si quieres especificar tus propios tipos. Esta versión realiza
      un mapeo usando el atributo *typemap* del gestor, que se
      establece en "__init__()" a un diccionario que contiene mapeo
      para "DEBUG", "INFO", "WARNING", "ERROR" y "CRITICAL". Si estas
      usando tus propios niveles, necesitarás omitir este método o
      colocar un diccionario a medida en el atributo *typemap* del
      gestor.

   getMessageID(record)

      Retorna el ID de mensaje para el registro. Si estas usando tus
      propios mensajes, podrás hacerlo pasando el *msg* al *logger*
      siendo un ID mas que un formato de cadena de caracteres. Luego
      aquí puedes usar una búsqueda de diccionario para obtener el ID
      de mensaje. Esta versión retorna 1, que es el ID de mensaje base
      en "win32service.pyd".

## SMTPHandler

The "SMTPHandler" class, located in the "logging.handlers" module,
supports sending logging messages to an email address via SMTP.

class logging.handlers.SMTPHandler(mailhost, fromaddr, toaddrs, subject, credentials=None, secure=None, timeout=1.0)

   Retorna una nueva instancia de la clase "SMTPHandler" . Esta
   instancia se inicializa con la dirección de: y para: y asunto: del
   correo electrónico. El *toaddrs* debe ser una lista de cadena de
   caracteres. Para especificar un puerto SMTP no estandarizado usa el
   formato de tupla (host, puerto) para el argumento *mailhost*. Si
   usas una cadena de caracteres, se utiliza el puerto estándar SMTP.
   Si tu servidor SMTP necesita autenticación, puedes especificar una
   tupla (usuario, contraseña) para el argumento de *credentials*.

   Para especificar el uso de un protocolo de seguridad (TLS), pasa
   una tupla al argumento *secure*. Esto solo se utilizará cuando sean
   provistas las credenciales de autenticación. La tupla deberá ser
   una tupla vacía o una tupla con único valor con el nombre de un
   archivo-clave *keyfile*, o una tupla de 2 valores con el nombre del
   archivo-clave *keyfile* y archivo certificado. (Esta tupla se pasa
   al método "smtplib.SMTP.starttls()" method.).

   Se puede especificar un tiempo de espera para comunicación con el
   servidor SMTP usando el argumento *timeout*.

   Distinto en la versión 3.3: Added the *timeout* parameter.

   emit(record)

      Formatea el registro y lo envía a las direcciones especificadas.

   getSubject(record)

      Si quieres especificar una línea de argumento que es registro-
      dependiente, sobrescribe (*override*) este método.

## MemoryHandler

The "MemoryHandler" class, located in the "logging.handlers" module,
supports buffering of logging records in memory, periodically flushing
them to a *target* handler. Flushing occurs whenever the buffer is
full, or when an event of a certain severity or greater is seen.

"MemoryHandler" es una subclase de la clase mas general
"BufferingHandler", que es una clase abstracta. Este almacena
temporalmente registros *logging* en la memoria. Cada vez que un
registro es agregado al búfer, se realiza una comprobación llamando al
método "shouldFlush()" para ver si dicho búfer debe ser descargado. Si
debiera, entonces el método "flush()" se espera que realice la
descarga.

class logging.handlers.BufferingHandler(capacity)

   Inicializa el gestor con un búfer de una capacidad especifica. Aquí
   capacidad significa el número de registros *logging* en el
   almacenamiento temporal.

   emit(record)

      Añade un registro al búfer. Si el método "shouldFlush()" retorna
      *true* , entonces llama al método "flush()" para procesar el
      búfer.

   flush()

      Para una instancia de "BufferingHandler", vaciar significa que
      establece el búfer a una lista vacía. Este método puede ser
      sobrescrito para implementar un comportamiento de vaciado más
      útil.

   shouldFlush(record)

      Retorna "True" si el búfer tiene aún capacidad. Este método
      puede ser omitido para implementar estrategias a medida de
      vaciado.

class logging.handlers.MemoryHandler(capacity, flushLevel=ERROR, target=None, flushOnClose=True)

   Retorna una nueva instancia de la clase "MemoryHandler" . La
   instancia se inicializa con un búfer del tamaño *capacity*. Si el
   *flushLevel* no se especifica, se usará "ERROR" . Si no se
   especifica *target* el objetivo deberá especificarse usando el
   método "setTarget()" -Antes de esto el gestor no realizará nada
   útil. Si se especifica *flushOnClose* como "False", entonces el
   búfer no se vaciará cuando el gestor se cierra. Si no se especifica
   o se especifica como "True", el comportamiento previo de vaciado
   del búfer sucederá cuando se cierre el gestor.

   Distinto en la versión 3.6: Se añadió el parámetro *flushOnClose*.

   close()

      Invoca al método "flush()" y establece el objetivo a 'None' y
      vacía el búfer.

   flush()

      Para una instancia de "MemoryHandler", el vaciado implica
      simplemente enviar los registros almacenados en el búfer al
      objetivo, si es que existe uno. El búfer también se limpia
      cuando se envían los registros almacenados al objetivo.
      Sobrescribe si deseas un comportamiento diferente.

   setTarget(target)

      Establece el gestor de objetivo para este gestor.

   shouldFlush(record)

      Comprueba si el búfer esta lleno o un registro igual o mas alto
      que *flushLevel*.

## HTTPHandler

The "HTTPHandler" class, located in the "logging.handlers" module,
supports sending logging messages to a web server, using either "GET"
or "POST" semantics.

class logging.handlers.HTTPHandler(host, url, method='GET', secure=False, credentials=None, context=None)

   Retorna una nueva instancia de la clase "HTTPHandler". el *host*
   puede ser de la forma "host:puerto", y necesitarás usar un numero
   de puerto especifico. Si no se especifica *method* se usará "GET" .
   Si *secure* es true se usará una conexión HTTPS. El parámetro
   *context* puede establecerse a una instancia "ssl.SSLContext" para
   establecer la configuración de SSL usado en la conexión HTTPS. Si
   se especifica *credentials* debe ser una tupla doble, consistente
   en usuario y contraseña, que se colocará en un encabezado de
   autorización HTTP usando autenticación básica. Si especificas
   credenciales también deberás especificar *secure=True* así tu
   usuario y contraseña no son pasados como texto en blanco por la
   conexión.

   Distinto en la versión 3.5: Se agregó el parámetro *context*.

   mapLogRecord(record)

      Provee un diccionario, basado en "record" para ser codificado en
      forma URL y enviado al servidor web. La implementación por
      defecto retorna "record.__dict__". Este método puede omitirse si
      por ejemplo solo se enviará al servidor web un subconjunto de la
      clase "LogRecord" o si se requiere enviar al servidor algo mas
      específico.

   emit(record)

      Envía el registro al servidor web como un diccionario codificado
      en URL. El método "mapLogRecord()" se utiliza para convertir el
      registro al diccionario que se enviará.

   Nota:

     Dado que preparar un registro para enviarlo a un servidor web no
     es lo mismo que una operación de formateo genérico, el uso de
     "setFormatter()" para especificar un "Formatter" para un
     "HTTPHandler" no tiene ningún efecto. En lugar de llamar a
     "format()", este controlador llama a "mapLogRecord()" y luego a
     "urllib.parse.urlencode()" para codificar el diccionario en una
     forma adecuada para enviar a un servidor web.

## QueueHandler

Added in version 3.2.

The "QueueHandler" class, located in the "logging.handlers" module,
supports sending logging messages to a queue, such as those
implemented in the "queue" or "multiprocessing" modules.

Junto con la clase "QueueListener", "QueueHandler" se puede usar para
permitir que los controladores hagan su trabajo en un hilo separado
del que realiza el registro. Esto es importante en aplicaciones web y
también en otras aplicaciones de servicio donde los subprocesos que
atienden a los clientes deben responder lo más rápido posible,
mientras que cualquier operación potencialmente lenta (como enviar un
correo electrónico a través de "SMTPHandler") se realiza en un
subproceso separado.

class logging.handlers.QueueHandler(queue)

   Retorna una nueva instancia de la clase "QueueHandler". La
   instancia se inicializa con la cola a la que se enviarán los
   mensajes. La cola puede ser cualquier objeto tipo-cola; es usado
   tal como por el método "enqueue()" que necesita saber como enviar
   los mensajes a ella. La cola no es *requerida* para tener una API
   de rastreo de tareas, lo que significa que puedes usar instancias
   de "SimpleQueue" como *queue*.

   Nota:

     Si estás usando "multiprocessing", debes evitar usar
     "SimpleQueue" y en su lugar usar "multiprocessing.Queue".

   Advertencia:

     The "multiprocessing" module uses an internal logger created and
     accessed via "get_logger()". "multiprocessing.Queue" will log
     "DEBUG" level messages upon items being queued. If those log
     messages are processed by a "QueueHandler" using the same
     "multiprocessing.Queue" instance, it will cause a deadlock or
     infinite recursion.

   emit(record)

      Pone en cola el resultado de preparar el LogRecord. Si ocurre
      una excepción (por ejemplo, porque una cola limitada se ha
      llenado), se invoca el método "handleError()" para manejar el
      error. Esto puede resultar en que el registro se descarte de
      manera silenciosa (si "logging.raiseExceptions" es "False") o en
      que se imprima un mensaje en "sys.stderr" (si
      "logging.raiseExceptions" es "True").

   prepare(record)

      Prepara un registro para poner en la cola. El objeto que retorna
      este método se colocará en cola.

      La implementación base le da formato al registro para fusionar
      el mensaje, los argumentos, la excepción y la información de la
      pila, si está presente. También elimina elementos que no se
      pueden serializar (*pickle*) del registro en el lugar.
      Específicamente, sobrescribe los atributos "msg" y "message" del
      registro con el mensaje fusionado (obtenido llamando al método
      "format()" del controlador) y establece los atributos "args",
      "exc_info" y "exc_text" a "None".

      Puedes querer hacer caso omiso de este método si quieres
      convertir el registro en un diccionario o cadena de caracteres
      JSON, o enviar una copia modificada del registro mientras dejas
      el original intacto.

      Nota:

        La implementación base formatea el mensaje con argumentos,
        establece los atributos "message" y "msg" en el mensaje
        formateado y establece los atributos "args" y "exc_text" en
        "None" para permitir serializado (*pickle*) y para evitar
        nuevos intentos de formateo. Esto significa que un controlador
        en el lado "QueueListener" no tendrá la información para hacer
        un formato personalizado, por ej. de excepciones. Es posible
        que desees crear una subclase de "QueueHandler" y anular este
        método para, por ej. evitar establecer "exc_text" en "None".
        Ten en cuenta que los cambios de "message" / "msg" / "args"
        están relacionados con garantizar que el registro se pueda
        seleccionar, y es posible que puedas o no evitar hacerlo
        dependiendo de si sus "args" son serializables. (Ten en cuenta
        que es posible que debas considerar no solo tu propio código,
        sino también el código en cualquier biblioteca que uses).

   enqueue(record)

      Coloca en la cola al registro usando "put_nowait()"; puede que
      quieras sobrescribe (*override*) esto si quieres usar una acción
      de bloqueo, o un tiempo de espera, o una implementación de cola
      a medida.

   listener

      Cuando se crea a través de la configuración usando
      "dictConfig()", este atributo contendrá una instancia de
      "QueueListener" para usar con este manejador. De lo contrario,
      será "None".

      Added in version 3.12.

## QueueListener

Added in version 3.2.

The "QueueListener" class, located in the "logging.handlers" module,
supports receiving logging messages from a queue, such as those
implemented in the "queue" or "multiprocessing" modules. The messages
are received from a queue in an internal thread and passed, on the
same thread, to one or more handlers for processing. While
"QueueListener" is not itself a handler, it is documented here because
it works hand-in-hand with "QueueHandler".

Junto con la clase "QueueHandler", "QueueListener" se puede usar para
permitir que los controladores hagan su trabajo en un hilo separado
del que realiza el registro. Esto es importante en aplicaciones web y
también en otras aplicaciones de servicio donde los subprocesos que
atienden a los clientes deben responder lo más rápido posible,
mientras que cualquier operación potencialmente lenta (como enviar un
correo electrónico a través de "SMTPHandler") se realiza en un
subproceso separado.

class logging.handlers.QueueListener(queue, *handlers, respect_handler_level=False)

   Retorna una nueva instancia de la clase "QueueListener". La
   instancia se inicializa con la cola para enviar mensajes a una
   lista de gestores que manejarán entradas colocadas en la cola. La
   cola puede ser cualquier objeto de tipo-cola, es usado tal como
   está por el método "dequeue()" que necesita saber como tomar los
   mensajes de esta. La cola no es *obligatoria* para tener la API de
   seguimiento de tareas (aunque se usa si está disponible), lo que
   significa que puede usar instancias "SimpleQueue" para *queue*.

   Nota:

     Si estás usando "multiprocessing", debes evitar usar
     "SimpleQueue" y en su lugar usar "multiprocessing.Queue".

   Si "respect_handler_level" es "True", se respeta un nivel de gestor
   (comparado con el nivel del mensaje) cuando decide si pasar el
   mensajes al gestor; de otra manera, el comportamiento es como en
   versiones anteriores de Python - de pasar cada mensaje a cada
   gestor.

   Distinto en la versión 3.5: Se agregó el argumento
   "respect_handler_levels".

   Distinto en la versión 3.14: "QueueListener" can now be used as a
   context manager via "with". When entering the context, the listener
   is started. When exiting the context, the listener is stopped.
   "__enter__()" returns the "QueueListener" object.

   dequeue(block)

      Extrae de la cola un registro y lo retorna, con opción a
      bloquearlo.

      La implementación base usa "get()". Puedes sobrescribir
      (*override*) este método si quieres usar tiempos de espera o
      trabajar con colas implementadas a medida.

   prepare(record)

      Prepara un registro para ser gestionado.

      Esta implementación solo retorna el registro que fue pasado.
      Puedes sobrescribir (*override*) este método para hacer una
      serialización a medida o una manipulación del registro antes de
      pasarlo a los gestores.

   handle(record)

      Manejar un registro.

      Esto solo realiza un bucle a través de los gestores
      ofreciéndoles el registro para ser gestionado. El objeto actual
      pasado a los gestores es aquel que es retornado por el método
      "prepare()".

   start()

      Da comienzo al oyente (*listener*).

      Esto da comienzo a un hilo en segundo plano para supervisar la
      cola de registros log a procesar.

      Distinto en la versión 3.14: Raises "RuntimeError" if called and
      the listener is already running.

   stop()

      Detiene el oyente (*listener*).

      Esto solicita terminar al hilo, y luego espera hasta que
      termine. Nota que si no llamas a esto antes de que tu aplicación
      salga, puede haber algunos registros que aun están en la cola,
      que no serán procesados.

   enqueue_sentinel()

      Escribe un centinela (*sentinel*) en la cola para decir al
      oyente (*listener*) de salir. Esta implementación usa
      "put_nowait()". Puedes sobrescribir (*override*) este método si
      quieres usar tiempos de espera o trabajar con implementaciones
      de cola a tu medida.

      Added in version 3.3.

Ver también:

  Módulo "logging"
     Referencia API para el módulo de *logging*.

  Módulo "logging.config"
     Configuración API para el módulo de *logging*.
