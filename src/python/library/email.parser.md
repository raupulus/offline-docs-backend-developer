---
title: '"email.parser": Parsing email messages'
source_url: https://docs.python.org/es/3
source_path: library/email.parser.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 2500
---

# "email.parser": Parsing email messages

**Código fuente:** Lib/email/parser.py

======================================================================

Se pueden construir estructuras de objetos de mensaje de dos formas:
pueden ser creados de puro invento al crear un objeto "EmailMessage",
añadir encabezados usando la interfaz de diccionario, y añadir
carga(s) usando el método "set_content()" y otros relacionados, o
pueden ser creados al analizar una representación serializada de un
mensaje de correo electrónico.

El paquete "email" proporciona un analizador estándar que entiende la
mayoría de estructuras de documentos de correo electrónico, incluyendo
documentos MIME.  Le puedes pasar al analizador bytes, una cadena de
caracteres o una archivo de objeto, y el analizador te retornará la
instancia "EmailMessage" raíz de la estructura del objeto. Para
mensajes simples que no sean MIME, la carga de su objeto raíz
probablemente será una cadena de caracteres conteniendo el texto o el
mensaje. Para mensajes MIME, el objeto raíz retornará "True" de su
método "is_multipart()", y las subpartes pueden ser accedidas a través
de los métodos de manipulación de carga, tales como "get_body()",
"iter_parts()", y "walk()".

De hecho hay dos interfaces de analizadores disponibles para usar, la
API "Parser" y la API progresiva "FeedParser".  La API "Parser" es más
útil si tú tienes el texto del mensaje entero en memoria, o si el
mensaje entero reside en un archivo en el sistema. "FeedParser" es más
apropiado cuando estás leyendo el mensaje de un *stream* que puede ser
bloqueado esperando más entrada (tal como leer un mensaje de correo
electrónico de un socket).  El "FeedParser" puede consumir y analizar
el mensaje de forma progresiva, y sólo retorna el objeto raíz cuando
cierras el analizador.

Tenga en cuenta que el analizador puede ser extendido en formas
limitadas, y por supuesto puedes implementar tu propio analizador
completamente desde cero.  Toda la lógica que conecta el analizador
empaquetado del paquete "email" y la clase "EmailMessage" está
encarnada en la clase "Policy", por lo que un analizador personalizado
puede crear árboles de objetos mensaje en cualquier forma que
encuentre necesario al implementar versiones personalizadas de los
métodos apropiados de "Policy".

## API *FeedParser*

La clase "BytesFeedParser", importado del módulo "email.feedparser",
proporciona una API que es propicia para el análisis progresivo de
mensajes de correo electrónico, tal como sería necesario cuando se
esté leyendo el texto de un mensaje de correo electrónico de una
fuente que puede bloquear (tal como un socket).  Desde luego se puede
usar la clase "BytesFeedParser" para analizar un mensaje de correo
electrónico completamente contenido en un *bytes-like object*, cadena
de caracteres, o archivo, pero la API "BytesParser" puede ser más
conveniente para tales casos de uso.  Las semánticas y resultados de
las dos API de los analizadores son idénticas.

La API de "BytesFeedParser" es simple; puedes crear una instancia, le
proporcionas un montón de bytes hasta que no haya más necesidad de
hacerlo, entonces cierras el analizador para recuperar el objeto del
mensaje raíz. El "BytesFeedParser" es extremadamente preciso cuando
está analizando mensajes conformes al estándar, y hace un buen trabajo
al analizar mensajes no conformes, proporcionando información acerca
de cómo un mensaje fue considerado inservible.  Ingresará una lista de
cualquier problema que encontró en el atributo "defects" del objeto
mensaje.  Véase el módulo "email.errors" para la lista de defectos que
puede encontrar.

Aquí está el API para "BytesFeedParser":

