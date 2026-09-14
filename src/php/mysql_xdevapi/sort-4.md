---
title: CrudOperationSortable::sort
description: Ordena los resultados
source_url: https://www.php.net/manual/es/mysql-xdevapi-crudoperationsortable.sort.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/crudoperationsortable/sort.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 18f9cbcbc
order: 53600
---

CrudOperationSortable::sort

Ordena los resultados

## Descripción

```php
abstract public mysql_xdevapi\CrudOperationSortable::sort(string $sort_expr): mysql_xdevapi\CrudOperationSortable
```php

Ordena el conjunto de resultados por el campo seleccionado en el argumento sort_expr. Los órdenes permitidos son ASC (Ascendente) o DESC (Descendente). Esta operación es equivalente a la operación SQL 'ORDER BY' y sigue el mismo conjunto de reglas.

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

`sort_expr`  
Una o más expresiones de ordenación pueden ser proporcionadas. La evaluación se realiza de izquierda a derecha, y cada expresión está separada por una coma.

## Valores devueltos

Un objeto CrudOperationSortable.

## Ejemplos

Ejemplo de `mysql_xdevapi\CrudOperationSortable::sort`

```
<?php

$res = $coll->find('job like \'Cavia\'')->sort('age desc', '_id desc')->execute();

?>

   
```php
