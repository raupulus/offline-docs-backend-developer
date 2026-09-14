---
title: '"zoneinfo" --- IANA time zone support'
source_url: https://docs.python.org/es/3
source_path: library/zoneinfo.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 4730
---

# "zoneinfo" --- IANA time zone support

Added in version 3.9.

**Código fuente:** Lib/zoneinfo

======================================================================

The "zoneinfo" module provides a concrete time zone implementation to
support the IANA time zone database as originally specified in **PEP
615**. By default, "zoneinfo" uses the system's time zone data if
available; if no system time zone data is available, the library will
fall back to using the first-party tzdata package available on PyPI.

Ver también:

  Modulo: "datetime"
     Proporciona los tipos "time" y "datetime" con los que está
     diseñada la clase "ZoneInfo".

  Package tzdata
     Paquete de origen mantenido por los desarrolladores del núcleo de
     CPython para suministrar datos de zonas horarias a través de
     PyPI.

Availability: not WASI.

This module does not work or is not available on WebAssembly. See
Plataformas WebAssembly for more information.

## Usando "ZoneInfo"

"ZoneInfo" es una implementación concreta de la clase base abstracta
"datetime.tzinfo", y está pensada para ser adjuntada a "tzinfo", bien
a través del constructor, del método "datetime.replace" o de
"datetime.astimezone":

   >>> from zoneinfo import ZoneInfo
   >>> import datetime as dt

   >>> when = dt.datetime(2020, 10, 31, 12, tzinfo=ZoneInfo("America/Los_Angeles"))
   >>> print(when)
   2020-10-31 12:00:00-07:00

   >>> when.tzname()
   'PDT'

Las fechas construidas de esta manera son compatibles con la
aritmética de fechas y manejan las transiciones del horario de verano
sin ninguna otra intervención:

   >>> when_add = when + dt.timedelta(days=1)

   >>> print(when_add)
   2020-11-01 12:00:00-08:00

   >>> when_add.tzname()
   'PST'

Estas zonas horarias también soportan el atributo "fold" introducido
en **PEP 495**.  Durante las transiciones de desfase que inducen
tiempos ambiguos (como una transición de horario de verano a horario
estándar), se utiliza el desfase de *antes* de la transición cuando
"fold=0", y el desfase *después* de la transición cuando "fold=1", por
ejemplo:

   >>> when = dt.datetime(2020, 11, 1, 1, tzinfo=ZoneInfo("America/Los_Angeles"))
   >>> print(when)
   2020-11-01 01:00:00-07:00

   >>> print(when.replace(fold=1))
   2020-11-01 01:00:00-08:00

Al convertir desde otra zona horaria, el pliegue se ajustará al valor
correcto:

   >>> LOS_ANGELES = ZoneInfo("America/Los_Angeles")
   >>> when_utc = dt.datetime(2020, 11, 1, 8, tzinfo=dt.timezone.utc)

   >>> # Before the PDT -> PST transition
   >>> print(when_utc.astimezone(LOS_ANGELES))
   2020-11-01 01:00:00-07:00

   >>> # After the PDT -> PST transition
   >>> print((when_utc + dt.timedelta(hours=1)).astimezone(LOS_ANGELES))
   2020-11-01 01:00:00-08:00

## Fuentes de datos

The "zoneinfo" module does not directly provide time zone data, and
instead pulls time zone information from the system time zone database
or the first-party PyPI package tzdata, if available. Some systems,
including notably Windows systems, do not have an IANA database
available, and so for projects targeting cross-platform compatibility
that require time zone data, it is recommended to declare a dependency
on tzdata. If neither system data nor tzdata are available, all calls
to "ZoneInfo" will raise "ZoneInfoNotFoundError".

### Configurando los orígenes de datos

Cuando se llama a "ZoneInfo(key)", el constructor busca primero en los
directorios especificados en "TZPATH" un archivo que coincida con
"key", y en caso de fallo busca una coincidencia en el paquete tzdata.
Este comportamiento puede configurarse de tres maneras:

1. El "TZPATH" por defecto cuando no se especifica otra cosa puede
   configurarse en tiempo de compilación.

2. "TZPATH" puede configurarse utilizando una variable de entorno.

