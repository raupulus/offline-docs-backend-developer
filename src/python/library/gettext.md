---
title: '"gettext" --- Multilingual internationalization services'
source_url: https://docs.python.org/es/3
source_path: library/gettext.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 2740
---

# "gettext" --- Multilingual internationalization services

**Código fuente:** Lib/gettext.py

======================================================================

The "gettext" module provides internationalization (I18N) and
localization (L10N) services for your Python modules and applications.
It supports both the GNU **gettext** message catalog API and a higher
level, class-based API that may be more appropriate for Python files.
The interface described below allows you to write your module and
application messages in one natural language, and provide a catalog of
translated messages for running under different natural languages.

También se dan algunas sugerencias para localizar sus módulos y
aplicaciones Python.

## GNU API **gettext**

The "gettext" module defines the following API, which is very similar
to the GNU **gettext** API.  If you use this API you will affect the
translation of your entire application globally.  Often this is what
you want if your application is monolingual, with the choice of
language dependent on the locale of your user.  If you are localizing
a Python module, or if your application needs to switch languages on
the fly, you probably want to use the class-based API instead.

gettext.bindtextdomain(domain, localedir=None)

   Bind the *domain* to the locale directory *localedir*.  More
   concretely, "gettext" will look for binary ".mo" files for the
   given domain using the path (on Unix):
   "*localedir*/*language*/LC_MESSAGES/*domain*.mo", where *language*
   is searched for in the environment variables "LANGUAGE", "LC_ALL",
   "LC_MESSAGES", and "LANG" respectively.

   Si *localedir* se omite o es "None", se retorna el enlace actual
   para *domain*. [1]

gettext.textdomain(domain=None)

   Cambia o consulta el dominio global actual. Si *domain* es "None",
   se retorna el dominio global actual; de lo contrario, el dominio
   global se establece en *domain*, que se retorna.

gettext.gettext(message, /)

   Retorna la traducción localizada de *message*, basada en el dominio
   global actual, el idioma y el directorio de configuración regional.
   Esta función suele tener un alias como "_()" en el espacio de
   nombres local (ver ejemplos a continuación).

gettext.dgettext(domain, message, /)

   Como "gettext()", pero busque el mensaje en el *domain*
   especificado.

gettext.ngettext(singular, plural, n, /)

   Como "gettext()", pero considere formas plurales. Si se encuentra
   una traducción, aplique la fórmula plural a *n* y retorna el
   mensaje resultante (algunos idiomas tienen más de dos formas
   plurales). Si no se encuentra ninguna traducción, retorna
   *singular* if *n* es 1; retorna *plural* de lo contrario.

   La fórmula Plural se toma del encabezado del catálogo. Es una
   expresión C o Python que tiene una variable libre *n*; la expresión
   se evalúa como el índice del plural en el catálogo. Consulte la
   documentación de GNU gettext para conocer la sintaxis precisa que
   se utilizará en archivos ".po" y las fórmulas para un variedad de
   idiomas.

gettext.dngettext(domain, singular, plural, n, /)

   Como "ngettext()", pero busque el mensaje en el *domain*
   especificado.

gettext.pgettext(context, message, /)

gettext.dpgettext(domain, context, message, /)

gettext.npgettext(context, singular, plural, n, /)

gettext.dnpgettext(domain, context, singular, plural, n, /)

   Similar a las funciones correspondientes sin la "p" en el prefijo
   (es decir, "gettext()", "dgettext()", "ngettext()", "dngettext()"),
   pero la traducción está restringida al mensaje dado *context*.

   Added in version 3.8.

Tenga en cuenta que **gettext** de GNU también define un método
"dcgettext()", pero esto no se consideró útil, por lo que actualmente
no está implementado.

Aquí hay un ejemplo del uso típico de esta API:

   import gettext
   gettext.bindtextdomain('myapplication', '/path/to/my/language/directory')
   gettext.textdomain('myapplication')
   _ = gettext.gettext
   # ...
   print(_('This is a translatable string.'))

