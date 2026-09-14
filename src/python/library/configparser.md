---
title: '"configparser" --- Configuration file parser'
source_url: https://docs.python.org/es/3
source_path: library/configparser.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 2100
---

# "configparser" --- Configuration file parser

**Código fuente:** Lib/configparser.py

======================================================================

Este módulo provee la clase "ConfigParser", la cual implementa un
lenguaje básico de configuración que proporciona una estructura
similar a la encontrada en los archivos INI de Microsoft Windows.
Puedes utilizarla para escribir programas Python que los usuarios
finales puedan personalizar con facilidad.

Nota:

  Esta biblioteca *no* interpreta o escribe los prefijos valor-tipo
  usados en la versión extendida de la sintaxis INI, utilizada en el
  registro de Windows.

Ver también:

  Módulo "tomllib"
     TOML es un formato bien-especificado para archivos de
     configuración de aplicaciones. Está específicamente diseñado para
     ser una versión mejorada de INI.

  Módulo "shlex"
     Soporta la creación de un mini-lenguaje parecido a shell de Unix,
     que puede utilizarse para archivos de configuración de
     aplicaciones.

  Módulo "json"
     El módulo "json" implementa un subconjunto de la sintaxis de
     JavaScript, que también puede utilizarse para configuración, pero
     no soporta comentarios.

## Inicio Rápido

Tomemos un archivo de configuración muy básico, el cual luce así:

   [DEFAULT]
   ServerAliveInterval = 45
   Compression = yes
   CompressionLevel = 9
   ForwardX11 = yes

   [forge.example]
   User = hg

   [topsecret.server.example]
   Port = 50022
   ForwardX11 = no

The structure of INI files is described in the following section.
Essentially, the file consists of sections, each of which contains
keys with values. "configparser" classes can read and write such
files.  Let's start by creating the above configuration file
programmatically.

   >>> import configparser
   >>> config = configparser.ConfigParser()
   >>> config['DEFAULT'] = {'ServerAliveInterval': '45',
   ...                      'Compression': 'yes',
   ...                      'CompressionLevel': '9'}
   >>> config['forge.example'] = {}
   >>> config['forge.example']['User'] = 'hg'
   >>> config['topsecret.server.example'] = {}
   >>> topsecret = config['topsecret.server.example']
   >>> topsecret['Port'] = '50022'     # mutates the parser
   >>> topsecret['ForwardX11'] = 'no'  # same here
   >>> config['DEFAULT']['ForwardX11'] = 'yes'
   >>> with open('example.ini', 'w') as configfile:
   ...   config.write(configfile)
   ...

Como puedes ver, podemos tratar al *config parser* como a un
diccionario. Existen diferencias,  descritas posteriormente, pero su
comportamiento es muy parecido al que esperarías de un diccionario.

Ahora que hemos creado y guardado el archivo de configuración, vamos a
releerlo y analizar los datos que contiene.

   >>> config = configparser.ConfigParser()
   >>> config.sections()
   []
   >>> config.read('example.ini')
   ['example.ini']
   >>> config.sections()
   ['forge.example', 'topsecret.server.example']
   >>> 'forge.example' in config
   True
   >>> 'python.org' in config
   False
   >>> config['forge.example']['User']
   'hg'
   >>> config['DEFAULT']['Compression']
   'yes'
   >>> topsecret = config['topsecret.server.example']
   >>> topsecret['ForwardX11']
   'no'
   >>> topsecret['Port']
   '50022'
   >>> for key in config['forge.example']:
   ...     print(key)
   user
   compressionlevel
   serveraliveinterval
   compression
   forwardx11
   >>> config['forge.example']['ForwardX11']
   'yes'

Como podemos apreciar, la API es muy clara. La única 'porción de
magia' está en la sección "DEFAULT", la cual proporciona los valores
por defecto para todas las demás secciones [1]. Observe también que
las claves de las secciones son insensibles a mayúsculas y minúsculas,
pero se almacenan en minúscula [1].

It is possible to read several configurations into a single
"ConfigParser", where the most recently added configuration has the
highest priority. Any conflicting keys are taken from the more recent
configuration while the previously existing keys are retained. The
example below reads in an "override.ini" file, which will override any
conflicting keys from the "example.ini" file.

   [DEFAULT]
   ServerAliveInterval = -1

   >>> config_override = configparser.ConfigParser()
   >>> config_override['DEFAULT'] = {'ServerAliveInterval': '-1'}
   >>> with open('override.ini', 'w') as configfile:
   ...     config_override.write(configfile)
   ...
   >>> config_override = configparser.ConfigParser()
   >>> config_override.read(['example.ini', 'override.ini'])
   ['example.ini', 'override.ini']
   >>> print(config_override.get('DEFAULT', 'ServerAliveInterval'))
   -1

Este comportamiento es equivalente a una llamada a
"ConfigParser.read()" pasando varios ficheros en el parámetro
*filenames*.

## Tipos de Datos Soportados

Los *config parsers* no especulan respecto a los tipos de datos de los
valores en los archivos de configuración, siempre los almacenan
internamente como cadenas de caracteres. Esto significa que si
necesitas otros tipos de datos, deberás hacer la conversión por ti
mismo:

   >>> int(topsecret['Port'])
   50022
   >>> float(topsecret['CompressionLevel'])
   9.0

Dado que esta tarea es muy común, los *config parsers* proporcionan
una amplia variedad de útiles métodos de lectura (*getter*) que
manejan enteros, números de punto flotante y booleanos. Este último es
el más interesante, porque puede no ser correcto pasar simplemente el
valor a "bool()", ya que "bool('False')" resultará en "True". Por esta
razón los *config parsers* proporcionan también el método
"getboolean()". Este método es insensible a mayúsculas y minúsculas, y
reconoce como valores booleanos a los valores "'yes'"/"'no'",
"'on'"/"'off'", "'true'"/"'false'" and "'1'"/"'0'" [1].  Por ejemplo:

   >>> topsecret.getboolean('ForwardX11')
   False
   >>> config['forge.example'].getboolean('ForwardX11')
   True
   >>> config.getboolean('forge.example', 'Compression')
   True

Además de "getboolean()", los *config parsers* también proporcionan
los métodos equivalentes "getint()" y "getfloat()". Puedes registrar
tus propios conversores, y personalizar los que se proporcionan. [1]

## Valores de contingencia

As with a dictionary, you can use a section's "get()" method to
provide fallback values:

   >>> topsecret.get('Port')
   '50022'
   >>> topsecret.get('CompressionLevel')
   '9'
   >>> topsecret.get('Cipher')
   >>> topsecret.get('Cipher', '3des-cbc')
   '3des-cbc'

