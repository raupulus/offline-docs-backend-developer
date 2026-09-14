---
title: TableUpdate::limit
description: Limita el número de filas actualizadas
source_url: https://www.php.net/manual/es/mysql-xdevapi-tableupdate.limit.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/tableupdate/limit.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 86e6094e8
order: 54730
---

TableUpdate::limit

Limita el número de filas actualizadas

## Descripción

```php
public mysql_xdevapi\TableUpdate::limit(int $rows): mysql_xdevapi\TableUpdate
```php

Define el número máximo de filas o documentos a actualizar.

## Parámetros

`rows`  
El número máximo de filas o documentos a actualizar.

## Valores devueltos

Un objeto TableUpdate.

## Ejemplos

Ejemplo de `mysql_xdevapi\TableUpdate::limit`

```
<?php
$session = mysql_xdevapi\getSession("mysqlx://user:password@localhost");

$schema = $session->getSchema("addressbook");
$table  = $schema->getTable("names");

$res = $table->update()
  ->set('level', 3)
  ->where('age > 15 and age < 22')
  ->limit(4)
  ->orderby(['age asc','name desc'])
  ->execute();

?>

   
```php
