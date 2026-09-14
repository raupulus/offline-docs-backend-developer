---
title: '"http.cookies" --- HTTP state management'
source_url: https://docs.python.org/es/3
source_path: library/http.cookies.txt
technology: python
version: '3.14'
license: PSF-2.0
retrieved_at: '2026-08-02'
section: library
order: 2870
---

# "http.cookies" --- HTTP state management

**Source code:** Lib/http/cookies.py

======================================================================

The "http.cookies" module defines classes for abstracting the concept
of cookies, an HTTP state management mechanism. It supports both
simple string-only cookies, and provides an abstraction for having any
serializable data-type as cookie value.

The module formerly strictly applied the parsing rules described in
the **RFC 2109** and **RFC 2068** specifications.  It has since been
discovered that MSIE 3.0x didn't follow the character rules outlined
in those specs; many current-day browsers and servers have also
relaxed parsing rules when it comes to cookie handling.  As a result,
this module now uses parsing rules that are a bit less strict than
they once were.

The character set, "string.ascii_letters", "string.digits" and
"!#$%&'*+-.^_`|~:" denote the set of valid characters allowed by this
module in a cookie name (as "key").

Distinto en la versión 3.3: Allowed ':' as a valid cookie name
character.

Nota:

  Al encontrar una cookie no válida, se lanza "CookieError", por lo
  que si los datos de su cookie provienen de un navegador, siempre
  debe prepararse para los datos no válidos y detectar "CookieError"
  en el análisis.

exception http.cookies.CookieError

   Error de excepción debido a la invalidez de **RFC 2109**: atributos
   incorrectos, encabezado *Set-Cookie* incorrecto, etc.

class http.cookies.BaseCookie([input])

   Esta clase es un objeto similar a un diccionario cuyas claves son
   cadenas  de caracteres y cuyos valores son "Morsel". Tenga en
   cuenta que al establecer una clave en un valor, el valor se
   convierte primero en "Morsel" que contiene la clave y el valor.

   Si se proporciona *input*, se pasa al método "load()".

class http.cookies.SimpleCookie([input])

   This class derives from "BaseCookie" and overrides "value_decode()"
   and "value_encode()". "SimpleCookie" supports strings as cookie
   values. When setting the value, "SimpleCookie" calls the builtin
   "str()" to convert the value to a string. Values received from HTTP
   are kept as strings.

Ver también:

  Módulo "http.cookiejar"
     HTTP cookie handling for web *clients*.  The "http.cookiejar" and
     "http.cookies" modules do not depend on each other.

  **RFC 2109** - Mecanismo de gestión de estado HTTP
     Esta es la especificación de gestión de estado implementada por
     este módulo.

## Objetos de cookie

BaseCookie.value_decode(val)

   Retorna una tupla "(real_value, coded_value)" de una representación
   de cadena de caracteres. "real_value" puede ser de cualquier tipo.
   Este método no decodifica en "BaseCookie" --- existe por lo que
   puede ser anulado.

BaseCookie.value_encode(val)

   Retorna una tupla "(real_value, coded_value)". *val* puede ser de
   cualquier tipo, pero "coded_value" siempre se convertirá en una
   cadena de caracteres. Este método no codifica en "BaseCookie" ---
   existe por lo que se puede anular.

   En general, debería darse el caso de que "value_encode()" y
   "value_decode()" sean inversas en el rango de *value_decode*.

BaseCookie.output(attrs=None, header='Set-Cookie:', sep='\r\n')

   Return a string representation suitable to be sent as HTTP headers.
   *attrs* and *header* are sent to each "Morsel"'s "output()" method.
   *sep* is used to join the headers together, and is by default the
   combination "'\r\n'" (CRLF).

BaseCookie.js_output(attrs=None)

   Retorna un fragmento de código JavaScript que, si se ejecuta en un
   navegador que admita JavaScript, actuará de la misma forma que si
   se enviaran los encabezados HTTP.

   El significado de *attrs* es el mismo que en "output()".

BaseCookie.load(rawdata)

   Si *rawdata* es una cadena de caracteres, analícela como un
   "HTTP_COOKIE" y agregue los valores que se encuentran allí como
   "Morsel"s. Si es un diccionario, equivale a:

      for k, v in rawdata.items():
          cookie[k] = v

## Objetos Morsel

