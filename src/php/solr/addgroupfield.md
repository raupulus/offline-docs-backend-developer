---
title: SolrQuery::addGroupField
description: Añade un campo a utilizar para agrupar los resultados
source_url: https://www.php.net/manual/es/solrquery.addgroupfield.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrquery/addgroupfield.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_reviewed: true
translation_revision: d00128a85
order: 78870
---

SolrQuery::addGroupField

Añade un campo a utilizar para agrupar los resultados

## Descripción

```php
public SolrQuery::addGroupField(string $value): SolrQuery
```php

El nombre del campo por el cual agrupar los resultados. El campo debe ser de valor único, y estar indexado o ser un tipo de campo que tenga una fuente de valor y funcione en una consulta de función, tal como ExternalFileField. Asimismo, debe ser un campo basado en string, tal como StrField o TextField. Utiliza el parámetro group.field.

## Parámetros

`value`  
El nombre del campo.

## Valores devueltos

Devuelve una instancia de `SolrQuery`.

## Véase también

SolrQuery::setGroup

SolrQuery::addGroupFunction

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
