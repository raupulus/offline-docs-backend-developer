---
title: ibase_commit_ret
description: Valida una transacción iBase sin cerrarla
source_url: https://www.php.net/manual/es/function.ibase-commit-ret.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ibase/functions/ibase-commit-ret.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ibase
translation_status: ready
translation_reviewed: false
translation_revision: 17b3531ad
order: 30230
---

ibase_commit_ret

Valida una transacción iBase sin cerrarla

## Descripción

```php
ibase_commit_ret([resource $link_or_trans_identifier]): bool
```php

Valida una transacción iBase sin cerrarla.

## Parámetros

`link_or_trans_identifier`  
Llamada sin argumento, valida la transacción por omisión de la conexión por omisión. Si el argumento `link_or_trans_identifier` es un identificador de conexión, su transacción por omisión es validada. Si el argumento `link_or_trans_identifier` es un identificador de transacción, esta será validada. El contexto de la transacción será retenido y, por lo tanto, las consultas ejecutadas en esta transacción no serán invalidadas.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.
