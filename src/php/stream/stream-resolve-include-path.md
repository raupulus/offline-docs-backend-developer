---
title: stream_resolve_include_path
description: Resuelve un nombre de fichero siguiendo las reglas de la ruta de inclusión
source_url: https://www.php.net/manual/es/function.stream-resolve-include-path.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/stream/functions/stream-resolve-include-path.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: stream
translation_status: ready
translation_reviewed: false
translation_revision: 0c9c2dd66
order: 88050
---

stream_resolve_include_path

Resuelve un nombre de fichero siguiendo las reglas de la ruta de inclusión

## Descripción

```php
stream_resolve_include_path(string $filename): string
```php

Resuelve el nombre de fichero `filename` utilizando la ruta de inclusión, siguiendo las mismas reglas que las funciones `fopen`/`include`.

## Parámetros

`filename`  
El nombre de fichero a resolver.

## Valores devueltos

Devuelve un `string` que contiene el nombre de fichero absoluto resuelto, o `false` si ocurre un error.

## Ejemplos

Ejemplo con `stream_resolve_include_path`

Ejemplo simple de utilización.

```
<?php
var_dump(stream_resolve_include_path("test.php"));
?>

    
```php

Resultado del ejemplo anterior es similar a:

    string(22) "/var/www/html/test.php"
