---
title: CollectionRemove::limit
description: Limita el número de documentos a eliminar
source_url: https://www.php.net/manual/es/mysql-xdevapi-collectionremove.limit.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/collectionremove/limit.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: 86e6094e8
order: 53420
---

CollectionRemove::limit

Limita el número de documentos a eliminar

## Descripción

```php
public mysql_xdevapi\CollectionRemove::limit(int $rows): mysql_xdevapi\CollectionRemove
```php

Define el número máximo de documentos a eliminar.

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

`rows`  
El número máximo de documentos a eliminar.

## Valores devueltos

Devuelve un objeto CollectionRemove que puede ser utilizado para ejecutar el comando, o para añadir operaciones adicionales.

## Ejemplos

Ejemplo de `mysql_xdevapi\CollectionRemove::limit`

```
<?php

$res = $coll->remove('job in (\'Barista\', \'Programmatore\', \'Ballerino\', \'Programmatrice\')')->limit(5)->sort(['age desc', 'name asc'])->execute();

?>

   
```php
