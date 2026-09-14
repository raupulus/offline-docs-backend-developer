---
title: SolrQuery::getFacetSort
description: Devuelve el tipo de ordenación de la faceta
source_url: https://www.php.net/manual/es/solrquery.getfacetsort.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrquery/getfacetsort.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_revision: '475439775'
order: 79200
---

SolrQuery::getFacetSort

Devuelve el tipo de ordenación de la faceta

## Descripción

```php
public SolrQuery::getFacetSort([string $field_override]): int
```php

Devuelve un entero (SolrQuery::FACET_SORT_INDEX o SolrQuery::FACET_SORT_COUNT)

## Parámetros

`field_override`  
El nombre del campo

## Valores devueltos

Devuelve un entero (SolrQuery::FACET_SORT_INDEX o SolrQuery::FACET_SORT_COUNT) en caso de éxito o `null` si no se estableció.
