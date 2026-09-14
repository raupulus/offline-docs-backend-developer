---
title: Nuevas características
source_url: https://www.php.net/manual/es/migration82.new-features.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: appendices/migration82/new-features.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: appendices
translation_status: ready
translation_reviewed: false
translation_revision: 681fd84db
order: 950
---

## Nuevas características

## Núcleo de PHP

### Atributo SensitiveParameter

Se ha añadido el atributo `#[\SensitiveParameter]` para expurgar datos sensibles en los rastros.

### Directiva INI error_log_mode

Se ha añadido la directiva INI [error_log_mode](#ini.error-log-mode) para permitir definir los permisos del archivo de registro de errores.

### Propiedades de enumeraciones en expresiones constantes

Ahora es posible recuperar las propiedades de las [enumeraciones](#language.enumerations) en expresiones constantes.

### Mejoras en el sistema de tipos

Ahora es posible usar `null` y `false` como tipos independientes.

Se ha añadido el tipo `true`.

Ahora es posible combinar tipos de intersección y unión. El tipo debe escribirse en DNF.

### Constantes en traits

Ahora es posible definir constantes en traits.

### Clases de solo lectura

Se ha añadido soporte para [readonly en clases](#language.oop5.basic.class.readonly).

## cURL

Se ha añadido la opción `CURLINFO_EFFECTIVE_METHOD`, que devuelve el método HTTP efectivo en el valor de retorno de `curl_getinfo`.

Exposición de [varias nuevas constantes](#migration82.constants.curl) de libcurl 7.62 a 7.80.

Se ha añadido la función `curl_upkeep` para realizar comprobaciones de mantenimiento de la conexión.

## DBA

El controlador LMDB ahora acepta las banderas `DBA_LMDB_USE_SUB_DIR` o `DBA_LMDB_NO_SUB_DIR` para determinar si debe crear o no un subdirectorio al crear un archivo de base de datos.

## OCI8

Se ha añadido la directiva INI [oci8.prefetch_lob_size](#ini.oci8.prefetch-lob-size) y la función `oci_set_prefetch_lob` para mejorar el rendimiento de las consultas LOB reduciendo el número de idas y vueltas entre PHP y la base de datos Oracle al recuperar los LOBs. Esto es utilizable con bases de datos Oracle 12.2 o más recientes.

## OpenSSL

Se ha añadido soporte AEAD para el algoritmo chacha20-poly1305.

## ODBC

Se han añadido las funciones `odbc_connection_string_is_quoted`, `odbc_connection_string_should_quote`, y `odbc_connection_string_quote`. Principalmente se utilizan en segundo plano en las extensiones ODBC y PDO_ODBC, pero se exponen al espacio de usuario para facilitar las pruebas unitarias, y para que las aplicaciones y bibliotecas de usuario puedan realizar el "quoting" por sí mismas.

## PCRE

Se ha añadido soporte para el modificador `n` (NO_AUTO_CAPTURE), que hace que los grupos simples `(xyz)` no sean capturables. Solo los grupos nombrados como `(?<name>xyz)` son capturables. Esto solo afecta a los grupos que son capturados, aún es posible usar referencias de subpatrones numeradas, y la tabla de coincidencias seguirá conteniendo resultados numerados.

## Random

Es una nueva extensión que organiza y consolida las implementaciones existentes relacionadas con los generadores de números aleatorios. Nuevos y mejores RNG están disponibles y los problemas de alcance se han eliminado.