## API basada en clases

The class-based API of the "gettext" module gives you more flexibility
and greater convenience than the GNU **gettext** API.  It is the
recommended way of localizing your Python applications and modules.
"gettext" defines a "GNUTranslations" class which implements the
parsing of GNU ".mo" format files, and has methods for returning
strings. Instances of this class can also install themselves in the
built-in namespace as the function "_()".

gettext.find(domain, localedir=None, languages=None, all=False)

   Esta función implementa el algoritmo de búsqueda de archivos
   estándar ".mo". Toma un *domain*, idéntico al que toma
   "textdomain()". Opcional *localedir* es como en "bindtextdomain()".
   *languages* opcionales es una lista de cadenas, donde cada cadena
   es un código de idioma.

   Si no se proporciona *localedir*, se utiliza el directorio de
   configuración regional predeterminado del sistema. [2] Si no se
   proporcionan *languages*, se buscan las siguientes variables de
   entorno: "LANGUAGE", "LC_ALL", "LC_MESSAGES", y "LANG". El primero
   que retorna un valor no vacío se usa para la variable *languages*.
   Las variables de entorno deben contener una lista de idiomas
   separados por dos puntos, que se dividirá en dos puntos para
   producir la lista esperada de cadenas de código de idioma.

   "find()" luego expande y normaliza los idiomas, y luego los itera,
   buscando un archivo existente construido con estos componentes:

   "*localedir*/*language*/LC_MESSAGES/*domain*.mo"

   El primer nombre de archivo que existe es retornado por "find()".
   Si no se encuentra dicho archivo, se retorna "None". Si se
   proporciona *all*, retorna una lista de todos los nombres de
   archivo, en el orden en que aparecen en la lista de idiomas o las
   variables de entorno.

gettext.translation(domain, localedir=None, languages=None, class_=None, fallback=False)

   Retorna una instancia de "*Translations" basada en *domain*,
   *localedir* y *languages*, que primero se pasan a "find()" para
   obtener una lista de las rutas de archivos ".mo" asociadas. Las
   instancias con nombres de archivos ".mo" idénticos se almacenan en
   caché. La clase concreta instanciada es *class_* si se proporciona,
   de lo contrario será "GNUTranslations". El constructor de esta
   clase debe aceptar un único argumento de tipo *file object*.

   Si se encuentran varios archivos, los archivos posteriores se
   utilizan como retrocesos para los anteriores. Para permitir la
   configuración de la reserva, "copy.copy()" se utiliza para clonar
   cada objeto de traducción del caché; los datos de la instancia real
   aún se comparten con el caché.

   Si no se encuentra el archivo ".mo", esta función genera "OSError"
   si *fallback* es falso (que es el valor predeterminado) y retorna
   una instancia de "NullTranslations" si *fallback* is verdadero.

   Distinto en la versión 3.3: "IOError" used to be raised, it is now
   an alias of "OSError".

   Distinto en la versión 3.11: el parámetro *codeset* se removió.

gettext.install(domain, localedir=None, *, names=None)

   Esto instala la función "_()" en el espacio de nombres incorporado
   de Python, basado en *domain* y *localedir* que se pasan a la
   función "translation()".

   Para el parámetro *names*, consulte la descripción del método del
   objeto de traducción "install()".

   Como se ve a continuación, generalmente marca las cadenas en su
   aplicación que son candidatas para la traducción, envolviéndolas en
   una llamada a la función "_()", como esta:

      print(_('This string will be translated.'))

   Para mayor comodidad, desea que la función "_()" se instale en el
   espacio de nombres integrado de Python, para que sea fácilmente
   accesible en todos los módulos de su aplicación.

   Distinto en la versión 3.11: *names* ahora es un parámetro de solo
   palabra clave.

### La clase "NullTranslations"

Las clases de traducción son las que realmente implementan la
traducción de cadenas de mensajes del archivo fuente original a
cadenas de mensajes traducidas. La clase base utilizada por todas las
clases de traducción es "NullTranslations"; Esto proporciona la
interfaz básica que puede utilizar para escribir sus propias clases de
traducción especializadas. Estos son los métodos de
"NullTranslations":