Por favor, fíjate que los valores por defecto tienen prioridad sobre
los valores de contingencia (*fallback*). Así, en nuestro ejemplo, la
clave "'CompressionLevel'" sólo fue especificada en la sección
"'DEFAULT'". Si tratamos de obtener su valor de la sección
"'topsecret.server.example'", obtendremos siempre el valor por
defecto, incluso si especificamos un valor de contingencia:

   >>> topsecret.get('CompressionLevel', '3')
   '9'

One more thing to be aware of is that the parser-level "get()" method
provides a custom, more complex interface, maintained for backwards
compatibility.  When using this method, a fallback value can be
provided via the "fallback" keyword-only argument:

   >>> config.get('forge.example', 'monster',
   ...            fallback='No such things as monsters')
   'No such things as monsters'

El mismo argumento "fallback" puede utilizarse con los métodos
"getint()", "getfloat()" y "getboolean()", por ejemplo:

   >>> 'BatchMode' in topsecret
   False
   >>> topsecret.getboolean('BatchMode', fallback=True)
   True
   >>> config['DEFAULT']['BatchMode'] = 'no'
   >>> topsecret.getboolean('BatchMode', fallback=True)
   False

## Estructura soportada para el archivo ini

Un archivo de configuración consta de secciones, cada una iniciada por
una cabecera "[section]", seguida por registros clave-valor separados
por una cadena de caracteres específica ("=" ó ":" por defecto [1]).
De forma predeterminada, los nombres de sección son sensibles a
mayúsculas y minúsculas pero las claves no [1]. Los espacios al inicio
y final de las claves y valores son eliminados. Los valores pueden ser
omitidos si el *parser* está configurado para permitirlo [1], en cuyo
caso el delimitador del dato clave-valor puede ser omitido también.
Los valores pueden ocupar varias líneas, siempre y cuando tengan una
indentación mayor que la primera línea del valor. Dependiendo del modo
del *parser*, las líneas en blanco pueden tratarse como parte de un
valor multilínea o ser ignoradas.

By default, a valid section name can be any string that does not
contain '\n'. To change this, see "ConfigParser.SECTCRE".

The first section name may be omitted if the parser is configured to
allow an unnamed top level section with "allow_unnamed_section=True".
In this case, the keys/values may be retrieved by "UNNAMED_SECTION" as
in "config[UNNAMED_SECTION]".

Los archivos de configuración pueden incluir comentarios, con
caracteres específicos como prefijos ("#" y ";" por defecto [1]). Los
comentarios pueden ocupar su propia línea, posiblemente indentada. [1]

Por ejemplo:

   [Simple Values]
   key=value
   spaces in keys=allowed
   spaces in values=allowed as well
   spaces around the delimiter = obviously
   you can also use : to delimit keys from values

   [All Values Are Strings]
   values like this: 1000000
   or this: 3.14159265359
   are they treated as numbers? : no
   integers, floats and booleans are held as: strings
   can use the API to get converted values directly: true

   [Multiline Values]
   chorus: I'm a lumberjack, and I'm okay
       I sleep all night and I work all day

   [No Values]
   key_without_value
   empty string value here =

   [You can use comments]
   # like this
   ; or this

   # By default only in an empty line.
   # Inline comments can be harmful because they prevent users
   # from using the delimiting characters as parts of values.
   # That being said, this can be customized.

       [Sections Can Be Indented]
           can_values_be_as_well = True
           does_that_mean_anything_special = False
           purpose = formatting for readability
           multiline_values = are
               handled just fine as
               long as they are indented
               deeper than the first line
               of a value
           # Did I mention we can indent comments, too?

## Unnamed Sections

The name of the first section (or unique) may be omitted and values
retrieved by the "UNNAMED_SECTION" attribute.

   >>> config = """
   ... option = value
   ...
   ... [  Section 2  ]
   ... another = val
   ... """
   >>> unnamed = configparser.ConfigParser(allow_unnamed_section=True)
   >>> unnamed.read_string(config)
   >>> unnamed.get(configparser.UNNAMED_SECTION, 'option')
   'value'

## Interpolación de valores

En el nivel superior de su funcionalidad central, "ConfigParser"
soporta la interpolación. Esto significa que los valores pueden ser
preprocesados, antes de ser retornados por los llamados a "get()".

class configparser.BasicInterpolation

   Es la implementación por defecto que utiliza "ConfigParser".
   Permite valores que contengan cadenas de formato, que hacen
   referencia a otros valores en la misma sección o a valores
   presentes en la sección especial *default* [1]. Valores por defecto
   adicionales pueden ser proporcionados en la inicialización.

   Por ejemplo:

      [Paths]
      home_dir: /Users
      my_dir: %(home_dir)s/lumberjack
      my_pictures: %(my_dir)s/Pictures

      [Escape]
      # use a %% to escape the % sign (% is the only character that needs to be escaped):
      gain: 80%%

   En el ejemplo anterior, "ConfigParser" con la *interpolación*
   establecida a "BasicInterpolation()" puede resolver "%(home_dir)s"
   al valor "home_dir" ("/Users" en este caso).  En efecto,
   "%(my_dir)s" podría resolverse como "/Users/lumberjack". Todas las
   interpolaciones son realizadas bajo demanda, de modo que las claves
   utilizadas en la cadena de referencias no requieren un orden
   específico en el archivo de configuración.

   Con "interpolation" establecida al valor "None", el *parser*
   retornará simplemente "%(my_dir)s/Pictures" como el valor de
   "my_pictures" y "%(home_dir)s/lumberjack" como el valor de
   "my_dir".

class configparser.ExtendedInterpolation

   Es un gestor alternativo para la interpolación, que implementa una
   sintaxis más avanzada; es utilizado, por ejemplo, en "zc.buildout".
   La interpolación es extendida al utilizar "${section:option}", a
   fin de especificar un valor que proviene de una sección externa. La
   interpolación puede cubrir múltiples niveles. Por conveniencia, si
   la parte "section:" es omitida, la interpolación utilizará la
   sección actual (y posiblemente los valores por defecto establecidos
   en la sección especial).

   Por ejemplo, la configuración indicada anteriormente, con
   interpolación básica, luciría de la siguiente manera utilizando
   interpolación extendida:

      [Paths]
      home_dir: /Users
      my_dir: ${home_dir}/lumberjack
      my_pictures: ${my_dir}/Pictures

      [Escape]
      # use a $$ to escape the $ sign ($ is the only character that needs to be escaped):
      cost: $$80

   También pueden buscarse valores en otras secciones:

      [Common]
      home_dir: /Users
      library_dir: /Library
      system_dir: /System
      macports_dir: /opt/local

      [Frameworks]
      Python: 3.2
      path: ${Common:system_dir}/Library/Frameworks/

      [Arthur]
      nickname: Two Sheds
      last_name: Jackson
      my_dir: ${Common:home_dir}/twosheds
      my_pictures: ${my_dir}/Pictures
      python_dir: ${Frameworks:path}/Python/Versions/${Frameworks:Python}

