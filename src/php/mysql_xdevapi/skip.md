---
title: CollectionModify::skip
description: Ignorar los elementos
source_url: https://www.php.net/manual/es/mysql-xdevapi-collectionmodify.skip.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/collectionmodify/skip.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: ee5228571
order: 53360
---

CollectionModify::skip

Ignorar los elementos

## Descripción

```php
public mysql_xdevapi\CollectionModify::skip(int $position): mysql_xdevapi\CollectionModify
```php

Ignora los N primeros elementos que de otro modo serían devueltos por una operación de búsqueda. Si el número de elementos ignorados es superior al tamaño del conjunto de resultados, entonces la operación de búsqueda devuelve un conjunto vacío.

## Parámetros

`position`  
El número de elementos a ignorar.

## Valores devueltos

Un objeto CollectionModify para ser utilizado en un procesamiento posterior.

## Ejemplos

Ejemplo de `mysql_xdevapi\CollectionModify::skip`

```
<?php

$coll->modify('age > :age')->sort('age desc')->unset(['age'])->bind(['age' => 20])->limit(4)->skip(1)->execute();

?>

   
```php