class http.cookies.Morsel

   Resumen de un par clave/valor, que tiene algunos atributos **RFC
   2109**.

   Morsels are dictionary-like objects, whose set of keys is constant
   --- the valid **RFC 2109** attributes, which are:

      expires
      path
      comment
      domain
      max-age
      secure
      version
      httponly
      samesite
      partitioned

   El atributo "httponly" especifica que la cookie solo se transfiere
   en solicitudes HTTP y no es accesible a través de JavaScript. Esto
   tiene como objetivo mitigar algunas formas de secuencias de
   comandos entre sitios.

   The attribute "samesite" controls when the browser sends the cookie
   with cross-site requests. This helps to mitigate CSRF attacks.
   Valid values are "Strict" (only sent with same-site requests),
   "Lax" (sent with same-site requests and top-level navigations), and
   "None" (sent with same-site and cross-site requests). When using
   "None", the "secure" attribute must also be set, as required by
   modern browsers.

   The attribute "partitioned" indicates to user agents that these
   cross-site cookies *should* only be available in the same top-level
   context that the cookie was first set in. For this to be accepted
   by the user agent, you **must** also set "Secure".

   In addition, it is recommended to use the "__Host" prefix when
   setting partitioned cookies to make them bound to the hostname and
   not the registrable domain. Read CHIPS (Cookies Having Independent
   Partitioned State) for full details and examples.

   Las claves no distinguen entre mayúsculas y minúsculas y su valor
   predeterminado es "''".

   Distinto en la versión 3.5: "__eq__()" now takes "key" and "value"
   into account.

   Distinto en la versión 3.7: Los atributos "key", "value" y
   "coded_value" son de solo lectura. Utilice "set()" para
   configurarlos.

   Distinto en la versión 3.8: Se agregó soporte para el atributo
   "samesite".

   Distinto en la versión 3.14: Added support for the "partitioned"
   attribute.

Morsel.value

   El valor de la cookie.

Morsel.coded_value

   El valor codificado de la cookie --- esto es lo que se debe enviar.

Morsel.key

   El nombre de la cookie.

Morsel.set(key, value, coded_value)

   Establezca los atributos *key*, *value* y *coded_value*.

Morsel.isReservedKey(K)

   Si *K* es miembro del conjunto de claves de una "Morsel".

Morsel.output(attrs=None, header='Set-Cookie:')

   Retorna una representación de cadena de caracteres del Morsel,
   adecuada para enviarse como un encabezado HTTP. De forma
   predeterminada, se incluyen todos los atributos, a menos que se
   proporcione *attrs*, en cuyo caso debería ser una lista de
   atributos a utilizar. *header* es por defecto ""Set-Cookie:"".

Morsel.js_output(attrs=None)

   Retorna un fragmento de código JavaScript que, si se ejecuta en un
   navegador que admita JavaScript, actuará de la misma forma que si
   se hubiera enviado el encabezado HTTP.

   El significado de *attrs* es el mismo que en "output()".

Morsel.OutputString(attrs=None)

   Retorna una cadena de caracteres que representa el Morsel, sin
   ningún HTTP o JavaScript circundante.

   El significado de *attrs* es el mismo que en "output()".

Morsel.update(values)

   Actualice los valores en el diccionario Morsel con los valores en
   el diccionario *values*. Lanza un error si alguna de las claves en
   el *values* dict no es un atributo válido **RFC 2109**.

   Distinto en la versión 3.5: se lanza un error para claves no
   válidas.

Morsel.copy(value)

   Retorna una copia superficial del objeto Morsel.

   Distinto en la versión 3.5: retorna un objeto Morsel en lugar de un
   dict.

Morsel.setdefault(key, value=None)

   Lanza un error si la clave no es un atributo válido **RFC 2109**;
   de lo contrario, se comporta igual que "dict.setdefault()".

## Ejemplo

The following example demonstrates how to use the "http.cookies"
module.

   >>> from http import cookies
   >>> C = cookies.SimpleCookie()
   >>> C["fig"] = "newton"
   >>> C["sugar"] = "wafer"
   >>> print(C) # generate HTTP headers
   Set-Cookie: fig=newton
   Set-Cookie: sugar=wafer
   >>> print(C.output()) # same thing
   Set-Cookie: fig=newton
   Set-Cookie: sugar=wafer
   >>> C = cookies.SimpleCookie()
   >>> C["rocky"] = "road"
   >>> C["rocky"]["path"] = "/cookie"
   >>> print(C.output(header="Cookie:"))
   Cookie: rocky=road; Path=/cookie
   >>> print(C.output(attrs=[], header="Cookie:"))
   Cookie: rocky=road
   >>> C = cookies.SimpleCookie()
   >>> C.load("chips=ahoy; vienna=finger") # load from a string (HTTP header)
   >>> print(C)
   Set-Cookie: chips=ahoy
   Set-Cookie: vienna=finger
   >>> C = cookies.SimpleCookie()
   >>> C.load('keebler="E=everybody; L=\\"Loves\\"; fudge=;";')
   >>> print(C)
   Set-Cookie: keebler="E=everybody; L=\"Loves\"; fudge=;"
   >>> C = cookies.SimpleCookie()
   >>> C["oreo"] = "doublestuff"
   >>> C["oreo"]["path"] = "/"
   >>> print(C)
   Set-Cookie: oreo=doublestuff; Path=/
   >>> C = cookies.SimpleCookie()
   >>> C["twix"] = "none for you"
   >>> C["twix"].value
   'none for you'
   >>> C = cookies.SimpleCookie()
   >>> C["number"] = 7 # equivalent to C["number"] = str(7)
   >>> C["string"] = "seven"
   >>> C["number"].value
   '7'
   >>> C["string"].value
   'seven'
   >>> print(C)
   Set-Cookie: number=7
   Set-Cookie: string=seven
