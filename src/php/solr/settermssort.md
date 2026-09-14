---
title: SolrQuery::setTermsSort
description: Especifica cómo ordenar los términos devueltos
source_url: https://www.php.net/manual/es/solrquery.settermssort.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrquery/settermssort.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_revision: b6e314781
order: 80710
---

SolrQuery::setTermsSort

Especifica cómo ordenar los términos devueltos

## Descripción

```php
public SolrQuery::setTermsSort(int $sortType): SolrQuery
```php

Si se usa SolrQuery::TERMS_SORT_COUNT, ordena los términos según la frecuencia del término (la mayor primero). Si se usa SolrQuery::TERMS_SORT_INDEX, devuelve los términos ordenados por índice

## Parámetros

`sortType`  
SolrQuery::TERMS_SORT_INDEX o SolrQuery::TERMS_SORT_COUNT

## Valores devueltos

Devuelve el objeto SolrQuery actual, si se usó el valor de retorno.
