---
title: Funciones modificadas
source_url: https://www.php.net/manual/es/migration71.changed-functions.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: appendices/migration71/changed-functions.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: appendices
translation_status: ready
translation_revision: ef9b464ad
order: 440
---

## Funciones modificadas

## Núcleo de PHP

- `getopt` tiene un tercer parámetro opcional que expone el índice del siguiente elemento en la lista de vectores de argumentos a procesar. Esto se hace a través de un parámetro por referencia.

- `getenv` ya no requiere su parámetro. Si se omite el parámetro, las variables de entorno actuales se devolverán como un array asociativo.

- `get_headers` tiene ahora un parámetro adicional para permitir el paso de contextos de flujo personalizados.

- `output_reset_rewrite_vars` ya no reinicializa la reescritura de las URL de las variables de sesión.

- `parse_url` es ahora más restrictivo y soporta RFC3986.

- `unpack` acepta ahora un tercer parámetro opcional para especificar el offset del inicio del desempaquetado.

## Sistema de ficheros

- `file_get_contents` acepta ahora un offset de búsqueda negativo si el flujo admite búsquedas.

- `tempnam` emite ahora un aviso cuando se recurre al directorio temporal del sistema.

## JSON

- `json_encode` acepta ahora una nueva opción, `JSON_UNESCAPED_LINE_TERMINATORS`, para desactivar el escape de los caracteres U+2028 y U+2029 cuando se proporciona `JSON_UNESCAPED_UNICODE`.

## Strings multibyte

- `mb_ereg` rechaza ahora las secuencias de octetos ilegales.

- `mb_ereg_replace` rechaza ahora las secuencias de octetos ilegales.

## PDO

- PDO::lastInsertId para PostgreSQL ahora lanzará un error cuando no se ha llamado a `nextval` para la sesión actual (la conexión postgres).

## PostgreSQL

- `pg_last_notice` acepta ahora un parámetro opcional para especificar una operación. Esto se puede hacer con una de las siguientes nuevas constantes: `PGSQL_NOTICE_LAST`, `PGSQL_NOTICE_ALL`, o `PGSQL_NOTICE_CLEAR`.

- `pg_fetch_all` acepta ahora un segundo parámetro opcional para especificar el tipo de resultado (similar al tercer parámetro de `pg_fetch_array`).

- `pg_select` acepta ahora un cuarto parámetro para especificar el tipo de resultado (similar al tercer parámetro de `pg_fetch_array`).

## Sesión

- `session_start` ahora devuelve `false` y ya no inicializa `$_SESSION` cuando el inicio de la sesión falla.
