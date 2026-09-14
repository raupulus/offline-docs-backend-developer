---
title: SolrQuery::addGroupFunction
description: Permite agrupar los resultados según los valores únicos de una consulta
  de función (argumento group.func)
source_url: https://www.php.net/manual/es/solrquery.addgroupfunction.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrquery/addgroupfunction.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_reviewed: true
translation_revision: dd07341fa
order: 78880
---

SolrQuery::addGroupFunction

Permite agrupar los resultados según los valores únicos de una consulta de función (argumento group.func)

## Descripción

```php
public SolrQuery::addGroupFunction(string $value): SolrQuery
```php

Añade una función de grupo (argumento group.func) Permite agrupar los resultados según los valores únicos de una consulta de función.

## Parámetros

`value`  

## Valores devueltos

`SolrQuery`

## Véase también

SolrQuery::setGroup

SolrQuery::addGroupField

SolrQuery::addGroupQuery

SolrQuery::addGroupSortField

SolrQuery::setGroupFacet

SolrQuery::setGroupOffset

SolrQuery::setGroupLimit

SolrQuery::setGroupMain

SolrQuery::setGroupNGroups

SolrQuery::setGroupTruncate

SolrQuery::setGroupFormat

SolrQuery::setGroupCachePercent
