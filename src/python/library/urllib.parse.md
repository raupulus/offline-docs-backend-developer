---
title: '"urllib.parse" --- Parse URLs into components'
source_url: https://docs.python.org/es/3
source_path: library/urllib.parse.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 4410
---

# "urllib.parse" --- Parse URLs into components

**Código fuente:** Lib/urllib/parse.py

======================================================================

Este modulo define una interfaz estándar para separar cadenas de texto
del Localizador de recursos uniforme (más conocido por las siglas URL,
del inglés *Uniform Resource Locator*) en componentes (esquema de
dirección, ubicación de red, ruta de acceso, etc.), para poder
combinar los componentes  nuevamente en una cadena de texto URL, y
convertir una "URL relativa" a una URL absoluta a partir de una "URL
base".

The module has been designed to match the internet RFC on Relative
Uniform Resource Locators. It supports the following URL schemes:
"file", "ftp", "gopher", "hdl", "http", "https", "imap", "itms-
services", "mailto", "mms", "news", "nntp", "prospero", "rsync",
"rtsp", "rtsps", "rtspu", "sftp", "shttp", "sip", "sips", "snews",
"svn", "svn+ssh", "telnet", "wais", "ws", "wss".

**Detalles de implementación de CPython:** The inclusion of the "itms-
services" URL scheme can prevent an app from passing Apple's App Store
review process for the macOS and iOS App Stores. Handling for the
"itms-services" scheme is always removed on iOS; on macOS, it *may* be
removed if CPython has been built with the "--with-app-store-
compliance" option.

The "urllib.parse" module defines functions that fall into two broad
categories: URL parsing and URL quoting. These are covered in detail
in the following sections.

This module's functions use the deprecated term "netloc" (or
"net_loc"), which was introduced in **RFC 1808**. However, this term
has been obsoleted by **RFC 3986**, which introduced the term
"authority" as its replacement. The use of "netloc" is continued for
backward compatibility.

## Análisis de URL

Las funciones de análisis de url se centran en dividir una cadena de
dirección URL en sus componentes o en combinar componentes de
dirección URL en una cadena de dirección URL.