class email.parser.BytesFeedParser(_factory=None, *, policy=policy.compat32)

   Crea una instancia de "BytesFeedParser". El argumento opcional
   *_factory* es un invocable sin argumentos; si no se especifica, usa
   el "message_factory" de *policy*.  Llama a *_factory* cuando sea
   necesario un nuevo objeto mensaje.

   Si se especifica *policy*, usa las reglas que especifica para
   actualizar la representación del mensaje.  Si *policy* no está
   puesta, usa la política (*policy*) "compat32", que mantiene
   compatibilidad con la versión 3.2 de Python del paquete de correo
   electrónico y proporciona a "Message" como la fábrica por defecto.
   Todas las otras políticas proveen a "EmailMessage" como el
   *_factory* por defecto. Para más información en lo demás que
   *policy* controla, véase la documentación "policy".

   Nota: **La palabra clave *policy* siempre debe estar
   especificada**; El valor por defecto cambiará a
   "email.policy.default" en una versión futura de Python.

   Added in version 3.2.

   Distinto en la versión 3.3: Se añadió la palabra clave *policy*.

   Distinto en la versión 3.6: *_factory* es por defecto la *policy*
   "message_factory".

   feed(data)

      Le proporciona al analizador algunos datos más.  *data* debe ser
      un *bytes-like object* conteniendo una o más líneas.  Las líneas
      pueden ser parciales y el analizador va a juntar tales líneas
      parciales apropiadamente.  las líneas pueden tener cualquiera de
      las tres terminaciones de línea comunes: retorno de cargo
      (*retorno de cargo*), nueva línea (*newline*), o retorno de
      cargo y nueva línea (pueden ser mezclados).

   close()

      Completa el análisis de todos los datos previamente
      proporcionados y retorna la raíz del objeto mensaje. No está
      definido lo que pasa si se llama a "feed()" después de que este
      método haya sido llamado.

class email.parser.FeedParser(_factory=None, *, policy=policy.compat32)

   Works like "BytesFeedParser" except that the input to the "feed()"
   method must be a string.  This is of limited utility, since the
   only way for such a message to be valid is for it to contain only
   ASCII text or, if "utf8" is "True", no binary attachments.

   Distinto en la versión 3.3: Se añadió la palabra clave *policy*.

## API *Parser*

The "BytesParser" class, imported from the "email.parser" module,
provides an API that can be used to parse a message when the complete
contents of the message are available in a *bytes-like object* or
file.  The "email.parser" module also provides "Parser" for parsing
strings, and header-only parsers, "BytesHeaderParser" and
"HeaderParser", which can be used if you're only interested in the
headers of the message.  "BytesHeaderParser" and "HeaderParser" can be
much faster in these situations, since they do not attempt to parse
the message body, instead setting the payload to the raw body.

class email.parser.BytesParser(_class=None, *, policy=policy.compat32)

   Crea una instancia de "BytesParser". Los argumentos *_class* y
   *policy* tiene el mismo significado y semántica que los argumentos
   *_factory* y *policy* de "BytesFeedParser".

   Nota: **La palabra clave *policy* siempre debe estar
   especificada**; El valor por defecto cambiará a
   "email.policy.default" en una versión futura de Python.

   Distinto en la versión 3.3: Se eliminó el argumento *strict* que
   fue deprecado en 2.4.  Se añadió la palabra clave *policy*.

   Distinto en la versión 3.6: *_class* es por defecto la política
   "message_factory".

   parse(fp, headersonly=False)

      Read all the data from the binary file-like object *fp*, parse
      the resulting bytes, and return the message object.  *fp* must
      support both the "readline()" and the "read()" methods.

      The bytes contained in *fp* must be formatted as a block of
      **RFC 5322** (or, if "utf8" is "True", **RFC 6532**) style
      headers and header continuation lines, optionally preceded by an
      envelope header.  The header block is terminated either by the
      end of the data or by a blank line.  Following the header block
      is the body of the message (which may contain MIME-encoded
      subparts, including subparts with a *Content-Transfer-Encoding*
      of "8bit").

      El argumento opcional *headersonly* es un flag que especifica si
      se debe analizar después de leer las cabeceras o no.  El valor
      por defecto es "False", significando que analiza el contenido
      entero del archivo.

   parsebytes(bytes, headersonly=False)

      Similar al método "parse()", excepto que toma un *bytes-like
      object* en vez de un objeto similar a un archivo.  Llamar a este
      método en un *bytes-like object* es equivalente a envolver a
      *bytes* en una instancia de "BytesIO" primero y llamar a
      "parse()".

      El argumento opcional *headersonly* es como el método "parse()".

   Added in version 3.2.

class email.parser.BytesHeaderParser(_class=None, *, policy=policy.compat32)

   Exactamente como "BytesParser", excepto que *headersonly* es por
   defecto "True".

   Added in version 3.3.

