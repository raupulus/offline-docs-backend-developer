---
title: '"urllib.request" --- Extensible library for opening URLs'
source_url: https://docs.python.org/es/3
source_path: library/urllib.request.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 4420
---

# "urllib.request" --- Extensible library for opening URLs

**Código fuente:** Lib/urllib/request.py

======================================================================

The "urllib.request" module defines functions and classes which help
in opening URLs (mostly HTTP) in a complex world --- basic and digest
authentication, redirections, cookies and more.

Ver también:

  Se recomienda el paquete Requests para una interfaz de cliente HTTP
  de mayor nivel.

Advertencia:

  On macOS it is unsafe to use this module in programs using
  "os.fork()" because the "getproxies()" implementation for macOS uses
  a higher-level system API. Set the environment variable "no_proxy"
  to "*" to avoid this problem (e.g. "os.environ["no_proxy"] = "*"").

Availability: not WASI.

This module does not work or is not available on WebAssembly. See
Plataformas WebAssembly for more information.

The "urllib.request" module defines the following functions:

urllib.request.urlopen(url, data=None, [timeout, ]*, context=None)

   Abre la *url*, la cual puede ser una cadena de texto que contenga
   una URL válida y correctamente codificada, o un objeto "Request".

   *data* debe ser un objeto que especifique datos adicionales a ser
   enviados al servidor o "None" si no se necesitan tales datos. Vea
   "Request" para más detalles.

   El módulo urllib.request usa HTTP/1.1 e incluye el encabezado
   "Connection:close" en sus peticiones HTTP.

   El parámetro opcional *timeout* especifica un tiempo de expiración
   en segundos para operaciones bloqueantes como el intento de
   conexión (si no se especifica, será usado el tiempo de expiración
   global predeterminado). Esto actualmente sólo funciona para
   conexiones HTTP, HTTPS y FTP.

   Si se especifica *context*, debe ser una instancia "ssl.SSLContext"
   describiendo las diferentes opciones SSL. Vea "HTTPSConnection"
   para más detalles.

   Esta función siempre retorna un objeto que puede actuar como un
   *gestor de contexto*, y tiene las propiedades *url*, *headers* y
   *status*. Véase "urllib.response.addinfourl" para más detalles
   sobre estas propiedades.

   Para URLs HTTP y HTTPS, esta función retorna un objeto
   "http.client.HTTPResponse" ligeramente modificado. Adicionalmente a
   los tres nuevos métodos anteriores, el atributo msg contiene la
   misma información que el atributo "reason" --- la frase de motivo
   devuelta por el servidor --- en lugar de los encabezados de la
   respuesta como se especifica en la documentación para
   "HTTPResponse".

   For FTP, file, and data URLs, this function returns a
   "urllib.response.addinfourl" object.

   Genera "URLError" en errores de protocolo.

   Tenga en cuenta que "None" puede ser retornado si ningún manejador
   gestiona la petición (aunque el "OpenerDirector" global instalado
   de manera predeterminada usa "UnknownHandler" para asegurar que
   esto nunca suceda).

   In addition, if proxy settings are detected (for example, when a
   "*_proxy" environment variable like "http_proxy" is set),
   "ProxyHandler" is default installed and makes sure the requests are
   handled through the proxy.

   La función heredada de Python 2.6 y anteriores "urllib.urlopen" ha
   sido descontinuada, "urllib.request.urlopen()" corresponde a la
   antigua "urllib2.urlopen". La gestión de proxy, la cual se hacía
   pasando un parámetro diccionario a "urllib.urlopen", puede ser
   obtenida usando objetos "ProxyHandler".

   El abridor predeterminado genera un evento de auditoría
   "urllib.Request" con los argumentos "fullurl", "data", "headers",
   "method" tomados del objeto de la petición.

   Distinto en la versión 3.2: *cafile* y *capath* fueron añadidos.Los
   hosts virtuales HTTPS ahora están soportados si es posible (esto
   es, si "ssl.HAS_SNI" es verdadero).*data* puede ser un objeto
   iterable.

   Distinto en la versión 3.3: *cadefault* fue añadido.

   Distinto en la versión 3.4.3: *context* fue añadido.

   Distinto en la versión 3.10: HTTPS connection now send an ALPN
   extension with protocol indicator "http/1.1" when no *context* is
   given. Custom *context* should set ALPN protocols with
   "set_alpn_protocols()".

   Distinto en la versión 3.13: Remove *cafile*, *capath* and
   *cadefault* parameters: use the *context* parameter instead.

urllib.request.install_opener(opener)

   Instala una instancia "OpenerDirector" como el abridor global
   predeterminado. Instalar un abridor sólo es necesario si quieres
   que urlopen use ese abridor; si no, simplemente invoca
   "OpenerDirector.open()" en lugar de "urlopen()". El código no
   comprueba por un "OpenerDirector" real y cualquier clase con la
   interfaz apropiada funcionará.

urllib.request.build_opener([handler, ...])

   Retorna una instancia "OpenerDirector", la cual encadena los
   manejadores en el orden dado. *handler*s pueden ser tanto
   instancias de "BaseHandler" o subclases de "BaseHandler" (en cuyo
   caso debe ser posible invocar el constructor sin ningún parámetro).
   Instancias de las siguientes clases estarán delante del *handler*s,
   a no ser que el *handler*s las contenga, instancias o subclases de
   ellas: "ProxyHandler" (si son detectadas configuraciones de proxy),
   "UnknownHandler", "HTTPHandler", "HTTPDefaultErrorHandler",
   "HTTPRedirectHandler", "FTPHandler", "FileHandler",
   "HTTPErrorProcessor".

   Si la instalación de Python tiene soporte SSL (ej. si se puede
   importar el módulo "ssl"), también será añadida "HTTPSHandler".

   Una subclase de "BaseHandler" puede cambiar también su atributo
   "handler_order" para modificar su posición en la lista de
   manejadores.

urllib.request.pathname2url(path, *, add_scheme=False)

   Convert the given local path to a "file:" URL. This function uses
   "quote()" function to encode the path.

   If *add_scheme* is false (the default), the return value omits the
   "file:" scheme prefix. Set *add_scheme* to true to return a
   complete URL.

   This example shows the function being used on Windows:

      >>> from urllib.request import pathname2url
      >>> path = 'C:\\Program Files'
      >>> pathname2url(path, add_scheme=True)
      'file:///C:/Program%20Files'

   Distinto en la versión 3.14: Windows drive letters are no longer
   converted to uppercase, and ":" characters not following a drive
   letter no longer cause an "OSError" exception to be raised on
   Windows.

   Distinto en la versión 3.14: Paths beginning with a slash are
   converted to URLs with authority sections. For example, the path
   "/etc/hosts" is converted to the URL "///etc/hosts".

   Distinto en la versión 3.14: The *add_scheme* parameter was added.