3. En runtime, la ruta de búsqueda puede ser manipulada usando la
   función "reset_tzpath()".

#### Configuración en tiempo de compilación

El "TZPATH" predeterminado incluye varias ubicaciones de
implementación comunes para la base de datos de la zona horaria
(excepto en Windows, donde no hay ubicaciones "conocidas" para los
datos de la zona horaria). En los sistemas POSIX, los distribuidores
posteriores y aquellos que compilan Python desde la fuente que saben
dónde se implementan los datos de la zona horaria del sistema pueden
cambiar la ruta de la zona horaria predeterminada especificando la
opción de tiempo de compilación "TZPATH" (o, más probablemente, el
"configure flag --with-tzpath"), que debería ser una cadena delimitada
por "os.pathsep".

En todas las plataformas, el valor configurado está disponible como la
clave "TZPATH" en "sysconfig.get_config_var()".

#### Configuración del entorno

Cuando se inicializa "TZPATH" (ya sea en el momento de la importación
o cuando se llama a "reset_tzpath()" sin argumentos), el módulo
"zoneinfo" utilizará la variable de entorno "PYTHONTZPATH", si existe,
para establecer la ruta de búsqueda.

PYTHONTZPATH

   Se trata de una cadena separada por "os.pathsep" que contiene la
   ruta de búsqueda de la zona horaria a utilizar. Debe consistir sólo
   en rutas absolutas y no relativas. Los componentes relativos
   especificados en "PYTHONTZPATH" no se utilizarán, pero por lo demás
   el comportamiento cuando se especifica una ruta relativa es
   definido por la implementación; CPython lanzará
   "InvalidTZPathWarning", pero otras implementaciones son libres de
   ignorar silenciosamente el componente erróneo o lanzar una
   excepción.

Para que el sistema ignore los datos del sistema y utilice el paquete
tzdata en su lugar, establezca "PYTHONTZPATH=""".

#### Configuración de tiempo de ejecución

La ruta de búsqueda de TZ también puede configurarse en tiempo de
ejecución mediante la función "reset_tzpath()". Por lo general, esta
operación no es aconsejable, aunque es razonable utilizarla en
funciones de prueba que requieran el uso de una ruta de zona horaria
específica (o que requieran deshabilitar el acceso a las zonas
horarias del sistema).

## La clase "ZoneInfo"

class zoneinfo.ZoneInfo(key)

   Una subclase concreta de "datetime.tzinfo" que representa una zona
   horaria IANA especificada por la cadena "key". Las llamadas al
   constructor primario siempre devolverán objetos que se comparan de
   forma idéntica; dicho de otro modo, salvo la invalidación de la
   caché mediante "ZoneInfo.clear_cache()", para todos los valores de
   "key", la siguiente afirmación siempre será verdadera:

      a = ZoneInfo(key)
      b = ZoneInfo(key)
      assert a is b

   La "key" debe tener la forma de una ruta POSIX relativa y
   normalizada, sin referencias de nivel superior. El constructor
   lanzará "ValueError" si se pasa una clave no conforme.

   Si no se encuentra ningún archivo que coincida con la "clave", el
   constructor lanzará "ZoneInfoNotFoundError".

La clase "ZoneInfo" tiene dos constructores alternativos:

classmethod ZoneInfo.from_file(file_obj, /, key=None)

   Construye un objeto "ZoneInfo" a partir de un objeto tipo archivo
   que retorna bytes (por ejemplo, un archivo abierto en modo binario
   o un objeto "io.BytesIO"). A diferencia del constructor primario,
   éste siempre construye un nuevo objeto.

   El parámetro "key" establece el nombre de la zona a efectos de
   "__str__()" y "__repr__()".

   Los objetos creados a través de este constructor no pueden ser
   serializados (ver pickling).

   "ValueError" is raised if the data read from *file_obj* is not a
   valid TZif file.

