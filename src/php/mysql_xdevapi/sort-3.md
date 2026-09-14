---
title: CollectionRemove::sort
description: Define el criterio de ordenación
source_url: https://www.php.net/manual/es/mysql-xdevapi-collectionremove.sort.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/collectionremove/sort.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 730ae1c76
order: 53430
---

CollectionRemove::sort

Define el criterio de ordenación

## Descripción

```php
public mysql_xdevapi\CollectionRemove::sort(string $sort_expr): mysql_xdevapi\CollectionRemove
```php

Ordena el conjunto de resultados por el campo seleccionado en el argumento sort_expr. Los órdenes permitidos son ASC (Ascending) o DESC (Descending). Esta operación es equivalente a la operación SQL 'ORDER BY' y sigue el mismo conjunto de reglas.

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

`sort_expr`  
Una o más expresiones de ordenación pueden ser proporcionadas. La evaluación se realiza de izquierda a derecha, y cada expresión está separada por una coma.

## Valores devueltos

Un objeto CollectionRemove que puede ser utilizado para ejecutar el comando, o para añadir operaciones adicionales.

## Ejemplos

Ejemplo de `mysql_xdevapi\CollectionRemove::sort`

```
<?php

$res = $coll->remove('true')->sort('age desc')->limit(2)->execute();

?>

   
```php
