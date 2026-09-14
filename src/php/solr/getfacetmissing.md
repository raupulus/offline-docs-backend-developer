---
title: SolrQuery::getFacetMissing
description: Devuelve el estado acutual del parámetro facet.missing
source_url: https://www.php.net/manual/es/solrquery.getfacetmissing.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrquery/getfacetmissing.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_revision: '475439775'
order: 79160
---

SolrQuery::getFacetMissing

Devuelve el estado acutual del parámetro facet.missing

## Descripción

```php
public SolrQuery::getFacetMissing([string $field_override]): bool
```php

Devuelve el estado acutual del parámetro facet.missing. Acepta una sobrescritura opcional de campos

## Parámetros

`field_override`  
El nombre del campo

## Valores devueltos

Devuelve un booleano en caso de éxito y `null` si no se estableció
