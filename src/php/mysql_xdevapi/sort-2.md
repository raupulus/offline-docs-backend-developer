---
title: CollectionModify::sort
description: Define los criterios de ordenación
source_url: https://www.php.net/manual/es/mysql-xdevapi-collectionmodify.sort.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/collectionmodify/sort.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: ee5228571
order: 53370
---

CollectionModify::sort

Define los criterios de ordenación

## Descripción

```php
public mysql_xdevapi\CollectionModify::sort(string $sort_expr): mysql_xdevapi\CollectionModify
```php

Ordena el conjunto de resultados por el campo seleccionado en el argumento sort_expr. Los órdenes permitidos son ASC (Ascendente) o DESC (Descendente). Esta operación es equivalente a la operación SQL 'ORDER BY' y sigue el mismo conjunto de reglas.

## Parámetros

`sort_expr`  
Una o más expresiones de ordenación pueden ser proporcionadas. La evaluación se realiza de izquierda a derecha y cada expresión debe estar separada por una coma.

## Valores devueltos

Un objeto CollectionModify que puede ser utilizado para un procesamiento posterior.

## Ejemplos

Ejemplo de `mysql_xdevapi\CollectionModify::sort`

```
<?php

$res = $coll->modify('true')->sort('name desc', 'age asc')->limit(4)->set('Married', 'NO')->execute();

?>

   
```php
