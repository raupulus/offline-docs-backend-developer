---
title: CrudOperationSkippable::skip
description: El número de operaciones a ignorar
source_url: https://www.php.net/manual/es/mysql-xdevapi-crudoperationskippable.skip.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/crudoperationskippable/skip.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 86e6094e8
order: 53590
---

CrudOperationSkippable::skip

El número de operaciones a ignorar

## Descripción

```php
abstract public mysql_xdevapi\CrudOperationSkippable::skip(int $skip): mysql_xdevapi\CrudOperationSkippable
```php

Ignora este número de registros en la operación devuelta.

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

`skip`  
El número de elementos a ignorar.

## Valores devueltos

Un objeto CrudOperationSkippable.

## Ejemplos

Ejemplo de `mysql_xdevapi\CrudOperationSkippable::skip`

```
<?php

$res = $coll->find('job like \'Programmatore\'')->limit(1)->skip(3)->sort('age asc')->execute();

?>

   
```php