## Acceso por protocolo de mapeo

Added in version 3.2.

Mapping protocol access is a generic name for functionality that
enables using custom objects as if they were dictionaries.  In case of
"configparser", the mapping interface implementation is using the
"parser['section']['option']" notation.

En particular, "parser['section']" retorna un proxy para los datos de
la sección en el *parser*. Esto significa que los valores no son
copiados, sino que son tomados del *parser* original sobre la marcha.

"configparser" objects behave as close to actual dictionaries as
possible. The mapping interface is complete and adheres to the
"MutableMapping" ABC. However, there are a few differences that should
be taken into account:

* Por defecto, todas las claves de las secciones se pueden acceder de
  una forma insensible a mayúsculas y minúsculas [1]. Ej. "for option
  in parser["section"]" entrega solamente nombres de claves de opción
  que han pasado por "optionxform". Esto significa, claves en
  minúscula por defecto. A la vez, para una sección que contiene la
  clave "'a'", ambas expresiones retornan "True":

     "a" in parser["section"]
     "A" in parser["section"]

* Todas las secciones también incluyen valores "DEFAULTSECT", lo que
  significa que ".clear()" en una sección puede no significar que esta
  quede vacía de forma visible. Ello debido a que los valores por
  defecto no pueden ser borrados de la sección (ya que técnicamente no
  están allí). Si fueron redefinidas en la sección, su borrado
  ocasiona que los valores por defecto sean visibles de nuevo.
  Cualquier intento de borrar un valor por defecto ocasiona una
  excepción "KeyError".

* "DEFAULTSECT" no puede ser eliminado del *parser*:

  * el intento de borrarlo lanza una excepción "ValueError",

  * "parser.clear()" lo deja intacto,

  * "parser.popitem()" nunca lo retorna.

* "parser.get(section, option, **kwargs)" - el segundo argumento
  **no** es un valor de contingencia. Observe, sin embargo, que los
  métodos "get()" a nivel de sección son compatibles tanto con el
  protocolo de mapeo como con la API clásica de *configparser*.

* "parser.items()" es compatible con el protocolo de mapeo (retorna
  una lista de pares *section_name*, *section_proxy* que estén
  incluidos en DEFAULTSECT). Sin embargo, este método también puede
  ser invocado con los argumentos: "parser.items(section, raw, vars)".
  Esta última llamada retorna una lista de pares *option*, *value*
  para una "section" específica, con todas las interpolaciones
  expandidas (a menos que se especifique "raw=True").

El protocolo de mapeo se implementa en el nivel superior de la actual
API heredada, de modo que esas subclases que sobre-escriben la
interfaz original aún deberían hacer funcionar el mapeo como se
esperaría.

## Personalizando el comportamiento del parser

There are nearly as many INI format variants as there are applications
using it. "configparser" goes a long way to provide support for the
largest sensible set of INI styles available.  The default
functionality is mainly dictated by historical background and it's
very likely that you will want to customize some of the features.

The most common way to change the way a specific config parser works
is to use the "__init__()" options:

* *defaults*, valor por defecto: "None"

  Esta opción acepta un diccionario de pares clave-valor, que debe ser
  colocado inicialmente en la sección "DEFAULT". De este modo se
  obtiene una manera elegante de apoyar los archivos de configuración
  concisos, que no especifican valores que sean los mismos
  documentados por defecto.

  Hint: if you want to specify default values for a specific section,
  use "read_dict()" before you read the actual file.

* *dict_type*, valor por defecto: "dict"

  Esta opción tiene un gran impacto en cómo funcionará el protocolo de
  mapeo, y cómo lucirán los archivos de configuración a escribir. Con
  el diccionario estándar, cada sección se almacena en el orden en que
  se añadieron al *parser*. Lo mismo ocurre con las opciones dentro de
  las secciones.

  Un tipo alternativo de diccionario puede ser utilizado, por ejemplo,
  para ordenar las secciones y opciones en un modo a posteriori
  (*write-back*).

  Por favor, tome en cuenta que: existen formas de agregar un par
  clave-valor en una sola operación. Cuando se utiliza un diccionario
  común en tales operaciones, el orden de las claves será el empleado
  en la creación. Por ejemplo:

     >>> parser = configparser.ConfigParser()
     >>> parser.read_dict({'section1': {'key1': 'value1',
     ...                                'key2': 'value2',
     ...                                'key3': 'value3'},
     ...                   'section2': {'keyA': 'valueA',
     ...                                'keyB': 'valueB',
     ...                                'keyC': 'valueC'},
     ...                   'section3': {'foo': 'x',
     ...                                'bar': 'y',
     ...                                'baz': 'z'}
     ... })
     >>> parser.sections()
     ['section1', 'section2', 'section3']
     >>> [option for option in parser['section3']]
     ['foo', 'bar', 'baz']

* *allow_no_value*, valor por defecto: "False"

  Some configuration files are known to include settings without
  values, but which otherwise conform to the syntax supported by
  "configparser".  The *allow_no_value* parameter to the constructor
  can be used to indicate that such values should be accepted:

     >>> import configparser

     >>> sample_config = """
     ... [mysqld]
     ...   user = mysql
     ...   pid-file = /var/run/mysqld/mysqld.pid
     ...   skip-external-locking
     ...   old_passwords = 1
     ...   skip-bdb
     ...   # we don't need ACID today
     ...   skip-innodb
     ... """
     >>> config = configparser.ConfigParser(allow_no_value=True)
     >>> config.read_string(sample_config)

     >>> # Settings with values are treated as before:
     >>> config["mysqld"]["user"]
     'mysql'

     >>> # Settings without values provide None:
     >>> config["mysqld"]["skip-bdb"]

     >>> # Settings which aren't specified still raise an error:
     >>> config["mysqld"]["does-not-exist"]
     Traceback (most recent call last):
       ...
     KeyError: 'does-not-exist'

* *delimiters*, valor por defecto: "('=', ':')"

  Los *delimiters* son cadenas de caracteres que separan las claves de
  los valores dentro de una sección. La primera ocurrencia de una
  cadena de separación en una línea se considera como un separador.
  Esto significa que los valores pueden contener separadores, no así
  las claves.

  Vea también el argumento *space_around_delimiters* de
  "ConfigParser.write()".

* *comment_prefixes*, valor por defecto: "('#', ';')"

