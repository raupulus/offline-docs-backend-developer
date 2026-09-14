---
title: SolrQuery::setGroupTruncate
description: Si es verdadero, los conteos de facetas se basan en el documento más
  relevante de cada grupo correspondiente a la consulta
source_url: https://www.php.net/manual/es/solrquery.setgrouptruncate.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrquery/setgrouptruncate.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_reviewed: true
translation_revision: dd07341fa
order: 80270
---

SolrQuery::setGroupTruncate

Si es verdadero, los conteos de facetas se basan en el documento más relevante de cada grupo correspondiente a la consulta

## Descripción

```php
public SolrQuery::setGroupTruncate(bool $value): SolrQuery
```php

Si es verdadero, los conteos de facetas se basan en el documento más relevante de cada grupo correspondiente a la consulta. El valor por omisión del servidor es false. Parámetro group.truncate

## Parámetros

`value`  

## Valores devueltos

## Véase también

SolrQuery::setGroup

SolrQuery::addGroupField

SolrQuery::addGroupFunction

SolrQuery::addGroupQuery

SolrQuery::addGroupSortField

SolrQuery::setGroupFacet

SolrQuery::setGroupOffset

SolrQuery::setGroupLimit

SolrQuery::setGroupMain

SolrQuery::setGroupNGroups

SolrQuery::setGroupFormat

SolrQuery::setGroupCachePercent
