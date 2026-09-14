---
title: CollectionModify::unset
description: Elimina el valor de los campos del documento
source_url: https://www.php.net/manual/es/mysql-xdevapi-collectionmodify.unset.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/collectionmodify/unset.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: ee5228571
order: 53380
---

CollectionModify::unset

Elimina el valor de los campos del documento

## Descripción

```php
public mysql_xdevapi\CollectionModify::unset(array $fields): mysql_xdevapi\CollectionModify
```php

Elimina los atributos de los documentos en una colección.

## Parámetros

`fields`  
Los atributos a eliminar de los documentos en una colección.

## Valores devueltos

Un objeto CollectionModify que puede ser utilizado para un procesamiento posterior.

## Ejemplos

Ejemplo de `mysql_xdevapi\CollectionModify::unset`

```
<?php

$res = $coll->modify('job like :job_name')->unset(["age", "name"])->bind(['job_name' => 'Plumber'])->execute();

?>

   
```php
