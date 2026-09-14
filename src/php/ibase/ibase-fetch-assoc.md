---
title: ibase_fetch_assoc
description: Recupera una fila del resultado de una consulta en un array asociativo
source_url: https://www.php.net/manual/es/function.ibase-fetch-assoc.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ibase/functions/ibase-fetch-assoc.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ibase
translation_status: ready
translation_reviewed: false
translation_revision: 17b3531ad
order: 30320
---

ibase_fetch_assoc

Recupera una fila del resultado de una consulta en un array asociativo

## Descripción

```php
ibase_fetch_assoc(resource $result, [int $fetch_flag]): array
```php

Recupera una fila del resultado de una consulta en un array asociativo.

`ibase_fetch_assoc` recupera una fila de datos a partir de `result`. Si dos o más columnas tienen el mismo nombre de campo, la última columna tendrá precedencia. Para acceder a las otras columnas con el mismo nombre, se debe hacer con sus índices numéricos utilizando `ibase_fetch_row` o utilizando alias en la consulta.

## Parámetros

`result`  
El conjunto de resultados.

`fetch_flag`  
`fetch_flag` es una combinación de las constantes `IBASE_TEXT` y `IBASE_UNIXTIME`. Pasar `IBASE_TEXT` hace que se devuelva el contenido del BLOB en lugar del ID del BLOB. Pasar `IBASE_UNIXTIME` hace que se devuelvan las fechas/horas en forma de timestamps UNIX en lugar de strings formateados.

## Valores devueltos

Devuelve un array asociativo que corresponde a la fila recuperada. Las llamadas siguientes devuelven la fila siguiente en el conjunto de resultados, o `false` si no hay más filas.

## Véase también

ibase_fetch_row

ibase_fetch_object
