---
title: SolrQuery::getTermsSort
description: Devuelve un entero indicando cómo son ordenados los términos
source_url: https://www.php.net/manual/es/solrquery.gettermssort.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrquery/gettermssort.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_revision: '475439775'
order: 79830
---

SolrQuery::getTermsSort

Devuelve un entero indicando cómo son ordenados los términos

## Descripción

```php
public SolrQuery::getTermsSort(): int
```php

SolrQuery::TERMS_SORT_INDEX indica que los términos son devueltos por orden de índice. SolrQuery::TERMS_SORT_COUNT implica que los términos son ordenados según la frecuencia del término (la más alta cuenta como la primera)

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un entero en caso de éxito y `null` si no se estableció.