classmethod ZoneInfo.no_cache(key)

   Un constructor alternativo que omite la caché del constructor. Es
   idéntico al constructor principal, pero retorna un nuevo objeto en
   cada llamada. Es muy probable que esto sea útil para propósitos de
   prueba o demostración, pero también se puede utilizar para crear un
   sistema con una estrategia de invalidación de caché diferente.

   Los objetos creados a través de este constructor también pasarán
   por encima de la caché de un proceso de deserialización cuando sean
   deserializados.

   Prudencia:

     El uso de este constructor puede cambiar la semántica de tus
     datetimes de manera sorprendente, sólo úsalo si sabes que lo
     necesitas.

También están disponibles los siguientes métodos de clase:

classmethod ZoneInfo.clear_cache(*, only_keys=None)

   Un método para invalidar la caché de la clase "ZoneInfo". Si no se
   pasan argumentos, se invalidan todas las cachés y la siguiente
   llamada al constructor primario de cada clave devolverá una nueva
   instancia.

   Si se pasa un iterable de nombres de claves al parámetro
   "only_keys", sólo se eliminarán de la caché las claves
   especificadas. Las claves pasadas a "only_keys" pero que no se
   encuentran en la caché se ignoran.

   Advertencia:

     Invocar esta función puede cambiar la semántica de las fechas y
     horas que utilizan "ZoneInfo" de formas sorprendentes; esto
     modifica el estado del módulo y, por lo tanto, puede tener
     efectos de gran alcance. Utilícela solo si sabe que la necesita.

La clase tiene un atributo:

