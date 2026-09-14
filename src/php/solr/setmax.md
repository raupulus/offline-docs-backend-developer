---
title: SolrCollapseFunction::setMax
description: Selecciona los encabezados de grupo por el valor máximo de un campo numérico
  o una consulta de función
source_url: https://www.php.net/manual/es/solrcollapsefunction.setmax.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrcollapsefunction/setmax.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_reviewed: true
translation_revision: dd07341fa
order: 77460
---

SolrCollapseFunction::setMax

Selecciona los encabezados de grupo por el valor máximo de un campo numérico o una consulta de función

## Descripción

```php
public SolrCollapseFunction::setMax(string $max): SolrCollapseFunction
```php

Selecciona los encabezados de grupo por el valor máximo de un campo numérico o una consulta de función.

## Parámetros

`max`  

## Valores devueltos

`SolrCollapseFunction`

## Ejemplos

Ejemplo de `SolrCollapseFunction::setMax`

```
<?php

$func = new SolrCollapseFunction('field_name');

$func->setMax('sum(cscore(),field(some_field))');

$query = new SolrQuery('*:*');

$query->collapse($func);

?>

   
```php
