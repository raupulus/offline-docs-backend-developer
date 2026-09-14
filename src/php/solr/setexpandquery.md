---
title: SolrQuery::setExpandQuery
description: Define el parámetro expand.q
source_url: https://www.php.net/manual/es/solrquery.setexpandquery.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrquery/setexpandquery.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_reviewed: true
translation_revision: 418e95fc8
order: 80030
---

SolrQuery::setExpandQuery

Define el parámetro expand.q

## Descripción

```php
public SolrQuery::setExpandQuery(string $q): SolrQuery
```php

Define el parámetro expand.q.

Sobrescribe el parámetro principal q, determina qué documentos incluir en el grupo principal.

## Parámetros

`q`  

## Valores devueltos

`SolrQuery`

## Véase también

SolrQuery::setExpand

SolrQuery::addExpandSortField

SolrQuery::removeExpandSortField

SolrQuery::setExpandRows

SolrQuery::addExpandFilterQuery

SolrQuery::removeExpandFilterQuery