urllib.request.url2pathname(url, *, require_scheme=False, resolve_host=False)

   Convert the given "file:" URL to a local path. This function uses
   "unquote()" to decode the URL.

   If *require_scheme* is false (the default), the given value should
   omit a "file:" scheme prefix. If *require_scheme* is set to true,
   the given value should include the prefix; a "URLError" is raised
   if it doesn't.

   The URL authority is discarded if it is empty, "localhost", or the
   local hostname. Otherwise, if *resolve_host* is set to true, the
   authority is resolved using "socket.gethostbyname()" and discarded
   if it matches a local IP address (as per **RFC 8089 §3**). If the
   authority is still unhandled, then on Windows a UNC path is
   returned, and on other platforms a "URLError" is raised.

   This example shows the function being used on Windows:

      >>> from urllib.request import url2pathname
      >>> url = 'file:///C:/Program%20Files'
      >>> url2pathname(url, require_scheme=True)
      'C:\\Program Files'

   Distinto en la versión 3.14: Windows drive letters are no longer
   converted to uppercase, and ":" characters not following a drive
   letter no longer cause an "OSError" exception to be raised on
   Windows.

   Distinto en la versión 3.14: The URL authority is discarded if it
   matches the local hostname. Otherwise, if the authority isn't empty
   or "localhost", then on Windows a UNC path is returned (as before),
   and on other platforms a "URLError" is raised.

   Distinto en la versión 3.14: The URL query and fragment components
   are discarded if present.

   Distinto en la versión 3.14: The *require_scheme* and
   *resolve_host* parameters were added.

urllib.request.getproxies()

   Esta función auxiliar retorna un diccionario de esquema para las
   asignaciones de URL del servidor proxy. Escanea el entorno en busca
   de variables denominadas "<scheme>_proxy", tomando en cuenta
   diferencia entre mayúsculas y minúsculas, para todos los sistemas
   operativos primero, y cuando no pueden encontrarla, buscan
   información proxy desde la Configuración del Sistema de macOS y
   desde Registros del Sistema para Windows. Si existen variables de
   entorno tanto en mayúsculas como en minúsculas (y no concuerdan),
   las minúsculas son preferidas.

   Nota:

     Si la variable del entorno "REQUEST_METHOD" está definida, lo
     cual usualmente indica que tu script está ejecutándose en un
     entorno CGI, la variable de entorno "HTTP_PROXY" (mayúsculas
     "_PROXY") será ignorada. Esto es porque esa variable puede ser
     inyectada por un cliente usando el encabezado HTTP "Proxy:". Si
     necesitas usar un proxy HTTP en un entorno CGI, usa
     "ProxyHandler" explícitamente o asegúrate de que el nombre de la
     variable está en minúsculas (o al menos el sufijo "_proxy").

Se proveen las siguientes clases:

class urllib.request.Request(url, data=None, headers={}, origin_req_host=None, unverifiable=False, method=None)

   Esta clase es un abstracción de una petición URL.

   *url* debe ser una cadena de texto que contenga una URL válida y
   correctamente codificada.

   *data* debe ser un objeto que especifique datos adicionales a
   enviar al servidor o "None" si no se necesitan tales datos.
   Actualmente las peticiones HTTP son las únicas que usan *data*. Los
   tipos de objetos soportados incluyen bytes, objetos como archivos e
   iterables de objetos como bytes. Si no se ha provisto el campo de
   encabezado "Content-Length" ni "Transfer-Encoding", "HTTPHandler"
   establecerá estos encabezados de acuerdo al tipo de *data*.
   "Content-Length" será usado para enviar objetos de bytes, mientras
   "Transfer-Encoding: chunked" como se especifica en **RFC 7230**,
   Sección 3.3.1 será usado para enviar archivos y otros iterables.

   Para un método de una petición HTTP POST, *data* debe ser un buffer
   en el formato estándar *application/x-www-form-urlencoded*. La
   función "urllib.parse.urlencode()" toma un mapeo o una secuencia de
   tuplas de dos valores y retorna una cadena de caracteres ASCII en
   este formato. Debe ser codificada a bytes antes de ser usada como
   el parámetro *data*.

   *headers* debe ser un diccionario, y será tratado como si
   "add_header()" fuera invocado con cada clave y valor como
   argumentos. Esto es usado frecuentemente para "parodiar" el valor
   de encabezado "User-Agent", el cual es usado por un navegador para
   identificarse a sí mismo -- algunos servidores HTTP sólo permiten
   peticiones que vienen de navegadores comunes a diferencia de los
   scripts. Por ejemplo, Mozilla Firefox puede identificarse a sí
   mismo como ""Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127
   Firefox/2.0.0.11"", mientras el agente de usuario predeterminado de
   "urllib" es ""Python-urllib/2.6"" (en Python 2.6). Todas las claves
   de los encabezados se envían en camel case.

   An appropriate "Content-Type" header should be included if the
   *data* argument is present.  If this header has not been provided
   and *data* is not "None", "Content-Type: application/x-www-form-
   urlencoded" will be added as a default.

   Los siguientes dos argumentos sólo tienen interés para la gestión
   correcta de cookies HTTP de terceros:

   *origin_req_host* debe ser el host de la petición de la transacción
   origen, como define **RFC 2965**. Por defecto es
   "http.cookiejar.request_host(self)". Este es el nombre de host o la
   dirección IP de la petición original que fue iniciada por el
   usuario. Por ejemplo, si la petición es para una imagen en un
   documento HTML, debe ser el host de la petición para la página que
   contiene la imagen.

   *unverifiable* debe indicar si la petición no es verificable, como
   define **RFC 2965**. Por defecto es "False". Una petición no
   verificable es una cuya URL el usuario no tuvo opción de aprobar.
   Por ejemplo, si la petición es por una imagen en un documento HTML
   y el usuario no tuvo opción de aprobar la obtención automática de
   la imagen, este debe ser verdadero.

   *method* should be a string that indicates the HTTP request method
   that will be used (e.g. "'HEAD'").  If provided, its value is
   stored in the "method" attribute and is used by "get_method()". The
   default is "'GET'" if *data* is "None" or "'POST'" otherwise.
   Subclasses may indicate a different default method by setting the
   "method" attribute in the class itself.

   Nota:

     La petición no funcionará como se espera si el objeto de datos es
     incapaz de entregar su contenido más de una vez (ej. un archivo o
     un iterable que puede producir el contenido sólo una vez) y la
     petición se reintentará para redirecciones HTTP o autenticación.
     El *data* es enviado al servidor HTTP directamente después de los
     encabezados. No hay soporte para una expectativa de
     funcionamiento 100% continuo en la biblioteca.

   Distinto en la versión 3.3: El argumento "Request.method" es
   añadido a la clase Request.

   Distinto en la versión 3.4: El atributo predeterminado
   "Request.method" puede ser indicado a nivel de clase.

   Distinto en la versión 3.6: No se genera un error si el "Content-
   Length" no ha sido provisto y *data* no es "None" ni un objeto de
   bytes. En su lugar recurre a la codificación de transferencia
   fragmentada.

