---
title: Funciones modificadas
source_url: https://www.php.net/manual/es/migration70.changed-functions.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: appendices/migration70/changed-functions.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: appendices
translation_status: ready
translation_revision: 976425d4f
order: 250
---

## Funciones modificadas

## Núcleo de PHP

- `debug_zval_dump` ahora muestra "int" en lugar de "long" y "float" en lugar de "double".

- La función `dirname` ahora toma un segundo parámetro opcional, `depth`, para obtener el nombre del directorio a `depth` niveles por encima del directorio actual.

- `getrusage` ahora es soportado en Windows.

- Las funciones `mktime` y `gmmktime` ya no aceptan el parámetro `is_dst`.

- La función `preg_replace` ya no soporta "\e" (`PREG_REPLACE_EVAL`). `preg_replace_callback` debe ser utilizado en su lugar.

- La función `setlocale` ya no acepta que el parámetro `category` sea pasado como cadena de caracteres. En su lugar se deben utilizar las constantes `LC_*`.

- Las funciones `exec`, `system` y `passthru` ahora tienen el byte NULL de protección.

- `shmop_open` ahora devuelve un recurso en lugar de un int, el cual se debe pasar a las funciones `shmop_size`, `shmop_write`, `shmop_read`, `shmop_close` y `shmop_delete`.

- `substr` y `iconv_substr` ahora devuelven una `string` vacía, si la longitud de la cadena es igual a \$start.

- `xml_parser_free` ya no es suficiente para liberar el recurso del analizador, si hace referencia a un objeto y ese objeto hace referencia a este recurso del analizador. En este caso, también es necesario destruir el \$parser.
