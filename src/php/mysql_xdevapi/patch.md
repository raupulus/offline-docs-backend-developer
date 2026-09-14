---
title: CollectionModify::patch
description: Corrige un documento
source_url: https://www.php.net/manual/es/mysql-xdevapi-collectionmodify.patch.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mysql_xdevapi/mysql_xdevapi/collectionmodify/patch.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mysql_xdevapi
translation_status: ready
translation_reviewed: false
translation_revision: ee5228571
order: 53330
---

CollectionModify::patch

Corrige un documento

## Descripción

```php
public mysql_xdevapi\CollectionModify::patch(string $document): mysql_xdevapi\CollectionModify
```php

Toma un objeto patch y lo aplica sobre uno o varios documentos, y puede actualizar varias propiedades del documento.

## Parámetros

`document`  
Un documento con las propiedades a aplicar a los documentos correspondientes.

## Valores devueltos

Un objeto CollectionModify.

## Ejemplos

Ejemplo de `mysql_xdevapi\CollectionModify::patch`

```
<?php

$res = $coll->modify('"Programmatore" IN job')->patch('{"Hobby" : "Programmare"}')->execute();

?>

   
```php
