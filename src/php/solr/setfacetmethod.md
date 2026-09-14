---
title: SolrQuery::setFacetMethod
description: Especifica el tipo de algoritmo a usar cuando se hace una faceta a un
  campo
source_url: https://www.php.net/manual/es/solrquery.setfacetmethod.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrquery/setfacetmethod.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_revision: b6e314781
order: 80130
---

SolrQuery::setFacetMethod

Especifica el tipo de algoritmo a usar cuando se hace una faceta a un campo

## Descripción

```php
public SolrQuery::setFacetMethod(string $method, [string $field_override]): SolrQuery
```php

Especifica el tipo de algoritmo a usar cuando se hace una faceta a un campo. Este método acepta la sobrescritura opcional de campos.

## Parámetros

`method`  
El método a usar.

`field_override`  
El nombre del campo.

## Valores devueltos

Devuelve el objeto SolrQuery actual, si se usó el valor de retorno.