class gettext.NullTranslations(fp=None)

   Toma un término opcional *file object* *fp*, que es ignorado por la
   clase base. Inicializa las variables de instancia "protegidas"
   *_info* y *_charset* que se establecen mediante clases derivadas,
   así como *_fallback*, que se establece a través de
   "add_fallback()". Luego llama a "self._parse(fp)" if *fp* no es
   "None".

   _parse(fp)

      No operativo en la clase base, este método toma el objeto de
      archivo *fp* y lee los datos del archivo, inicializando su
      catálogo de mensajes. Si tiene un formato de archivo de catálogo
      de mensajes no admitido, debe sobrescribir este método para
      analizar su formato.

   add_fallback(fallback)

      Agrega *fallback* como el objeto de respaldo para el objeto de
      traducción actual. Un objeto de traducción debe consultar la
      reserva si no puede proporcionar una traducción para un mensaje
      dado.

   gettext(message, /)

      Si se ha establecido una reserva, reenvíe "gettext()" a la
      reserva. De lo contrario, retorna *message*. Anulado en clases
      derivadas.

   ngettext(singular, plural, n, /)

      Si se ha establecido una reserva, reenvíe "ngettext()" a la
      reserva. De lo contrario, retorna *singular* si *n* es 1; volver
      *plural* de lo contrario. Anulado en clases derivadas.

   pgettext(context, message, /)

      Si se ha establecido una reserva, reenvía "pgettext()" a la
      reserva. De lo contrario, retorna el mensaje traducido. Anulado
      en clases derivadas.

      Added in version 3.8.

   npgettext(context, singular, plural, n, /)

      Si se ha establecido una reserva, reenvía "npgettext()" a la
      reserva. De lo contrario, retorna el mensaje traducido. Anulado
      en clases derivadas.

      Added in version 3.8.

   info()

      Return a dictionary containing the metadata found in the message
      catalog file.

   charset()

      Retorna la codificación del archivo de catálogo de mensajes.

   install(names=None)

      Este método instala "gettext()" en el espacio de nombres
      incorporado, vinculándolo a "_".

      Si se proporciona el parámetro *names*, debe ser una secuencia
      que contenga los nombres de las funciones que desea instalar en
      el espacio de nombres incorporado, además de "_()". Los nombres
      compatibles son "'gettext'", "'ngettext'", "'pgettext'" y
      "'npgettext'".

      Considere que esta es solo una manera, aunque la más
      conveniente, de hacer disponible la función "_()" en su
      aplicación. Ya que afecta a toda la aplicación de manera global,
      y en particular al espacio de nombres integrado, los módulos
      localizados nunca deben instalar "_()". En lugar de ello,
      deberían utilizar este código para hacer que "_()" esté
      disponible en su módulo:

         import gettext
         t = gettext.translation('mymodule', ...)
         _ = t.gettext

      Esto pone "_()" solo en el espacio de nombres global del módulo
      y, por lo tanto, solo afecta las llamadas dentro de este módulo.

      Distinto en la versión 3.8: Se agregó "'pgettext'" y
      "'npgettext'".

### La clase "GNUTranslations"

The "gettext" module provides one additional class derived from
"NullTranslations": "GNUTranslations".  This class overrides
"_parse()" to enable reading GNU **gettext** format ".mo" files in
both big-endian and little-endian format.

"GNUTranslations" parses optional metadata out of the translation
catalog. It is convention with GNU **gettext** to include metadata as
the translation for the empty string. This metadata is in **RFC
822**-style "key: value" pairs, and should contain the "Project-Id-
Version" key.  If the key "Content-Type" is found, then the "charset"
property is used to initialize the "protected" "_charset" instance
variable, defaulting to "None" if not found.  If the charset encoding
is specified, then all message ids and message strings read from the
catalog are converted to Unicode using this encoding, else ASCII is
assumed.

