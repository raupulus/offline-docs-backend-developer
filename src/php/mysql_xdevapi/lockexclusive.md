---
title: CollectionFind::lockExclusive
description: Ejecuta la operación con un BLOQUEO EXCLUSIVO
source_url: https://www.php.net/manual/es/mysql-xdevapi-collectionfind.lockexclusive.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/collectionfind/lockexclusive.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: ee5228571
order: 53230
---

CollectionFind::lockExclusive

Ejecuta la operación con un BLOQUEO EXCLUSIVO

## Descripción

```php
public mysql_xdevapi\CollectionFind::lockExclusive([int $lock_waiting_option]): mysql_xdevapi\CollectionFind
```php

Bloquea el documento de manera exclusiva. Mientras el documento está bloqueado, otras transacciones no pueden actualizar el documento, utilizar `SELECT ... LOCK IN SHARE MODE`, o leer los datos en ciertos niveles de aislamiento de transacción. Las lecturas coherentes ignoran los bloqueos establecidos en los registros que existen en la vista de lectura.

Para evitar problemas de concurrencia, es lógico utilizar esta función con el método mysql_xdevapi\Collection::modify. Esencialmente, esta función utiliza bloqueos de línea para serializar el acceso a las líneas.

## Parámetros

`lock_waiting_option`  
Una opción de espera opcional. Por omisión, es `MYSQLX_LOCK_DEFAULT`. Los valores válidos son estas constantes:

- `MYSQLX_LOCK_DEFAULT`

- `MYSQLX_LOCK_NOWAIT`

- `MYSQLX_LOCK_SKIP_LOCKED`

## Valores devueltos

Devuelve un objeto CollectionFind que puede ser utilizado para un procesamiento posterior.

## Ejemplos

Ejemplo de `mysql_xdevapi\CollectionFind::lockExclusive`

```
<?php
$session = mysql_xdevapi\getSession("mysqlx://user:password@localhost");

$schema     = $session->getSchema("addressbook");
$collection = $schema->createCollection("people");

$session->startTransaction();

$result = $collection
  ->find("age > 50")
  ->lockExclusive()
  ->execute();

// ... realizar una operación sobre el objeto

// Validar la transacción y desbloquear el documento
$session->commit();
?>

   
```php