* *inline_comment_prefixes*, valor por defecto: "None"

  Los prefijos de comentario son cadenas de caracteres que indican el
  inicio de un comentario válido dentro de un archivo de
  configuración. Los *comment_prefixes* son utilizados solamente en lo
  que serían líneas en blanco (opcionalmente indentadas), mientras que
  *inline_comment_prefixes* pueden ser utilizados después de cada
  valor válido (ej. nombres de sección, opciones y también líneas en
  blanco). De forma predeterminada, los comentarios en la misma línea
  están deshabilitados, y tanto "'#'" como "';'" se utilizan como
  prefijos para comentarios que ocupan toda la línea.

  Distinto en la versión 3.2: In previous versions of "configparser"
  behaviour matched "comment_prefixes=('#',';')" and
  "inline_comment_prefixes=(';',)".

  Por favor, observe que los *config parsers* no soportan el escapado
  de los prefijos de comentarios, de modo que la utilización de los
  *inline_comment_prefixes* puede impedir que los usuarios
  especifiquen valores de opciones que incluyan caracteres empleados
  como prefijos de comentarios. Ante la duda, evite especificar los
  *inline_comment_prefixes*. En cualquier circunstancia, la única
  forma de almacenar caracteres prefijos de comentario al inicio de
  una línea, en valores multilínea, es mediante la interpolación del
  prefijo, por ejemplo:

     >>> from configparser import ConfigParser, ExtendedInterpolation
     >>> parser = ConfigParser(interpolation=ExtendedInterpolation())
     >>> # the default BasicInterpolation could be used as well
     >>> parser.read_string("""
     ... [DEFAULT]
     ... hash = #
     ...
     ... [hashes]
     ... shebang =
     ...   ${hash}!/usr/bin/env python
     ...   ${hash} -*- coding: utf-8 -*-
     ...
     ... extensions =
     ...   enabled_extension
     ...   another_extension
     ...   #disabled_by_comment
     ...   yet_another_extension
     ...
     ... interpolation not necessary = if # is not at line start
     ... even in multiline values = line #1
     ...   line #2
     ...   line #3
     ... """)
     >>> print(parser['hashes']['shebang'])

     #!/usr/bin/env python
     # -*- coding: utf-8 -*-
     >>> print(parser['hashes']['extensions'])

     enabled_extension
     another_extension
     yet_another_extension
     >>> print(parser['hashes']['interpolation not necessary'])
     if # is not at line start
     >>> print(parser['hashes']['even in multiline values'])
     line #1
     line #2
     line #3

* *strict*, valor por defecto: "True"

  When set to "True", the parser will not allow for any section or
  option duplicates while reading from a single source (using
  "read_file()", "read_string()" or "read_dict()").  It is recommended
  to use strict parsers in new applications.

  Distinto en la versión 3.2: In previous versions of "configparser"
  behaviour matched "strict=False".

* *empty_lines_in_values*, valor por defecto: "True"

  En los *config parsers*, los valores pueden abarcar varias líneas,
  siempre y cuando estén indentadas a un nivel superior al de la clave
  que las contiene. De forma predeterminada, los *parsers* permiten
  que las líneas en blanco formen parte de los valores. Igualmente,
  las claves pueden estar indentadas a sí mismas de forma arbitraria,
  a fin de mejorar la legibilidad. Por lo tanto, cuando los archivos
  de configuración se vuelven grandes y complejos, es fácil para el
  usuario el perder la pista de la estructura del archivo. Tomemos
  como ejemplo:

     [Section]
     key = multiline
       value with a gotcha

      this = is still a part of the multiline value of 'key'

  Esto puede ser especialmente problemático de observar por parte del
  usuario, en caso que se esté utilizando un tipo de fuente
  proporcional para editar el archivo. Y es por ello que, cuando tu
  aplicación no necesite valores con líneas en blanco, debes
  considerar invalidarlas. Esto ocasionaría que las líneas en blanco
  sirvan para dividir a las claves, siempre. En el ejemplo anterior,
  produciría dos claves: "key" y "this".

* *default_section*, valor por defecto: "configparser.DEFAULTSECT" (es
  decir: ""DEFAULT"")

  El convenio de permitir una sección especial con valores por defecto
  para otras secciones, o con propósito de interpolación, es un
  concepto poderoso de esta librería, el cual permite a los usuarios
  crear configuraciones declarativas complejas. Esta sección se suele
  denominar ""DEFAULT"", pero puede personalizarse para corresponder a
  cualquier otro nombre de sección. Algunas valores comunes son:
  ""general"" ó ""common"". El nombre proporcionado es utilizado para
  reconocer las secciones por defecto al momento de realizar la
  lectura desde cualquier fuente, y es utilizado ante cualquier
  escritura al archivo de configuración. Su valor actual puede
  obtenerse utilizando el atributo "parser_instance.default_section" y
  puede ser modificado en tiempo de ejecución (es decir, para
  convertir archivos de un formato a otro).

* *interpolation*, valor por defecto:
  "configparser.BasicInterpolation"

  El comportamiento de la interpolación puede ser personalizado al
  proporcionar un gestor personalizado mediante el argumento
  *interpolation*. El valor "None" se utiliza para desactivar la
  interpolación por completo, mientras que "ExtendedInterpolation()"
  proporciona una variante más avanzada, inspirada por "zc.buildout".
  Más información al respecto en la sección dedicada de la
  documentación. El "RawConfigParser" tiene un valor por defecto de
  "None".

* *converters*, valor por defecto: no definido

  Config parsers provide option value getters that perform type
  conversion.  By default "getint()", "getfloat()", and "getboolean()"
  are implemented.  Should other getters be desirable, users may
  define them in a subclass or pass a dictionary where each key is a
  name of the converter and each value is a callable implementing said
  conversion.  For instance, passing "{'decimal': decimal.Decimal}"
  would add "getdecimal()" on both the parser object and all section
  proxies.  In other words, it will be possible to write both
  "parser_instance.getdecimal('section', 'key', fallback=0)" and
  "parser_instance['section'].getdecimal('key', 0)".

  Si el conversor necesita acceder al estado del *parser*, este puede
  ser implementado como un método en una subclase del *config parser*.
  Si el nombre de este método comienza con "get", estará disponible en
  todas las secciones proxy, en su forma compatible con diccionarios
  (vea el ejemplo anterior de "getdecimal()").

Una personalización más avanzada puede conseguirse al sustituir los
valores por defecto de estos atributos del *parser*. Los valores por
defecto son definidos en las clases, de modo que pueden ser
sustituidos por las subclases o mediante la asignación de atributos.

ConfigParser.BOOLEAN_STATES

   Por defecto, al utilizar el método "getboolean()", los *config
   parsers* consideran a los siguientes valores como "True": "'1'",
   "'yes'", "'true'", "'on'" y a los siguientes valores como "False":
   "'0'", "'no'", "'false'", "'off'".  Puedes cambiar ello
   proporcionando un diccionario personalizado de cadenas de
   caracteres, con sus correspondientes valores booleanos. Por
   ejemplo:

      >>> custom = configparser.ConfigParser()
      >>> custom['section1'] = {'funky': 'nope'}
      >>> custom['section1'].getboolean('funky')
      Traceback (most recent call last):
      ...
      ValueError: Not a boolean: nope
      >>> custom.BOOLEAN_STATES = {'sure': True, 'nope': False}
      >>> custom['section1'].getboolean('funky')
      False

   Otros pares booleanos comunes incluyen "accept"/"reject" ó
   "enabled"/"disabled".

