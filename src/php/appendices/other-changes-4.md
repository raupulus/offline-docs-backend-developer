---
title: Otros cambios
source_url: https://www.php.net/manual/es/migration73.other-changes.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: appendices/migration73/other-changes.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: appendices
translation_status: ready
translation_reviewed: false
translation_revision: 97c4cc922
order: 650
---

## Otros cambios

## Núcleo de PHP

### Set(raw)cookie acepta el argumento \$options

`setcookie` y `setrawcookie` ahora también aceptan la siguiente firma:

```php
setcookie(string $name, [string $value], [array $options]): bool
```php

donde `$options` es un array asociativo que puede tener cualquiera de las siguientes claves `"expires"`, `"path"`, `"domain"`, `"secure"`, `"httponly"` y `"samesite"`.

### Nuevas directivas INI Syslog

Se han añadido las siguientes directivas INI para personalizar el registro, si [error_log](#ini.error-log) está definido en `syslog`:

[syslog.facility](#ini.syslog.facility)  
Especifica qué tipo de programa está registrando el mensaje.

[syslog.filter](#ini.syslog.filter)  
Especifica el tipo de filtro para filtrar los mensajes registrados, con los tipos de filtros soportados - `all`, `no-ctrl` y `ascii`. A partir de PHP 7.3.8, `raw` también está disponible, restaurando el comportamiento de syslog correspondiente a versiones anteriores de PHP. Este filtro también afectará a las llamadas a `syslog`.

[syslog.ident](#ini.syslog.ident)  
Especifica la cadena de identificación que precederá a cada mensaje.

### Recolector de basura

El [GC cíclico](#features.gc.collecting-cycles) ha sido mejorado, lo que mejora significativamente el rendimiento.

### Diversos

`var_export` ahora exporta objetos `stdClass` como un array modificado en objeto (`(object) array( ... )`), en lugar de usar el método inexistente stdClass::\_\_setState.

`debug_zval_dump` ha sido modificado para mostrar arrays y objetos recursivos de la misma manera que `var_dump`. Ahora, no los muestra dos veces.

`array_push` y `array_unshift` ahora pueden ser llamados con un solo argumento, lo cual es particularmente práctico con el operador de descomposición.

## Depurador PHP interactivo

Las constantes no utilizadas `PHPDBG_FILE`, `PHPDBG_METHOD`, `PHPDBG_LINENO` y `PHPDBG_FUNC` han sido eliminadas.

## Gestor de procesos FastCGI

La función `getallheaders` ahora también está disponible.

## Biblioteca URL cliente

Ahora se requiere libcurl ≥ 7.15.5.

## Filtrado de datos

`FILTER_VALIDATE_FLOAT` ahora soporta la opción `thousand`, que define el conjunto de caracteres de separación para los miles. El valor por defecto es (`"',."`) retrocompatible con versiones anteriores de PHP.

`FILTER_SANITIZE_ADD_SLASHES` ha sido añadido como un alias del filtro `magic_quotes` (`FILTER_SANITIZE_MAGIC_QUOTES`). El filtro `magic_quotes` está sujeto a ser eliminado en futuras versiones de PHP.

## FTP

El modo de transferencia por defecto ha sido cambiado a `binary`.

## Funciones de internacionalización

`Normalizer::NONE` está obsoleto cuando PHP está enlazado a ICU ≥ 56.

Introducción de `Normalizer::FORM_KC_CF` como argumento de Normalizer::normalize para la normalización `NFKC_Casefold`; disponible cuando PHP está enlazado a ICU ≥ 56.

## Notación de objetos JavaScript

Se ha añadido una nueva bandera, `JSON_THROW_ON_ERROR`, que puede ser utilizada con `json_decode` o `json_encode` y provoca que se lance la nueva excepción `JsonException` en caso de error, en lugar de establecer el estado de error global que se recupera con `json_last_error` y `json_last_error_msg`. `JSON_PARTIAL_OUTPUT_ON_ERROR` tiene prioridad sobre `JSON_THROW_ON_ERROR`.

## Cadena multibyte

La opción de configuración `--with-libmbfl` ya no está disponible.

## ODBC (Unificado)

La gestión de `ODBCRouter` y `Birdstep` incluyendo la directiva ini `birdstep.max_links` han sido eliminadas.

## OPcache

La directiva ini `opcache.inherited_hack` ha sido eliminada. El valor era ignorado desde PHP 5.3.0.

## OpenSSL

Se han añadido las opciones de flujo ssl `min_proto_version` y `max_proto_version` así como constantes enlazadas para varios valores de protocolo TLS.

## Expresiones regulares (Perl-Compatible)

La [extensión PCRE](#book.pcre) ha sido actualizada a PCRE2, lo que puede provocar cambios menores en el comportamiento (por ejemplo, las clases de caracteres en las clases son ahora estrictamente interpretadas), y amplía la sintaxis de expresión regular existente.

`preg_quote` ahora escapa el carácter `'#'`.

## Funciones Microsoft SQL Server y Sybase (PDO_DBLIB)

El atributo `PDO::DBLIB_ATTR_SKIP_EMPTY_ROWSETS` ha sido añadido para permitir el salto automático de conjuntos de filas vacíos.

El atributo `PDO::DBLIB_ATTR_TDS_VERSION` ha sido añadido para exponer la versión de TDS.

Las columnas DATETIME2 ahora se tratan como columnas DATETIME.

## Funciones SQLite (PDO_SQLITE)

Las bases de datos SQLite3 ahora pueden ser abiertas en modo solo lectura definiendo el nuevo atributo `PDO::SQLITE_ATTR_OPEN_FLAGS` a `PDO::SQLITE_OPEN_READONLY`.

## Manejo de sesiones

`session_set_cookie_params` ahora soporta la siguiente firma:

```php
session_set_cookie_params(array $options): bool
```

donde `$options` es un array asociativo que puede contener cualquiera de estas claves `"lifetime"`, `"path"`, `"domain"`, `"secure"`, `"httponly"` y `"samesite"`. En consecuencia, el valor de retorno de `session_get_cookie_params` ahora también tiene un elemento con la clave `"samesite"`. Además, se ha añadido la nueva directiva ini `session.cookie_samesite` para definir el valor por defecto de SameSite para las cookies. Por defecto a `""` (cadena vacía), de modo que no se define ninguna directiva SameSite. El valor puede ser `"Lax"` o `"Strict"`, que define el valor de SameSite.

## Tidy

La construcción con [tidyp](https://github.com/petdance/tidyp) ahora es transparente. Dado que tidyp no proporciona una API para obtener la fecha de construcción, `tidy_get_release` y tidy::getRelease devuelven `'unknown'` en este caso.

## Analizador XML

El valor de retorno de la función de devolución de llamada de `xml_set_external_entity_ref_handler` ya no se ignora si la extensión se construyó con libxml. Anteriormente, el valor de retorno era ignorado, y el análisis nunca cesaba.

## Zip

La construcción estática de libzip está desaconsejada, pero sigue siendo posible añadiendo la opción de configuración `--without-libzip`.

## Compresión Zlib

Se ha añadido la opción de contexto zlib/level para el [wrapper de compresión zlib](#wrappers.compression) para facilitar la definición del nivel de compresión deseado.
