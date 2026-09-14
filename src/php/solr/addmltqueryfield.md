---
title: SolrQuery::addMltQueryField
description: Mapea a mlt.qf
source_url: https://www.php.net/manual/es/solrquery.addmltqueryfield.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrquery/addmltqueryfield.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_revision: b6e314781
order: 78930
---

SolrQuery::addMltQueryField

Mapea a mlt.qf

## Descripción

```php
public SolrQuery::addMltQueryField(string $field, float $boost): SolrQuery
```php

Mapea a mlt.qf. Se usa para especificar campos de consultas y sus boosts

## Parámetros

`field`  
El nombre del campo

`boost`  
Su valor boost

## Valores devueltos

Devuelve el objeto SolrQuery actual, si se usa el valor de retorno.
