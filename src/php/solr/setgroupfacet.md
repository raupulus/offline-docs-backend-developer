---
title: SolrQuery::setGroupFacet
description: Define el parámetro group.facet
source_url: https://www.php.net/manual/es/solrquery.setgroupfacet.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrquery/setgroupfacet.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_reviewed: true
translation_revision: 86e7c61ef
order: 80210
---

SolrQuery::setGroupFacet

Define el parámetro group.facet

## Descripción

```php
public SolrQuery::setGroupFacet(bool $value): SolrQuery
```php

Determina si las facetas agrupadas deben ser calculadas para los campos facetados especificados en los parámetros facet.field. Las facetas agrupadas se calculan en función del primer grupo especificado.

## Parámetros

`value`  

## Valores devueltos

## Véase también

SolrQuery::setGroup

SolrQuery::addGroupField

SolrQuery::addGroupFunction

SolrQuery::addGroupQuery

SolrQuery::addGroupSortField

SolrQuery::setGroupOffset

SolrQuery::setGroupLimit

SolrQuery::setGroupMain

SolrQuery::setGroupNGroups

SolrQuery::setGroupTruncate

SolrQuery::setGroupFormat

SolrQuery::setGroupCachePercent
