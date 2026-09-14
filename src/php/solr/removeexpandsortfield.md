---
title: SolrQuery::removeExpandSortField
description: Elimina un campo de ordenación de expansión del parámetro expand.sort
source_url: https://www.php.net/manual/es/solrquery.removeexpandsortfield.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrquery/removeexpandsortfield.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_reviewed: true
translation_revision: dd07341fa
order: 79870
---

SolrQuery::removeExpandSortField

Elimina un campo de ordenación de expansión del parámetro expand.sort

## Descripción

```php
public SolrQuery::removeExpandSortField(string $field): SolrQuery
```php

Se elimina un campo de ordenación de expansión del parámetro expand.sort.

## Parámetros

`field`  
El nombre del campo

## Valores devueltos

`SolrQuery`

## Véase también

SolrQuery::setExpand

SolrQuery::addExpandSortField

SolrQuery::setExpandRows

SolrQuery::setExpandQuery

SolrQuery::addExpandFilterQuery

SolrQuery::removeExpandFilterQuery
