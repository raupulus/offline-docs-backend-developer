---
title: SolrQuery::addFacetDateOther
description: Añade otro parámetro facet.date.other
source_url: https://www.php.net/manual/es/solrquery.addfacetdateother.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrquery/addfacetdateother.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_revision: b6e314781
order: 78820
---

SolrQuery::addFacetDateOther

Añade otro parámetro facet.date.other

## Descripción

```php
public SolrQuery::addFacetDateOther(string $value, [string $field_override]): SolrQuery
```php

Establece el parámetro facet.date.other. Acepta la sobrescritura opcional de campos

## Parámetros

`value`  
El valor a usar.

`field_override`  
El nombre del campo para la sobrescritura.

## Valores devueltos

Devuelve el objeto SolrQuery actual, si se usa el valor de retorno.
