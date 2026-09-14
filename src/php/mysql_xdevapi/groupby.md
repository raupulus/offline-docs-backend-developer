---
title: CollectionFind::groupBy
description: Define los criterios de agrupación
source_url: https://www.php.net/manual/es/mysql-xdevapi-collectionfind.groupby.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/collectionfind/groupby.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 10cf63a9a
order: 53200
---

CollectionFind::groupBy

Define los criterios de agrupación

## Descripción

```php
public mysql_xdevapi\CollectionFind::groupBy(string $sort_expr): mysql_xdevapi\CollectionFind
```php

Esta función puede ser utilizada para agrupar el conjunto de resultados por una o más columnas. Es a menudo utilizada con funciones de agregación tales como `COUNT`, `MAX`, `MIN`, `SUM` etc.

## Parámetros

`sort_expr`  
La o las columnas que deben ser utilizadas para la operación de agrupación, esto puede ser una cadena única o un array de argumentos de string, uno para cada columna.

## Valores devueltos

Un objeto CollectionFind que puede ser utilizado para un procesamiento posterior.

## Ejemplos

Ejemplo de `mysql_xdevapi\CollectionFind::groupBy`

```
<?php

// Asumiendo que $coll es un objeto Collection válido

// Extrae todos los documentos de la Collection y agrupa los resultados por el campo 'name'
$res = $coll->find()->groupBy('name')->execute();

?>

   
```php
