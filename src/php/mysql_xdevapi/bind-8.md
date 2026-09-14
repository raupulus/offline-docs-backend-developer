---
title: TableUpdate::bind
description: Liga los argumentos de la solicitud de actualización
source_url: https://www.php.net/manual/es/mysql-xdevapi-tableupdate.bind.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/tableupdate/bind.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 18f9cbcbc
order: 54700
---

TableUpdate::bind

Liga los argumentos de la solicitud de actualización

## Descripción

```php
public mysql_xdevapi\TableUpdate::bind(array $placeholder_values): mysql_xdevapi\TableUpdate
```php

Liga un valor a un emplazamiento específico.

## Parámetros

`placeholder_values`  
El nombre del emplazamiento reservado y el valor a ligar, definidos como un array JSON.

## Valores devueltos

Un objeto TableUpdate.

## Ejemplos

Ejemplo de `mysql_xdevapi\TableUpdate::bind`

```
<?php
$session = mysql_xdevapi\getSession("mysqlx://user:password@localhost");

$schema = $session->getSchema("addressbook");
$table  = $schema->getTable("names");

$table->update()
  ->set('status', 'admin')
  ->where('name = :name and age > :age')
  ->bind(['name' => 'Bernie', 'age' => 2000])
  ->execute();

?>

   
```php