urllib.parse.urlsplit(urlstring, scheme=None, allow_fragments=True)

   Parse a URL into five components, returning a 5-item *named tuple*
   "SplitResult" or "SplitResultBytes". This corresponds to the
   general structure of a URL: "scheme://netloc/path?query#fragment".
   Each tuple item is a string, possibly empty.

   The delimiters as shown above are not part of the result, except
   for a leading slash in the *path* component, which is retained if
   present.

   Additionally, the netloc property is broken down into these
   additional attributes added to the returned object: username,
   password, hostname, and port.

   Percent-encoded sequences are not decoded.

   For example:

      >>> from urllib.parse import urlsplit
      >>> urlsplit("scheme://netloc/path?query#fragment")
      SplitResult(scheme='scheme', netloc='netloc', path='/path',
                  query='query', fragment='fragment')
      >>> o = urlsplit("http://docs.python.org:80/3/library/urllib.parse.html?"
      ...              "highlight=params#url-parsing")
      >>> o
      SplitResult(scheme='http', netloc='docs.python.org:80',
                  path='/3/library/urllib.parse.html',
                  query='highlight=params', fragment='url-parsing')
      >>> o.scheme
      'http'
      >>> o.netloc
      'docs.python.org:80'
      >>> o.hostname
      'docs.python.org'
      >>> o.port
      80
      >>> o._replace(fragment="").geturl()
      'http://docs.python.org:80/3/library/urllib.parse.html?highlight=params'

   Following the syntax specifications in **RFC 1808**, "urlsplit()"
   recognizes a netloc only if it is properly introduced by '//'.
   Otherwise the input is presumed to be a relative URL and thus to
   start with a path component.

      >>> from urllib.parse import urlsplit
      >>> urlsplit('//www.cwi.nl:80/%7Eguido/Python.html')
      SplitResult(scheme='', netloc='www.cwi.nl:80', path='/%7Eguido/Python.html',
                  query='', fragment='')
      >>> urlsplit('www.cwi.nl/%7Eguido/Python.html')
      SplitResult(scheme='', netloc='', path='www.cwi.nl/%7Eguido/Python.html',
                  query='', fragment='')
      >>> urlsplit('help/Python.html')
      SplitResult(scheme='', netloc='', path='help/Python.html',
                  query='', fragment='')

   El argumento *scheme* proporciona el esquema de direccionamiento
   predeterminado, que solo se utilizará si la dirección URL no
   especifica uno.  Debe ser del mismo tipo (texto o bytes) que
   *urlstring*, excepto que el valor predeterminado "''"  siempre está
   permitido, y se convierte automáticamente a "b''" si aplica.

   Si el argumento *allow_fragments* es falso, los identificadores de
   fragmento no son reconocidos. Sino que, son analizados como parte
   de la ruta, parámetros o componentes de la consulta y el "fragment"
   es configurado como una cadena vacía en el valor retornado.

   El valor retornado es un *named tuple*, lo que significa que se
   puede tener acceso a sus elementos por índice o como atributos con
   nombre, que son:

   +--------------------+---------+---------------------------+--------------------------+
   | Atributo           | Índice  | Valor                     | Valor si no está         |
   |                    |         |                           | presente                 |
   |====================|=========|===========================|==========================|
   | "scheme"           | 0       | Especificador de esquema  | parámetro *scheme*       |
   |                    |         | de URL                    |                          |
   +--------------------+---------+---------------------------+--------------------------+
   | "netloc"           | 1       | Parte de ubicación de red | cadena vacía             |
   +--------------------+---------+---------------------------+--------------------------+
   | "path"             | 2       | Hierarchical path         | cadena vacía             |
   +--------------------+---------+---------------------------+--------------------------+
   | "query"            | 3       | Componente de consulta    | cadena vacía             |
   +--------------------+---------+---------------------------+--------------------------+
   | "fragment"         | 4       | Identificador de          | cadena vacía             |
   |                    |         | fragmento                 |                          |
   +--------------------+---------+---------------------------+--------------------------+
   | "username"         |         | Nombre de usuario         | "None"                   |
   +--------------------+---------+---------------------------+--------------------------+
   | "password"         |         | Contraseña                | "None"                   |
   +--------------------+---------+---------------------------+--------------------------+
   | "hostname"         |         | Nombre de host            | "None"                   |
   |                    |         | (minúsculas)              |                          |
   +--------------------+---------+---------------------------+--------------------------+
   | "port"             |         | Número de puerto como     | "None"                   |
   |                    |         | entero, si está presente  |                          |
   +--------------------+---------+---------------------------+--------------------------+

   La lectura del atributo "port" lanzará un "ValueError" si se
   especifica un puerto no válido en la dirección URL.  Consulte la
   sección Resultados del análisis estructurado para obtener más
   información sobre el objeto de resultado.

   Los corchetes no coincidentes en el atributo "netloc" lanzarán un
   "ValueError".

   Los caracteres del atributo "netloc" que se descomponen en la
   normalización de NFKC (según lo utilizado por la codificación IDNA)
   en cualquiera de "/", "?", "#", "@" o ":" lanzará un "ValueError".
   Si la dirección URL se descompone antes del análisis, no se
   producirá ningún error.

   Following some of the WHATWG spec that updates **RFC 3986**,
   leading C0 control and space characters are stripped from the URL.
   "\n", "\r" and tab "\t" characters are removed from the URL at any
   position.

   As is the case with all named tuples, the subclass has a few
   additional methods and attributes that are particularly useful. One
   such method is "_replace()". The "_replace()" method will return a
   new "SplitResult" object replacing specified fields with new
   values.

      >>> from urllib.parse import urlsplit
      >>> u = urlsplit('//www.cwi.nl:80/%7Eguido/Python.html')
      >>> u
      SplitResult(scheme='', netloc='www.cwi.nl:80', path='/%7Eguido/Python.html',
                  query='', fragment='')
      >>> u._replace(scheme='http')
      SplitResult(scheme='http', netloc='www.cwi.nl:80', path='/%7Eguido/Python.html',
                  query='', fragment='')

   Advertencia:

     "urlsplit()" no realiza validaciones. Mire  URL parsing security
     para más información.

   Distinto en la versión 3.2: Se han añadido capacidades de análisis
   de URL IPv6.

   Distinto en la versión 3.3: The fragment is now parsed for all URL
   schemes (unless *allow_fragments* is false), in accordance with
   **RFC 3986**.  Previously, an allowlist of schemes that support
   fragments existed.

   Distinto en la versión 3.6: Los números de puerto fuera de rango
   ahora generan "ValueError", en lugar de retornar "None".

   Distinto en la versión 3.8: Los caracteres que afectan al análisis
   de netloc en la normalización de NFKC ahora lanzarán "ValueError".

   Distinto en la versión 3.10: Los caracteres ASCII de nueva línea y
   tab se eliminan de la URL.

   Distinto en la versión 3.12: Los caracteres de control WHATWG C0 y
   de espacio se eliminan de la URL.

