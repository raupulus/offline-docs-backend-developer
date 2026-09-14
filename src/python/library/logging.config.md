---
title: '"logging.config" --- Logging configuration'
source_url: https://docs.python.org/es/3
source_path: library/logging.config.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 3120
---

# "logging.config" --- Logging configuration

**Código fuente:** Lib/logging/config.py

##### Important

Esta página solo contiene información de referencia. Para tutoriales,
por favor consulte

* Tutorial Básico

* Tutorial Avanzado

* Guía de registro *Logging*

======================================================================

Esta sección describe la API para configurar el módulo de registro.

## Funciones de configuración

The following functions configure the logging module. They are located
in the "logging.config" module.  Their use is optional --- you can
configure the logging module using these functions or by making calls
to the main API (defined in "logging" itself) and defining handlers
which are declared either in "logging" or "logging.handlers".

logging.config.dictConfig(config)

   Toma la configuración de registro de un diccionario.  Los
   contenidos de este diccionario se describen en Esquema del
   diccionario de configuración a continuación.

   Si se encuentra un error durante la configuración, esta función
   lanzará un "ValueError", "TypeError", "AttributeError" o
   "ImportError" con un mensaje descriptivo adecuado.  La siguiente es
   una lista (posiblemente incompleta) de condiciones que lanzarán un
   error:

   * Un "level" que no es una cadena o que es una cadena que no
     corresponde a un nivel de registro real.

   * Un valor de "propagate" que no es booleano.

   * Una identificación que no tiene un destino correspondiente.

   * Una identificación de gestor inexistente encontrada durante una
     llamada incremental.

   * Un nombre de registrador no válido.

   * Incapacidad para resolver un objeto interno o externo.

   Parsing is performed by the "DictConfigurator" class, whose
   constructor is passed the dictionary used for configuration, and
   has a "configure()" method.  The "logging.config" module has a
   callable attribute "dictConfigClass" which is initially set to
   "DictConfigurator". You can replace the value of "dictConfigClass"
   with a suitable implementation of your own.

   "dictConfig()" llama "dictConfigClass" pasando el diccionario
   especificado, y luego llama al método "configure()" en el objeto
   retornado para que la configuración surta efecto:

      def dictConfig(config):
          dictConfigClass(config).configure()

   For example, a subclass of "DictConfigurator" could call
   "DictConfigurator.__init__()" in its own "__init__()", then set up
   custom prefixes which would be usable in the subsequent
   "configure()" call. "dictConfigClass" would be bound to this new
   subclass, and then "dictConfig()" could be called exactly as in the
   default, uncustomized state.

   Added in version 3.2.

logging.config.fileConfig(fname, defaults=None, disable_existing_loggers=True, encoding=None)

   Lee la configuración de registro desde un archivo de formato de
   "configparser". El formato del archivo debe ser como se describe en
   Formato de archivo de configuración. Esta función se puede invocar
   varias veces desde una aplicación, lo que permite al usuario final
   seleccionar entre varias configuraciones predeterminadas (si el
   desarrollador proporciona un mecanismo para presentar las opciones
   y cargar la configuración elegida).

   It will raise "FileNotFoundError" if the file doesn't exist and
   "RuntimeError" if the file is invalid or empty.

   Parámetros:
      * **fname** -- A filename, or a file-like object, or an instance
        derived from "RawConfigParser". If a "RawConfigParser"-derived
        instance is passed, it is used as is. Otherwise, a
        "ConfigParser" is instantiated, and the configuration read by
        it from the object passed in "fname". If that has a
        "readline()" method, it is assumed to be a file-like object
        and read using "read_file()"; otherwise, it is assumed to be a
        filename and passed to "read()".

      * **defaults** -- Defaults to be passed to the "ConfigParser"
        can be specified in this argument.

      * **disable_existing_loggers** -- If specified as "False",
        loggers which exist when this call is made are left enabled.
        The default is "True" because this enables old behaviour in a
        backward-compatible way. This behaviour is to disable any
        existing non-root loggers unless they or their ancestors are
        explicitly named in the logging configuration.

      * **encoding** -- La codificación que se usa para abrir archivos
        cuando *fname* es nombre del archivo.

   Distinto en la versión 3.4: Una instancia de una subclase de
   "RawConfigParser"  ahora se acepta como un valor para "fname". Esto
   facilita:

      * Uso de un archivo de configuración donde la configuración de
        registro es solo parte de la configuración general de la
        aplicación.

      * Uso de una configuración leída de un archivo, y luego
        modificada por la aplicación que lo usa (por ejemplo, basada
        en parámetros de línea de comandos u otros aspectos del
        entorno de ejecución) antes de pasar a "fileConfig".

   Distinto en la versión 3.10: Added the *encoding* parameter.

   Distinto en la versión 3.12: An exception will be thrown if the
   provided file doesn't exist or is invalid or empty.