class email.parser.Parser(_class=None, *, policy=policy.compat32)

   Esta clase es paralela a "BytesParser", pero trata entradas de
   cadenas de caracteres.

   Distinto en la versión 3.3: Se eliminó el argumento *strict*.  Se
   añadió la palabra clave *policy*.

   Distinto en la versión 3.6: *_class* es por defecto la política
   "message_factory".

   parse(fp, headersonly=False)

      Lee todos los datos del modo texto del objeto parecido a archivo
      *fp*, analiza el texto resultante, y retorna el objeto mensaje
      raíz.  *fp* debe soportar tanto el método "readline()" y el
      método "read()" en objetos parecidos a archivos.

      Además de el requisito del modo texto, este método opera como
      "BytesParser.parse()".

   parsestr(text, headersonly=False)

      Similar al método "parse()", excepto que toma un objeto de
      cadena de caracteres de un objeto similar a un archivo.  Llamar
      a este método en una cadena de caracteres es equivalente a
      envolver a *text* en una instancia de "StringIO" primero y
      llamar a "parse()".

      El argumento opcional *headersonly* es como el método "parse()".

class email.parser.HeaderParser(_class=None, *, policy=policy.compat32)

   Exactamente como "Parser", excepto que *headersonly* es por defecto
   "True".

Ya que crear una estructura de un objeto mensaje de una cadena de
caracteres o un objeto archivo es una tarea tan común, Se
proporcionaron 4 funciones como una conveniencia.  Están disponibles
en paquete de espacio de nombres de alto nivel "email".

email.message_from_bytes(s, _class=None, *, policy=policy.compat32)

   Retorna una estructura del objeto mensaje de un *bytes-like
   object*. Esto es equivalente a "BytesParser().parsebytes(s)". El
   argumento opcional *_class* y *policy* son interpretados como
   sucede con el constructor de clase "BytesParser".

   Added in version 3.2.

   Distinto en la versión 3.3: Se eliminó el argumento *strict*.  Se
   añadió la palabra clave *policy*.

email.message_from_binary_file(fp, _class=None, *, policy=policy.compat32)

   Retorna una estructura árbol del objeto mensaje de un *file object*
   binario abierto.  Esto es equivalente a "BytesParser().parse(fp)".
   *_class* y *policy* son interpretados como sucede con el
   constructor de clase "BytesParser".

   Added in version 3.2.

   Distinto en la versión 3.3: Se eliminó el argumento *strict*.  Se
   añadió la palabra clave *policy*.

email.message_from_string(s, _class=None, *, policy=policy.compat32)

   Retorna una estructura del objeto mensaje de una cadena de
   caracteres.  Esto es equivalente a "Parser().parsestr(s)". *_class*
   y *policy* son interpretados como sucede con el constructor de
   clase "Parser".

   Distinto en la versión 3.3: Se eliminó el argumento *strict*.  Se
   añadió la palabra clave *policy*.

email.message_from_file(fp, _class=None, *, policy=policy.compat32)

   Retorna una estructura árbol del objeto mensaje de un *file object*
   abierto. Esto es equivalente a "Parser().parse(fp)".  *_class* y
   *policy* son interpretados como sucede con el constructor de clase
   "Parser".

   Distinto en la versión 3.3: Se eliminó el argumento *strict*.  Se
   añadió la palabra clave *policy*.

   Distinto en la versión 3.6: *_class* es por defecto la política
   "message_factory".

Aquí está un ejemplo de cómo puedes usar "message_from_bytes()" en una
entrada interactiva de Python:

   >>> import email
   >>> msg = email.message_from_bytes(myBytes)

## Notas adicionales

Aquí están algunas notas sobre la semántica del análisis:

* La mayoría de los mensajes de tipo que no son *multipart* son
  actualizados como un solo objeto mensaje con una carga de cadena de
  caracteres.  Estos objetos retornarán "False" para "is_multipart()",
  y "iter_parts()" cederá (*yield*) una lista vacía.

* Todos los mensajes de tipo *multipart* serán analizados como un
  objeto mensaje contenedor con una lista de objetos sub-mensajes para
  sus cargas.  El mensaje del contenedor externo retornará "True" para
  "is_multipart()", y "iter_parts()" cederá (*yield*) una lista de
  subpartes.

* La mayoría de mensajes con una tipo de contenido de *message/** (tal
  como *message/delivery-status* y *message/rfc822*) también serán
  analizados como objetos contenedores que contienen una lista de
  cargas de longitud 1. Su método "is_multipart()" retornará "True".
  El único elemento cedido (*yielded*) por "iter_parts()" será un
  objeto sub-mensaje.

* Algunos mensajes de conformidad no estándar pueden no ser
  internamente consistentes acerca de su *multipart*-idad. Tales
  mensajes pueden tener una cabecera *Content-Type* de tipo
  *multipart*, pero su método "is_multipart()" puede retornar "False".
  Si tales mensajes son analizados con "FeedParser", tendrán una
  instancia de la clase "MultipartInvariantViolationDefect" en su
  lista de atributos *defects*.  Véase "email.errors" para más
  detalles.