urllib.parse.parse_qs(qs, keep_blank_values=False, strict_parsing=False, encoding='utf-8', errors='replace', max_num_fields=None, separator='&')

   Analizar una cadena de consulta proporcionada como argumento de
   cadena (datos de tipo *application/x-www-form-urlencoded*).  Los
   datos se retornan como un diccionario.  Las claves de diccionario
   son los nombres de variable de consulta únicos y los valores son
   listas de valores para cada nombre.

   El argumento opcional *keep_blank_values* es un indicador que
   indica si los valores en blanco de las consultas codificadas por
   porcentaje deben tratarse como cadenas en blanco. Un valor
   verdadero indica que los espacios en blanco deben conservarse como
   cadenas en blanco.  El valor falso predeterminado indica que los
   valores en blanco deben omitirse y tratarse como si no se hubieran
   incluido.

   El argumento opcional *strict_parsing* es una marca que indica qué
   hacer con los errores de análisis.  Si es falso (valor
   predeterminado), los errores se omiten silenciosamente.  Si es
   verdadero, los errores generan una excepción "ValueError".

   Los parámetros opcionales *encoding* y *errors* especifican cómo
   descodificar secuencias codificadas porcentualmente en caracteres
   Unicode, tal como lo acepta el método "bytes.decode()".

   El argumento opcional *max_num_fields* es el número máximo de
   campos que se van a leer. Si se establece, se produce un
   "ValueError" si hay más de *max_num_fields* campos leídos.

   El argumento opcional *separator* es el símbolo que se usa para
   separar los argumentos de la cadena de consulta. El valor por
   defecto es "&".

   Utilice la función "urllib.parse.urlencode()" (con el parámetro
   "doseq" establecido en "True") para convertir dichos diccionarios
   en cadenas de consulta.

   Distinto en la versión 3.2: Agregue los parámetros *encoding* y
   *errors*.

   Distinto en la versión 3.8: Añadido parámetro *max_num_fields*.

   Distinto en la versión 3.10: Añadido parámetro *separator* con un
   valor por defecto de "&". Versiones de Python anterior a Python
   3.10 permitían el uso de ";" y "&" como separadores de la cadena de
   consulta. Esto ha sido cambiado para aceptar sólo una llave
   separadora, siendo "&" el separador por defecto.

   Obsoleto desde la versión 3.14: Accepting objects with false values
   (like "0" and "[]") except empty strings and byte-like objects and
   "None" is now deprecated.

