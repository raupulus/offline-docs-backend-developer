---
title: TableSelect::lockShared
description: Ejecuta SHARED LOCK
source_url: https://www.php.net/manual/es/mysql-xdevapi-tableselect.lockshared.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/tableselect/lockshared.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 86e6094e8
order: 54660
---

TableSelect::lockShared

Ejecuta SHARED LOCK

## Descripción

```php
public mysql_xdevapi\TableSelect::lockShared([int $lock_waiting_option]): mysql_xdevapi\TableSelect
```php

Ejecuta una operación de lectura con SHARED LOCK. Solo un bloqueo puede estar activo a la vez.

## Parámetros

`lock_waiting_option`  
Una opción de espera opcional que se establece por omisión en `MYSQLX_LOCK_DEFAULT`. Los valores válidos son:

- `MYSQLX_LOCK_DEFAULT`

- `MYSQLX_LOCK_NOWAIT`

- `MYSQLX_LOCK_SKIP_LOCKED`

## Valores devueltos

Un objeto TableSelect.

## Ejemplos

Ejemplo de `mysql_xdevapi\TableSelect::lockShared`

```
<?php
$session = mysql_xdevapi\getSession("mysqlx://user:password@localhost");

$schema = $session->getSchema("addressbook");
$table  = $schema->getTable("names");

$session->startTransaction();

$result = $table->select('name', 'age')
  ->lockShared(MYSQLX_LOCK_NOWAIT)
  ->execute();

$session->commit();

$row = $result->fetchAll();
print_r($row);
?>

   
```php

Resultado del ejemplo anterior es similar a:

    Array
    (
        [0] => Array
            (
                [name] => John
                [age] => 42
            )
        [1] => Array
            (
                [name] => Sam
                [age] => 42
            )
    )
