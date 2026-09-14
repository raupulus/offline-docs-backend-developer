---
title: Pending removal in future versions
source_url: https://docs.python.org/es/3
source_path: deprecations/pending-removal-in-future.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: deprecations
order: 950
---

# Pending removal in future versions

Las siguientes APIs serán eliminadas en el futuro, aunque no hay fecha
de planificación exacta para ello.

* "argparse":

  * Nesting argument groups and nesting mutually exclusive groups are
    deprecated.

  * Passing the undocumented keyword argument *prefix_chars* to
    "add_argument_group()" is now deprecated.

  * The "argparse.FileType" type converter is deprecated.

* "builtins":

  * Generadores: las firmas "throw(type, exc, tb)" y "athrow(type,
    exc, tb)" están obsoletas: utilice "throw(exc)" y "athrow(exc)" en
    su lugar, la firma de argumento único.

  * Actualmente Python acepta literales numéricos seguidos
    inmediatamente de palabras clave, por ejemplo, "0in x", "1or x",
    "0if 1else 2". Permite expresiones confusas y ambiguas como
    "[0x1for x in y]" (que se puede interpretar como "[0x1 for x in
    y]" o "[0x1f or x in y]"). Se genera una advertencia de sintaxis
    si el literal numérico va seguido inmediatamente de una de las
    palabras clave "and", "else", "for", "if", "in", "is" y "or". En
    una versión futura, se cambiará a un error de sintaxis. (gh-87999)

  * Compatibilidad con los métodos "__index__()" e "__int__()" que
    retornan un tipo que no es int: estos métodos serán necesarios
    para retornar una instancia de una subclase estricta de "int".

  * Compatibilidad con el método "__float__()" que retorna una
    subclase estricta de "float": será necesario que estos métodos
    retornen una instancia de "float".

  * Compatibilidad con el método "__complex__()" que retorna una
    subclase estricta de "complex": será necesario que estos métodos
    retornen una instancia de "complex".

  * Ahora está obsoleto el paso de un número complejo como argumento
    *real* o *imag* en el constructor "complex()"; solo debe pasarse
    como un único argumento posicional. (Contribución de Serhiy
    Storchaka en gh-109218.)

* "calendar": Las constantes "calendar.January" y "calendar.February"
  han quedado obsoletas y han sido reemplazadas por "calendar.JANUARY"
  y "calendar.FEBRUARY". (Contribución de Prince Roshan en gh-103636.)

* "codecs": use "open()" instead of "codecs.open()". (gh-133038)

* "codeobject.co_lnotab": use el método "codeobject.co_lines()" en su
  lugar.

* "datetime":

  * "utcnow()": use "datetime.datetime.now(tz=datetime.UTC)".

  * "utcfromtimestamp()": use
    "datetime.datetime.fromtimestamp(timestamp, tz=datetime.UTC)".

* "gettext": El valor plural tiene que ser un entero.

* "importlib":

  * El parámetro *debug_override* de "cache_from_source()" queda
    obsoleto: use el parámetro *optimization* en su lugar.

* "importlib.metadata":

  * Interfaz de tupla "EntryPoints".

  * "None" implícito en valores retornados.

* "logging": el método "warn()" ha quedado obsoleto desde Python 3.3,
  use "warning()" en su lugar.

* "mailbox": El uso del modo de entrada y texto StringIO está
  obsoleto, use BytesIO y el modo binario en su lugar.

* "os": Llamando a "os.register_at_fork()" en procesos multi-hilos.

* "pydoc.ErrorDuringImport": El valor de tupla para el parámetro
  *exc_info* queda obsoleto, use una excepción en su lugar.

* "re": Ahora se aplican reglas más estrictas para las referencias
  numéricas de grupos y los nombres de grupos en expresiones
  regulares. Ahora solo se aceptan secuencias de dígitos ASCII como
  referencia numérica. El nombre de grupo en patrones de bytes y
  cadenas de reemplazo ahora solo puede contener letras y dígitos
  ASCII y guiones bajos. (Contribución de Serhiy Storchaka en
  gh-91760.)

* Módulos "sre_compile", "sre_constants" y "sre_parse".

* "shutil": el parámetro *onerror* de "rmtree()" queda obsoleto en
  Python 3.12; use el parámetro *onexc* en su lugar.

* Opciones y protocolos de "ssl":

  * "ssl.SSLContext" sin argumento de protocolo queda obsoleto.

  * "ssl.SSLContext": "set_npn_protocols()" y
    "selected_npn_protocol()" quedan obsoletas: use ALPN en su lugar.

  * Opciones "ssl.OP_NO_SSL*"

  * Opciones "ssl.OP_NO_TLS*"

  * "ssl.PROTOCOL_SSLv3"

  * "ssl.PROTOCOL_TLS"

  * "ssl.PROTOCOL_TLSv1"

  * "ssl.PROTOCOL_TLSv1_1"

  * "ssl.PROTOCOL_TLSv1_2"

  * "ssl.TLSVersion.SSLv3"

  * "ssl.TLSVersion.TLSv1"

  * "ssl.TLSVersion.TLSv1_1"

* Métodos de "threading":

  * "threading.Condition.notifyAll()": use "notify_all()".

  * "threading.Event.isSet()": use "is_set()".

  * "threading.Thread.isDaemon()", "threading.Thread.setDaemon()": use
    el atributo "threading.Thread.daemon".

  * "threading.Thread.getName()", "threading.Thread.setName()": use el
    atributo "threading.Thread.name".

  * "threading.currentThread()": use "threading.current_thread()".

  * "threading.activeCount()": use "threading.active_count()".

* "typing.Text" (gh-92332).

* The internal class "typing._UnionGenericAlias" is no longer used to
  implement "typing.Union". To preserve compatibility with users using
  this private class, a compatibility shim will be provided until at
  least Python 3.17. (Contributed by Jelle Zijlstra in gh-105499.)

* "unittest.IsolatedAsyncioTestCase": queda deprecado retornar un
  valor que no sea "None" en un caso de prueba.

* Funciones deprecadas de "urllib.parse": use "urlparse()" en su lugar

  * "splitattr()"

  * "splithost()"

  * "splitnport()"

  * "splitpasswd()"

  * "splitport()"

  * "splitquery()"

  * "splittag()"

  * "splittype()"

  * "splituser()"

  * "splitvalue()"

  * "to_bytes()"

* "wsgiref": "SimpleHandler.stdout.write()" no debería hacer
  escrituras parciales.

* "xml.etree.ElementTree": La prueba del valor de verdad de un
  "Element" está obsoleta. En una versión futura, siempre retornará
  "True". En su lugar, es preferible realizar pruebas explícitas
  "len(elem)" o "elem is not None".

* "sys._clear_type_cache()" is deprecated: use
  "sys._clear_internal_caches()" instead.