logging.config.listen(port=DEFAULT_LOGGING_CONFIG_PORT, verify=None)

   Inicia un servidor de socket en el puerto especificado y escucha
   nuevas configuraciones. Si no se especifica ningún puerto, se usa
   el valor predeterminado del módulo "DEFAULT_LOGGING_CONFIG_PORT".
   Las configuraciones de registro se enviarán como un archivo
   adecuado para su procesamiento por "dictConfig()" o "fileConfig()".
   Retorna una instancia de "Thread" en la que puede llamar "start()"
   para iniciar el servidor, y que puede "join()" cuando corresponda .
   Para detener el servidor, llame a "stopListening()".

   El argumento "verify", si se especifica, debe ser invocable, lo que
   debería verificar si los bytes recibidos en el socket son válidos y
   deben procesarse. Esto podría hacerse encriptando y / o firmando lo
   que se envía a través del socket, de modo que el "verify" invocable
   pueda realizar la verificación o descifrado de la firma. El llamado
   invocable "verify" se llama con un solo argumento (los bytes
   recibidos a través del socket) y debe retornar los bytes a
   procesar, o "None" para indicar que los bytes deben descartarse.
   Los bytes retornados podrían ser los mismos que los pasados en
   bytes (por ejemplo, cuando solo se realiza la verificación), o
   podrían ser completamente diferentes (tal vez si se realizó el
   descifrado).

   Para enviar una configuración al socket, lea el archivo de
   configuración y envíelo al socket como una secuencia de bytes
   precedida por una cadena de longitud de cuatro bytes empaquetada en
   binario usando "struct.pack('>L', n)".

   Nota:

     Debido a que partes de la configuración se pasan a través de
     "eval()", el uso de esta función puede abrir a sus usuarios a un
     riesgo de seguridad. Si bien la función solo se une a un socket
     en "localhost" y, por lo tanto, no acepta conexiones de máquinas
     remotas, hay escenarios en los que se puede ejecutar código no
     confiable bajo la cuenta del proceso que llama "listen()".
     Específicamente, si el proceso que llama "listen()" se ejecuta en
     una máquina multiusuario donde los usuarios no pueden confiar el
     uno en el otro, entonces un usuario malintencionado podría hacer
     arreglos para ejecutar código esencialmente arbitrario en el
     proceso del usuario víctima, simplemente conectándose al socket
     "listen()" de la víctima y enviando una configuración que ejecuta
     cualquier código que el atacante quiera ejecutar en el proceso de
     la víctima. Esto es especialmente fácil de hacer si se usa el
     puerto predeterminado, pero no es difícil incluso si se usa un
     puerto diferente. Para evitar el riesgo de que esto suceda, use
     el argumento "verify" para "listen()" para escuchar y evitar que
     se apliquen configuraciones no reconocidas.

   Distinto en la versión 3.4: Se agregó el argumento "verify".

   Nota:

     Si desea enviar configuraciones al oyente que no deshabiliten los
     registradores existentes, deberá usar un formato JSON para la
     configuración, que utilizará "dictConfig()" para la
     configuración. Este método le permite especificar
     "disable_existing_loggers" como "False" en la configuración que
     envía.

logging.config.stopListening()

   Detiene el servidor de escucha que se creó con una llamada a
   "listen()". Esto normalmente se llama antes de llamar "join()" en
   el valor de retorno de "listen()".

## Consideraciones de seguridad

The logging configuration functionality tries to offer convenience,
and in part this is done by offering the ability to convert text in
configuration files into Python objects used in logging configuration
- for example, as described in Objetos definidos por el usuario.
However, these same mechanisms (importing callables from user-defined
modules and calling them with parameters from the configuration) could
be used to invoke any code you like, and for this reason you should
treat configuration files from untrusted sources with *extreme
caution* and satisfy yourself that nothing bad can happen if you load
them, before actually loading them.

## Esquema del diccionario de configuración

La descripción de una configuración de registro requiere una lista de
los diversos objetos para crear y las conexiones entre ellos; por
ejemplo, puede crear un gestor llamado 'consola' y luego decir que el
registrador llamado 'inicio' enviará sus mensajes al gestor 'consola'.
Estos objetos no se limitan a los proporcionados por el módulo
"logging" porque podría escribir su propia clase de formateador o
gestor. Los parámetros de estas clases también pueden necesitar
incluir objetos externos como "sys.stderr". La sintaxis para describir
estos objetos y conexiones se define en Conexiones de objeto a
continuación.

### Detalles del esquema del diccionario

El diccionario pasado a "dictConfig()" debe contener las siguientes
claves:

* *version* - se establece en un valor entero que representa la
  versión del esquema. El único valor válido en este momento es 1,
  pero tener esta clave permite que el esquema evolucione sin perder
  la compatibilidad con versiones anteriores.

