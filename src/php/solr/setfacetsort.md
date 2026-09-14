---
title: SolrQuery::setFacetSort
description: Determina el orden de las restricciones de campos de faceta
source_url: https://www.php.net/manual/es/solrquery.setfacetsort.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrquery/setfacetsort.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_revision: b6e314781
order: 80180
---

SolrQuery::setFacetSort

Determina el orden de las restricciones de campos de faceta

## Descripción

```php
public SolrQuery::setFacetSort(int $facetSort, [string $field_override]): SolrQuery
```php

Determina el orden de las restricciones de campos de faceta

## Parámetros

`facetSort`  
Use SolrQuery::FACET_SORT_INDEX para ordenar por índice o SolrQuery::FACET_SORT_COUNT para ordenar por cuenta.

`field_override`  
El nombre del campo.

## Valores devueltos

Devuelve el objeto SolrQuery actual, si se usó el valor de retorno.
