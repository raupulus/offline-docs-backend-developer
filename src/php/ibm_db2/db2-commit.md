---
title: db2_commit
description: Confirmar una transacción
source_url: https://www.php.net/manual/es/function.db2-commit.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ibm_db2/functions/db2-commit.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ibm_db2
translation_status: ready
translation_reviewed: false
translation_revision: 020edc73b
order: 30680
---

db2_commit

Confirmar una transacción

## Descripción

```php
db2_commit(resource $connection): bool
```php

Confirma una transacción en progreso en la conexión especificada e inicia una nueva transacción. Las aplicaciones en PHP normalmente confirman las transacciones automáticamente debido a que el modo AUTOCOMMIT por defecto está activado, por lo que el uso de `db2_commit` no es necesario a menos que el modo AUTOCOMMIT haya sido desactivado en la conexión especificada.

## Parámetros

`connection`  
Es la conexión válida devuelta por `db2_connect` o `db2_pconnect`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

db2_autocommit

db2_rollback