class urllib.request.OpenerDirector

   La clase "OpenerDirector" abre URLs mediante la encadenación
   conjunta de "BaseHandler". Este maneja el encadenamiento de
   manejadores y la recuperación de errores.

class urllib.request.BaseHandler

   Esta es la clase base para todos los manejadores registrados --- y
   manejan sólo las mecánicas simples del registro.

class urllib.request.HTTPDefaultErrorHandler

   Una clase la cual define un manejador predeterminado para los
   errores de respuesta HTTP; todas las respuestas son convertidas en
   excepciones "HTTPError".

class urllib.request.HTTPRedirectHandler

   Una clase para manejar redirecciones.

class urllib.request.HTTPCookieProcessor(cookiejar=None)

   Una clase para manejar Cookies HTTP.

class urllib.request.ProxyHandler(proxies=None)

   Causa que las peticiones vayan a través de un proxy. Si se provee
   *proxies*, debe ser un diccionario mapeando nombres de protocolos a
   URLs de proxies. Por defecto lee la lista de proxies de las
   variables de entorno "<protocol>_proxy". Si no se establecen
   variables de entorno de proxy, entonces se obtienen las
   configuraciones de proxy en un entorno Windows desde la sección del
   registro de Configuraciones de Internet y en un entorno macOS se
   obtiene la información de proxy desde el Framework de Configuración
   del Sistema.

   Para deshabilitar la detección automática de proxy pasa un
   diccionario vacío.

   La variable de entorno "no_proxy" puede ser usada para especificar
   hosts los cuales no deben ser alcanzados mediante proxy; si se
   establece, debe ser una lista separada por comas de sufijos de
   nombres de host, con ":port" añadidos opcionalmente, por ejemplo
   "cern.ch,ncsa.uiuc.edu,some.host:8080".

   Nota:

     "HTTP_PROXY" será ignorado si se establece una variable
     "REQUEST_METHOD"; vea la documentación de "getproxies()".

class urllib.request.HTTPPasswordMgr

   Mantiene una base de datos de mapeos "(realm, uri) -> (user,
   password)".

class urllib.request.HTTPPasswordMgrWithDefaultRealm

   Mantiene una base de datos de mapeos "(realm, uri) -> (user,
   password)". Un reino de "None" se considera un reino caza todo, el
   cual es buscado si ningún otro reino encaja.

class urllib.request.HTTPPasswordMgrWithPriorAuth

   Una variante de "HTTPPasswordMgrWithDefaultRealm" que también tiene
   una base de datos de mapeos "uri -> is_authenticated". Puede ser
   usada por un manejador BasicAuth para determinar cuando enviar
   credenciales de autenticación inmediatamente en lugar de esperar
   primero a una respuesta "401".

   Added in version 3.5.

class urllib.request.AbstractBasicAuthHandler(password_mgr=None)

   Esta es una clase mixin que ayuda con la autenticación HTTP, tanto
   al host remoto y a un proxy. Si se proporciona *password_mgr*, debe
   ser algo compatible con "HTTPPasswordMgr"; refiera a la sección
   Objetos HTTPPasswordMgr para información sobre la interfaz que debe
   ser soportada. Si *passwd_mgr* proporciona también métodos
   "is_authenticated" y "update_authenticated" (vea Objetos
   HTTPPasswordMgrWithPriorAuth), entonces el manejador usará el
   "is_authenticated" resultado para una URI dada para determinar el
   envío o no de credenciales de autenticación con la petición. Si
   "is_authenticated" retorna "True" para la URI, las peticiones
   subsecuentes a la URI o cualquiera de las super URIs incluirán
   automáticamente los credenciales de autenticación.

   Added in version 3.5: Añadido soporte "is_authenticated".

class urllib.request.HTTPBasicAuthHandler(password_mgr=None)

   Administra autenticación con el host remoto. Si se proporciona
   *password_mgr*, debe ser compatible con "HTTPPasswordMgr"; refiera
   a la sección Objetos HTTPPasswordMgr para información sobre la
   interfaz que debe ser soportada. HTTPBasicAuthHandler lanzará un
   "ValueError" cuando se presente con un esquema de Autenticación
   incorrecto.

class urllib.request.ProxyBasicAuthHandler(password_mgr=None)

   Administra autenticación con el proxy. Si se proporciona
   *password_mgr* debe ser compatible con "HTTPPasswordMgr"; refiera a
   la sección Objetos HTTPPasswordMgr para información sobre la
   interfaz que debe ser soportada.

class urllib.request.AbstractDigestAuthHandler(password_mgr=None)

   Esto es una clase mixin que ayuda con la autenticación HTTP, tanto
   al host remoto como a un proxy. Si se proporciona *password_mgr*
   debe ser compatible con "HTTPPasswordMgr"; refiera a la sección
   Objetos HTTPPasswordMgr para información sobre la interfaz que debe
   ser soportada.

   Distinto en la versión 3.14: Added support for HTTP digest
   authentication algorithm "SHA-256".

class urllib.request.HTTPDigestAuthHandler(password_mgr=None)

   Maneja autenticación con el host remoto. Si se proporciona
   *password_mgr* debe ser compatible con "HTTPPasswordMgr"; refiera a
   la sección Objetos HTTPPasswordMgr para información sobre la
   interfaz que debe ser soportada. Cuando se añaden tanto el
   Manejador de Autenticación Digest (*Digest Authentication Handler*)
   como el Manejador de Autenticación Básico (*Basic Authentication
   Handler*) la Autenticación Digest siempre se intenta primero. Si la
   Autenticación Digest retorna una respuesta 40x de nuevo, se envía
   al controlador de Autenticación Básica para Manejar. Este método
   Handler lanzará un "ValueError" cuando sea presentado con un
   esquema de autenticación diferente a Digest o Básico.

   Distinto en la versión 3.3: Genera "ValueError" en Esquema de
   Autenticación no soportado.

class urllib.request.ProxyDigestAuthHandler(password_mgr=None)

   Administra autenticación con el proxy. Si se proporciona
   *password_mgr* debe ser compatible con "HTTPPasswordMgr"; refiera a
   la sección Objetos HTTPPasswordMgr para información sobre la
   interfaz que debe ser soportada.

class urllib.request.HTTPHandler

   Una clase para gestionar apertura de URLs HTTP.

class urllib.request.HTTPSHandler(debuglevel=0, context=None, check_hostname=None)

   Una clase para gestionar apertura de URLs HTTPS. *context* y
   *check_hostname* tienen el mismo significado que en
   "http.client.HTTPSConnection".

   Distinto en la versión 3.2: *context* y *check_hostname* fueron
   añadidos.

class urllib.request.FileHandler

   Abre archivos locales.

class urllib.request.DataHandler

   Abre URLs de datos.

   Added in version 3.4.

class urllib.request.FTPHandler

   Abre URLs FTP.

class urllib.request.CacheFTPHandler

   Abre URLs FTP, manteniendo una caché de conexiones FTP abiertas
   para minimizar retrasos.

class urllib.request.UnknownHandler

   Una clase caza todo para gestionar URLs desconocidas.

