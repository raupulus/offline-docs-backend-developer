---
title: SolrQuery::addStatsFacet
description: Recupera una devolución de subresultados para valores dentro de la faceta
  dada
source_url: https://www.php.net/manual/es/solrquery.addstatsfacet.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrquery/addstatsfacet.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_revision: e50e79746
order: 78950
---

SolrQuery::addStatsFacet

Recupera una devolución de subresultados para valores dentro de la faceta dada

## Descripción

```php
public SolrQuery::addStatsFacet(string $field): SolrQuery
```php

Recupera una devolución de subresultados para valores dentro de la faceta dada. Mapea al campo stats.facet

## Parámetros

`field`  
El nombre del campo

## Valores devueltos

Devuelve el objeto SolrQuery actual, si se usa el valor de retorno.