Todas las demás claves son opcionales, pero si están presentes se
interpretarán como se describe a continuación. En todos los casos a
continuación, donde se menciona un 'dict de configuración', se
verificará la clave especial "'()'" para ver si se requiere una
instanciación personalizada. Si es así, el mecanismo descrito en
Objetos definidos por el usuario a continuación se usa para crear una
instancia; de lo contrario, el contexto se usa para determinar qué
instanciar.

* *formatters* - el valor correspondiente será un diccionario en el
  que cada clave es una identificación de formateador y cada valor es
  un diccionario que describe cómo configurar la instancia
  correspondiente "Formatter".

  Se busca el diccionario de configuración por las siguientes claves
  opcionales que corresponden a los argumentos pasados para crear un
  objeto "Formatter":

  * "format"

  * "datefmt"

  * "style"

  * "validate" (desde la versión >=3.8)

  * "defaults" (since version >=3.12)

  Una clave opcional "class" indica el nombre de la de clase del
  formateador (como un módulo punteado y nombre de clase).  Por su
  parte los argumentos de instanciación son "Formatter", de este modo
  esta clave es más útil para instanciar una subclase personalizada de
  "Formatter".  Por ejemplo, la clase alternativa presentaría
  excepciones rastreadas en un formato amplio o resumido.  Si tu
  formateador necesita claves de configuración diferentes o extra
  debes usar Objetos definidos por el usuario.

* *filters* - el valor correspondiente será un diccionario en el que
  cada clave es una identificación de filtro y cada valor es un
  diccionario que describe cómo configurar la instancia de filtro
  correspondiente.

  El diccionario de configuración busca la clave "name" (por defecto
  en la cadena vacía) y esto se utiliza para construir una instancia
  de "logging.Filter".

* *handlers* - el valor correspondiente será un diccionario en el que
  cada clave es una identificación de gestor y cada valor es un
  diccionario que describe cómo configurar la instancia del gestor
  correspondiente.

  El diccionario de configuración busca las siguientes claves:

  * "clase" (obligatorio).  Este es el nombre completo de la clase de
    gestor.

  * "level" (opcional).  El nivel del gestor.

  * "formatter" (opcional).  La identificación del formateador para
    este gestor.

  * "filters" (opcional).  Una lista de identificadores de los filtros
    para este gestor.

    Distinto en la versión 3.11: "filters" can take filter instances
    in addition to ids.

  Todas las claves *other* se pasan como argumentos de palabras clave
  al constructor del gestor. Por ejemplo, dado el fragmento:

     handlers:
       console:
         class : logging.StreamHandler
         formatter: brief
         level   : INFO
         filters: [allow_foo]
         stream  : ext://sys.stdout
       file:
         class : logging.handlers.RotatingFileHandler
         formatter: precise
         filename: logconfig.log
         maxBytes: 1024
         backupCount: 3

  el gestor con id "console" se instancia como
  "logging.StreamHandler", usando "sys.stdout" como la secuencia
  subyacente.  El gestor con la identificación "file" se instancia
  como "logging.handlers.RotatingFileHandler" con los argumentos de la
  palabra clave "filename='logconfig.log', maxBytes=1024,
  backupCount=3".

* *loggers* - el valor correspondiente será un diccionario en el que
  cada clave es un nombre de *logger* y cada valor es un diccionario
  que describe cómo configurar la instancia de *Logger*
  correspondiente.

  El diccionario de configuración busca las siguientes claves:

  * "level" (opcional). El nivel del registrador.

  * "propagate" (opcional).  La configuración de propagación del
    registrador.

  * "filters" (opcional). Una lista de identificadores de los filtros
    para este registrador.

    Distinto en la versión 3.11: "filters" can take filter instances
    in addition to ids.

  * "handlers" (opcional).  Una lista de identificadores de los
    gestores para este registrador.

  Los registradores especificados se configurarán de acuerdo con el
  nivel, la propagación, los filtros y los gestores especificados.

* *root* - Esta será la configuración para el registrador raíz. El
  procesamiento de la configuración será como para cualquier
  registrador, excepto que la configuración de "propagate" no será
  aplicable.

* *incremental* - si la configuración debe interpretarse como
  incremental a la configuración existente. Este valor predeterminado
  es "False", lo que significa que la configuración especificada
  reemplaza la configuración existente con la misma semántica que la
  utilizada por la API existente "fileConfig()".

  Si el valor especificado es "True", la configuración se procesa como
  se describe en la sección sobre Configuración incremental.

* *disable_existing_loggers* - si se debe deshabilitar cualquier
  registrador que no sea raíz existente. Esta configuración refleja el
  parámetro del mismo nombre en "fileConfig()". Si está ausente, este
  parámetro tiene el valor predeterminado "True". Este valor se ignora
  si *incremental* es "True".

### Configuración incremental

