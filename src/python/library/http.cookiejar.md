---
title: '"http.cookiejar" --- Cookie handling for HTTP clients'
source_url: https://docs.python.org/es/3
source_path: library/http.cookiejar.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 2860
---

# "http.cookiejar" --- Cookie handling for HTTP clients

**Código fuente:** Lib/http/cookiejar.py

======================================================================

The "http.cookiejar" module defines classes for automatic handling of
HTTP cookies.  It is useful for accessing websites that require small
pieces of data -- *cookies* -- to be set on the client machine by an
HTTP response from a web server, and then returned to the server in
later HTTP requests.

Both the regular Netscape cookie protocol and the protocol defined by
**RFC 2965** are handled.  RFC 2965 handling is switched off by
default. **RFC 2109** cookies are parsed as Netscape cookies and
subsequently treated either as Netscape or RFC 2965 cookies according
to the 'policy' in effect. Note that the great majority of cookies on
the internet are Netscape cookies. "http.cookiejar" attempts to follow
the de-facto Netscape cookie protocol (which differs substantially
from that set out in the original Netscape specification), including
taking note of the "max-age" and "port" cookie-attributes introduced
with RFC 2965.

Nota:

  The various named parameters found in *Set-Cookie* and *Set-Cookie2*
  headers (for example, "domain" and "expires") are conventionally
  referred to as *attributes*.  To distinguish them from Python
  attributes, the documentation for this module uses the term *cookie-
  attribute* instead.

El módulo define la siguiente excepción:

exception http.cookiejar.LoadError

   Las instancias de "FileCookieJar" provocan esta excepción al no
   cargar las cookies desde un archivo. "LoadError" es una subclase de
   "OSError".

   Distinto en la versión 3.3: "LoadError" used to be a subtype of
   "IOError", which is now an alias of "OSError".

Se proporcionan las siguientes clases:

class http.cookiejar.CookieJar(policy=None)

   *policy* es un objeto implementando la interfaz "CookiePolicy".

   La clase "CookieJar" almacena HTTP cookies. Ésta extrae cookies de
   los request de HTTP, y las retorna en forma de responses de HTTP.
   Las instancias de "CookieJar" automáticamente expiran las cookies
   contenidas cuando es necesario. Las subclases también son
   responsables de almacenar y recuperar cookies de un archivo o base
   de datos.

class http.cookiejar.FileCookieJar(filename=None, delayload=None, policy=None)

   *policy* es un objeto implementando la interfaz "CookiePolicy".
   Para los otros argumentos, te recomendamos visitar la documentación
   correspondiente a los atributos.

   Una "CookieJar" puede cargar cookies de, y posiblemente almacenar,
   un archivo en el disco. Las cookies **NO** son cargadas desde un
   archivo nombrado hasta que alguno de los métodos "load()" o
   "revert()" es llamado. Subclases de esta clase son documentadas en
   la sección Subclases FileCookieJar y co-operación con navegadores
   web.

   Esto no debe inicializarse directamente; en su lugar, use sus
   subclases a continuación.

   Distinto en la versión 3.8: El parámetro filename soporta un *path-
   like object*.

class http.cookiejar.CookiePolicy

   Esta clase es responsable de decidir si cada cookie debe ser
   aceptada del servidor, o retornada al mismo.

