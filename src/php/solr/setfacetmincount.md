---
title: SolrQuery::setFacetMinCount
description: Mapea a facet.mincount
source_url: https://www.php.net/manual/es/solrquery.setfacetmincount.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrquery/setfacetmincount.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_revision: b6e314781
order: 80140
---

SolrQuery::setFacetMinCount

Mapea a facet.mincount

## Descripción

```php
public SolrQuery::setFacetMinCount(int $mincount, [string $field_override]): SolrQuery
```php

Establece el mínimo de campos de faceta que deberían ser incluidos en la respuesta

## Parámetros

`mincount`  
El mínimo

`field_override`  
El nombre del campo.

## Valores devueltos

Devuelve el objeto SolrQuery actual, si se usó el valor de retorno.