Ya que los identificadores de mensajes también se leen como cadenas
Unicode, todos los métodos "*gettext()" considerarán a los
identificadores de mensajes como cadenas Unicode, y no como cadenas de
bytes.

The entire set of key/value pairs are placed into a dictionary and set
as the "protected" "_info" instance variable.

Si el número mágico del archivo ".mo" no es válido, el número de
versión principal es inesperado, o si se producen otros problemas al
leer el archivo, se crea una instancia de "GNUTranslations" puede
generar "OSError".

class gettext.GNUTranslations

   Los siguientes métodos se anulan desde la implementación de la
   clase base:

   gettext(message, /)

      Busca el *message* id en el catálogo y retorna la cadena de
      caracteres de mensaje correspondiente, como una cadena Unicode.
      Si no hay una entrada en el catálogo para el *message* id, y se
      ha establecido una retroceso (*fallback*), la búsqueda se
      reenvía al método de retroceso "gettext()". De lo contrario, se
      retorna el *message* id.

   ngettext(singular, plural, n, /)

      Realiza una búsqueda de formas plurales de una identificación de
      mensaje. *singular* se usa como la identificación del mensaje
      para fines de búsqueda en el catálogo, mientras que *n* se usa
      para determinar qué forma plural usar. La cadena del mensaje
      retornado es una cadena de caracteres Unicode.

      Si la identificación del mensaje no se encuentra en el catálogo
      y se especifica una reserva, la solicitud se reenvía al método
      de reserva "ngettext()". De lo contrario, cuando *n* es 1 se
      retorna *singular*, y *plural* se retorna en todos los demás
      casos.

      Aquí hay un ejemplo:

         n = len(os.listdir('.'))
         cat = GNUTranslations(somefile)
         message = cat.ngettext(
             'There is %(num)d file in this directory',
             'There are %(num)d files in this directory',
             n) % {'num': n}

   pgettext(context, message, /)

      Busca el *context* y *message* id en el catálogo y retorna la
      cadena de de caracteres mensaje correspondiente, como una cadena
      de caracteres Unicode. Si no hay ninguna entrada en el catálogo
      para el *message* id y *context*, y se ha establecido un
      retroceso (*fallback*), la búsqueda se reenvía al método de
      retroceso "pgettext()". De lo contrario, se retorna el *message*
      id.

      Added in version 3.8.

   npgettext(context, singular, plural, n, /)

      Realiza una búsqueda de formas plurales de una identificación de
      mensaje. *singular* se usa como la identificación del mensaje
      para fines de búsqueda en el catálogo, mientras que *n* se usa
      para determinar qué forma plural usar.

      Si la identificación del mensaje para *context* no se encuentra
      en el catálogo y se especifica una reserva, la solicitud se
      reenvía al método de reserva "npgettext()". De lo contrario,
      cuando *n * es 1 se retorna *singular*, y *plural* se retorna en
      todos los demás casos.

      Added in version 3.8.

### Soporte de catálogo de mensajes de Solaris

El sistema operativo Solaris define su propio formato de archivo
binario ".mo", pero como no se puede encontrar documentación sobre
este formato, no es compatible en este momento.

### El constructor del catálogo

GNOME uses a version of the "gettext" module by James Henstridge, but
this version has a slightly different API.  Its documented usage was:

   import gettext
   cat = gettext.Catalog(domain, localedir)
   _ = cat.gettext
   print(_('hello world'))

Para la compatibilidad con este módulo anterior, la función
"Catalog()" es un alias para la función "translation()" descrita
anteriormente.

Una diferencia entre este módulo y el de Henstridge: sus objetos de
catálogo admitían el acceso a través de una API de mapeo, pero esto
parece estar sin usar y, por lo tanto, actualmente no es compatible.

## Internacionalizando sus programas y módulos