class http.cookiejar.DefaultCookiePolicy(blocked_domains=None, allowed_domains=None, netscape=True, rfc2965=False, rfc2109_as_netscape=None, hide_cookie2=False, strict_domain=False, strict_rfc2965_unverifiable=True, strict_ns_unverifiable=False, strict_ns_domain=DefaultCookiePolicy.DomainLiberal, strict_ns_set_initial_dollar=False, strict_ns_set_path=False, secure_protocols=('https', 'wss'))

   Constructor arguments should be passed as keyword arguments only.
   *blocked_domains* is a sequence of domain names that we never
   accept cookies from, nor return cookies to. *allowed_domains* if
   not "None", this is a sequence of the only domains for which we
   accept and return cookies. *secure_protocols* is a sequence of
   protocols for which secure cookies can be added to. By default
   *https* and *wss* (secure websocket) are considered secure
   protocols. For all other arguments, see the documentation for
   "CookiePolicy" and "DefaultCookiePolicy" objects.

   "DefaultCookiePolicy" implements the standard accept / reject rules
   for Netscape and **RFC 2965** cookies.  By default, **RFC 2109**
   cookies (that is, cookies received in a *Set-Cookie* header with a
   version cookie-attribute of 1) are treated according to the RFC
   2965 rules.  However, if RFC 2965 handling is turned off or
   "rfc2109_as_netscape" is "True", RFC 2109 cookies are 'downgraded'
   by the "CookieJar" instance to Netscape cookies, by setting the
   "version" attribute of the "Cookie" instance to 0.
   "DefaultCookiePolicy" also provides some parameters to allow some
   fine-tuning of policy.

class http.cookiejar.Cookie

   This class represents Netscape, **RFC 2109** and **RFC 2965**
   cookies.  It is not expected that users of "http.cookiejar"
   construct their own "Cookie" instances.  Instead, if necessary,
   call "make_cookies()" on a "CookieJar" instance.

Ver también:

  Módulo "urllib.request"
     Apertura de URL con manejo automático de cookies.

  Módulo "http.cookies"
     HTTP cookie classes, principally useful for server-side code.
     The "http.cookiejar" and "http.cookies" modules do not depend on
     each other.

  https://curl.se/rfc/cookie_spec.html
     The specification of the original Netscape cookie protocol.
     Though this is still the dominant protocol, the 'Netscape cookie
     protocol' implemented by all the major browsers (and
     "http.cookiejar") only bears a passing resemblance to the one
     sketched out in "cookie_spec.html".

  **RFC 2109** - Mecanismo de Gestión de Estados HTTP
     Obsoleto por **RFC 2965**. Usa *Set-Cookie* con versión=1.

  **RFC 2965** - Mecanismo de Gestión de Estados HTTP
     El protocolo Netscape con los errores solucionados. Usa *Set-
     Cookie2* en lugar de *Set-Cookie*. No es ampliamente usado.

  https://kristol.org/cookie/errata.html
     Fe de erratas sin finalizar hasta el **RFC 2965**.

  **RFC 2964** - Mecanismo de Gestión de Estados HTTP

## CookieJar and FileCookieJar objects

Los objetos "CookieJar" soportan el protocolo *iterator* para iterar
sobre los objetos "Cookie" contenidos.

"CookieJar" tiene los siguientes métodos:

CookieJar.add_cookie_header(request)

   Añade la cookie correcta a la cabecera del request.

   If policy allows (that is, the "rfc2965" and "hide_cookie2"
   attributes of the "CookieJar"'s "CookiePolicy" instance are true
   and false respectively), the *Cookie2* header is also added when
   appropriate.

   The *request* object (usually a "urllib.request.Request" instance)
   must support the methods "get_full_url()", "has_header()",
   "get_header()", "header_items()", "add_unredirected_header()" and
   the attributes "host", "type", "unverifiable" and "origin_req_host"
   as documented by "urllib.request".

   Distinto en la versión 3.3: *request* object needs
   "origin_req_host" attribute. Dependency on a deprecated method
   "get_origin_req_host()" has been removed.

CookieJar.extract_cookies(response, request)

   Extrae las cookies del *response* HTTP y las almacena en el
   "CookieJar", donde está permitido por la policy.

   El "CookieJar" buscará por cabeceras *Set-Cookie* y *Set-Cookie2*
   permitidos en el argumento *response*, y almacena las cookies
   cuando es apropiado (sujeto a la aprobación del método
   "CookiePolicy.set_ok()").

   The *response* object (usually the result of a call to
   "urllib.request.urlopen()", or similar) should support an "info()"
   method, which returns an "email.message.Message" instance.

   The *request* object (usually a "urllib.request.Request" instance)
   must support the method "get_full_url()" and the attributes "host",
   "unverifiable" and "origin_req_host", as documented by
   "urllib.request".  The request is used to set default values for
   cookie-attributes as well as for checking that the cookie is
   allowed to be set.

   Distinto en la versión 3.3: *request* object needs
   "origin_req_host" attribute. Dependency on a deprecated method
   "get_origin_req_host()" has been removed.