urllib.parse.parse_qsl(qs, keep_blank_values=False, strict_parsing=False, encoding='utf-8', errors='replace', max_num_fields=None, separator='&')

   Analizar una cadena de consulta proporcionada como argumento de
   cadena (datos de tipo *application/x-www-form-urlencoded*).  Los
   datos se retornan como una lista de pares de nombre y valor.

   El argumento opcional *keep_blank_values* es un indicador que
   indica si los valores en blanco de las consultas codificadas por
   porcentaje deben tratarse como cadenas en blanco. Un valor
   verdadero indica que los espacios en blanco deben conservarse como
   cadenas en blanco.  El valor falso predeterminado indica que los
   valores en blanco deben omitirse y tratarse como si no se hubieran
   incluido.

   El argumento opcional *strict_parsing* es una marca que indica qué
   hacer con los errores de análisis.  Si es falso (valor
   predeterminado), los errores se omiten silenciosamente.  Si es
   verdadero, los errores generan una excepción "ValueError".

   Los parámetros opcionales *encoding* y *errors* especifican cómo
   descodificar secuencias codificadas porcentualmente en caracteres
   Unicode, tal como lo acepta el método "bytes.decode()".

   El argumento opcional *max_num_fields* es el número máximo de
   campos que se van a leer. Si se establece, se produce un
   "ValueError" si hay más de *max_num_fields* campos leídos.

   El argumento opcional *separator* es el símbolo que se usa para
   separar los argumentos de la cadena de consulta. El valor por
   defecto es "&".

   Utilice la función "urllib.parse.urlencode()" para convertir dichas
   listas de pares en cadenas de consulta.

   Distinto en la versión 3.2: Agregue los parámetros *encoding* y
   *errors*.

   Distinto en la versión 3.8: Añadido parámetro *max_num_fields*.

   Distinto en la versión 3.10: Añadido parámetro *separator* con un
   valor por defecto de "&". Versiones de Python anterior a Python
   3.10 permitían el uso de ";" y "&" como separadores de la cadena de
   consulta. Esto ha sido cambiado para aceptar sólo una llave
   separadora, siendo "&" el separador por defecto.

urllib.parse.urlunsplit(parts)

   Construct a URL from a tuple as returned by "urlsplit()". The
   *parts* argument can be any five-item iterable. This may result in
   a slightly different, but equivalent URL, if the URL that was
   parsed originally had unnecessary delimiters (for example, a "?"
   with an empty query; the RFC states that these are equivalent).

urllib.parse.urlparse(urlstring, scheme=None, allow_fragments=True)

   This is similar to "urlsplit()", but additionally splits the *path*
   component on *path* and *params*. This function returns a 6-item
   *named tuple* "ParseResult" or "ParseResultBytes". Its items are
   the same as for the "urlsplit()" result, except that *params* is
   inserted at index 3, between *path* and *query*.

   This function is based on obsoleted **RFC 1738** and **RFC 1808**,
   which listed *params* as the main URL component. The more recent
   URL syntax allows parameters to be applied to each segment of the
   *path* portion of the URL (see **RFC 3986**). "urlsplit()" should
   generally be used instead of "urlparse()". A separate function is
   needed to separate the path segments and parameters.

urllib.parse.urlunparse(parts)

   Combine the elements of a tuple as returned by "urlparse()" into a
   complete URL as a string. The *parts* argument can be any six-item
   iterable. This may result in a slightly different, but equivalent
   URL, if the URL that was parsed originally had unnecessary
   delimiters (for example, a ? with an empty query; the RFC states
   that these are equivalent).

urllib.parse.urljoin(base, url, allow_fragments=True)

   Construya una URL completa ("absoluta") combinando una "URL base"
   (*base*) con otra URL (*url*).  Informalmente, esto utiliza
   componentes de la dirección URL base, en particular el esquema de
   direccionamiento, la ubicación de red y (parte de) la ruta de
   acceso, para proporcionar los componentes que faltan en la
   dirección URL relativa.  Por ejemplo:

   >>> from urllib.parse import urljoin
   >>> urljoin('http://www.cwi.nl/%7Eguido/Python.html', 'FAQ.html')
   'http://www.cwi.nl/%7Eguido/FAQ.html'

   The *allow_fragments* argument has the same meaning and default as
   for "urlsplit()".

   Nota:

     Si *url* es una URL absoluta (es decir, comienza con "//" o
     "scheme://"), el nombre de host y/o esquema de *url* estará
     presente en el resultado.  Por ejemplo:

        >>> urljoin('http://www.cwi.nl/%7Eguido/Python.html',
        ...         '//www.python.org/%7Eguido')
        'http://www.python.org/%7Eguido'

     Si no desea ese comportamiento, preprocesa las partes *url* con
     "urlsplit()" y "urlunsplit()", eliminando posibles partes
     *esquema* y *netloc*.

   Advertencia:

     Because an absolute URL may be passed as the "url" parameter, it
     is generally **not secure** to use "urljoin" with an attacker-
     controlled "url". For example in,
     "urljoin("https://website.com/users/", username)", if "username"
     can contain an absolute URL, the result of "urljoin" will be the
     absolute URL.

   Distinto en la versión 3.5: Comportamiento actualizado para
   coincidir con la semántica definida en **RFC 3986**.