La internacionalización (I18N) se refiere a la operación mediante la
cual un programa conoce varios idiomas. La localización (L10N) se
refiere a la adaptación de su programa, una vez internacionalizado, al
idioma local y los hábitos culturales. Para proporcionar mensajes
multilingües para sus programas de Python, debe seguir los siguientes
pasos:

1. prepare su programa o módulo marcando especialmente cadenas
   traducibles

2. ejecuta un conjunto de herramientas sobre tus archivos marcados
   para generar catálogos de mensajes sin procesar

3. crear traducciones específicas del idioma de los catálogos de
   mensajes

4. use the "gettext" module so that message strings are properly
   translated

Para preparar su código para la internacionalización (I18N), necesita
revisar todas las cadenas de texto en sus archivos. Cualquier cadena
que requiera traducción debe ser marcada envolviéndola en "_('...')"
---, lo que equivale a una llamada a la función "_". Por ejemplo:

   filename = 'mylog.txt'
   message = _('writing a log message')
   with open(filename, 'w') as fp:
       fp.write(message)

En este ejemplo, la cadena de caracteres "'writing a log message'"
está marcada como candidata para la traducción, mientras que las
cadenas "'mylog.txt'" y "'w'" no lo están.

Hay algunas herramientas para extraer las cadenas destinadas a la
traducción. El GNU **gettext** original solo admitía el código fuente
C o C++, pero su versión extendida **xgettext** escanea el código
escrito en varios idiomas, incluido Python, para encontrar cadenas
marcadas como traducibles. Babel es una biblioteca de
internacionalización de Python que incluye un script "pybabel" para
extraer y compilar catálogos de mensajes. El programa de François
Pinard llamado **xpot** hace un trabajo similar y está disponible como
parte de su po-utils package.

(Python también incluye versiones de Python puro de estos programas,
llamadas **pygettext.py** y **msgfmt.py**; algunas distribuciones de
Python las instalarán por usted. **pygettext.py** es similar a
**xgettext**, pero solo entiende el código fuente de Python y no puede
manejar otros lenguajes de programación como C o C++. **pygettext.py**
admite una interfaz de línea de comandos similar a **xgettext**; para
detalles sobre su uso, ejecute "pygettext.py --help". **msgfmt.py** es
binario compatible con GNU **msgfmt**. Con estos dos programas, es
posible que no necesite el paquete GNU **gettext** para
internacionalizar sus aplicaciones Python.)

**xgettext**, **pygettext**, y herramientas similares generan archivos
".po" que son catálogos de mensajes. Son archivos estructurados
legibles por humanos que contienen cada cadena marcada en el código
fuente, junto con un marcador de posición para las versiones
traducidas de estas cadenas.

Copies of these ".po" files are then handed over to the individual
human translators who write translations for every supported natural
language.  They send back the completed language-specific versions as
a "<language-name>.po" file that's compiled into a machine-readable
".mo" binary catalog file using the **msgfmt** program.  The ".mo"
files are used by the "gettext" module for the actual translation
processing at run-time.

How you use the "gettext" module in your code depends on whether you
are internationalizing a single module or your entire application. The
next two sections will discuss each case.

### Agregar configuración regional a su módulo

Si está aplicando configuración regional a su módulo, debe tener
cuidado de no realizar cambios globales, por ejemplo, al espacio de
nombres integrado. No debe utilizar la API GNU **gettext**, sino la
API basada en clases.

Digamos que su módulo se llama "spam" y los diversos archivos ".mo" de
traducciones del lenguaje natural del módulo residen en
"/usr/share/locale" en formato GNU **gettext**. Esto es lo que pondría
en la parte superior de su módulo:

   import gettext
   t = gettext.translation('spam', '/usr/share/locale')
   _ = t.gettext

### Agregar configuración regional a su aplicación

Si está localizando su aplicación, puede instalar globalmente la
función "_()" en el espacio de nombres integrado, normalmente en el
archivo principal de su aplicación. Esto hará que todos los archivos
específicos de la aplicación puedan usar "_('...')" sin necesidad de
instalarla explícitamente en cada uno de ellos.

