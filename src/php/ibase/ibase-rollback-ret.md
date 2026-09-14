---
title: ibase_rollback_ret
description: Anula una transacción sin cerrarla
source_url: https://www.php.net/manual/es/function.ibase-rollback-ret.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ibase/functions/ibase-rollback-ret.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ibase
translation_status: ready
translation_reviewed: false
translation_revision: 17b3531ad
order: 30500
---

ibase_rollback_ret

Anula una transacción sin cerrarla

## Descripción

```php
ibase_rollback_ret([resource $link_or_trans_identifier]): bool
```php

Anula una transacción sin cerrarla.

## Parámetros

`link_or_trans_identifier`  
Si `ibase_rollback_ret` es llamada sin argumento, anula la transacción por omisión del enlace por omisión. Si el argumento `link_or_trans_identifier` es un identificador de conexión, la transacción por omisión de esta conexión será anulada. Si el argumento `link_or_trans_identifier` es un identificador de transacción, esta será anulada. El contexto de la transacción será retenido y, por lo tanto, las consultas ejecutadas en esta transacción no serán invalidadas.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.