ZoneInfo.key

   Se trata de un *attribute* de sólo lectura que retorna el valor de
   "key" pasado al constructor, que debe ser una clave de búsqueda en
   la base de datos de zonas horarias de la IANA (por ejemplo,
   "America/New_York", "Europe/Paris" o "Asia/Tokyo".

   Para las zonas construidas a partir de un archivo sin especificar
   un parámetro "key", se establecerá como "None".

   Nota:

     Aunque es una práctica algo común exponerlos a los usuarios
     finales, estos valores están diseñados para ser claves primarias
     para representar las zonas relevantes y no necesariamente
     elementos orientados al usuario.  Se pueden utilizar proyectos
     como CLDR (Unicode Common Locale Data Repository) para obtener
     cadenas más fáciles de usar a partir de estas claves.

### Representaciones de cadenas

La representación de cadena que se retorna al llamar a "str" sobre un
objeto "ZoneInfo" utiliza por defecto el atributo "ZoneInfo.key" (ver
la nota de uso en la documentación del atributo):

   >>> zone = ZoneInfo("Pacific/Kwajalein")
   >>> str(zone)
   'Pacific/Kwajalein'

   >>> when = dt.datetime(2020, 4, 1, 3, 15, tzinfo=zone)
   >>> f"{when.isoformat()} [{when.tzinfo}]"
   '2020-04-01T03:15:00+12:00 [Pacific/Kwajalein]'

Para los objetos construidos a partir de un fichero sin especificar un
parámetro "key", "str" vuelve a llamar a "repr`()". El parámetro
"repr" de "ZoneInfo" está definido por la implementación y no es
necesariamente estable entre versiones, pero se garantiza que no es
una clave válida de "ZoneInfo".Pickled.

### Serialización de Pickle

En lugar de serializar todos los datos de transición, los objetos
"ZoneInfo" se serializan por clave, y los objetos "ZoneInfo"
construidos a partir de archivos (incluso los que tienen un valor por
"key" especifico) no pueden ser serializados.

El comportamiento de un archivo "ZoneInfo" depende de cómo se haya
construido:

1. "ZoneInfo(key)": When constructed with the primary constructor, a
   "ZoneInfo" object is serialized by key, and when deserialized, the
   deserializing process uses the primary and thus it is expected that
   these are the same object as other references to the same time
   zone.  For example, if "europe_berlin_pkl" is a string containing a
   pickle constructed from "ZoneInfo("Europe/Berlin")", one would
   expect the following behavior:

      >>> a = ZoneInfo("Europe/Berlin")
      >>> b = pickle.loads(europe_berlin_pkl)
      >>> a is b
      True

2. "ZoneInfo.no_cache(key)": Cuando se construye a partir del
   constructor que evita la caché, el objeto "ZoneInfo" también se
   serializa por clave, pero cuando se deserializa, el proceso de
   deserialización utiliza el constructor que evita la caché. Si
   "europe_berlin_pkl_nc" es una cadena que contiene un pickle
   construido a partir de "ZoneInfo.no_cache("Europe/Berlin")", cabría
   esperar el siguiente comportamiento:

      >>> a = ZoneInfo("Europe/Berlin")
      >>> b = pickle.loads(europe_berlin_pkl_nc)
      >>> a is b
      False

3. "ZoneInfo.from_file(file_obj, /, key=None)": When constructed from
   a file, the "ZoneInfo" object raises an exception on pickling. If
   an end user wants to pickle a "ZoneInfo" constructed from a file,
   it is recommended that they use a wrapper type or a custom
   serialization function: either serializing by key or storing the
   contents of the file object and serializing that.

Este método de serialización requiere que los datos de la zona horaria
para la clave requerida estén disponibles tanto en el lado de
serialización como en el de deserialización, de forma similar a como
se espera que las referencias a las clases y funciones existan tanto
en el entorno de serialización como en el de deserialización. También
significa que no se garantiza la consistencia de los resultados cuando
se retira un "ZoneInfo" recogido en un entorno con una versión
diferente de los datos de la zona horaria.

## Funciones

zoneinfo.available_timezones()

   Obtiene un conjunto que contiene todas las claves válidas para las
   zonas horarias de la IANA disponibles en cualquier lugar de la ruta
   de zonas horarias. Se recalcula en cada llamada a la función.

   Esta función sólo incluye los nombres de zona canónicos y no
   incluye las zonas "especiales" como las que se encuentran bajo los
   directorios "posix/" y "right/", o la zona "posixrules".

   Prudencia:

     Esta función puede abrir un gran número de archivos, ya que la
     mejor manera de determinar si un archivo en la ruta de la zona
     horaria es una zona horaria válida es leer la "magic string"
     (cadena mágica) al principio.

   Nota:

     Estos valores no están diseñados para ser expuestos a los
     usuarios finales; para los elementos de cara al usuario, las
     aplicaciones deberían utilizar algo como CLDR (el Unicode Common
     Locale Data Repository) para obtener cadenas más fáciles de usar.
     Véase también la nota de advertencia sobre "ZoneInfo.key".

zoneinfo.reset_tzpath(to=None)

   Establece o restablece la ruta de búsqueda de la zona horaria
   ("TZPATH") para el módulo. Cuando se llama sin argumentos, "TZPATH"
   se establece en el valor por defecto.

   La llamada a "reset_tzpath" no invalidará la caché de "ZoneInfo",
   por lo que las llamadas al constructor primario de "ZoneInfo" sólo
   utilizarán el nuevo "TZPATH" en caso de que se pierda la caché.

   El parámetro "to" debe ser un *sequence* de cadenas o "os.PathLike"
   y no una cadena, todos los cuales deben ser rutas absolutas.
   "ValueError" se lanzará si se pasa algo que no sea una ruta
   absoluta.

## Globales

zoneinfo.TZPATH

   Una secuencia de sólo lectura que representa la ruta de búsqueda de
   zonas horarias -- cuando se construye un "ZoneInfo" a partir de una
   clave, la clave se une a cada entrada del "TZPATH", y se utiliza el
   primer archivo encontrado.

   "TZPATH" sólo puede contener rutas absolutas, nunca relativas,
   independientemente de cómo esté configurado.

   El objeto al que apunta "zoneinfo.TZPATH" puede cambiar en
   respuesta a una llamada a "reset_tzpath()", por lo que se
   recomienda utilizar "zoneinfo.TZPATH" en lugar de importar "TZPATH"
   desde "zoneinfo" o asignar una variable de larga duración a
   "zoneinfo.TZPATH".

   Para más información sobre la configuración de la ruta de búsqueda
   de zonas horarias, consulte Configurando los orígenes de datos.

## Excepciones y advertencias

exception zoneinfo.ZoneInfoNotFoundError

   Se lanza cuando la construcción de un objeto "ZoneInfo" falla
   porque la clave especificada no puede encontrarse en el sistema. Es
   una subclase de "KeyError".

exception zoneinfo.InvalidTZPathWarning

   Se lanza cuando "PYTHONTZPATH" contiene un componente no válido que
   será filtrado, como una ruta relativa.