CookieJar.set_policy(policy)

   Establece la instancia "CookiePolicy" para ser usada.

CookieJar.make_cookies(response, request)

   Retorna una secuencia de objetos "Cookie" extraída del objeto
   *response*.

   Revisa la documentación "extract_cookies()" para conocer las
   interfaces necesarias de los argumentos *response* y *request*.

CookieJar.set_cookie_if_ok(cookie, request)

   Establece una "Cookie" si la política (*policy*) dice OK para
   hacerlo.

CookieJar.set_cookie(cookie)

   Establece una "Cookie", sin consultar con la política (*policy*)
   para ver si se debe de establecer o no.

CookieJar.clear([domain[, path[, name]]])

   Borra algunas cookies.

   Si se invoca sin argumentos, borra todas las cookies. Si se le da
   un solo argumento. sólo las cookies que pertenecen a tal *domain*
   serán removidas. Si se le da dos argumentos, las cookies
   pertenecientes al especificado *domain* y *path* URL serán
   removidas. Si se le da tres argumentos, entonces la cookie con el
   especificado *domain*, *path* y *name* será removida.

   Lanza "KeyError" si no existe ninguna cookie que coincida.

CookieJar.clear_session_cookies()

   Descarta todas las cookies de la sesión.

   Discards all contained cookies that have a true "discard" attribute
   (usually because they had either no "max-age" or "expires" cookie-
   attribute, or an explicit "discard" cookie-attribute).  For
   interactive browsers, the end of a session usually corresponds to
   closing the browser window.

   Note that the "save()" method won't save session cookies anyway,
   unless you ask otherwise by passing a true *ignore_discard*
   argument.

"FileCookieJar" implementa los siguientes métodos adicionales:

FileCookieJar.save(filename=None, ignore_discard=False, ignore_expires=False)

   Guarda las cookies en un archivo.

   Esta clase base genera "NotImplementedError". Las subclases podrían
   dejar este método sin implementar.

   *filename* is the name of file in which to save cookies.  If
   *filename* is not specified, "self.filename" is used (whose default
   is the value passed to the constructor, if any); if "self.filename"
   is "None", "ValueError" is raised.

   *ignore_discard*: almacena incluso las cookies configuradas para
   ser descartadas. *ignore_expires*: almacena las cookies que han
   caducado

   El archivo se sobrescribe si ya existe, borrando así todas las
   cookies que contiene. Las cookies guardadas se pueden restaurar
   después utilizando los métodos "load()" o "revert()".

FileCookieJar.load(filename=None, ignore_discard=False, ignore_expires=False)

   Carga las cookies desde un archivo.

   Las viejas cookies son guardadas a menos que sean sobre escritas
   por nuevas recién cargadas.

   Los argumentos son en cuanto a "save()".

   El archivo nombrado debe estar en un formato entendible para la
   clase, o se lanzará un "LoadError". Además, puede generarse un
   "OSError", por ejemplo, si el archivo no existe.

   Distinto en la versión 3.3: Solía levantarse un "IOError", pero
   ahora es un alias de "OSError".

FileCookieJar.revert(filename=None, ignore_discard=False, ignore_expires=False)

   Limpia todas las cookies y recarga las cookies de un archivo
   guardado.

   "revert()" puede levantar las mismas excepciones que "load()". Si
   hay un fallo. el estado del objeto no se alterará.

Instancias "FileCookieJar" tienen los siguientes atributos públicos:

FileCookieJar.filename

   Nombre del archivo predeterminado para el archivo en donde se
   almacenan las cookies. Este atributo podría ser asignado.