ConfigParser.optionxform(option)

   Este método realiza la transformación de los nombres de opciones
   para cada operación de lectura, obtención o asignación. Por defecto
   convierte los nombres a minúsculas. Esto significa que, cuando un
   archivo de configuración es escrito, todas las claves son
   convertidas a minúsculas. Sobre-escribe este método si tal
   comportamiento no es adecuado. Por ejemplo:

      >>> config = """
      ... [Section1]
      ... Key = Value
      ...
      ... [Section2]
      ... AnotherKey = Value
      ... """
      >>> typical = configparser.ConfigParser()
      >>> typical.read_string(config)
      >>> list(typical['Section1'].keys())
      ['key']
      >>> list(typical['Section2'].keys())
      ['anotherkey']
      >>> custom = configparser.RawConfigParser()
      >>> custom.optionxform = lambda option: option
      >>> custom.read_string(config)
      >>> list(custom['Section1'].keys())
      ['Key']
      >>> list(custom['Section2'].keys())
      ['AnotherKey']

   Nota:

     La función *optionxform* transforma los nombres de opción a una
     forma canónica. Esta debería ser una función idempotente: si el
     nombre ya está en su forma canónica, debería retornarse sin
     cambios.

ConfigParser.SECTCRE

   Es una expresión regular compilada que se utiliza para parsear
   cabeceras de sección. Por defecto hace corresponder "[section]" con
   el nombre ""section"". Los espacios en blanco son considerados
   parte del nombre de sección, por lo que "[  larch  ]" será leído
   como la sección de nombre ""  larch  "". Sobre-escribe este
   atributo si tal comportamiento no es adecuado. Por ejemplo:

      >>> import re
      >>> config = """
      ... [Section 1]
      ... option = value
      ...
      ... [  Section 2  ]
      ... another = val
      ... """
      >>> typical = configparser.ConfigParser()
      >>> typical.read_string(config)
      >>> typical.sections()
      ['Section 1', '  Section 2  ']
      >>> custom = configparser.ConfigParser()
      >>> custom.SECTCRE = re.compile(r"\[ *(?P<header>[^]]+?) *\]")
      >>> custom.read_string(config)
      >>> custom.sections()
      ['Section 1', 'Section 2']

   Nota:

     Mientras que los objetos *ConfigParser* también utilizan un
     atributo "OPTCRE" para reconocer las líneas de opciones, no se
     recomienda su sobre-escritura porque puede interferir con las
     opciones *allow_no_value* y *delimiters* del constructor.

## Ejemplos de la API heredada

Mainly because of backwards compatibility concerns, "configparser"
provides also a legacy API with explicit "get"/"set" methods.  While
there are valid use cases for the methods outlined below, mapping
protocol access is preferred for new projects.  The legacy API is at
times more advanced, low-level and downright counterintuitive.

Un ejemplo de escritura a un archivo de configuración:

   import configparser

   config = configparser.RawConfigParser()

   # Please note that using RawConfigParser's set functions, you can assign
   # non-string values to keys internally, but will receive an error when
   # attempting to write to a file or when you get it in non-raw mode. Setting
   # values using the mapping protocol or ConfigParser's set() does not allow
   # such assignments to take place.
   config.add_section('Section1')
   config.set('Section1', 'an_int', '15')
   config.set('Section1', 'a_bool', 'true')
   config.set('Section1', 'a_float', '3.1415')
   config.set('Section1', 'baz', 'fun')
   config.set('Section1', 'bar', 'Python')
   config.set('Section1', 'foo', '%(bar)s is %(baz)s!')

   # Writing our configuration file to 'example.cfg'
   with open('example.cfg', 'w') as configfile:
       config.write(configfile)

Un ejemplo de lectura de un archivo de configuración, nuevamente:

   import configparser

   config = configparser.RawConfigParser()
   config.read('example.cfg')

   # getfloat() raises an exception if the value is not a float
   # getint() and getboolean() also do this for their respective types
   a_float = config.getfloat('Section1', 'a_float')
   an_int = config.getint('Section1', 'an_int')
   print(a_float + an_int)

   # Notice that the next output does not interpolate '%(bar)s' or '%(baz)s'.
   # This is because we are using a RawConfigParser().
   if config.getboolean('Section1', 'a_bool'):
       print(config.get('Section1', 'foo'))

Para obtener la interpolación, utilice "ConfigParser":

   import configparser

   cfg = configparser.ConfigParser()
   cfg.read('example.cfg')

   # Set the optional *raw* argument of get() to True if you wish to disable
   # interpolation in a single get operation.
   print(cfg.get('Section1', 'foo', raw=False))  # -> "Python is fun!"
   print(cfg.get('Section1', 'foo', raw=True))   # -> "%(bar)s is %(baz)s!"

   # The optional *vars* argument is a dict with members that will take
   # precedence in interpolation.
   print(cfg.get('Section1', 'foo', vars={'bar': 'Documentation',
                                          'baz': 'evil'}))

   # The optional *fallback* argument can be used to provide a fallback value
   print(cfg.get('Section1', 'foo'))
         # -> "Python is fun!"

   print(cfg.get('Section1', 'foo', fallback='Monty is not.'))
         # -> "Python is fun!"

   print(cfg.get('Section1', 'monster', fallback='No such things as monsters.'))
         # -> "No such things as monsters."

   # A bare print(cfg.get('Section1', 'monster')) would raise NoOptionError
   # but we can also use:

   print(cfg.get('Section1', 'monster', fallback=None))
         # -> None

Los valores por defecto están disponibles en ambos tipos de
ConfigParsers. Ellos son utilizados en la interpolación cuando una
opción utilizada no está definida en otro lugar.

   import configparser

   # New instance with 'bar' and 'baz' defaulting to 'Life' and 'hard' each
   config = configparser.ConfigParser({'bar': 'Life', 'baz': 'hard'})
   config.read('example.cfg')

   print(config.get('Section1', 'foo'))     # -> "Python is fun!"
   config.remove_option('Section1', 'bar')
   config.remove_option('Section1', 'baz')
   print(config.get('Section1', 'foo'))     # -> "Life is hard!"

## Objetos ConfigParser