urllib.parse.urldefrag(url)

   Si *url* contiene un identificador de fragmento, retorne una
   versión modificada de *url* sin identificador de fragmento y el
   identificador de fragmento como una cadena independiente.  Si no
   hay ningún identificador de fragmento en *url*, retorne *url* sin
   modificar y una cadena vacía.

   El valor retornado es un *named tuple*, se puede acceder a sus
   elementos por índice o como atributos con nombre:

   +--------------------+---------+---------------------------+------------------------+
   | Atributo           | Índice  | Valor                     | Valor si no está       |
   |                    |         |                           | presente               |
   |====================|=========|===========================|========================|
   | "url"              | 0       | URL sin fragmento         | cadena vacía           |
   +--------------------+---------+---------------------------+------------------------+
   | "fragment"         | 1       | Identificador de          | cadena vacía           |
   |                    |         | fragmento                 |                        |
   +--------------------+---------+---------------------------+------------------------+

   Consulte la sección Resultados del análisis estructurado para
   obtener más información sobre el objeto de resultado.

   Distinto en la versión 3.2: El resultado es un objeto estructurado
   en lugar de una simple tupla de 2.

urllib.parse.unwrap(url)

   Extrae la url de una URL envuelta (es decir, una cadena de
   caracteres formateada como "<URL:scheme://host/path>",
   "<scheme://host/path>", "URL:scheme://host/path" or
   "scheme://host/path"). Si *url* no es una URL envuelta, se retorna
   sin cambios.

## Análisis de seguridad de URL

Las APIs "urlsplit()" y "urlparse()" no realizan **validación** de las
entradas.  Es posible que no produzcan errores en entradas que otras
aplicaciones consideren inválidas.  También pueden tener éxito en
algunas entradas que podrían no ser consideradas URLs en otros
lugares.  Su propósito es más la funcionalidad práctica que la pureza.

En vez de generar una excepción en una entrada inusual, pueden
devolver algunas partes componentes como una cadenas vacías. O los
componentes pueden contener más de lo que deberían.

Se recomienda que los usuarios de estas APIs, en las que los valores
se pueden usar en cualquier lugar con implicaciones de seguridad,
codifiquen de forma defensiva. Realicen algunas comprobaciones en su
código antes de confiar en un componente devuelto. ¿Tiene sentido ese
"scheme"? ¿Es ese "path" sensible? ¿Hay algo extraño en ese
"hostname"? etc.

Lo que constituye una URL no está universalmente bien definido.
Aplicaciones diferentes tienen diferentes necesidades y restricciones
deseadas. Por ejemplo, la WHATWG spec describe lo que requieren los
clientes web orientados al usuario, como un navegador web. Mientras
**RFC 3986** es más general. Estas funciones incorporan algunos
aspectos de ambos, pero no se puede afirmar que cumpla con ninguno de
los dos. Las API y el código de usuario existente con expectativas
sobre comportamientos específicos son anteriores a ambos estándares,
lo que nos lleva a ser muy cautelosos realizando cambios en el
comportamiento de la API.

## Análisis de bytes codificados ASCII

Las funciones de análisis de URL se diseñaron originalmente para
funcionar solo en cadenas de caracteres. En la práctica, es útil poder
manipular las direcciones URL correctamente citadas y codificadas como
secuencias de bytes ASCII. En consecuencia, las funciones de análisis
de URL de este módulo funcionan en los objetos "bytes" y "bytearray",
además de los objetos "str".

Si se pasan datos "str", el resultado también contendrá solo los datos
"str". Si se pasan datos "bytes" o "bytearray", el resultado contendrá
solo los datos "bytes".

Si intenta mezclar datos "str" con "bytes" o "bytearray" en una sola
llamada de función, se producirá un "TypeError", mientras que al
intentar pasar valores de bytes no ASCII se desencadenará
"UnicodeDecodeError".