FileCookieJar.delayload

   Si es true, carga perezosamente las cookies desde el disco. Este
   atributo no se debería de asignar. Esta es solo una pista, debido a
   que solo el rendimiento, y no al comportamiento (a menos que las
   cookies en el disco sean cambiadas). Un objeto "CookieJar" puede
   ignorarlo. Ninguna de las clases de "FileCookieJar" incluidas en la
   librería estándar carga las cookies de manera perezosa.

## Subclases FileCookieJar y co-operación con navegadores web

Las siguientes subclases "CookieJar" son proveídas para lectura y
escritura.

class http.cookiejar.MozillaCookieJar(filename=None, delayload=None, policy=None)

   Un "FileCookieJar" que puede cargar y guardar cookies al disco en
   el formato de archivo "cookies.txt" de Mozilla (que también es
   utilizado por curl y los navegadores Lynx y Netscape).

   Nota:

     Esto puede perder información acerca de cookies **RFC 2965**, y
     también sobre atributos nuevos o no estándar como "port".

   Advertencia:

     Realiza una copia de seguridad de tus cookies antes de
     guardarlas, especialmente si tienes cookies cuya perdida /
     corrupción puede ser inconveniente (hay algunas sutilezas que
     pueden conducir a ligeros cambios en el archivo sobre una carga /
     guardado round-trip).

   También toma en cuenta que las cookies guardadas mientras Mozilla
   se está ejecutando se volverán torpes debido a Mozilla.

class http.cookiejar.LWPCookieJar(filename=None, delayload=None, policy=None)

   Un "FileCookieJar" que puede cargar y guardar en disco en formato
   compatible con el formato de archivo "Set-Cookie3" de la librería
   libwww-perl. Estos es conveniente si tu quieres guardar cookies en
   un archivo legible para los humanos.

   Distinto en la versión 3.8: El parámetro filename soporta un *path-
   like object*.

## CookiePolicy objects

Objetos implementando la interfaz "CookiePolicy" tienen los siguientes
métodos:

CookiePolicy.set_ok(cookie, request)

   Retorna un valor booleano indicando si la cookie debe ser aceptada
   o no desde el servidor.

   *cookie* es una instancia de "Cookie". *request* es un objeto
   implementando la interfaz definida por la documentación de
   "CookieJar.extract_cookies()".

CookiePolicy.return_ok(cookie, request)

   Retorna un valor booleano indicando si la cookie debe ser retornada
   o no al servidor.

   *cookie* es una instancia de "Cookie". *request* es un objeto
   implementando la interfaz definida por la documentación de
   "CookieJar.add_cookie_header()".

CookiePolicy.domain_return_ok(domain, request)

   Retorna "False" si las cookies no deben de ser retornadas, a partir
   del dominio cookie dado.

   Este método es una optimización. Elimina la necesidad de verificar
   cada cookie con un domino en particular (lo cual puede involucrar
   la lectura de muchos archivos). Retornando true de
   "domain_return_ok()" y "path_return_ok()" deja todo el trabajo a
   "return_ok()".

   Si "domain_return_ok()" retorna true para el dominio de cookies,
   "path_return_ok()" es llamado para el path de cookies. De otra
   manera, "path_return_ok()" y "return_ok()" no son nunca llamados
   para ese dominio de cookies. Si "path_return_ok()" retorna true,
   "return_ok()" es llamado con el objeto "Cookie" en sí para una
   revisión completa. De otra manera, "return_ok()" es nunca llamado
   para ese path de cookies.

   Ten en cuenta que "domain_return_ok()" es llamado para cada dominio
   *cookie*, no solamente para el dominio *request*. Por ejemplo, la
   función podría ser llamada con ambos "".example.com"" y
   ""www.example.com"" si el dominio request es ""www.example.com"".
   Lo mismo se aplica para "path_return_ok()".

   El argumento *request* es tal y como es documentado para
   "return_ok()".

CookiePolicy.path_return_ok(path, request)

   Retorna "False" si las cookies no deben de ser retornadas, dado el
   path de las cookies.

   Revisa la documentación para "domain_return_ok()".

