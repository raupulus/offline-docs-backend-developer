---
title: SolrQuery::getFacetDateOther
description: Devuelve el valor del parámetro facet.date.other
source_url: https://www.php.net/manual/es/solrquery.getfacetdateother.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrquery/getfacetdateother.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_revision: '475439775'
order: 79100
---

SolrQuery::getFacetDateOther

Devuelve el valor del parámetro facet.date.other

## Descripción

```php
public SolrQuery::getFacetDateOther([string $field_override]): array
```php

Devuelve el valor del parámetro facet.date.other. Este método acepta una sobrescritura opcional de campos.

## Parámetros

`field_override`  
El nombre del campo

## Valores devueltos

Devuelve un `array` en caso de éxito y `null` si no se estableció.