Para admitir una conversión más sencilla de objetos de resultado entre
"str" y "bytes", todos los valores retornados de las funciones de
análisis de URL proporcionan un método "encode()" (cuando el resultado
contiene "str" data) o un método "decode()" (cuando el resultado
contiene datos "bytes"). Las firmas de estos métodos coinciden con las
de los métodos correspondientes "str" y "bytes" (excepto que la
codificación predeterminada es "'ascii"' en lugar de "'utf-8"'). Cada
uno produce un valor de un tipo correspondiente que contiene datos
"bytes" (para los métodos "encode()") o "str" (para "decode()"
métodos).

Las aplicaciones que necesitan operar en direcciones URL
potencialmente citadas incorrectamente que pueden contener datos no
ASCII tendrán que realizar su propia decodificación de bytes a
caracteres antes de invocar los métodos de análisis de URL.

El comportamiento descrito en esta sección solo se aplica a las
funciones de análisis de URL. Las funciones de citación de URL
utilizan sus propias reglas al producir o consumir secuencias de bytes
como se detalla en la documentación de las funciones de citación de
URL individuales.

Distinto en la versión 3.2: Las funciones de análisis de URL ahora
aceptan secuencias de bytes codificadas en ASCII

## Resultados del análisis estructurado

The result objects from the "urlsplit()", "urlparse()"  and
"urldefrag()" functions are subclasses of the "tuple" type. These
subclasses add the attributes listed in the documentation for those
functions, the encoding and decoding support described in the previous
section, as well as an additional method:

urllib.parse.SplitResult.geturl()

   Retorna la versión re-combinada de la dirección URL original como
   una cadena. Esto puede diferir de la dirección URL original en que
   el esquema se puede normalizar a minúsculas y los componentes
   vacíos pueden descartarse. En concreto, se quitarán los parámetros
   vacíos, las consultas y los identificadores de fragmento.

   Para los resultados "urldefrag()", solo se eliminarán los
   identificadores de fragmento vacíos. Para los resultados
   "urlsplit()" y "urlparse()", todos los cambios observados se
   realizarán en la URL retornada por este método.

   El resultado de este método permanece inalterado si se pasa de
   nuevo a través de la función de análisis original:

   >>> from urllib.parse import urlsplit
   >>> url = 'HTTP://www.Python.org/doc/#'
   >>> r1 = urlsplit(url)
   >>> r1.geturl()
   'http://www.Python.org/doc/'
   >>> r2 = urlsplit(r1.geturl())
   >>> r2.geturl()
   'http://www.Python.org/doc/'

Las clases siguientes proporcionan las implementaciones de los
resultados del análisis estructurado cuando se opera en objetos "str":

class urllib.parse.DefragResult(url, fragment)

   Clase concreta para los resultados de "urldefrag()" que contienen
   datos "str". El método "encode()" retorna una instancia
   "DefragResultBytes".

   Added in version 3.2.

class urllib.parse.ParseResult(scheme, netloc, path, params, query, fragment)

   Clase concreta para los resultados de "urlparse()" que contiene
   "str" data. El método "encode()" retorna una instancia
   "ParseResultBytes".

class urllib.parse.SplitResult(scheme, netloc, path, query, fragment)

   Clase concreta para los resultados de "urlsplit()" que contiene
   "str" data. El método "encode()" retorna una instancia
   "SplitResultBytes".

Las clases siguientes proporcionan las implementaciones de los
resultados del análisis cuando se opera en objetos "bytes" o
"bytearray":

class urllib.parse.DefragResultBytes(url, fragment)

   Clase concreta para los resultados de "urldefrag()" que contienen
   datos "bytes". El método "decode()" retorna una instancia
   "DefragResult".

   Added in version 3.2.

class urllib.parse.ParseResultBytes(scheme, netloc, path, params, query, fragment)

   Clase concreta para los resultados "urlparse()" que contienen datos
   "bytes". El método "decode()" retorna una instancia "ParseResult".

   Added in version 3.2.

class urllib.parse.SplitResultBytes(scheme, netloc, path, query, fragment)

   Clase concreta para los resultados de "urlsplit()" que contienen
   datos "bytes". El método "decode()" retorna una instancia
   "SplitResult".

   Added in version 3.2.

## Cita de URL

Las funciones de citación de URL se centran en tomar datos del
programa y hacerlos seguros para su uso como componentes URL citando
caracteres especiales y codificando adecuadamente texto no ASCII.
También admiten la inversión de estas operaciones para volver a crear
los datos originales a partir del contenido de un componente de
dirección URL si esa tarea aún no está cubierta por las funciones de
análisis de URL anteriores.

urllib.parse.quote(string, safe='/', encoding=None, errors=None)

   Reemplaza caracteres especiales en *string* con la secuencia de
   escape "%*xx*". Las letras, los dígitos y los caracteres "'_.-~'"
   nunca se citan. De forma predeterminada, esta función está pensada
   para citar la sección de ruta de acceso de la dirección URL. El
   parámetro opcional *safe* especifica caracteres ASCII adicionales
   que no se deben citar --- su valor predeterminado es "'/'".

   *string* puede ser un objeto "str" o "bytes".

   Distinto en la versión 3.7: Se ha movido de **RFC 2396** a **RFC
   3986** para citar cadenas URL. Ahora se incluye "~" en el conjunto
   de caracteres reservados.

   The optional *encoding* and *errors* parameters specify how to deal
   with non-ASCII characters, as accepted by the "str.encode()"
   method. Although these parameters default to "None" in the function
   signature, when processing "str" inputs, *encoding* effectively
   defaults to "'utf-8'" and *errors* to "'strict'", meaning
   unsupported characters raise a "UnicodeEncodeError". *encoding* and
   *errors* must not be supplied if *string* is a "bytes", or a
   "TypeError" is raised.

   Tenga en cuenta que "quote(string, safe, encoding, errors)" es
   equivalente a "quote_from_bytes(string.encode(encoding, errors),
   safe)".

   Ejemplo: "quote('/El Niño/')" produce "'/El%20Ni%C3%B1o/'".

