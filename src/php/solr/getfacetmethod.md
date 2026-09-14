---
title: SolrQuery::getFacetMethod
description: Devuelve el valor del parámetro facet.method
source_url: https://www.php.net/manual/es/solrquery.getfacetmethod.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrquery/getfacetmethod.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_revision: '475439775'
order: 79140
---

SolrQuery::getFacetMethod

Devuelve el valor del parámetro facet.method

## Descripción

```php
public SolrQuery::getFacetMethod([string $field_override]): string
```php

Devuelve el valor del parámetro facet.method. Acepta una sobrescritura opcional de campos.

## Parámetros

`field_override`  
El nombre del campo

## Valores devueltos

Devuelve una cadena en caso de éxito y `null` si no se establece