class urllib.request.HTTPErrorProcessor

   Procesa errores de respuestas HTTP.

## Objetos Request

Los siguientes métodos describen la interfaz pública de "Request" por
lo que pueden ser sobrescritos en subclases. También define varios
atributos públicos que pueden ser usado por clientes para inspeccionar
la respuesta analizada.

Request.full_url

   La URL original pasada al constructor.

   Distinto en la versión 3.4.

   Request.full_url es una propiedad con setter, getter y deleter.
   Obtener "full_url" retorna la petición URL original con el
   fragmento, si este estaba presente.

Request.type

   El esquema de URI.

Request.host

   La autoridad de URI, típicamente un host, pero también puede
   contener un puerto separado por un caracter de doble punto.

Request.origin_req_host

   El host original de la petición, sin puerto.

Request.selector

   La ruta de URI. Si "Request" usa un proxy, entonces selector será
   la URL completa que se pasa al proxy.

Request.data

   El cuerpo de la entidad para la solicitud o "None" si no es
   especificado.

   Distinto en la versión 3.4: Cambiar el valor de "Request.data"
   elimina ahora el encabezado "Content-Length" si fue establecido o
   calculado previamente.

Request.unverifiable

   booleano, indica si la petición no es verificable como se define
   por **RFC 2965**.

Request.method

   El método de petición HTTP a usar. Por defecto su valor es "None",
   lo que significa que "get_method()" realizará su cálculo normal del
   método a usar. Su valor puede ser definido (sobrescribiendo así el
   cálculo predeterminado en "get_method()") tanto proporcionando un
   valor por defecto estableciéndolo a nivel de clase en una subclase
   de "Request" o pasando un valor al constructor de "Request" por
   medio del argumento *method*.

   Added in version 3.3.

   Distinto en la versión 3.4: Un valor predeterminado puede ser
   establecido ahora en subclases; previamente sólo podía ser definido
   mediante el argumento del constructor.

Request.get_method()

   Retorna una cadena indicando el método de petición HTTP. Si
   "Request.method" no es "None", retorna su valor, de otra forma
   retorna "'GET'" si "Request.data" es "None" o "'POST'" si no lo es.
   Esto sólo es significativo para peticiones HTTP.

   Distinto en la versión 3.3: get_method ahora mira el valor de
   "Request.method".

Request.add_header(key, val)

   Añade otro encabezado a la petición. Los encabezados actualmente
   son ignorados por todos los manejadores excepto los manejadores
   HTTP, donde son añadidos a la lista de encabezados enviados al
   servidor. Tenga en cuenta que no puede haber más de un encabezado
   con el mismo nombre y las invocaciones posteriores sobrescribirán
   las invocaciones previas en caso de que *key* colisione.
   Actualmente, esto no es una pérdida de funcionalidad HTTP, ya que
   todos los encabezados que tienen sentido cuando son usados más de
   una vez tienen una manera (específica de encabezado) de ganar la
   misma funcionalidad usando sólo un encabezado. Tenga en cuenta que
   los encabezados agregados con este método también se agregan a las
   solicitudes redirigidas.

Request.add_unredirected_header(key, header)

   Añade un encabezado que no será añadido a una petición
   redireccionada.

Request.has_header(header)

   Retorna si la instancia tiene el encabezado nombrado (comprueba
   tanto regular como no redirigido).

Request.remove_header(header)

   Elimina el encabezado nombrado de la instancia de la petición
   (desde encabezados regulares y no redireccionados).

   Added in version 3.4.

Request.get_full_url()

   Retorna la URL dada en el constructor.

   Distinto en la versión 3.4.

   Retorna "Request.full_url"

Request.set_proxy(host, type)

   Prepara la petición conectando a un servidor proxy. Los *host* y
   *type* reemplazarán aquellos de la instancia y el selector de la
   instancia será la URL original dada en el constructor.

Request.get_header(header_name, default=None)

   Retorna el valor del encabezado dado.

Request.header_items()

   Retorna una lista de tuplas (header_name, header_value) de los
   encabezados de la Petición.

Distinto en la versión 3.4: Los métodos de petición add_data,
has_data, get_data, get_type, get_host, get_selector,
get_origin_req_host y is_unverifiable que quedaron obsoletos desde 3.3
han sido eliminados.

## Objetos OpenerDirector

Las instancias de "OpenerDirector" tienen los siguientes métodos:

OpenerDirector.add_handler(handler)

   *handler* debe ser una instancia de "BaseHandler". Los siguientes
   métodos son buscados y añadidos a las cadenas posibles (tenga en
   cuenta que los errores HTTP son un caso espacial). Tenga en cuenta
   que, en los siguientes, *protocol* debe ser remplazado con el
   protocolo actual a manejar, por ejemplo "http_response()" sería el
   protocolo HTTP del manejador de respuesta. También *type* debe ser
   remplazado con el código HTTP actual, por ejemplo
   "http_error_404()" manejaría errores HTTP 404.

   * "<protocol>_open()" --- signal that the handler knows how to open
     *protocol* URLs.

     Vea "BaseHandler.<protocol>_open()" para más información.

   * "http_error_<type>()" --- signal that the handler knows how to
     handle HTTP errors with HTTP error code *type*.

     Vea "BaseHandler.http_error_<nnn>()" para más información.

   * "<protocol>_error()" --- signal that the handler knows how to
     handle errors from (non-"http") *protocol*.

   * "<protocol>_request()" --- signal that the handler knows how to
     pre-process *protocol* requests.

     Vea "BaseHandler.<protocol>_request()" para más información.

   * "<protocol>_response()" --- signal that the handler knows how to
     post-process *protocol* responses.

     Vea "BaseHandler.<protocol>_response()" para más información.

OpenerDirector.open(url, data=None[, timeout])

   Abre la *url* dada (la cual puede ser un objeto de petición o una
   cadena de caracteres), pasando opcionalmente el *data* dado. Los
   argumentos, los valores de retorno y las excepciones generadas son
   las mismas que aquellas de "urlopen()" (las cuales simplemente
   invocan el método "open()" en el "OpenerDirector" instalado
   global). El parámetro opcional *timeout* especifica un tiempo de
   expiración en segundos para operaciones bloqueantes como el intento
   de conexión (si no se especifica, el tiempo de expiración global
   será usado). La característica de tiempo de expiración actualmente
   funciona sólo para conexiones HTTP, HTTPS y FTP.

OpenerDirector.error(proto, *args)

   Handle an error of the given protocol.  This will call the
   registered error handlers for the given protocol with the given
   arguments (which are protocol specific).  The HTTP protocol is a
   special case which uses the HTTP response code to determine the
   specific error handler; refer to the "http_error_<type>()" methods
   of the handler classes.

   Retorna si los valores y excepciones generadas son las mismas que
   aquellas de "urlopen()".

Los objetos OpenerDirector abren URLs en tres etapas:

El orden en el cual esos métodos son invocados dentro de cada etapa es
determinado ordenando las instancias manejadoras.

