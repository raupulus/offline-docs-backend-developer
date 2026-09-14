---
title: SolrQuery::addFacetDateField
description: Mapea a facet.date
source_url: https://www.php.net/manual/es/solrquery.addfacetdatefield.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrquery/addfacetdatefield.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_revision: 734ddd27a
order: 78810
---

SolrQuery::addFacetDateField

Mapea a facet.date

## Descripción

```php
public SolrQuery::addFacetDateField(string $dateField): SolrQuery
```php

Este método permite especificar un campo que debería ser tratado como una faceta.

Se puede usar mútiples veces con diferentes nombres de campos para indicar mútiples campos de facetas

## Parámetros

`dateField`  
El nombre del campo de fecha.

## Valores devueltos

Devuelve un objeto SolrQuery.