class configparser.ConfigParser(defaults=None, dict_type=dict, allow_no_value=False, *, delimiters=('=', ':'), comment_prefixes=('#', ';'), inline_comment_prefixes=None, strict=True, empty_lines_in_values=True, default_section=configparser.DEFAULTSECT, interpolation=BasicInterpolation(), converters={}, allow_unnamed_section=False)

   La *config parser* principal. Si se proporciona *defaults*, su
   valor es inicializado en el diccionario de valores por defecto
   intrínsecos. Si se proporciona *dict_type*, se utiliza para crear
   el diccionario de objetos para la lista de secciones, las opciones
   dentro de una sección, y los valores por defecto.

   Si se proporciona *delimiters*, se utiliza como un conjunto de
   cadenas de caracteres que dividen las claves de los valores. Si se
   proporciona *comment_prefixes*, se utiliza como un conjunto de
   cadenas de caracteres que preceden a los comentarios, en líneas que
   estarían, de otro modo, vacías.  Los comentarios pueden estar
   indentados. Si se proporciona *inline_comment_prefixes*, se utiliza
   como un conjunto de cadenas de caracteres que preceden a los
   comentarios en líneas que no están vacías.

   Cuando *strict* es "True" (por defecto), el *parser* no permitirá
   duplicados en ninguna sección u opción, al realizar la lectura de
   una sola fuente (archivo, cadena de caracteres o diccionario),
   generando una excepción "DuplicateSectionError" ó
   "DuplicateOptionError".  Cuando *empty_lines_in_values* es "False"
   (valor por defecto: "True"), cada línea en blanco indica el fin de
   una opción.  De otro modo, las líneas en blanco de una opción
   multilínea son tratadas como parte del valor de esta. Cuando
   *allow_no_value* es "True" (valor por defecto: "False"), se aceptan
   opciones sin valores; el valor que toman esas opciones es "None" y
   serán serializadas sin el delimitador final.

   Cuando se proporciona *default_section*, se define el nombre de la
   sección especial que contiene valores por defecto para otras
   secciones y con propósito de interpolación (habitualmente
   denominada ""DEFAULT""). Este valor puede obtenerse y modificarse
   en tiempo de ejecución utilizando el atributo de instancia
   "default_section". Esto no volverá a evaluar un fichero de
   configuración previamente analizado sintácticamente (*parsed*),
   pero se usará al escribir configuraciones de analizado sintáctico
   (*parsed*) en un nuevo fichero de configuración.

   La interpolación puede personalizarse al proporcionar un gestor
   personalizado, mediante el argumento *interpolation*. El valor
   "None" se utiliza para desactivar la interpolación completamente,
   "ExtendedInterpolation()" proporciona una variante avanzada,
   inspirada en "zc.buildout". Más al respecto puede encontrarse en la
   correspondiente sección de la documentación.

   Todos los nombres de opción que se utilizan en la interpolación
   pasarán por el método "optionxform()", igual que cualquier otra
   referencia a un nombre de opción. Por lo tanto, si se utiliza la
   implementación por defecto de "optionxform()" (la cual convierte
   los nombres de opción a minúsculas), los valores "foo %(bar)s" y
   "foo %(BAR)s" son equivalentes.

   When *converters* is given, it should be a dictionary where each
   key represents the name of a type converter and each value is a
   callable implementing the conversion from string to the desired
   datatype.  Every converter gets its own corresponding "get*()"
   method on the parser object and section proxies.

   When *allow_unnamed_section* is "True" (default: "False"), the
   first section name can be omitted. See the "Unnamed Sections"
   section.

   It is possible to read several configurations into a single
   "ConfigParser", where the most recently added configuration has the
   highest priority. Any conflicting keys are taken from the more
   recent configuration while the previously existing keys are
   retained. The example below reads in an "override.ini" file, which
   will override any conflicting keys from the "example.ini" file.

      [DEFAULT]
      ServerAliveInterval = -1

      >>> config_override = configparser.ConfigParser()
      >>> config_override['DEFAULT'] = {'ServerAliveInterval': '-1'}
      >>> with open('override.ini', 'w') as configfile:
      ...     config_override.write(configfile)
      ...
      >>> config_override = configparser.ConfigParser()
      >>> config_override.read(['example.ini', 'override.ini'])
      ['example.ini', 'override.ini']
      >>> print(config_override.get('DEFAULT', 'ServerAliveInterval'))
      -1

   Distinto en la versión 3.1: El valor por defecto de *dict_type* es
   "collections.OrderedDict".

   Distinto en la versión 3.2: se agregaron los argumentos
   *allow_no_value*, *delimiters*, *comment_prefixes*, *strict*,
   *empty_lines_in_values*, *default_section* y *interpolation*.

   Distinto en la versión 3.5: Se agregó el argumento *converters*.

   Distinto en la versión 3.7: The *defaults* argument is read with
   "read_dict()", providing consistent behavior across the parser:
   non-string keys and values are implicitly converted to strings.

   Distinto en la versión 3.8: El valor por defecto para *dict_type*
   es "dict", dado que este ahora preserva el orden de inserción.

   Distinto en la versión 3.13: Raise a "MultilineContinuationError"
   when *allow_no_value* is "True", and a key without a value is
   continued with an indented line.

   Distinto en la versión 3.13: The *allow_unnamed_section* argument
   was added.

   defaults()

      Retorna un diccionario que contiene los valores por defecto para
      toda la instancia.

   sections()

      Retorna una lista de las secciones disponibles; *default
      section* no se incluye en la lista.

   add_section(section)

      Agrega una sección llamada *section* a la instancia. Si ya
      existe una sección con el nombre proporcionado, se genera la
      excepción "DuplicateSectionError". Si se suministra el nombre
      *default section*, se genera la excepción "ValueError". El
      nombre de la sección debe ser una cadena de caracteres, de lo
      contrario, se genera la excepción "TypeError".

      Distinto en la versión 3.2: Nombres de sección que no sean del
      tipo cadena de caracteres generan la excepción "TypeError".

   has_section(section)

      Indica si la sección de nombre *section* existe en la
      configuración. No se permite *default section*.

   options(section)

      Retorna una lista de opciones disponibles en la sección
      especificada.

   has_option(section, option)

      Si la sección indicada existe, y esta contiene las opción
      proporcionada, retorna "True"; de lo contrario, retorna "False".
      Si la sección especificada es "None" o una cadena de caracteres
      vacía, se asume DEFAULT.

   read(filenames, encoding=None)

      Intenta leer y analizar sintácticamente (*parse*) un iterable de
      nombres de archivos, retornando una lista de nombres de archivos
      que han sido analizados (*parsed*) con éxito.

      Si *filenames* es una cadena de caracteres, un objeto "bytes" o
      un *path-like object*, es tratado como un simple nombre de
      archivo. Si un archivo mencionado en *filenames* no puede ser
      abierto, será ignorado. Está diseñado de forma que puedas
      especificar un iterable de potenciales ubicaciones para archivos
      de configuración (por ejemplo, el directorio actual, el
      directorio *home* del usuario, o algún directorio del sistema),
      y todos los archivos de configuración existentes serán leídos.

      Si no existe ninguno de los archivos mencionados, la instancia
      de "ConfigParser" contendrá un conjunto de datos vacío. Una
      aplicación que requiera valores iniciales, que sean cargados
      desde un archivo,  deberá cargar el(los) archivo(s) requerido(s)
      utilizando "read_file()" antes de llamar a "read()" para
      cualquier otro archivo opcional:

         import configparser, os

         config = configparser.ConfigParser()
         config.read_file(open('defaults.cfg'))
         config.read(['site.cfg', os.path.expanduser('~/.myapp.cfg')],
                     encoding='cp1250')

      Distinto en la versión 3.2: Added the *encoding* parameter.
      Previously, all files were read using the default encoding for
      "open()".

      Distinto en la versión 3.6.1: El parámetro *filenames* acepta un
      *path-like object*.

      Distinto en la versión 3.7: El parámetro *filenames* acepta un
      objeto "bytes".

   read_file(f, source=None)

      Leer y analizar (*parse*) los datos de configuración de *f*, el
      cual debe ser un iterable que retorne cadenas de caracteres
      Unicode (por ejemplo, archivos abiertos en modo texto).

      Optional argument *source* specifies the name of the file being
      read.  If not given and *f* has a "name" attribute, that is used
      for *source*; the default is "'<???>'".

      Added in version 3.2: Replaces "readfp()".

   read_string(string, source='<string>')

      Analiza (*parse*) los datos de configuración desde una cadena de
      caracteres.

      El argumento opcional *source* especifica un nombre para la
      cadena de caracteres proporcionada, relativo al contexto. Si no
      se proporciona, se utiliza "'<string>'". Esto, por lo general,
      debería ser una ruta de archivo o una URL.

      Added in version 3.2.

   read_dict(dictionary, source='<dict>')

      Carga la configuración a partir de cualquier objeto que
      proporcione un método "items()", similar a un diccionario. Las
      claves son nombres de secciones, los valores son diccionarios
      con claves y valores que deben estar presentes en la sección. Si
      el tipo de diccionario utilizado preserva el orden, las
      secciones y sus claves serán agregados en orden. Los valores son
      convertidos a cadenas de caracteres de forma automática.

      El argumento opcional *source* especifica un nombre para el
      diccionario proporcionado, relativo al contexto. Si no se
      proporciona, se utiliza "<dict>".

      Este método puede utilizarse para copiar el estado entre
      *parsers*.

      Added in version 3.2.

   get(section, option, *, raw=False, vars=None[, fallback])

      Obtiene el valor de una *option* para la sección indicada. Si se
      proporciona *vars*, tiene que ser un diccionario. El valor de
      *option* será buscado en *vars* (si se proporciona), en
      *section* y en *DEFAULTSECT*, en ese orden. Si la clave no se
      encuentra, y se ha proporcionado *fallback*, este es utilizado
      como un valor de contingencia. Se puede utilizar "None" como
      valor de contingencia (*fallback*).

      Todas las interpolaciones "'%'" son expandidas en el valor
      retornado, a menos que el argumento *raw* sea *true*. Los
      valores para la interpolación de las claves son buscados de la
      misma forma que para la opción.

      Distinto en la versión 3.2: Los argumentos *raw*, *vars* y
      *fallback* son argumentos nombrados solamente, a fin de proteger
      a los usuarios de los intentos de emplear el tercer argumento
      como el valor de contingencia de *fallback* (especialmente
      cuando se utiliza el protocolo de mapeo).

   getint(section, option, *, raw=False, vars=None[, fallback])

      Un cómodo método para forzar a entero el valor de la opción de
      la sección indicada. Revise "get()" para una explicación acerca
      de *raw*, *vars* y *fallback*.

   getfloat(section, option, *, raw=False, vars=None[, fallback])

      A convenience method which coerces the *option* in the specified
      *section* to a floating-point number.  See "get()" for
      explanation of *raw*, *vars* and *fallback*.

   getboolean(section, option, *, raw=False, vars=None[, fallback])

      Un cómodo método para forzar a booleano el valor de la opción de
      la sección indicada. Tome nota que los valores aceptados para la
      opción son "'1'", "'yes'", "'true'", and "'on'", para que el
      método retorne "True", y "'0'", "'no'", "'false'", y "'off'"
      para que el método retorne "False". Esos valores de cadenas de
      caracteres son revisados sin diferenciar mayúsculas de
      minúsculas. Cualquier otro valor ocasionará que se genere la
      excepción "ValueError". Revise "get()" para una explicación
      acerca de *raw*, *vars* y *fallback*.

   items(raw=False, vars=None)
   items(section, raw=False, vars=None)

      Cuando no se proporciona el argumento *section*, retorna una
      lista de pares *section_name*, *section_proxy*, incluyendo
      DEFAULTSECT.

      De lo contrario, retorna una lista de pares *name*, *value* para
      las opciones de la sección especificada. Los argumentos
      opcionales tienen el mismo significado que en el método "get()".

      Distinto en la versión 3.8: Los elementos que estén en *vars* no
      aparecen en el resultado. El comportamiento previo mezcla las
      opciones actuales del *parser* con las variables proporcionadas
      para la interpolación.

   set(section, option, value)

      Si la sección indicada existe, asigna el valor especificado a la
      opción indicada; en caso contrario, genera la excepción
      "NoSectionError". *option* y *value* deben ser cadenas de
      caracteres; de lo contrario, se genera la excepción "TypeError".

   write(fileobject, space_around_delimiters=True)

      Escribe una representación de la configuración al *file object*
      especificado, el cual debe ser abierto en modo texto (aceptando
      cadenas de caracteres). Esta representación puede ser analizada
      (*parsed*) por una posterior llamada a "read()". Si
      *space_around_delimiters* es *true*, los delimitadores entre
      claves y valores son rodeados por espacios.

      Distinto en la versión 3.14: Raises InvalidWriteError if this
      would write a representation which cannot be accurately parsed
      by a future "read()" call from this parser.

   Nota:

     Los comentarios presentes en el fichero original no se mantienen
     cuando se vuelve a escribir la configuración. Qué es considerado
     un comentario depende de los valores asignados a *comment_prefix*
     e *inline_comment_prefix*.

   remove_option(section, option)

      Elimina la opción especificada de la sección indicada. Si la
      sección no existe, se genera una excepción "NoSectionError". Si
      la opción existía antes de la eliminación, retorna "True"; de lo
      contrario retorna "False".

   remove_section(section)

      Elimina la sección especificada de la configuración. Si la
      sección existía, retorna "True". De lo contrario, retorna
      "False".

   optionxform(option)

      Transforma el nombre de opción *option* de la forma en que se
      encontraba en el archivo de entrada o como fue pasada por el
      código del cliente, a la forma en que debe ser utilizada en las
      estructuras internas. La implementación por defecto retorna una
      versión en minúsculas de *option*; las subclases pueden sobre-
      escribirla o el código del cliente puede asignar un atributo de
      su nombre en las instancias, para afectar su comportamiento.

      No necesitas crear una subclase del *parser* para utilizar este
      método, ya que también puedes asignarlo en una instancia a una
      función, la cual reciba una cadena de caracteres como argumento
      y retorne otra. Por ejemplo, estableciéndola a "str", se hará
      que los nombres de opciones sean sensibles a mayúsculas y
      minúsculas:

         cfgparser = ConfigParser()
         cfgparser.optionxform = str

      Tome en cuenta que cuando se leen archivos de configuración, los
      espacios en blanco alrededor de los nombres de opción son
      eliminados antes de llamar a "optionxform()".

