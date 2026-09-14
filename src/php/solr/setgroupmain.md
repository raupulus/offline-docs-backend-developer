---
title: SolrQuery::setGroupMain
description: Si es verdadero, el resultado del primer comando de agrupación de campo
  se utiliza como lista de resultados principal en la respuesta, utilizando group.format=simple
source_url: https://www.php.net/manual/es/solrquery.setgroupmain.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrquery/setgroupmain.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_reviewed: true
translation_revision: d00128a85
order: 80240
---

SolrQuery::setGroupMain

Si es verdadero, el resultado del primer comando de agrupación de campo se utiliza como lista de resultados principal en la respuesta, utilizando group.format=simple

## Descripción

```php
public SolrQuery::setGroupMain(string $value): SolrQuery
```php

Si `true`, el resultado del primer comando de agrupación de campo se utiliza como lista de resultados principal en la respuesta, utilizando `group.format=simple`.

## Parámetros

`value`  
Si `true`, el resultado del primer comando de agrupación de campo se utiliza como lista de resultados principal en la respuesta.

## Valores devueltos

Devuelve una instancia de `SolrQuery`.

## Véase también

SolrQuery::setGroup

SolrQuery::addGroupField

SolrQuery::addGroupFunction

SolrQuery::addGroupQuery

SolrQuery::addGroupSortField

SolrQuery::setGroupFacet

SolrQuery::setGroupOffset

SolrQuery::setGroupMain

SolrQuery::setGroupNGroups

SolrQuery::setGroupTruncate

SolrQuery::setGroupFormat

SolrQuery::setGroupCachePercent
