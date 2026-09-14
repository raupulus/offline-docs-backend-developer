---
title: CollectionFind::lockShared
description: Ejecuta la operación con un BLOQUEO COMPARTIDO
source_url: https://www.php.net/manual/es/mysql-xdevapi-collectionfind.lockshared.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/collectionfind/lockshared.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: ee5228571
order: 53240
---

CollectionFind::lockShared

Ejecuta la operación con un BLOQUEO COMPARTIDO

## Descripción

```php
public mysql_xdevapi\CollectionFind::lockShared([int $lock_waiting_option]): mysql_xdevapi\CollectionFind
```php

Permite el compartimiento de documentos entre múltiples transacciones que están bloqueadas en modo compartido.

Otras sesiones pueden leer las filas, pero no pueden modificarlas hasta que su transacción no haya sido validada.

Si una de estas filas ha sido modificada por otra transacción que no ha sido validada, la consulta esperará a que esta transacción termine para poder utilizar los últimos valores.

## Parámetros

`lock_waiting_option`  
Una opción de espera opcional. Por omisión, es `MYSQLX_LOCK_DEFAULT`. Los valores válidos son estas constantes:

- `MYSQLX_LOCK_DEFAULT`

- `MYSQLX_LOCK_NOWAIT`

- `MYSQLX_LOCK_SKIP_LOCKED`

## Valores devueltos

Un objeto CollectionFind que puede ser utilizado para un tratamiento ulterior.

## Ejemplos

Ejemplo de `mysql_xdevapi\CollectionFind::lockShared`

```
<?php
$session = mysql_xdevapi\getSession("mysqlx://user:password@localhost");

$schema     = $session->getSchema("addressbook");
$collection = $schema->createCollection("people");

$session->startTransaction();

$result = $collection
  ->find("age > 50")
  ->lockShared()
  ->execute();

// ... leer el objeto en modo compartido

// Validar la transacción y desbloquear el documento
$session->commit();
?>

   
```php