1. Every handler with a method named like "<protocol>_request()" has
   that method called to pre-process the request.

2. Handlers with a method named like "<protocol>_open()" are called to
   handle the request. This stage ends when a handler either returns a
   non-"None" value (ie. a response), or raises an exception (usually
   "URLError").  Exceptions are allowed to propagate.

   In fact, the above algorithm is first tried for methods named
   "default_open()".  If all such methods return "None", the algorithm
   is repeated for methods named like "<protocol>_open()".  If all
   such methods return "None", the algorithm is repeated for methods
   named "unknown_open()".

   Tenga en cuenta que la implementación de esos métodos puede
   involucrar invocaciones de los métodos "open()" y "error()" de la
   instancia "OpenerDirector" padre.

3. Every handler with a method named like "<protocol>_response()" has
   that method called to post-process the response.

## Objetos BaseHandler

Los objetos "BaseHandler" proporcionan un par de métodos que son
útiles directamente y otros que están destinados a ser utilizados por
clases derivadas. Estos están pensados para uso directo:

BaseHandler.add_parent(director)

   Añade un director como padre.

BaseHandler.close()

   Elimina cualquier padre.

El siguiente atributo y los siguientes métodos sólo deben ser usados
por clases derivadas de "BaseHandler".

Nota:

  The convention has been adopted that subclasses defining
  "<protocol>_request()" or "<protocol>_response()" methods are named
  "*Processor"; all others are named "*Handler".

BaseHandler.parent

   Un "OpenerDirector" válido, el cual puede ser utilizado para abrir
   usando un protocolo diferente, o para manejar errores.

BaseHandler.default_open(req)

   Este método no es definido en "BaseHandler", pero las subclases
   deben definirlo si quieren cazar todas las URLs.

   This method, if implemented, will be called by the parent
   "OpenerDirector".  It should return a file-like object as described
   in the return value of the "open()" method of "OpenerDirector", or
   "None". It should raise "URLError", unless a truly exceptional
   thing happens (for example, "MemoryError" should not be mapped to
   "URLError").

   Este método será invocado antes de cualquier método de apertura
   específico de protocolo.

BaseHandler.<protocol>_open(req)

   Este método no está definido en "BaseHandler", pero las subclases
   deben definirlo si quieren manejar URLs con el protocolo dado.

   This method, if defined, will be called by the parent
   "OpenerDirector". Return values should be the same as for
   "default_open()".

BaseHandler.unknown_open(req)

   Este método *no* está definido en "BaseHandler", pero las subclases
   deben definirlo si quieren cazar todas las URLs sin manejador
   registrado para abrirlo.

   Este método, si está implementado, será invocado por el "parent" de
   "OpenerDirector". Los valores retornados deben ser los mismos que
   para "default_open()".

BaseHandler.http_error_default(req, fp, code, msg, hdrs)

   Este método *no* está definido en "BaseHandler", pero las subclases
   deben sobreescribirlo si pretenden proporcionar una solución
   general para los errores HTTP que de otro modo no se manejarían.
   Sería invocado automáticamente por el "OpenerDirector" obteniendo
   el error y no debe ser invocado normalmente en otras
   circunstancias.

   "OpenerDirector" will call this method with five positional
   arguments:

   1. a "Request" object,

   2. a file-like object with the HTTP error body,

   3. the three-digit code of the error, as a string,

   4. the user-visible explanation of the code, as a string, and

   5. the headers of the error, as a mapping object.

   Los valores de retorno y las excepciones generadas deben ser los
   mismos que aquellos de "urlopen()".

BaseHandler.http_error_<nnn>(req, fp, code, msg, hdrs)

   *nnn* debe ser un código de error HTTP de tres dígitos. Este método
   tampoco está definido en "BaseHandler", pero será invocado, si
   existe, en una instancia de una subclase, cuando ocurra un error
   HTTP con código *nnn*.

   Las subclases deben sobrescribir este método para manejar errores
   HTTP específicos.

   Arguments, return values and exceptions raised should be the same
   as for "http_error_default()".

BaseHandler.<protocol>_request(req)

   Este método *no* está definido en "BaseHandler", pero las subclases
   deben definirlo si pretenden preprocesar peticiones del protocolo
   dado.

   Este método, si está definido, será invocado por el
   "OpenerDirector" padre. *req* será un objeto "Request". El valor
   retornado debe ser un objeto "Request".

BaseHandler.<protocol>_response(req, response)

   Este método *no* está definido en "BaseHandler", pero las subclases
   deben definirlo si quieren postprocesar respuestas del protocolo
   dado.

   Este método, si está definido, será invocado por el
   "OpenerDirector" padre. *req* será un objeto "Request". *response*
   será un objeto que implementa la misma interfaz que el valor
   retornado de "urlopen()". El valor retornado debe implementar la
   misma interfaz que el valor retornado de "urlopen()".

## Objetos HTTPRedirectHandler

Nota:

  Algunas redirecciones HTTP requieren acción desde el código del
  módulo del cliente. Si este es el caso, se genera "HTTPError". Vea
  **RFC 2616** para más detalles de los significados precisos de los
  diferentes códigos de redirección.An "HTTPError" exception raised as
  a security consideration if the HTTPRedirectHandler is presented
  with a redirected URL which is not an HTTP, HTTPS or FTP URL.

HTTPRedirectHandler.redirect_request(req, fp, code, msg, hdrs, newurl)

   Return a "Request" or "None" in response to a redirect. This is
   called by the default implementations of the "http_error_30*()"
   methods when a redirection is received from the server.  If a
   redirection should take place, return a new "Request" to allow
   "http_error_30*()" to perform the redirect to *newurl*.  Otherwise,
   raise "HTTPError" if no other handler should try to handle this
   URL, or return "None" if you can't but another handler might.

   Nota:

     La implementación predeterminada de este método no sigue
     estrictamente **RFC 2616**, la cual dice que las respuestas 301 y
     302 a peticiones POST no deben ser redirigidas automáticamente
     sin confirmación por el usuario. En realidad, los navegadores
     permiten redirección automática de esas respuestas, cambiando el
     POST a un "GET" y la implementación predeterminada reproduce este
     comportamiento.

HTTPRedirectHandler.http_error_301(req, fp, code, msg, hdrs)

   Redirecciona a la URL "Location:" o "URI:". Este método es invocado
   por el "OpenerDirector" padre al obtener una respuesta HTTP 'moved
   permanently'.

HTTPRedirectHandler.http_error_302(req, fp, code, msg, hdrs)

   Lo mismo que "http_error_301()", pero invocado para la respuesta
   'found'.

HTTPRedirectHandler.http_error_303(req, fp, code, msg, hdrs)

   Lo mismo que "http_error_301()", pero invocado para la respuesta
   'see other'.

HTTPRedirectHandler.http_error_307(req, fp, code, msg, hdrs)

   Lo mismo que "http_error_301()", pero invocado para la respuesta
   'redirección temporal'. No permite cambiar el método de solicitud
   de "POST" a "GET".