Es difícil proporcionar flexibilidad completa para la configuración
incremental. Por ejemplo, debido a que los objetos como los filtros y
formateadores son anónimos, una vez que se configura una
configuración, no es posible hacer referencia a dichos objetos
anónimos al aumentar una configuración.

Además, no hay un caso convincente para alterar arbitrariamente el
gráfico de objetos de registradores, gestores, filtros, formateadores
en tiempo de ejecución, una vez que se configura una configuración; la
verbosidad de los registradores y gestores se puede controlar
simplemente estableciendo niveles (y, en el caso de los registradores,
flags de propagación). Cambiar el gráfico de objetos de manera
arbitraria y segura es problemático en un entorno de subprocesos
múltiples; Si bien no es imposible, los beneficios no valen la
complejidad que agrega a la implementación.

Por lo tanto, cuando la tecla "incremental" de un diccionario de
configuración está presente y es "True", el sistema ignorará por
completo cualquier entrada de "formatters" y "filters", y procesará
solo el "level" configuraciones en las entradas de "handlers", y las
configuraciones de "level" y "propagate" en las entradas de "loggers"
y "root".

El uso de un valor en la configuración diccionario permite que las
configuraciones se envíen a través del cable como dictados en vinagre
a un escucha de socket. Por lo tanto, la verbosidad de registro de una
aplicación de larga ejecución puede modificarse con el tiempo sin
necesidad de detener y reiniciar la aplicación.

### Conexiones de objeto

El esquema describe un conjunto de objetos de registro (registradores,
gestores, formateadores, filtros) que están conectados entre sí en un
gráfico de objetos. Por lo tanto, el esquema necesita representar
conexiones entre los objetos. Por ejemplo, supongamos que, una vez
configurado, un registrador particular le ha adjuntado un gestor
particular. A los fines de esta discusión, podemos decir que el
registrador representa la fuente y el gestor el destino de una
conexión entre los dos. Por supuesto, en los objetos configurados esto
está representado por el registrador que tiene una referencia al
gestor. En la configuración dict, esto se hace dando a cada objeto de
destino una identificación que lo identifica inequívocamente, y luego
utilizando la identificación en la configuración del objeto de origen
para indicar que existe una conexión entre el origen y el objeto de
destino con esa identificación.

Entonces, por ejemplo, considere el siguiente fragmento de YAML:

   formatters:
     brief:
       # configuration for formatter with id 'brief' goes here
     precise:
       # configuration for formatter with id 'precise' goes here
   handlers:
     h1: #This is an id
      # configuration of handler with id 'h1' goes here
      formatter: brief
     h2: #This is another id
      # configuration of handler with id 'h2' goes here
      formatter: precise
   loggers:
     foo.bar.baz:
       # other configuration for logger 'foo.bar.baz'
       handlers: [h1, h2]

(Nota: YAML se usa aquí porque es un poco más legible que el
formulario fuente Python equivalente para el diccionario.)

Los identificadores para los registradores son los nombres de los
registradores que se utilizarían mediante programación para obtener
una referencia a esos registradores, por ejemplo "foo.bar.baz".  Los
identificadores para Formateadores y Filtros pueden ser cualquier
valor de cadena (como "breve", "preciso" arriba) y son transitorios,
ya que solo son significativos para procesar el diccionario de
configuración y se utilizan para determinar conexiones entre objetos ,
y no persisten en ninguna parte cuando se completa la llamada de
configuración.

El fragmento anterior indica que el registrador llamado "foo.bar.baz"
debe tener dos gestores adjuntos, que se describen mediante los
identificadores de gestor "h1" y "h2". El formateador para "h1" es el
descrito por identificador "brief", y el formateador para "h2" es el
descrito por identificador "precise".

### Objetos definidos por el usuario

El esquema admite objetos definidos por el usuario para gestores,
filtros y formateadores.  (Los registradores no necesitan tener
diferentes tipos para diferentes instancias, por lo que no hay soporte
en este esquema de configuración para las clases de registrador
definidas por el usuario).

Los objetos a configurar son descritos por diccionarios que detallan
su configuración. En algunos lugares, el sistema de registro podrá
inferir del contexto cómo se va a instanciar un objeto, pero cuando se
va a instanciar un objeto definido por el usuario, el sistema no sabrá
cómo hacerlo. Con el fin de proporcionar una flexibilidad completa
para la creación de instancias de objetos definidos por el usuario, el
usuario debe proporcionar una 'fábrica', una llamada que se llama con
un diccionario de configuración y que retorna el objeto instanciado.
Esto se indica mediante una ruta de importación absoluta a la fábrica
disponible bajo la tecla especial "'()'". Aquí hay un ejemplo
concreto:

   formatters:
     brief:
       format: '%(message)s'
     default:
       format: '%(asctime)s %(levelname)-8s %(name)-15s %(message)s'
       datefmt: '%Y-%m-%d %H:%M:%S'
     custom:
         (): my.package.customFormatterFactory
         bar: baz
         spam: 99.9
         answer: 42