configparser.UNNAMED_SECTION

   A special object representing a section name used to reference the
   unnamed section (see Unnamed Sections).

configparser.MAX_INTERPOLATION_DEPTH

   The maximum depth for recursive interpolation for "get()" when the
   *raw* parameter is false.  This is relevant only when the default
   *interpolation* is used.

## Objetos RawConfigParser

class configparser.RawConfigParser(defaults=None, dict_type=dict, allow_no_value=False, *, delimiters=('=', ':'), comment_prefixes=('#', ';'), inline_comment_prefixes=None, strict=True, empty_lines_in_values=True, default_section=configparser.DEFAULTSECT, interpolation=BasicInterpolation(), converters={}, allow_unnamed_section=False)

   Variante heredada de "ConfigParser". Tiene la interpolación
   deshabilitada por defecto y permite nombres de sección que no sean
   cadenas de caracteres, nombres de opciones, y valores a través de
   sus métodos inseguros "add_section" y "set", así como el manejo
   heredado del argumento nombrado "defaults=".

   Distinto en la versión 3.2: se agregaron los argumentos
   *allow_no_value*, *delimiters*, *comment_prefixes*, *strict*,
   *empty_lines_in_values*, *default_section* y *interpolation*.

   Distinto en la versión 3.5: Se agregó el argumento *converters*.

   Distinto en la versión 3.8: El valor por defecto para *dict_type*
   es "dict", dado que este ahora preserva el orden de inserción.

   Distinto en la versión 3.13: The *allow_unnamed_section* argument
   was added.

   Nota:

     Considere el uso de "ConfigParser" en su lugar, el cual verifica
     los tipos de datos de los valores que se almacenarán
     internamente. Si no quieres la interpolación, puedes utilizar
     "ConfigParser(interpolation=None)".

   add_section(section)

      Add a section named *section* or "UNNAMED_SECTION" to the
      instance.

      If the given section already exists, "DuplicateSectionError" is
      raised. If the *default section* name is passed, "ValueError" is
      raised. If "UNNAMED_SECTION" is passed and support is disabled,
      "UnnamedSectionDisabledError" is raised.

      No se comprueba el tipo de datos de *section*, con lo cual se
      permite que los usuarios creen secciones con nombres que no sean
      cadenas de caracteres. Este comportamiento no está soportado y
      puede ocasionar errores internos.

   Distinto en la versión 3.14: Added support for "UNNAMED_SECTION".

   set(section, option, value)

      Si existe la sección indicada, asigna el valor especificado a la
      sección indicada; de lo contrario, genera la excepción
      "NoSectionError". Aunque es posible utilizar "RawConfigParser"
      (ó "ConfigParser" con parámetros *raw* con valor *true*) como
      almacenamiento interno para valores que no sean cadenas de
      caracteres, el funcionamiento completo (incluyendo la
      interpolación y escritura en archivos) sólo puede lograrse
      utilizando valores del tipo cadena de caracteres.

      Este método permite que los usuarios asignen valores que no sean
      cadenas de caracteres a las claves, internamente. Este
      comportamiento no está soportado y causará errores cuando se
      intente escribir en un archivo o cuando se intente obtenerlo en
      un modo no *raw*. **Utilice la API del protocolo de mapeo**, la
      cual no permite ese tipo de asignaciones.

