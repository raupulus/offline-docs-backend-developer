---
title: Funciones eliminadas
source_url: https://www.php.net/manual/es/migration70.incompatible.removed-functions.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: appendices/migration70/incompatible/removed-functions.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: appendices
translation_status: ready
translation_revision: 976425d4f
order: 330
---

## Funciones eliminadas

### `call_user_method` y `call_user_method_array`

Estas funciones se deprecaron en PHP 4.1.0 en favor de `call_user_func` y `call_user_func_array`. También se pueden utilizar las [funciones variables](#functions.variable-functions) y/o el operador [`...`](#functions.variable-arg-list).

### Todas las funciones ereg\*

Todas las funciones `ereg` se han eliminado. [PCRE](#book.pcre) es una alternativa recomendada.

### Alias [mcrypt](#book.mcrypt)

La función obsoleta `mcrypt_generic_end` se ha reemplazado por `mcrypt_generic_deinit`.

Además, las funciones obsoletas `mcrypt_ecb`, `mcrypt_cbc`, `mcrypt_cfb` y `mcrypt_ofb` se han reemplazado por el uso de `mcrypt_decrypt` con la constante apropiada `MCRYPT_MODE_*`.

### Todas las funciones ext/mysql

Todas las funciones [ext/mysql](#book.mysql) se han eliminado. Para más información sobre la elección de otra API MySQL, consulte [elegir una API MySQL](#mysqlinfo.api.choosing).

### Todas las funciones ext/mssql

Todas las funciones `ext/mssql` se han eliminado. <a href="#ref.pdo-sqlsrv" role="alternatives">PDO_SQLSRV</a><span data-wrapper="1" role="alternatives">,</span><span data-wrapper="1" role="alternatives"> </span><a href="#ref.pdo-odbc" role="alternatives">PDO_ODBC</a><span data-wrapper="1" role="alternatives">,</span><span data-wrapper="1" role="alternatives"> </span><a href="#book.sqlsrv" role="alternatives">SQLSRV</a><span data-wrapper="1" role="alternatives">,</span><span data-wrapper="1" role="alternatives"> </span><a href="#book.uodbc" role="alternatives">Unified ODBC API</a>

### [intl](#book.intl) alias

Los alias obsoletos `datefmt_set_timezone_id` y IntlDateFormatter::setTimeZoneID se han eliminado y reemplazado respectivamente por `datefmt_set_timezone` y IntlDateFormatter::setTimeZone.

### `set_magic_quotes_runtime`

`set_magic_quotes_runtime`, así como su alias `magic_quotes_runtime`, se han eliminado. Se deprecaron desde PHP 5.3.0 y no tienen efecto desde la eliminación de las comillas mágicas en PHP 5.4.0.

### `set_socket_blocking`

El alias obsoleto `set_socket_blocking` se ha eliminado y reemplazado por `stream_set_blocking`.

### `dl` con PHP-FPM

`dl` ya no se puede utilizar con PHP-FPM. Continúa funcionando en las SAPIs CLI y Embed.

### Funciones [GD](#book.image) Type1

El soporte para las fuentes PostScript Type1 se ha eliminado de la extensión GD, lo que conlleva la eliminación de las siguientes funciones:

- `imagepsbbox`

- `imagepsencodefont`

- `imagepsextendfont`

- `imagepsfreefont`

- `imagepsloadfont`

- `imagepsslantfont`

- `imagepstext`

En su lugar, se recomienda utilizar las fuentes TrueType y sus funciones asociadas.