El fragmento de YAML anterior define tres formateadores. El primero,
con identificador "breve", es una instancia estándar
"logging.Formatter" con la cadena de formato especificada. El segundo,
con identificador "predeterminado", tiene un formato más largo y
también define el formato de hora explícitamente, y dará como
resultado "logging.Formatter" inicializado con esas dos cadenas de
formato. En forma de fuente Python, los formateadores "breve" y
"predeterminado" tienen sub-diccionarios de configuración:

   {
     'format' : '%(message)s'
   }

y:

   {
     'format' : '%(asctime)s %(levelname)-8s %(name)-15s %(message)s',
     'datefmt' : '%Y-%m-%d %H:%M:%S'
   }

respectivamente, y como estos diccionarios no contienen la clave
especial "'()'", la instanciación se infiere del contexto: como
resultado, se crean las instancias estándar "logging.Formatter".  El
sub-diccionario de configuración para el tercer formateador, con
identificador "custom", es:

   {
     '()' : 'my.package.customFormatterFactory',
     'bar' : 'baz',
     'spam' : 99.9,
     'answer' : 42
   }

y esto contiene la clave especial "'()'", lo que significa que se
desea la creación de instancias definida por el usuario.  En este
caso, se utilizará la llamada especificada de fábrica especificada. Si
es una llamada real, se usará directamente; de lo contrario, si
especifica una cadena (como en el ejemplo), la llamada real se ubicará
utilizando mecanismos de importación normales. Se llamará al invocable
con los elementos **restantes** en el sub-diccionario de configuración
como argumentos de palabras clave.  En el ejemplo anterior, se
supondrá que el formateador con identificador "custom" será retornado
por la llamada:

   my.package.customFormatterFactory(bar='baz', spam=99.9, answer=42)

Advertencia:

  The values for keys such as "bar", "spam" and "answer" in the above
  example should not be configuration dictionaries or references such
  as "cfg://foo" or "ext://bar", because they will not be processed by
  the configuration machinery, but passed to the callable as-is.

La clave "'()'" se ha utilizado como clave especial porque no es un
nombre de parámetro de palabra clave válido, por lo que no entrará en
conflicto con los nombres de los argumentos de palabras clave
utilizados en la llamada. El "'()'" también sirve como mnemónico de
que el valor correspondiente es invocable.

Distinto en la versión 3.11: Los miembros "filter" de "handlers" y
"loggers" pueden tomar instancias de filtro en adición a
identificadores.

You can also specify a special key "'.'" whose value is a mapping of
attribute names to values. If found, the specified attributes will be
set on the user-defined object before it is returned. Thus, with the
following configuration:

   {
     '()' : 'my.package.customFormatterFactory',
     'bar' : 'baz',
     'spam' : 99.9,
     'answer' : 42,
     '.' {
       'foo': 'bar',
       'baz': 'bozz'
     }
   }

el formateador retornado tendrá el atributo "foo" establecido en
"'bar'" y el atributo "baz" establecido en "'bozz'".

Advertencia:

  The values for attributes such as "foo" and "baz" in the above
  example should not be configuration dictionaries or references such
  as "cfg://foo" or "ext://bar", because they will not be processed by
  the configuration machinery, but set as attribute values as-is.

### Handler configuration order

Handlers are configured in alphabetical order of their keys, and a
configured handler replaces the configuration dictionary in (a working
copy of) the "handlers" dictionary in the schema. If you use a
construct such as "cfg://handlers.foo", then initially
"handlers['foo']" points to the configuration dictionary for the
handler named "foo", and later (once that handler has been configured)
it points to the configured handler instance. Thus,
"cfg://handlers.foo" could resolve to either a dictionary or a handler
instance. In general, it is wise to name handlers in a way such that
dependent handlers are configured *after* any handlers they depend on;
that allows something like "cfg://handlers.foo" to be used in
configuring a handler that depends on handler "foo". If that dependent
handler were named "bar", problems would result, because the
configuration of "bar" would be attempted before that of "foo", and
"foo" would not yet have been configured. However, if the dependent
handler were named "foobar", it would be configured after "foo", with
the result that "cfg://handlers.foo" would resolve to configured
handler "foo", and not its configuration dictionary.

### Acceso a objetos externos

Hay momentos en que una configuración debe referirse a objetos
externos a la configuración, por ejemplo, "sys.stderr". Si el
diccionario de configuración se construye utilizando el código Python,
esto es sencillo, pero surge un problema cuando la configuración se
proporciona a través de un archivo de texto (por ejemplo, JSON, YAML).
En un archivo de texto, no hay una forma estándar de distinguir
"sys.stderr" de la cadena literal "'sys.stderr'". Para facilitar esta
distinción, el sistema de configuración busca ciertos prefijos
especiales en valores de cadena y los trata especialmente. Por
ejemplo, si la cadena literal "'ext://sys.stderr'" se proporciona como
un valor en la configuración, entonces la "ext://" se eliminará y se
procesará el resto del valor utilizando mecanismos normales de
importación.

