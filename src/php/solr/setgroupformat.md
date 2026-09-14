---
title: SolrQuery::setGroupFormat
description: Define el formato de grupo, la estructura de resultado (argumento group.format)
source_url: https://www.php.net/manual/es/solrquery.setgroupformat.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrquery/setgroupformat.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_reviewed: true
translation_revision: dd07341fa
order: 80220
---

SolrQuery::setGroupFormat

Define el formato de grupo, la estructura de resultado (argumento group.format)

## Descripción

```php
public SolrQuery::setGroupFormat(string $value): SolrQuery
```php

Define el argumento group.format. Si este argumento se establece en simple, los documentos agrupados se presentan en una sola lista plana, y los argumentos start y rows afectan al número de documentos en lugar de los grupos. Valores aceptados: grouped/simple

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

SolrQuery::setGroupTruncate

SolrQuery::setGroupCachePercent
