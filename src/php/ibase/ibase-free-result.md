---
title: ibase_free_result
description: Libera un resultado iBase
source_url: https://www.php.net/manual/es/function.ibase-free-result.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ibase/functions/ibase-free-result.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ibase
translation_status: ready
translation_reviewed: false
translation_revision: 17b3531ad
order: 30380
---

ibase_free_result

Libera un resultado iBase

## Descripción

```php
ibase_free_result(resource $result_identifier): bool
```php

Libera un resultado iBase.

## Parámetros

`result_identifier`  
Un conjunto de caracteres, creado por la función `ibase_query` o por la función `ibase_execute`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.
