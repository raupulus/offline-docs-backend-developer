---
title: CrudOperationBindable::bind
description: Liga un valor a un espacio reservado
source_url: https://www.php.net/manual/es/mysql-xdevapi-crudoperationbindable.bind.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/crudoperationbindable/bind.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 18f9cbcbc
order: 53570
---

CrudOperationBindable::bind

Liga un valor a un espacio reservado

## Descripción

```php
abstract public mysql_xdevapi\CrudOperationBindable::bind(array $placeholder_values): mysql_xdevapi\CrudOperationBindable
```php

Liga un valor a un espacio reservado específico.

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

`placeholder_values`  
El nombre de los espacios reservados y los valores a ligar.

## Valores devueltos

Un objeto CrudOperationBindable

## Ejemplos

Ejemplo de `mysql_xdevapi\CrudOperationBindable::bind`

```
<?php

$res = $coll->modify('name like :name')->arrayInsert('job[0]', 'Calciatore')->bind(['name' => 'ENTITY'])->execute();
$res = $table->delete()->orderby('age desc')->where('age < 20 and age > 12 and name != :name')->bind(['name' => 'Tierney'])->limit(2)->execute();

?>

   
```php