El manejo de dichos prefijos se realiza de manera análoga al manejo
del protocolo: existe un mecanismo genérico para buscar prefijos que
coincidan con la expresión regular
"^(?P<prefix>[a-z]+)://(?P<suffix>.*)$" por el cual, si se reconoce el
"prefix", el "suffix" se procesa de manera dependiente del prefijo y
el resultado del procesamiento reemplaza el valor de la cadena. Si no
se reconoce el prefijo, el valor de la cadena se dejará tal cual.

### Acceso a objetos internos

Además de los objetos externos, a veces también es necesario hacer
referencia a los objetos en la configuración. El sistema de
configuración hará esto implícitamente para las cosas que conoce. Por
ejemplo, el valor de cadena "'DEBUG'" para un "level" en un
registrador o gestor se convertirá automáticamente al valor
"logging.DEBUG", y las entradas "handlers", "filters" y "formatter"
tomarán una identificación de objeto y se resuelven en el objeto de
destino apropiado.

Sin embargo, se necesita un mecanismo más genérico para los objetos
definidos por el usuario que no conoce el módulo "logging".  Por
ejemplo, considere "logging.handlers.MemoryHandler", que toma un
argumento "target" que es otro gestor para delegar. Dado que el
sistema ya conoce esta clase, entonces en la configuración, el
"target" dado solo necesita ser la identificación del objeto del
gestor de destino relevante, y el sistema resolverá el gestor desde la
identificación.  Sin embargo, si un usuario define un
"my.package.MyHandler" que tiene un gestor "alternate", el sistema de
configuración no sabría que el "alternate" se refería a un gestor.
Para atender esto, un sistema de resolución genérico permite al
usuario especificar:

   handlers:
     file:
       # configuration of file handler goes here

     custom:
       (): my.package.MyHandler
       alternate: cfg://handlers.file

La cadena literal "'cfg://handlers.file'" se resolverá de manera
análoga a las cadenas con el prefijo "ext://", pero buscando en la
configuración misma en lugar del espacio de nombres de importación. El
mecanismo permite el acceso por punto o por índice, de manera similar
a la proporcionada por "str.format". Por lo tanto, dado el siguiente
fragmento:

   handlers:
     email:
       class: logging.handlers.SMTPHandler
       mailhost: localhost
       fromaddr: my_app@domain.tld
       toaddrs:
         - support_team@domain.tld
         - dev_team@domain.tld
       subject: Houston, we have a problem.

in the configuration, the string "'cfg://handlers'" would resolve to
the dict with key "handlers", the string "'cfg://handlers.email" would
resolve to the dict with key "email" in the "handlers" dict, and so
on.  The string "'cfg://handlers.email.toaddrs[1]" would resolve to
"'dev_team@domain.tld'" and the string
"'cfg://handlers.email.toaddrs[0]'" would resolve to the value
"'support_team@domain.tld'". The "subject" value could be accessed
using either "'cfg://handlers.email.subject'" or, equivalently,
"'cfg://handlers.email[subject]'".  The latter form only needs to be
used if the key contains spaces or non-alphanumeric characters. Please
note that the characters "[" and "]" are not allowed in the keys. If
an index value consists only of decimal digits, access will be
attempted using the corresponding integer value, falling back to the
string value if needed.

Dada una cadena "cfg://handlers.myhandler.mykey.123", esto se
resolverá en "config_dict['handlers']['myhandler']['mykey']['123']".
Si la cadena se especifica como "cfg:
//handlers.myhandler.mykey[123]", el sistema intentará recuperar el
valor de "config_dict['handlers']['myhandler']['mykey'][123]", y
vuelva a "config_dict['handlers']['myhandler']['mykey']['123']" si eso
falla.

### Resolución de importación e importadores personalizados

La resolución de importación, por defecto, utiliza la función
incorporada "__import__()" para importar. Es posible que desee
reemplazar esto con su propio mecanismo de importación: si es así,
puede reemplazar el atributo "importer" de "DictConfigurator" o su
superclase, la clase "BaseConfigurator". Sin embargo, debe tener
cuidado debido a la forma en que se accede a las funciones desde las
clases a través de descriptores. Si está utilizando un Python
invocable para realizar sus importaciones, y lo desea definir a nivel
de clase en lugar de a nivel de instancia, debe envolverlo con
"staticmethod()". Por ejemplo:

   from importlib import import_module
   from logging.config import BaseConfigurator

   BaseConfigurator.importer = staticmethod(import_module)

No necesita envolver con "staticmethod()" si está configurando la
importación invocable en un configurador *instance*.

### Configuring QueueHandler and QueueListener