En el caso simple, entonces, solo necesita agregar el siguiente bit de
código al archivo del controlador principal de su aplicación:

   import gettext
   gettext.install('myapplication')

Si necesita establecer el directorio de configuración regional, puede
pasarlo a la función "install()":

   import gettext
   gettext.install('myapplication', '/usr/share/locale')

### Cambiar idiomas sobre la marcha

Si su programa necesita admitir muchos idiomas al mismo tiempo, es
posible que desee crear varias instancias de traducción y luego
cambiar entre ellas explícitamente, de esta manera:

   import gettext

   lang1 = gettext.translation('myapplication', languages=['en'])
   lang2 = gettext.translation('myapplication', languages=['fr'])
   lang3 = gettext.translation('myapplication', languages=['de'])

   # start by using language1
   lang1.install()

   # ... time goes by, user selects language 2
   lang2.install()

   # ... more time goes by, user selects language 3
   lang3.install()

### Traducciones diferidas

En la mayoría de las situaciones de codificación, las cadenas se
traducen donde se codifican. Sin embargo, ocasionalmente, debe marcar
cadenas para la traducción, pero diferir la traducción real hasta más
tarde. Un ejemplo clásico es:

   animals = ['mollusk',
              'albatross',
              'rat',
              'penguin',
              'python', ]
   # ...
   for a in animals:
       print(a)

Aquí, desea marcar las cadenas en la lista de "animals" como
traducibles, pero en realidad no desea traducirlas hasta que se
impriman.

Aquí hay una manera de manejar esta situación:

   def _(message): return message

   animals = [_('mollusk'),
              _('albatross'),
              _('rat'),
              _('penguin'),
              _('python'), ]

   del _

   # ...
   for a in animals:
       print(_(a))

Esto funciona ya que la definición ficticia de "_()" devuelve
simplemente la cadena sin modificar. Además, esta definición ficticia
sobrescribirá de manera temporal cualquier definición de "_()" en el
espacio de nombres integrado (hasta el uso del comando "del"). No
obstante, tenga cuidado si ya existe una definición previa de "_()" en
el espacio de nombres local.

Tenga en cuenta que el segundo uso de "_()" no identificará "a" como
traducible al programa **gettext**, porque el parámetro no es un
literal de cadena.

Otra forma de manejar esto es con el siguiente ejemplo:

   def N_(message): return message

   animals = [N_('mollusk'),
              N_('albatross'),
              N_('rat'),
              N_('penguin'),
              N_('python'), ]

   # ...
   for a in animals:
       print(_(a))

En este caso, está marcando las cadenas traducibles con la función
"N_()", la cual no generará conflictos con ninguna definición de
"_()". Sin embargo, deberá enseñar a su programa de extracción de
mensajes a buscar cadenas traducibles marcadas con "N_()".
**xgettext**, **pygettext**, "pybabel extract", y **xpot** todos
soportan esto mediante el uso de la opción de línea de comandos "-k".
La elección de "N_`()" aquí es completamente arbitraria; podría haber
sido también "MarkThisStringForTranslation()".

## Agradecimientos

Las siguientes personas contribuyeron con código, comentarios,
sugerencias de diseño, implementaciones anteriores y una valiosa
experiencia para la creación de este módulo:

* *Peter Funk*

* *James Henstridge*

* *Juan David Ibáñez Palomar*

* *Marc-André Lemburg*

* Martin von Löwis

* *François Pinard*

* *Barry Warsaw*

* *Gustavo Niemeyer*

-[ Notas al pie ]-

[1] The default locale directory is system dependent; for example, on
    Red Hat Linux it is "/usr/share/locale", but on Solaris it is
    "/usr/lib/locale". The "gettext" module does not try to support
    these system dependent defaults; instead its default is
    "*sys.base_prefix*/share/locale" (see "sys.base_prefix"). For this
    reason, it is always best to call "bindtextdomain()" with an
    explicit absolute path at the start of your application.

[2] Vea la nota al pie de página para "bindtextdomain()" arriba.