Adicionalmente a los métodos implementados anteriormente, las
implementaciones de la interfaz "CookiePolicy" también deben de
proporcionar los siguientes atributos, indicando cuales protocolos
deben de ser utilizados, y como. Todos estos atributos se pueden
asignar.

CookiePolicy.netscape

   Implementa el protocolo Netscape.

CookiePolicy.rfc2965

   Implementa el protocolo **RFC 2965**.

CookiePolicy.hide_cookie2

   No añadas la cabecera *Cookie2* a las requests (la presencia de
   esta cabecera indica al servidor que nosotros entendemos las
   cookies **RFC 2965**).

El camino más útil para definir una clase "CookiePolicy" es haciendo
una subclase de "DefaultCookiePolicy" y sobre escribir algunos o todos
los métodos anteriores. "CookiePolicy" en sí misma puede ser utilizada
como una 'null policy' para permitir establecer y recibir algunas o
todas las cookies (esto raramente puede ser útil).

## DefaultCookiePolicy objects

Implementa las reglas estándar para aceptar y retornar cookies.

Ambas cookies, **RFC 2965** y Netscape son cubiertas. El manejo del
RFC 2965 está desactivado de forma predeterminada.

La forma más sencilla de proporcionar tu propia política (*policy*) es
sobre escribir esta clase y llamar sus métodos en tus implementaciones
modificadas antes de añadir tu propias comprobaciones adicionales:

   import http.cookiejar
   class MyCookiePolicy(http.cookiejar.DefaultCookiePolicy):
       def set_ok(self, cookie, request):
           if not http.cookiejar.DefaultCookiePolicy.set_ok(self, cookie, request):
               return False
           if i_dont_want_to_store_this_cookie(cookie):
               return False
           return True

En adición a las características requeridas para implementar la
interfaz "CookiePolicy", esta clase te permite que bloquees o permitas
dominios de establecer y recibir cookies. También hay algunos
interruptores estrictos que te permiten ajustar un poco las reglas
flojas del protocolo Netscape (a costa de bloquear algunas cookies
benignas).

A domain blocklist and allowlist is provided (both off by default).
Only domains not in the blocklist and present in the allowlist (if the
allowlist is active) participate in cookie setting and returning.  Use
the *blocked_domains* constructor argument, and "blocked_domains()"
and "set_blocked_domains()" methods (and the corresponding argument
and methods for *allowed_domains*).  If you set an allowlist, you can
turn it off again by setting it to "None".

Los dominios en listas de bloqueos o permitidos que no comienzan con
un punto deben ser iguales al dominio de la cookie para que coincidan.
Por ejemplo, ""example.com"" coincide con una entrada de lista de
bloqueo de ""example.com"", pero ""www.example.com"" no. Los dominios
que comienzan con un punto también se corresponden con dominios más
específicos. Por ejemplo, tanto ""www.example.com"" como
""www.coyote.example.com"" coinciden con "".example.com"" (pero el
propio ""example.com"" no lo hace). Las direcciones IP son una
excepción y deben coincidir exactamente. Por ejemplo, si block_domains
contiene ""192.168.1.2"" y "".168.1.2"", 192.168.1.2 está bloqueado,
pero 193.168.1.2 no.

"DefaultCookiePolicy" implementa los siguientes métodos adicionales:

DefaultCookiePolicy.blocked_domains()

   Retorna una secuencia de dominios bloqueados (en forma de tupla).

DefaultCookiePolicy.set_blocked_domains(blocked_domains)

   Establece la secuencia de dominios bloqueados.

DefaultCookiePolicy.is_blocked(domain)

   Retorna "True" si *domain* está en la lista de bloqueo para
   establecer o recibir cookies.

DefaultCookiePolicy.allowed_domains()

   Return "None", or the sequence of allowed domains (as a tuple).

DefaultCookiePolicy.set_allowed_domains(allowed_domains)

   Set the sequence of allowed domains, or "None".

DefaultCookiePolicy.is_not_allowed(domain)

   Retorna "True" si *domain* no está en la lista de permitidos para
   establecer o recibir cookies.

