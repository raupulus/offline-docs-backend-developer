---
title: yaz_database
description: Especifica las bases de datos dentro de una sesión
source_url: https://www.php.net/manual/es/function.yaz-database.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/yaz/functions/yaz-database.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: yaz
translation_status: ready
translation_revision: 96c9d88ba
order: 107790
---

yaz_database

Especifica las bases de datos dentro de una sesión

## Descripción

```php
yaz_database(resource $id, string $databases): bool
```php

Esta función permite cambiar las bases de datos dentro de una sesión por una o más bases de datos especificadas a ser usadas en la búsqueda, recuperación, etc. - primordialmente a las bases de datos especificadas a ser llamadas `yaz_connect`.

## Parámetros

`id`  
El recurso de conexión devuelto por `yaz_connect`.

`databases`  
Una cadena conteniendo una o más bases de datos. Múltiple bases de datos son separadas por un signo de más`+`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.
