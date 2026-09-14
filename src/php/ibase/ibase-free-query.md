---
title: ibase_free_query
description: Libera la memoria reservada por una consulta preparada
source_url: https://www.php.net/manual/es/function.ibase-free-query.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ibase/functions/ibase-free-query.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ibase
translation_status: ready
translation_reviewed: false
translation_revision: 17b3531ad
order: 30370
---

ibase_free_query

Libera la memoria reservada por una consulta preparada

## Descripción

```php
ibase_free_query(resource $query): bool
```php

Libera la memoria reservada por una consulta preparada.

## Parámetros

`query`  
Una consulta preparada con la función `ibase_prepare`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.