Las instancias "DefaultCookiePolicy" tienen los siguientes atributos,
que son todos inicializados desde los argumentos del constructor del
mismo nombre, y el cual todos pueden ser asignados a.

DefaultCookiePolicy.rfc2109_as_netscape

   If true, request that the "CookieJar" instance downgrade **RFC
   2109** cookies (that is, cookies received in a *Set-Cookie* header
   with a version cookie-attribute of 1) to Netscape cookies by
   setting the version attribute of the "Cookie" instance to 0.  The
   default value is "None", in which case RFC 2109 cookies are
   downgraded if and only if **RFC 2965** handling is turned off.
   Therefore, RFC 2109 cookies are downgraded by default.

Interruptores generales de rigurosidad:

DefaultCookiePolicy.strict_domain

   No permite que los sitios establezcan dominios de dos componentes
   con dominios country-code top-level como ".co.uk", ".gov.uk",
   ".co.nz".etc. ¡Esto está lejos de ser perfecto y no está
   garantizado a que vaya a funcionar!

Interruptores de rigurosidad del protocolo **RFC 2965**:

DefaultCookiePolicy.strict_rfc2965_unverifiable

   Siga las reglas **RFC 2965** sobre transacciones no verificables
   (normalmente, una transacción no verificable es una del resultado
   de una redirección o una solicitud de una imagen alojada en otro
   sitio). Si esto es falso, las cookies *nunca* se bloquean en base a
   la verificabilidad

Interruptores de rigurosidad del protocolo Netscape:

DefaultCookiePolicy.strict_ns_unverifiable

   Aplica las reglas del **RFC 2965** a transacciones no verificables
   incluso a cookies Netscape.

DefaultCookiePolicy.strict_ns_domain

   Indicadores que señalan que tan estricto deben ser con las reglas
   de domain-matching para cookies Netscape. Consulte a continuación
   los valores aceptables.

DefaultCookiePolicy.strict_ns_set_initial_dollar

   Ignora las cookies en las cabeceras Set-Cookie: que tengan nombres
   que comienzan con "'$'".

DefaultCookiePolicy.strict_ns_set_path

   No permite establecer cookies cuyo path no concuerde con el request
   URI.

"strict_ns_domain" is a collection of flags.  Its value is constructed
by or-ing together (for example,
"DomainStrictNoDots|DomainStrictNonDomain" means both flags are set).

DefaultCookiePolicy.DomainStrictNoDots

   When setting cookies, the 'host prefix' must not contain a dot (for
   example, "www.foo.bar.com" can't set a cookie for ".bar.com",
   because "www.foo" contains a dot).

DefaultCookiePolicy.DomainStrictNonDomain

   Cookies that did not explicitly specify a "domain" cookie-attribute
   can only be returned to a domain equal to the domain that set the
   cookie (for example, "spam.example.com" won't be returned cookies
   from "example.com" that had no "domain" cookie-attribute).

DefaultCookiePolicy.DomainRFC2965Match

   Cuando se establecen las cookies, requiere de un completo
   emparejamiento de dominio **RFC 2965**.

Los siguientes atributos son proveídos por conveniencia, y son las
combinaciones más útiles de los indicadores anteriores:

DefaultCookiePolicy.DomainLiberal

   Equivalent to 0 (that is, all of the above Netscape domain
   strictness flags switched off).

DefaultCookiePolicy.DomainStrict

   Equivalente a "DomainStrictNoDots|DomainStrictNonDomain".

## Cookie objects

"Cookie" instances have Python attributes roughly corresponding to the
standard cookie-attributes specified in the various cookie standards.
The correspondence is not one-to-one, because there are complicated
rules for assigning default values, because the "max-age" and
"expires" cookie-attributes contain equivalent information, and
because **RFC 2109** cookies may be 'downgraded' by "http.cookiejar"
from version 1 to version 0 (Netscape) cookies.

La asignación a estos atributos no debe de ser necesario excepto en
raras circunstancias en un método "CookiePolicy". La clase no aplica
consistencia interna, por lo que tienes que saber lo que estás
haciendo si lo estas aplicando.

