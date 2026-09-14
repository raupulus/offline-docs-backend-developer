---
title: CollectionRemove::execute
description: Ejecuta la operación de eliminación
source_url: https://www.php.net/manual/es/mysql-xdevapi-collectionremove.execute.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/collectionremove/execute.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 18f9cbcbc
order: 53410
---

CollectionRemove::execute

Ejecuta la operación de eliminación

## Descripción

```php
public mysql_xdevapi\CollectionRemove::execute(): mysql_xdevapi\Result
```php

La función execute debe ser invocada para desencadenar el envío de la solicitud de operación CRUD al servidor por parte del cliente.

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Objeto Result.

## Ejemplos

Ejemplo de `mysql_xdevapi\CollectionRemove::execute`

```
<?php

$res = $coll->remove('true')->sort('age desc')->limit(2)->execute();

?>

   
```php
