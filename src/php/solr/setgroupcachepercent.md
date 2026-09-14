---
title: SolrQuery::setGroupCachePercent
description: Define el porcentaje de caché para el agrupamiento de resultados
source_url: https://www.php.net/manual/es/solrquery.setgroupcachepercent.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrquery/setgroupcachepercent.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_reviewed: true
translation_revision: be295015d
order: 80200
---

SolrQuery::setGroupCachePercent

Define el porcentaje de caché para el agrupamiento de resultados

## Descripción

```php
public SolrQuery::setGroupCachePercent(int $percent): SolrQuery
```php

Definir este parámetro con un número mayor que 0 activa la caché para el agrupamiento de resultados. El agrupamiento de resultados ejecuta dos búsquedas; esta opción almacena en caché la segunda búsqueda. El valor por omisión del servidor es 0. Las pruebas han demostrado que la caché de grupo solo mejora el tiempo de búsqueda con consultas booleanas, genéricas y difusas. Para consultas simples como las consultas de término o "match all", la caché de grupo degrada el rendimiento. Parámetro group.cache.percent

## Parámetros

`percent`  

## Valores devueltos

## Errores/Excepciones

Genera una `SolrIllegalArgumentException` si se ha pasado un argumento inválido.

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

SolrQuery::setGroupFormat