## Excepciones

exception configparser.Error

   Base class for all other "configparser" exceptions.

exception configparser.NoSectionError

   Excepción generada cuando no se encuentra una sección especificada.

exception configparser.DuplicateSectionError

   Exception raised if "add_section()" is called with the name of a
   section that is already present or in strict parsers when a section
   if found more than once in a single input file, string or
   dictionary.

   Distinto en la versión 3.2: Added the optional *source* and
   *lineno* attributes and parameters to "__init__()".

exception configparser.DuplicateOptionError

   Excepción generada por *parsers* estrictos si una sola opción
   aparece dos veces durante la lectura de un solo archivo, cadena de
   caracteres o diccionario. Captura errores de escritura o
   relacionados con el uso de mayúsculas y minúsculas, ej. un
   diccionario podría tener dos claves que representan la misma clave
   de configuración bajo un esquema insensible a mayúsculas y
   minúsculas.

exception configparser.NoOptionError

   Excepción generada cuando una opción especificada no se encuentra
   en una sección indicada.

exception configparser.InterpolationError

   Clase base para excepciones generadas por problemas que ocurren al
   realizar la interpolación de cadenas de caracteres.

exception configparser.InterpolationDepthError

   Excepción generada cuando la interpolación de cadenas de caracteres
   no puede completarse, debido a que el número de iteraciones excede
   a "MAX_INTERPOLATION_DEPTH". Subclase de "InterpolationError".

exception configparser.InterpolationMissingOptionError

   Excepción generada cuando no existe una opción referida por un
   valor. Subclase de "InterpolationError".

exception configparser.InterpolationSyntaxError

   Excepción generada cuando el texto fuente, donde se realizan las
   sustituciones, no se ajusta a la sintaxis requerida. Subclase de
   "InterpolationError".

exception configparser.MissingSectionHeaderError

   Excepción generada cuando se intenta analizar (*parse*) un archivo
   que no tiene encabezados de sección.

exception configparser.ParsingError

   Excepción generada cuando ocurren errores intentando analizar
   (*parse*) un archivo.

   Distinto en la versión 3.12: The "filename" attribute and
   "__init__()" constructor argument were removed.  They have been
   available using the name "source" since 3.2.

exception configparser.MultilineContinuationError

   Exception raised when a key without a corresponding value is
   continued with an indented line.

   Added in version 3.13.

exception configparser.UnnamedSectionDisabledError

   Exception raised when attempting to use the "UNNAMED_SECTION"
   without enabling it.

      Added in version 3.14.

exception configparser.InvalidWriteError

   Exception raised when an attempted "ConfigParser.write()" would not
   be parsed accurately with a future "ConfigParser.read()" call.

   Ex: Writing a key beginning with the "ConfigParser.SECTCRE" pattern
   would parse as a section header when read. Attempting to write this
   will raise this exception.

   Added in version 3.14.

-[ Notas al pie ]-

[1] Los *config parsers* permiten una gran personalización. Si estás
    interesado en modificar el comportamiento descrito por la
    referencia de la nota al pie, consulta la sección Customizing
    Parser Behaviour.
