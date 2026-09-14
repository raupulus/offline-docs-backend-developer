---
title: svn_fs_abort_txn
description: Interrumpir una transacción
source_url: https://www.php.net/manual/es/function.svn-fs-abort-txn.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/svn/functions/svn-fs-abort-txn.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: svn
translation_status: ready
translation_reviewed: false
translation_revision: 997700a58
order: 90000
---

svn_fs_abort_txn

Interrumpir una transacción

## Descripción

```php
svn_fs_abort_txn(resource $txn): bool
```php

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

Detiene una transacción, retorna `true` si todo es correcto, `false` en caso contrario.

## Parámetros

`txn`  

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Notas

> [!WARNING]
> Esta función es *EXPERIMENTAL*. El comportamiento de esta función, su nombre, y toda la documentación alrededor de esta función puede cambiar sin previo aviso en una próxima versión de PHP. Esta función debe ser utilizada bajo su propio riesgo.