If you want to configure a "QueueHandler", noting that this is
normally used in conjunction with a "QueueListener", you can configure
both together. After the configuration, the "QueueListener" instance
will be available as the "listener" attribute of the created handler,
and that in turn will be available to you using "getHandlerByName()"
and passing the name you have used for the "QueueHandler" in your
configuration. The dictionary schema for configuring the pair is shown
in the example YAML snippet below.

   handlers:
     qhand:
       class: logging.handlers.QueueHandler
       queue: my.module.queue_factory
       listener: my.package.CustomListener
       handlers:
         - hand_name_1
         - hand_name_2
         ...

The "queue" and "listener" keys are optional.

If the "queue" key is present, the corresponding value can be one of
the following:

* An object implementing the "Queue.put_nowait" and "Queue.get" public
  API. For instance, this may be an actual instance of "queue.Queue"
  or a subclass thereof, or a proxy obtained by
  "multiprocessing.managers.SyncManager.Queue()".

  This is of course only possible if you are constructing or modifying
  the configuration dictionary in code.

* A string that resolves to a callable which, when called with no
  arguments, returns the queue instance to use. That callable could be
  a "queue.Queue" subclass or a function which returns a suitable
  queue instance, such as "my.module.queue_factory()".

* A dict with a "'()'" key which is constructed in the usual way as
  discussed in Objetos definidos por el usuario. The result of this
  construction should be a "queue.Queue" instance.

If the  "queue" key is absent, a standard unbounded "queue.Queue"
instance is created and used.

If the "listener" key is present, the corresponding value can be one
of the following:

* A subclass of "logging.handlers.QueueListener". This is of course
  only possible if you are constructing or modifying the configuration
  dictionary in code.

* A string which resolves to a class which is a subclass of
  "QueueListener", such as "'my.package.CustomListener'".

* A dict with a "'()'" key which is constructed in the usual way as
  discussed in Objetos definidos por el usuario. The result of this
  construction should be a callable with the same signature as the
  "QueueListener" initializer.

If the "listener" key is absent, "logging.handlers.QueueListener" is
used.

The values under the "handlers" key are the names of other handlers in
the configuration (not shown in the above snippet) which will be
passed to the queue listener.

Any custom queue handler and listener classes will need to be defined
with the same initialization signatures as "QueueHandler" and
"QueueListener".

Added in version 3.12.

## Formato de archivo de configuración

El formato del archivo de configuración que entiende "fileConfig()" se
basa en la funcionalidad "configparser". El archivo debe contener
secciones llamadas "[loggers]", "[handlers]" y "[formatters]" que
identifican por nombre las entidades de cada tipo que se definen en el
archivo. Para cada una de esas entidades, hay una sección separada que
identifica cómo se configura esa entidad. Por lo tanto, para un
registrador llamado "log01" en la sección "[loggers]", los detalles de
configuración relevantes se encuentran en una sección
"[logger_log01]". Del mismo modo, un gestor llamado "hand01" en la
sección "[handlers]" tendrá su configuración en una sección llamada
"[handler_hand01]", mientras que un formateador llamado "form01" en el
"[formatters]" sección tendrá su configuración especificada en una
sección llamada "[formatter_form01]". La configuración del registrador
raíz debe especificarse en una sección llamada "[logger_root]".

Nota:

  La API "fileConfig()" es más antigua que la API "dictConfig()" y no
  proporciona funcionalidad para cubrir ciertos aspectos del registro.
  Por ejemplo, no puede configurar objetos "Filter", que permiten el
  filtrado de mensajes más allá de niveles enteros simples, usando
  "fileConfig()". Si necesita tener instancias de "Filter" en su
  configuración de registro, deberá usar "dictConfig()". Tenga en
  cuenta que las mejoras futuras a la funcionalidad de configuración
  se agregarán a "dictConfig()", por lo que vale la pena considerar la
  transición a esta API más nueva cuando sea conveniente hacerlo.

A continuación se dan ejemplos de estas secciones en el archivo.

   [loggers]
   keys=root,log02,log03,log04,log05,log06,log07

   [handlers]
   keys=hand01,hand02,hand03,hand04,hand05,hand06,hand07,hand08,hand09

   [formatters]
   keys=form01,form02,form03,form04,form05,form06,form07,form08,form09

El registrador raíz debe especificar un nivel y una lista de gestores.
A continuación se muestra un ejemplo de una sección de registrador
raíz.

   [logger_root]
   level=NOTSET
   handlers=hand01

La entrada "level" puede ser una de "DEBUG, INFO, WARNING, ERROR,
CRITICAL" o "NOTSET". Solo para el registrador raíz, "NOTSET"
significa que todos los mensajes se registrarán. Los valores de nivel
son "evaluados" en el contexto del espacio de nombres del paquete
"logging".

La entrada "handlers" es una lista separada por comas de nombres de
gestores, que debe aparecer en la sección "[handlers]". Estos nombres
deben aparecer en la sección "[handlers]" y tener las secciones
correspondientes en el archivo de configuración.

