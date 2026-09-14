---
title: ibase_trans
description: Prepara una transacción interBase
source_url: https://www.php.net/manual/es/function.ibase-trans.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/ibase/functions/ibase-trans.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: ibase
translation_status: ready
translation_reviewed: false
translation_revision: 2d8dcd319
order: 30560
---

ibase_trans

Prepara una transacción interBase

## Descripción

```php
ibase_trans([int $trans_args], [resource $link_identifier]): resource
```php

```php
ibase_trans([resource $link_identifier]): resource
```

Prepara una transacción interBase.

> [!NOTE]
> La primera llamada a `ibase_trans` devolverá la transacción por omisión para la conexión actual. Todas las transacciones iniciadas por `ibase_trans` serán anuladas al final de la ejecución del script si no han sido validadas o anuladas por las funciones `ibase_commit` o `ibase_rollback` respectivamente.

> [!NOTE]
> `ibase_trans` acepta varios argumentos `trans_args` y `link_identifier`. Esto permite realizar transacciones en varias conexiones a diferentes bases de datos, que serán validadas utilizando el algoritmo `2-phase`. Esto significa que se pueden actualizar varias bases de datos. Esto NO significa que se puedan utilizar varias bases de datos en una misma consulta.
>
> Si se utilizan las transacciones en varias bases de datos, se debe especificar `link_id` y `transaction_id` en las funciones `ibase_query` y `ibase_prepare`.

## Parámetros

`trans_args`  
`trans_args` puede ser una combinación de las siguientes constantes: `IBASE_READ`, `IBASE_WRITE`, `IBASE_COMMITTED`, `IBASE_CONSISTENCY`, `IBASE_CONCURRENCY`, `IBASE_REC_VERSION`, `IBASE_REC_NO_VERSION`, `IBASE_WAIT` y `IBASE_NOWAIT`.

`link_identifier`  
Un identificador de conexión a InterBase. Si se omite, se utilizará la última conexión abierta.

## Valores devueltos

Devuelve un recurso de transacción, o `false` si ocurre un error.