HTTPRedirectHandler.http_error_308(req, fp, code, msg, hdrs)

   Lo mismo que "http_error_301()", pero invocado para la respuesta
   'redirección permanente'. No permite cambiar el método de solicitud
   de "POST" a "GET".

   Added in version 3.11.

## Objetos HTTPCookieProcessor

Las instancias "HTTPCookieProcessor" tienen un atributo:

HTTPCookieProcessor.cookiejar

   El "http.cookiejar.CookieJar" en el cual las cookies están
   almacenadas.

## Objetos ProxyHandler

ProxyHandler.<protocol>_open(request)

   The "ProxyHandler" will have a method "<protocol>_open()" for every
   *protocol* which has a proxy in the *proxies* dictionary given in
   the constructor.  The method will modify requests to go through the
   proxy, by calling "request.set_proxy()", and call the next handler
   in the chain to actually execute the protocol.

## Objetos HTTPPasswordMgr

Estos métodos están disponibles en los objetos "HTTPPasswordMgr" y
"HTTPPasswordMgrWithDefaultRealm".

HTTPPasswordMgr.add_password(realm, uri, user, passwd)

   *uri* puede ser una única URI o una secuencia de URIs. *realm*,
   *user* y *passwd* deben ser cadenas. Esto causa que "(user,
   passwd)" se utilice como tokens de autenticación cuando la
   autenticación para *realm* y para una super URI de ninguna de las
   URIs dadas es provista.

HTTPPasswordMgr.find_user_password(realm, authuri)

   Obtener usuario/contraseña para el reino y URI dados, si alguno ha
   sido dado. Este método retornará "(None, None)" si no hay
   usuario/contraseña concordante.

   Para objetos "HTTPPasswordMgrWithDefaultRealm", el reino "None"
   será buscado si el *realm* dado no tiene usuario/contraseña
   concordante.

## Objetos HTTPPasswordMgrWithPriorAuth

Esta manejador de contraseña extiende
"HTTPPasswordMgrWithDefaultRealm" para soportar el seguimiento de URIs
para las cuales deben ser enviadas siempre credenciales de
autenticación.

HTTPPasswordMgrWithPriorAuth.add_password(realm, uri, user, passwd, is_authenticated=False)

   *realm*, *uri*, *user*, *passwd* son como para
   "HTTPPasswordMgr.add_password()". *is_authenticated* establece el
   valor inicial del indicador "is_authenticated" para la URI o lista
   de URIs dadas. Si se especifica *is_authenticated* como "True",
   *realm* se ignora.

HTTPPasswordMgrWithPriorAuth.find_user_password(realm, authuri)

   Lo mismo que para objetos "HTTPPasswordMgrWithDefaultRealm"

HTTPPasswordMgrWithPriorAuth.update_authenticated(self, uri, is_authenticated=False)

   Actualiza el indicador "is_authenticated" para la *uri* o lista de
   URIs dadas.

HTTPPasswordMgrWithPriorAuth.is_authenticated(self, authuri)

   Retorna el estado actual del indicador "is_authenticated" para la
   URI dada.

## Objetos AbstractBasicAuthHandler