urllib.parse.quote_plus(string, safe='', encoding=None, errors=None)

   Como "quote()", pero también reemplaza espacios con signos más,
   como se requiere para citar valores de formularios HTML al momento
   de construir una cadena de consulta que será parte de una URL. Los
   signos más en la cadena de caracteres original se escapan, a no ser
   que se incluyan en *safe*. Además el valor de *safe* no es */* por
   defecto.

   Ejemplo: "quote_plus('/El Niño/')" produce "'%2FEl+Ni%C3%B1o%2F'".

urllib.parse.quote_from_bytes(bytes, safe='/')

   Como "quote()", pero acepta un objeto "bytes" en lugar de un "str",
   y no realiza la codificación de cadena a bytes.

   Ejemplo: "quote_from_bytes(b'a&\xef')" produce "'a%26%EF'".

urllib.parse.unquote(string, encoding='utf-8', errors='replace')

   Reemplaza secuencias de escape "%*xx*" con los caracteres
   individuales correspondientes. Los parámetros opcionales *encoding*
   y *errors* especifican cómo descodificar secuencias codificadas
   porcentualmente a caracteres Unicode, tal como lo acepta el método
   "bytes.decode()".

   *string* puede ser un objeto "str" o "bytes".

   *encoding* por defecto es "'utf-8"'. *errors* por defecto es
   "'replace"', lo que significa que las secuencias no válidas se
   reemplazan por un carácter de marcador de posición.

   Ejemplo: "unquote('/El%20Ni%C3%B1o/')" produce "'/El Niño/'".

   Distinto en la versión 3.9: El parámetro *string* admite bytes y
   cadenas de caracteres (anteriormente sólo cadenas de caracteres).

urllib.parse.unquote_plus(string, encoding='utf-8', errors='replace')

   Como "unquote()", pero también reemplaza los signos más por
   espacios, como es requerido al decodificar valores de formularios
   HTML.

   *string* debe ser "str".

   Ejemplo: "unquote_plus('/El+Ni%C3%B1o/')" produce "'/El Niño/'".

urllib.parse.unquote_to_bytes(string)

   Reemplaza los escapes "%*xx*" por sus equivalentes de un solo
   octeto y retorna un objeto "bytes".

   *string* puede ser un objeto "str" o "bytes".

   Si es un "str", los caracteres no ASCII sin escapar en *string* se
   codifican en bytes UTF-8.

   Ejemplo: "unquote_to_bytes('a%26%EF')" produce "b'a&\xef'".

urllib.parse.urlencode(query, doseq=False, safe='', encoding=None, errors=None, quote_via=quote_plus)

   Convierta un objeto de asignación o una secuencia de tuplas de dos
   elementos, que pueden contener objetos "str" o "bytes", en una
   cadena de texto ASCII codificada porcentualmente.  Si la cadena
   resultante se va a utilizar como una operación *data* para post con
   la función "URLlib.request.urlopen()", entonces debe codificarse en
   bytes, de lo contrario resultaría en un "TypeError".

   La cadena resultante es una serie de pares "key=value" separados
   por caracteres "'&'", donde tanto *key* como *value* se citan
   mediante la función *quote_via*.  De forma predeterminada,
   "quote_plus()" se utiliza para citar los valores, lo que significa
   que los espacios se citan como un carácter "'+'" y '/' los
   caracteres se codifican como "%2F", que sigue el estándar para las
   solicitudes GET ("application/x-www-form-urlencoded").  Una función
   alternativa que se puede pasar como *quote_via* es "quote()", que
   codificará espacios como "%20" y no codificará caracteres '/'.
   Para obtener el máximo control de lo que se cita, utilice "quote" y
   especifique un valor para *safe*.

   Cuando se utiliza una secuencia de tuplas de dos elementos como
   argumento *query*, el primer elemento de cada tupla es una clave y
   el segundo es un valor. El valor en sí mismo puede ser una
   secuencia y, en ese caso, si el parámetro opcional *doseq* se
   evalúa como "True", se generan pares individuales "key=value"
   separados por "'&'" para cada elemento de la secuencia de valores
   de la clave.  El orden de los parámetros de la cadena codificada
   coincidirá con el orden de las tuplas de parámetros de la
   secuencia.

   Los parámetros *safe*, *encoding* y *errors* se pasan a *quote_via*
   (los parámetros *encoding* y *errors* solo se pasan cuando un
   elemento de consulta es "str").

   Para revertir este proceso de codificación, en este módulo se
   proporcionan "parse_qs()" y "parse_qsl()" para analizar cadenas de
   consulta en estructuras de datos de Python.

   Consulte urllib examples para averiguar cómo se puede utilizar el
   método  "urllib.parse.urlencode()" para generar una cadena de
   consulta para una dirección URL o datos para POST.

   Distinto en la versión 3.2: El parámetro *query* admite bytes y
   objetos de cadena.

   Distinto en la versión 3.5: Added the *quote_via* parameter.

   Obsoleto desde la versión 3.14: Accepting objects with false values
   (like "0" and "[]") except empty strings and byte-like objects and
   "None" is now deprecated.

Ver también:

  WHATWG -  URL estándar actual
     Grupo de trabajo para el estándar URL que define URLs, dominio,
     dirección IP, formato *application/x-www-form-urlencoded* y su
     API.

  **RFC 3986** - Identificadores uniformes de recursos
     Este es el estándar actual (STD66). Cualquier cambio en el módulo
     urllib.parse debe ajustarse a esto. Se podrían observar ciertas
     desviaciones, que son principalmente para fines de compatibilidad
     con versiones anteriores y para ciertos requisitos de análisis de
     facto como se observa comúnmente en los principales navegadores.

  **RFC 2732** - Formato de direcciones IPv6 literales en URL.
     Esto especifica los requisitos de análisis de las direcciones URL
     IPv6.

  **RFC 2396** - Identificadores uniformes de recursos (URI): Sintaxis
  genérica
     Documento que describe los requisitos sintácticos genéricos para
     los nombres de recursos uniformes (URL) y los localizadores
     uniformes de recursos (URL).

  **RFC 2368** - El esquema mailto URL.
     Análisis de requisitos para esquemas de URL de correo a correo.

  **RFC 1808** - Localizadores uniformes de recursos relativos
     Esta solicitud de comentarios incluye las reglas para unirse a
     una URL absoluta y relativa, incluyendo un buen número de
     "Ejemplos anormales" que rigen el tratamiento de los casos
     fronterizos.

  **RFC 1738** - Localizadores uniformes de recursos (URL)
     Esto especifica la sintaxis formal y la semántica de las
     direcciones URL absolutas.
