---
title: CrudOperationLimitable::limit
description: Define el límite de resultados
source_url: https://www.php.net/manual/es/mysql-xdevapi-crudoperationlimitable.limit.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/crudoperationlimitable/limit.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 86e6094e8
order: 53580
---

CrudOperationLimitable::limit

Define el límite de resultados

## Descripción

```php
abstract public mysql_xdevapi\CrudOperationLimitable::limit(int $rows): mysql_xdevapi\CrudOperationLimitable
```php

Define el número máximo de resultados o documentos a devolver.

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

`rows`  
El número máximo de resultados o documentos.

## Valores devueltos

Un objeto CrudOperationLimitable.

## Ejemplos

Ejemplo de `mysql_xdevapi\CrudOperationLimitable::limit`

```
<?php

$res = $coll->find()->fields(['name as n','age as a','job as j'])->groupBy('j')->limit(11)->execute();
$res = $table->update()->set('age',69)->where('age > 15 and age < 22')->limit(4)->orderby(['age asc','name desc'])->execute();

?>

   
```php
