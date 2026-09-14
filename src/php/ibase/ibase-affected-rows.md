---
title: ibase_affected_rows
description: Devuelve el número de filas afectadas por la última consulta iBase
source_url: https://www.php.net/manual/es/function.ibase-affected-rows.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ibase/functions/ibase-affected-rows.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ibase
translation_status: ready
translation_reviewed: false
translation_revision: 17b3531ad
order: 30110
---

ibase_affected_rows

Devuelve el número de filas afectadas por la última consulta iBase

## Descripción

```php
ibase_affected_rows([resource $link_identifier]): int
```php

Devuelve el número de filas que fueron afectadas por la última consulta (INSERT, UPDATE o DELETE) que fue ejecutada en el contexto de transacción especificado por `link_identifier`.

## Parámetros

`link_identifier`  
Un contexto de transacción. Si `link_identifier` es un recurso de conexión, se utiliza la transacción por omisión.

## Valores devueltos

Devuelve el número de filas, en forma de un `int`.

## Véase también

ibase_query

ibase_execute
