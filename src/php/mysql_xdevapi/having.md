---
title: CollectionFind::having
description: Define la condición para las funciones de agregación
source_url: https://www.php.net/manual/es/mysql-xdevapi-collectionfind.having.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/collectionfind/having.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: a7f80c716
order: 53210
---

CollectionFind::having

Define la condición para las funciones de agregación

## Descripción

```php
public mysql_xdevapi\CollectionFind::having(string $sort_expr): mysql_xdevapi\CollectionFind
```php

Esta función puede ser utilizada después de la operación 'field' para hacer una selección sobre los documentos a extraer.

## Parámetros

`sort_expr`  
Debe ser una expresión SQL válida, el uso de funciones de agregación está permitido.

## Valores devueltos

Un objeto CollectionFind que puede ser utilizado para un procesamiento posterior.

## Ejemplos

Ejemplo de `mysql_xdevapi\CollectionFind::having`

```
<?php

//Asumiendo que $coll es un objeto Collection válido

//Encuentra todos los documentos para los cuales la edad es mayor que 40,
//Solo las columnas 'name' y 'age' son devueltas en el objeto Result
$res = $coll->find()->fields(['name','age'])->having('age > 40')->execute();

?>

   
```php
