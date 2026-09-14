---
title: SolrQuery::getFacetLimit
description: Devuelve el número máximo de restricciones que deberían ser devueltas
  por los campos facet
source_url: https://www.php.net/manual/es/solrquery.getfacetlimit.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrquery/getfacetlimit.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_revision: '475439775'
order: 79130
---

SolrQuery::getFacetLimit

Devuelve el número máximo de restricciones que deberían ser devueltas por los campos facet

## Descripción

```php
public SolrQuery::getFacetLimit([string $field_override]): int
```php

Devuelve el número máximo de restricciones que deberían ser devueltas por los campos facet. Este método acepta una sobrescritura opcional de campos

## Parámetros

`field_override`  
El nombre del campo a sobrescribir.

## Valores devueltos

Devuelve un entero en caso de éxito y `null` si no se estableció
