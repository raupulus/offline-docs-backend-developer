---
title: parse_url
description: Analiza una URL y devuelve sus componentes
source_url: https://www.php.net/manual/es/function.parse-url.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/url/functions/parse-url.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: url
translation_status: ready
translation_reviewed: false
translation_revision: b3194d546
order: 100240
---

parse_url

Analiza una URL y devuelve sus componentes

## Descripción

```php
parse_url(string $url, [int $component]): int
```php

Esta función analiza una URL y devuelve un array asociativo que contiene todos los elementos presentes en la misma. Los valores de los elementos del array *NO ESTÁN* decodificados de la URL.

Esta función **no está** diseñada para validar la URL proporcionada, solo la divide en las partes enumeradas a continuación. Las URL parciales e inválidas también son aceptadas, la función `parse_url` hará todo lo posible para analizarlas correctamente.

> [!CAUTION]
> Esta función no sigue ningún estándar URI o URL establecido. Devolverá resultados incorrectos o sin sentido para URL relativas o malformadas. Incluso para URL válidas, el resultado puede diferir del de otro analizador de URL, ya que existen múltiples estándares diferentes relacionados con las URL que se dirigen a diferentes casos de uso y que difieren en sus requisitos.
>
> El procesamiento de una URL con analizadores que siguen diferentes estándares de URL es una fuente común de vulnerabilidades de seguridad. Por ejemplo, la validación de una URL contra una lista de nombres de host permitidos con el analizador A podría ser ineficaz cuando la recuperación real del recurso utiliza el analizador B que extrae los nombres de host de manera diferente.
>
> Las clases `Uri\Rfc3986\Uri` y `Uri\WhatWg\Url` siguen estrictamente los estándares RFC 3986 y WHATWG URL respectivamente. Se recomienda encarecidamente utilizar estas clases para todo el código nuevo y migrar los usos existentes de la función `parse_url` a estas clases, a menos que el comportamiento de `parse_url` deba preservarse por razones de compatibilidad.

## Parámetros

`url`  
La URL a analizar.

<!-- -->

`component`  
Puede ser una de las constantes entre `PHP_URL_SCHEME`, `PHP_URL_HOST`, `PHP_URL_PORT`, `PHP_URL_USER`, `PHP_URL_PASS`, `PHP_URL_PATH`, `PHP_URL_QUERY` o `PHP_URL_FRAGMENT` para recuperar únicamente una parte de la URL como `string` (excepto cuando se proporciona `PHP_URL_PORT`; en este caso, el valor devuelto será un `int`).

## Valores devueltos

Para URL realmente mal formadas, `parse_url` puede devolver `false`.

Si el parámetro `component` se omite, se devuelve un `array` asociativo. Al menos un elemento estará presente en el array. Estas son las claves potenciales de este array:

- `scheme` - por ejemplo `http`

- `host`

- `port`

- `user`

- `pass`

- `path`

- `query` - después del signo de interrogación "`?`"

- `fragment` - después del símbolo de almohadilla "`#`"

Si el parámetro `component` está especificado, `parse_url` devuelve un `string` (o un `int`, en el caso de `PHP_URL_PORT`) en lugar de un `array`. Si el componente solicitado no existe en la URL, `null` será devuelto. A partir de PHP 8.0.0, `parse_url` distingue entre los fragmentos y consultas ausentes y vacíos:

    http://example.com/foo → query = null, fragment = null
    http://example.com/foo? → query = "",   fragment = null
    http://example.com/foo# → query = null, fragment = ""
    http://example.com/foo?# → query = "",   fragment = ""

Anteriormente todos los casos resultaban en la consulta y el fragmento siendo `null`.

Cabe señalar que los caracteres de control (ver `ctype_cntrl`) en los componentes son reemplazados por un guion bajo (`_`).

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.0.0 | `parse_url` distingue ahora entre los fragmentos y consultas ausentes y vacíos. |

## Ejemplos

Ejemplo con `parse_url`

```
<?php
$url = 'http://username:password@hostname:9090/path?arg=value#anchor';

var_dump(parse_url($url));
var_dump(parse_url($url, PHP_URL_SCHEME));
var_dump(parse_url($url, PHP_URL_USER));
var_dump(parse_url($url, PHP_URL_PASS));
var_dump(parse_url($url, PHP_URL_HOST));
var_dump(parse_url($url, PHP_URL_PORT));
var_dump(parse_url($url, PHP_URL_PATH));
var_dump(parse_url($url, PHP_URL_QUERY));
var_dump(parse_url($url, PHP_URL_FRAGMENT));
?>

    
```php

El ejemplo anterior mostrará:

    array(8) {
      ["scheme"]=>
      string(4) "http"
      ["host"]=>
      string(8) "hostname"
      ["port"]=>
      int(9090)
      ["user"]=>
      string(8) "username"
      ["pass"]=>
      string(8) "password"
      ["path"]=>
      string(5) "/path"
      ["query"]=>
      string(9) "arg=value"
      ["fragment"]=>
      string(6) "anchor"
    }
    string(4) "http"
    string(8) "username"
    string(8) "password"
    string(8) "hostname"
    int(9090)
    string(5) "/path"
    string(9) "arg=value"
    string(6) "anchor"

Ejemplo con la función `parse_url` sin esquema

```
<?php
$url = '//www.example.com/path?googleguy=googley';

// Antes de PHP 5.4.7, la ruta sería "//www.example.com/path"
var_dump(parse_url($url));
?>

    
```php

El ejemplo anterior mostrará:

    array(3) {
      ["host"]=>
      string(15) "www.example.com"
      ["path"]=>
      string(5) "/path"
      ["query"]=>
      string(17) "googleguy=googley"
    }

## Notas

> [!NOTE]
> `parse_url` fue creada específicamente para analizar URL y no URI. Sin embargo, por razones de compatibilidad adyacente, PHP hace una excepción para el esquema `file://` donde los triples slashs (`file:///`...) están permitidos. Todos los demás esquemas son inválidos.

## Véase también

`pathinfo`, `parse_str`, `http_build_query`, `dirname`, `basename`, [RFC 3986](https://datatracker.ietf.org/doc/html/rfc3986)
