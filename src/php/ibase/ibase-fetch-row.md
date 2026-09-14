---
title: ibase_fetch_row
description: Lee una línea de una base Interbase
source_url: https://www.php.net/manual/es/function.ibase-fetch-row.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ibase/functions/ibase-fetch-row.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ibase
translation_status: ready
translation_reviewed: false
translation_revision: 17b3531ad
order: 30340
---

ibase_fetch_row

Lee una línea de una base Interbase

## Descripción

```php
ibase_fetch_row(resource $result_identifier, [int $fetch_flag]): array
```php

`ibase_fetch_row` recupera una línea de datos desde el conjunto de resultados dado.

Las llamadas siguientes a `ibase_fetch_row` devolverán la próxima línea en el resultado, o bien `false` si no hay más líneas.

## Parámetros

`result_identifier`  
Un identificador de resultado InterBase.

`fetch_flag`  
`fetch_flag` es una combinación de las constantes `IBASE_TEXT` y `IBASE_UNIXTIME`. Pasar `IBASE_TEXT` hace que se devuelva el contenido del BLOB en lugar del ID del BLOB. Pasar `IBASE_UNIXTIME` hace que se devuelvan los valores de fecha/hora en forma de timestamps UNIX en lugar de strings formateadas.

## Valores devueltos

Devuelve un array correspondiente a la línea recuperada, o `false` si no hay más líneas. Cada columna del resultado se almacena en una posición del array, comenzando en 0.

## Véase también

ibase_fetch_assoc

ibase_fetch_object
