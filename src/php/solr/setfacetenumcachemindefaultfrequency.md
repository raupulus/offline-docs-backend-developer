---
title: SolrQuery::setFacetEnumCacheMinDefaultFrequency
description: Establece la frecuencia de documento mínima usada para determinar la
  cuenta de términos
source_url: https://www.php.net/manual/es/solrquery.setfacetenumcachemindefaultfrequency.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrquery/setfacetenumcachemindefaultfrequency.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_revision: b6e314781
order: 80110
---

SolrQuery::setFacetEnumCacheMinDefaultFrequency

Establece la frecuencia de documento mínima usada para determinar la cuenta de términos

## Descripción

```php
public SolrQuery::setFacetEnumCacheMinDefaultFrequency(int $frequency, [string $field_override]): SolrQuery
```php

Establece la frecuencia de documento mínima usada para determinar la cuenta de términos

## Parámetros

`value`  
La frecuencia mínima

`field_override`  
El nombre del campo.

## Valores devueltos

Devuelve el objeto SolrQuery actual, si se usó el valor de retorno.