Para los registradores que no sean el registrador raíz, se requiere
información adicional. Esto se ilustra en el siguiente ejemplo.

   [logger_parser]
   level=DEBUG
   handlers=hand01
   propagate=1
   qualname=compiler.parser

Las entradas "level" y "handlers" se interpretan como para el
registrador raíz, excepto que si el nivel de un registrador que no sea
raíz se especifica como "NOTSET", el sistema consulta a los
registradores más arriba en la jerarquía para determinar el nivel
efectivo del registrador. La entrada "propagate" se establece en 1
para indicar que los mensajes deben propagarse a los gestores que
están más arriba en la jerarquía del registrador, o 0 para indicar que
los mensajes **no** se propagan a los gestores en la jerarquía
superior. La entrada "qualname" es el nombre jerárquico del canal del
registrador, es decir, el nombre utilizado por la aplicación para
obtener el registrador.

Las secciones que especifican la configuración del gestor se
ejemplifican a continuación.

   [handler_hand01]
   class=StreamHandler
   level=NOTSET
   formatter=form01
   args=(sys.stdout,)

La entrada "class" indica la clase del gestor (según lo determinado
por "eval()" en el espacio de nombres del paquete "logging"). El
"level" se interpreta como para los registradores, y "NOTSET" se
entiende como 'registrar todo'.

La entrada "formatter" indica el nombre clave del formateador para
este gestor. Si está en blanco, se utiliza un formateador
predeterminado ("logging._defaultFormatter"). Si se especifica un
nombre, debe aparecer en la sección "[formatters]" y tener una sección
correspondiente en el archivo de configuración.

La entrada "args", cuando es "evaluada" en el contexto del espacio de
nombres del paquete "logging", es la lista de argumentos para el
constructor de la clase gestor. Consulte los constructores de los
gestores relevantes, o los ejemplos a continuación, para ver cómo se
construyen las entradas típicas. Si no se proporciona, el valor
predeterminado es "()".

La entrada opcional "kwargs", cuando es "evaluada" en el contexto del
espacio de nombres del paquete "logging", es el diccionario generado a
partir de los argumentos de palabra clave  para el constructor de la
clase gestor. Si no se proporciona, el valor predeterminado es "{}".

   [handler_hand02]
   class=FileHandler
   level=DEBUG
   formatter=form02
   args=('python.log', 'w')

   [handler_hand03]
   class=handlers.SocketHandler
   level=INFO
   formatter=form03
   args=('localhost', handlers.DEFAULT_TCP_LOGGING_PORT)

   [handler_hand04]
   class=handlers.DatagramHandler
   level=WARN
   formatter=form04
   args=('localhost', handlers.DEFAULT_UDP_LOGGING_PORT)

   [handler_hand05]
   class=handlers.SysLogHandler
   level=ERROR
   formatter=form05
   args=(('localhost', handlers.SYSLOG_UDP_PORT), handlers.SysLogHandler.LOG_USER)

   [handler_hand06]
   class=handlers.NTEventLogHandler
   level=CRITICAL
   formatter=form06
   args=('Python Application', '', 'Application')

   [handler_hand07]
   class=handlers.SMTPHandler
   level=WARN
   formatter=form07
   args=('localhost', 'from@abc', ['user1@abc', 'user2@xyz'], 'Logger Subject')
   kwargs={'timeout': 10.0}

   [handler_hand08]
   class=handlers.MemoryHandler
   level=NOTSET
   formatter=form08
   target=
   args=(10, ERROR)

   [handler_hand09]
   class=handlers.HTTPHandler
   level=NOTSET
   formatter=form09
   args=('localhost:9022', '/log', 'GET')
   kwargs={'secure': True}

Las secciones que especifican la configuración del formateador se
caracterizan por lo siguiente.

   [formatter_form01]
   format=F1 %(asctime)s %(levelname)s %(message)s %(customfield)s
   datefmt=
   style=%
   validate=True
   defaults={'customfield': 'defaultvalue'}
   class=logging.Formatter

Los argumentos para la configuración del formateador son los mismos
que las claves en el esquema del diccionario formatters section.

The "defaults" entry, when evaluated in the context of the "logging"
package's namespace, is a dictionary of default values for custom
formatting fields. If not provided, it defaults to "None".

Nota:

  Debido al uso de "eval()" como se describió anteriormente, existen
  riesgos potenciales de seguridad que resultan del uso de "listen()"
  para enviar y recibir configuraciones a través de sockets. Los
  riesgos se limitan a donde múltiples usuarios sin confianza mutua
  ejecutan código en la misma máquina; consulte la documentación de
  "listen()" para obtener más información.

Ver también:

  Módulo "logging"
     Referencia de API para el módulo de registro.

  Módulo "logging.handlers"
     Gestores útiles incluidos con el módulo de registro.
