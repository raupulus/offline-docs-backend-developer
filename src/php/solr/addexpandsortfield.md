---
title: SolrQuery::addExpandSortField
description: Ordena los documentos en los grupos extendidos (parámetro expand.sort)
source_url: https://www.php.net/manual/es/solrquery.addexpandsortfield.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrquery/addexpandsortfield.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_reviewed: true
translation_revision: dd07341fa
order: 78800
---

SolrQuery::addExpandSortField

Ordena los documentos en los grupos extendidos (parámetro expand.sort)

## Descripción

```php
public SolrQuery::addExpandSortField(string $field, [string $order]): SolrQuery
```php

Ordena los documentos en los grupos extendidos (parámetro expand.sort).

## Parámetros

`field`  
El nombre del campo

`order`  
Orden ASC/DESC, utiliza las constantes SolrQuery::ORDER\_\*.

Valor por omisión: `SolrQuery::ORDER_DESC`

## Valores devueltos

`SolrQuery`

## Véase también

SolrQuery::setExpand

SolrQuery::removeExpandSortField

SolrQuery::setExpandRows

SolrQuery::setExpandQuery

SolrQuery::addExpandFilterQuery

SolrQuery::removeExpandFilterQuery
