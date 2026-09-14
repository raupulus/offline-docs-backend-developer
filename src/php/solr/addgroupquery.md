---
title: SolrQuery::addGroupQuery
description: Permite agrupar los documentos que coinciden con la consulta dada
source_url: https://www.php.net/manual/es/solrquery.addgroupquery.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrquery/addgroupquery.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_reviewed: true
translation_revision: dd07341fa
order: 78890
---

SolrQuery::addGroupQuery

Permite agrupar los documentos que coinciden con la consulta dada

## Descripción

```php
public SolrQuery::addGroupQuery(string $value): SolrQuery
```php

Permite agrupar los documentos que coinciden con la consulta dada. Añade la consulta al parámetro group.query

## Parámetros

`value`  

## Valores devueltos

`SolrQuery`

## Véase también

SolrQuery::setGroup

SolrQuery::addGroupField

SolrQuery::addGroupFunction

SolrQuery::addGroupSortField

SolrQuery::setGroupFacet

SolrQuery::setGroupOffset

SolrQuery::setGroupLimit

SolrQuery::setGroupMain

SolrQuery::setGroupNGroups

SolrQuery::setGroupTruncate

SolrQuery::setGroupFormat

SolrQuery::setGroupCachePercent