AbstractBasicAuthHandler.http_error_auth_reqed(authreq, host, req, headers)

   Maneja una autenticación de petición obteniendo un par
   usuario/contraseña y reintentando la petición. *authreq* debe ser
   el nombre del encabezado donde la información sobre el reino se
   incluye en la petición, *host* especifica la URL y ruta para la
   cual autenticar, *req* debe ser el objeto "Request" (fallido) y
   *headers* deben ser los encabezados de error.

   *host* is either an authority (e.g. ""python.org"") or a URL
   containing an authority component (e.g. ""https://python.org/"").
   In either case, the authority must not contain a userinfo component
   (so, ""python.org"" and ""python.org:80"" are fine,
   ""joe:password@python.org"" is not).

## Objetos HTTPBasicAuthHandler

HTTPBasicAuthHandler.http_error_401(req, fp, code, msg, hdrs)

   Reintenta la petición con la información de autenticación, si está
   disponible.

## Objetos ProxyBasicAuthHandler

ProxyBasicAuthHandler.http_error_407(req, fp, code, msg, hdrs)

   Reintenta la petición con la información de autenticación, si está
   disponible.

## Objetos AbstractDigestAuthHandler

AbstractDigestAuthHandler.http_error_auth_reqed(authreq, host, req, headers)

   *authreq* debe ser el nombre del encabezado donde la información
   sobre el reino está incluida en la petición, *host* debe ser el
   host al que autenticar, *req* debe ser el objeto "Request"
   (fallido) y *headers* deben ser los encabezados de error.

## Objetos HTTPDigestAuthHandler

HTTPDigestAuthHandler.http_error_401(req, fp, code, msg, hdrs)

   Reintenta la petición con la información de autenticación, si está
   disponible.

## Objetos ProxyDigestAuthHandler

ProxyDigestAuthHandler.http_error_407(req, fp, code, msg, hdrs)

   Reintenta la petición con la información de autenticación, si está
   disponible.

## Objetos HTTPHandler

HTTPHandler.http_open(req)

   Send an HTTP request, which can be either GET or POST, depending on
   "req.data".

## Objetos HTTPSHandler

HTTPSHandler.https_open(req)

   Send an HTTPS request, which can be either GET or POST, depending
   on "req.data".

## Objetos FileHandler

FileHandler.file_open(req)

   Abre el archivo localmente, si no hay nombre de host, o el nombre
   de host es "'localhost'".

   Distinto en la versión 3.2: This method is applicable only for
   local hostnames.  When a remote hostname is given, a "URLError" is
   raised.

## Objetos DataHandler

DataHandler.data_open(req)

   Read a data URL. This kind of URL contains the content encoded in
   the URL itself. The data URL syntax is specified in **RFC 2397**.
   This implementation ignores white spaces in base64 encoded data
   URLs so the URL may be wrapped in whatever source file it comes
   from. But even though some browsers don't mind about a missing
   padding at the end of a base64 encoded data URL, this
   implementation will raise a "ValueError" in that case.

## Objetos FTPHandler

FTPHandler.ftp_open(req)

   Abre el archivo FTP indicado por *req*. El inicio de sesión siempre
   se realiza con un usuario y contraseña vacíos.

## Objetos CacheFTPHandler

Los objetos "CacheFTPHandler" son objetos "FTPHandler" con los
siguientes métodos adicionales:

CacheFTPHandler.setTimeout(t)

   Establece el tiempo de expiración de conexiones a *t* segundos.

CacheFTPHandler.setMaxConns(m)

   Establece el número máximo de conexiones cacheadas a *m*.

## Objetos UnknownHandler

UnknownHandler.unknown_open()

   Genera una excepción "URLError".

## Objetos HTTPErrorProcessor

HTTPErrorProcessor.http_response(request, response)

   Procesa errores de respuestas HTTP.

   Para códigos de error que no están en el rango de los 200, el
   objeto de respuesta es retornado inmediatamente.

   For non-200 error codes, this simply passes the job on to the
   "http_error_<type>()" handler methods, via
   "OpenerDirector.error()". Eventually, "HTTPDefaultErrorHandler"
   will raise an "HTTPError" if no other handler handles the error.

HTTPErrorProcessor.https_response(request, response)

   Procesa los errores HTTPS de las respuestas.

   Este comportamiento es el mismo que "http_response()".

## Ejemplos

Adicionalmente a los ejemplos siguientes, se dan más ejemplos en HOWTO
- Cómo obtener recursos de Internet con el paquete urllib.

This example gets the python.org main page and displays the first 300
bytes of it:

   >>> import urllib.request
   >>> with urllib.request.urlopen('https://www.python.org/') as f:
   ...     # The response may be compressed (for example, 'gzip').
   ...     print(f.headers.get('Content-Encoding'))
   ...     data = f.read()
   ...     if f.headers.get('Content-Encoding') == 'gzip':
   ...         import gzip
   ...         data = gzip.decompress(data)
   ...     print(data[:300].decode('utf-8', errors='replace'))

Tenga en cuenta que urlopen retorna un objeto de bytes. Esto es porque
no hay forma para urlopen de determinar automáticamente la
codificación del flujo de bytes que recibe del servidor HTTP. En
general, un programa decodificará el objeto de bytes retornado a
cadena de caracteres una vez que determine o adivine la codificación
apropiada.

The following HTML spec document,
https://html.spec.whatwg.org/#charset, lists the various ways in which
an HTML or an XML document could have specified its encoding
information.

For additional information, see the W3C document:
https://www.w3.org/International/questions/qa-html-encoding-
declarations.

As the python.org website uses *utf-8* encoding as specified in its
meta tag, we will use the same for decoding the bytes object:

   >>> with urllib.request.urlopen('https://www.python.org/') as f:
   ...     # Check for compression and decode appropriately.
   ...     enc = f.headers.get('Content-Encoding')
   ...     data = f.read()
   ...     if enc == 'gzip':
   ...         import gzip
   ...         data = gzip.decompress(data)
   ...     print(data[:100].decode('utf-8', errors='replace'))
   ...

It is also possible to achieve the same result without using the
*context manager* approach:

   >>> import urllib.request
   >>> f = urllib.request.urlopen('https://www.python.org/')
   >>> try:
   ...     enc = f.headers.get('Content-Encoding')
   ...     data = f.read()
   ...     if enc == 'gzip':
   ...         import gzip
   ...         data = gzip.decompress(data)
   ...     print(data[:100].decode('utf-8', errors='replace'))
   ... finally:
   ...     f.close()

En el siguiente ejemplo, estamos enviando un flujo de datos a la
entrada estándar de un CGI y leyendo los datos que nos retorna. Tenga
en cuenta que este ejemplo sólo funcionará cuando la instalación de
Python soporte SSL.

   >>> import urllib.request
   >>> req = urllib.request.Request(url='https://localhost/cgi-bin/test.cgi',
   ...                       data=b'This data is passed to stdin of the CGI')
   >>> with urllib.request.urlopen(req) as f:
   ...     print(f.read().decode('utf-8'))
   ...
   Got Data: "This data is passed to stdin of the CGI"

El código para el CGI de muestra usado en el ejemplo anterior es:

   #!/usr/bin/env python
   import sys
   data = sys.stdin.read()
   print('Content-type: text/plain\n\nGot Data: "%s"' % data)

Aquí hay un ejemplo de realizar una petición "PUT" usando "Request":

   import urllib.request
   DATA = b'some data'
   req = urllib.request.Request(url='http://localhost:8080', data=DATA, method='PUT')
   with urllib.request.urlopen(req) as f:
       pass
   print(f.status)
   print(f.reason)

Uso de Autenticación HTTP Básica:

   import urllib.request
   # Create an OpenerDirector with support for Basic HTTP Authentication...
   auth_handler = urllib.request.HTTPBasicAuthHandler()
   auth_handler.add_password(realm='PDQ Application',
                             uri='https://mahler:8092/site-updates.py',
                             user='klem',
                             passwd='kadidd!ehopper')
   opener = urllib.request.build_opener(auth_handler)
   # ...and install it globally so it can be used with urlopen.
   urllib.request.install_opener(opener)
   with urllib.request.urlopen('http://www.example.com/login.html') as f:
       print(f.read().decode('utf-8'))

"build_opener()" provides many handlers by default, including a
"ProxyHandler".  By default, "ProxyHandler" uses the environment
variables named "<scheme>_proxy", where "<scheme>" is the URL scheme
involved.  For example, the "http_proxy" environment variable is read
to obtain the HTTP proxy's URL.

Este ejemplo reemplaza el "ProxyHandler" predeterminado por uno que
usa URLs de proxy suministradas mediante programación y añade soporte
de autorización de proxy con "ProxyBasicAuthHandler".

   proxy_handler = urllib.request.ProxyHandler({'http': 'http://www.example.com:3128/'})
   proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()
   proxy_auth_handler.add_password('realm', 'host', 'username', 'password')

   opener = urllib.request.build_opener(proxy_handler, proxy_auth_handler)
   # This time, rather than install the OpenerDirector, we use it directly:
   with opener.open('http://www.example.com/login.html') as f:
      print(f.read().decode('utf-8'))

Añadiendo encabezados HTTP:

Usa el argumento *headers* en el constructor de "Request", o:

   import urllib.request
   req = urllib.request.Request('http://www.example.com/')
   req.add_header('Referer', 'https://www.python.org/')
   # Customize the default User-Agent header value:
   req.add_header('User-Agent', 'urllib-example/0.1 (Contact: . . .)')
   with urllib.request.urlopen(req) as f:
       print(f.read().decode('utf-8'))

"OpenerDirector" añade automáticamente un encabezado *User-Agent* a
cada "Request". Para cambiar esto:

   import urllib.request
   opener = urllib.request.build_opener()
   opener.addheaders = [('User-agent', 'Mozilla/5.0')]
   with opener.open('http://www.example.com/') as f:
      print(f.read().decode('utf-8'))

También, recuerda que algunos encabezados estándar (*Content-Length*,
*Content-Type* y *Host*) son añadidos cuando se pasa "Request" a
"urlopen()" (o "OpenerDirector.open()").

Aquí hay un ejemplo de sesión que usa el método "GET" para obtener una
URL que contiene los parámetros:

   >>> import urllib.request
   >>> import urllib.parse
   >>> params = urllib.parse.urlencode({'spam': 1, 'eggs': 2, 'bacon': 0})
   >>> url = "https://www.python.org/?%s" % params
   >>> with urllib.request.urlopen(url) as f:
   ...     print(f.read().decode('utf-8'))
   ...

El siguiente ejemplo usa el método POST en su lugar. Tenga en cuenta
que la salida de parámetros desde urlencode es codificada a bytes
antes de ser enviados a urlopen como datos:

   >>> import urllib.request
   >>> import urllib.parse
   >>> data = urllib.parse.urlencode({'spam': 1, 'eggs': 2, 'bacon': 0})
   >>> data = data.encode('ascii')
   >>> with urllib.request.urlopen("https://httpbin.org/post", data) as f:
   ...     print(f.read().decode('utf-8'))
   ...

El siguiente ejemplo usa un proxy HTTP especificado, sobrescribiendo
las configuraciones de entorno:

   >>> import urllib.request
   >>> proxies = {'http': 'http://proxy.example.com:8080/'}
   >>> opener = urllib.request.build_opener(urllib.request.ProxyHandler(proxies))
   >>> with opener.open("https://www.python.org") as f:
   ...     f.read().decode('utf-8')
   ...

El siguiente ejemplo no usa proxies, sobrescribiendo las variables de
entorno:

   >>> import urllib.request
   >>> opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
   >>> with opener.open("https://www.python.org/") as f:
   ...     f.read().decode('utf-8')
   ...

## Interfaz heredada

Las siguientes funciones y clases están portadas desde el módulo
"urllib" de Python 2 (en oposición a "urllib2"). Ellas pueden estar
obsoletas en algún punto del futuro.

urllib.request.urlretrieve(url, filename=None, reporthook=None, data=None)

   Copy a network object denoted by a URL to a local file. If the URL
   points to a local file, the object will not be copied unless
   filename is supplied. Return a tuple "(filename, headers)" where
   *filename* is the local file name under which the object can be
   found, and *headers* is whatever the "info()" method of the object
   returned by "urlopen()" returned (for a remote object). Exceptions
   are the same as for "urlopen()".

   El segundo argumento, si está presente, especifica la localización
   a la que será copiada el objeto (si está ausente, la localización
   será un archivo temporal con un nombre generado). El tercer
   argumento, si está presente, es un objeto invocable que será
   invocado una vez que se establezca la conexión de red y después de
   eso una vez después de cada lectura de bloque. Al invocable se le
   pasarán tres argumentos; una cuenta de los bloques transferidos
   hasta el momento, un tamaño de bloque en bytes y el tamaño total
   del archivo. El tercer argumento puede ser "-1" en servidores FTP
   antiguos los cuales no retornan un tamaño de archivo en respuesta a
   una solicitud de recuperación.

   El siguiente ejemplo ilustra el escenario de uso más común:

      >>> import urllib.request
      >>> local_filename, headers = urllib.request.urlretrieve('https://python.org/')
      >>> html = open(local_filename)
      >>> html.close()

   Si la *url* usa el esquema de identificador "http:", el argumento
   opcional *data* puede ser dado para especificar una petición "POST"
   (normalmente el tipo de petición es "GET"). El argumento *data*
   debe ser un objeto de bytes en formato *application/x-www-form-
   urlencoded*; vea la función "urllib.parse.urlencode()".

   "urlretrieve()" will raise "ContentTooShortError" when it detects
   that the amount of data available  was less than the expected
   amount (which is the size reported by a  *Content-Length* header).
   This can occur, for example, when the  download is interrupted.

   El *Content-Length* es tratado como un límite inferior: si no hay
   más datos a leer, urlretrieve lee más datos, pero si están
   disponibles menos datos, se genera la excepción.

   You can still retrieve the downloaded data in this case, it is
   stored in the "content" attribute of the exception instance.

   Si no fue proporcionado el encabezado *Content-Length*, urlretrieve
   no puede comprobar el tamaño de los datos que han sido descargados,
   y sólo los retorna. En este caso sólo tienes que asumir que la
   descarga fue exitosa.

urllib.request.urlcleanup()

   Cleans up temporary files that may have been left behind by
   previous calls to "urlretrieve()".  It also resets the default
   global opener installed by "install_opener()".

## "urllib.request" Restrictions

* Actualmente, sólo uno de los siguientes protocolo están soportados:
  HTTP (versiones 0.9 y 1.0), FTP, archivos locales y URLs de datos.

  Distinto en la versión 3.4: Añadido soporte para URLs de datos.

* La característica de caché de "urlretrieve()" ha sido deshabilitada
  hasta que alguien encuentre el tiempo para hackear el procesamiento
  adecuado de los encabezados de tiempo de Expiración.

* Debería haber una función para consultar si una URL en particular
  está en la caché.

* Para compatibilidad con versiones anteriores, si una URL parece
  apuntar a un archivo local pero el archivo no puede ser abierto, la
  URL es reinterpretada usando el protocolo FTP. Esto a veces puede
  causar mensajes de error confusos.

* Las funciones "urlopen()" y "urlretrieve()" pueden causar retrasos
  arbitrariamente largos mientras esperan a que se configure una
  conexión de red. Esto significa que es difícil construir un cliente
  Web interactivo usando estas funciones sin utilizar hilos.

* Los datos retornados por "urlopen()" o "urlretrieve()" son los datos
  en crudo retornados por el servidor. Estos pueden ser datos binarios
  (como una imagen), texto plano o (por ejemplo) HTML. El protocolo
  HTTP provee información de tipo en el encabezado de respuesta, el
  cual puede ser inspeccionado mirando el encabezado *Content-Type*.
  Si los datos retornados son HTML, puedes usar el módulo
  "html.parser" para analizarlos.

* The code handling the FTP protocol cannot differentiate between a
  file and a directory.  This can lead to unexpected behavior when
  attempting to read a URL that points to a file that is not
  accessible.  If the URL ends in a "/", it is assumed to refer to a
  directory and will be handled accordingly.  But if an attempt to
  read a file leads to a 550 error (meaning the URL cannot be found or
  is not accessible, often for permission reasons), then the path is
  treated as a directory in order to handle the case when a directory
  is specified by a URL but the trailing "/" has been left off.  This
  can cause misleading results when you try to fetch a file whose read
  permissions make it inaccessible; the FTP code will try to read it,
  fail with a 550 error, and then perform a directory listing for the
  unreadable file. If fine-grained control is needed, consider using
  the "ftplib" module.

# "urllib.response" --- Response classes used by urllib

The "urllib.response" module defines functions and classes which
define a minimal file-like interface, including "read()" and
"readline()". Functions defined by this module are used internally by
the "urllib.request" module. The typical response object is a
"urllib.response.addinfourl" instance:

class urllib.response.addinfourl

   url

      :URL del recurso obtenido, comúnmente usado para determinar si
      se ha seguido una redirección.

   headers

      Retorna las cabeceras de la respuesta en la forma de una
      instancia de "EmailMessage".

   status

      Added in version 3.9.

      Código de estado  retornado por el servidor.

   geturl()

      Obsoleto desde la versión 3.9: Obsoleto en favor de "url".

   info()

      Obsoleto desde la versión 3.9: Obsoleto en favor de "headers".

   code

      Obsoleto desde la versión 3.9: Obsoleto en favor de "status".

   getcode()

      Obsoleto desde la versión 3.9: Obsoleto en favor de "status".
