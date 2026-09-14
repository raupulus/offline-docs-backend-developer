---
title: ibase_rollback
description: Anula una transacción interBase
source_url: https://www.php.net/manual/es/function.ibase-rollback.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ibase/functions/ibase-rollback.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ibase
translation_status: ready
translation_reviewed: false
translation_revision: 17b3531ad
order: 30510
---

ibase_rollback

Anula una transacción interBase

## Descripción

```php
ibase_rollback([resource $link_or_trans_identifier]): bool
```php

Anula una transacción interBase.

## Parámetros

`link_or_trans_identifier`  
Cuando `ibase_rollback` es llamada sin argumento, anula la transacción por omisión del enlace por omisión. Si el argumento `link_or_trans_identifier` es un identificador de conexión, la transacción por omisión de dicha conexión será anulada. Si el argumento `link_or_trans_identifier` es un identificador de transacción, esta será anulada.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.
