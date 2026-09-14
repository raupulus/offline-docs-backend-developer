---
title: SolrQuery::addExpandFilterQuery
description: Sobrescribe la consulta de filtro principal, determina qué documentos
  incluir en el grupo principal
source_url: https://www.php.net/manual/es/solrquery.addexpandfilterquery.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrquery/addexpandfilterquery.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_reviewed: true
translation_revision: dd07341fa
order: 78790
---

SolrQuery::addExpandFilterQuery

Sobrescribe la consulta de filtro principal, determina qué documentos incluir en el grupo principal

## Descripción

```php
public SolrQuery::addExpandFilterQuery(string $fq): SolrQuery
```php

Sobrescribe la consulta de filtro principal, determina qué documentos incluir en el grupo principal.

## Parámetros

`fq`  

## Valores devueltos

`SolrQuery`

## Véase también

SolrQuery::setExpand

SolrQuery::addExpandSortField

SolrQuery::removeExpandSortField

SolrQuery::setExpandRows

SolrQuery::setExpandQuery

SolrQuery::removeExpandFilterQuery