Cookie.version

   Integer or "None".  Netscape cookies have "version" 0. **RFC 2965**
   and **RFC 2109** cookies have a "version" cookie-attribute of 1.
   However, note that "http.cookiejar" may 'downgrade' RFC 2109
   cookies to Netscape cookies, in which case "version" is 0.

Cookie.name

   Nombre de la cookie (un string).

Cookie.value

   Cookie value (a string), or "None".

Cookie.port

   String representing a port or a set of ports (for example, '80', or
   '80,8080'), or "None".

Cookie.domain

   Cookie domain (a string).

Cookie.path

   Cookie path (a string, for example, "'/acme/rocket_launchers'").

Cookie.secure

   "True" si cookie sólo debe de ser retornada sobre una conexión
   segura.

Cookie.expires

   Integer expiry date in seconds since epoch, or "None".  See also
   the "is_expired()" method.

Cookie.discard

   "True" si esta es una sesión de cookies.

Cookie.comment

   String comment from the server explaining the function of this
   cookie, or "None".

Cookie.comment_url

   URL linking to a comment from the server explaining the function of
   this cookie, or "None".

Cookie.rfc2109

   "True" if this cookie was received as an **RFC 2109** cookie (that
   is, the cookie arrived in a *Set-Cookie* header, and the value of
   the Version cookie-attribute in that header was 1).  This attribute
   is provided because "http.cookiejar" may 'downgrade' RFC 2109
   cookies to Netscape cookies, in which case "version" is 0.

Cookie.port_specified

   "True" si un puerto o un conjunto de puertos fue explícitamente
   especificado por el servidor (en la cabecera *Set-Cookie* / *Set-
   Cookie2*).

Cookie.domain_specified

   "True" si un domino fue explícitamente especificado por el
   servidor.

Cookie.domain_initial_dot

   "True" si el dominio explícitamente especificado por el servidor
   empieza con un punto ("'.'").

Las cookies pueden tener cookie-attribute no estándar adicionales. Se
pueden acceder a estos usando los siguientes métodos:

Cookie.has_nonstandard_attr(name)

   Retorna "True" si cookie tiene nombrado el cookie-attribute.

Cookie.get_nonstandard_attr(name, default=None)

   Si la cookie tiene nombrado el cookie-attribute, retorna su valor.
   De otra manera, retorna *default*.

Cookie.set_nonstandard_attr(name, value)

   Retorna el valor del nombrado cookie-attribute.

La clase "Cookie" también define el siguiente método:

Cookie.is_expired(now=None)

   "True" si la cookie ha excedido el tiempo que el servidor solicitó
   para que expirara. Si *now* es dado (en segundos desde la parte
   temporal), retorna si la cookie ha expirado en el momento
   especificado.

## Ejemplos

The first example shows the most common usage of "http.cookiejar":

   import http.cookiejar, urllib.request
   cj = http.cookiejar.CookieJar()
   opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
   r = opener.open("http://example.com/")

Este ejemplo ilustra como abrir una URL usando tus cookies Netscape,
Mozilla, o Lynx (asume la convención Unix/Netscape para la ubicación
del archivo de cookies):

   import os, http.cookiejar, urllib.request
   cj = http.cookiejar.MozillaCookieJar()
   cj.load(os.path.join(os.path.expanduser("~"), ".netscape", "cookies.txt"))
   opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
   r = opener.open("http://example.com/")

El siguiente ejemplo ilustra el uso de "DefaultCookiePolicy". Activa
las cookies **RFC 2965**, es más estricto con respecto a los dominios
cuando se establecen o se retornan cookies Netscape, y bloquea algunos
dominios para establecer o retornar cookies:

   import urllib.request
   from http.cookiejar import CookieJar, DefaultCookiePolicy
   policy = DefaultCookiePolicy(
       rfc2965=True, strict_ns_domain=Policy.DomainStrict,
       blocked_domains=["ads.net", ".ads.net"])
   cj = CookieJar(policy)
   opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
   r = opener.open("http://example.com/")
