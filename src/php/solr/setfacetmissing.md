---
title: SolrQuery::setFacetMissing
description: Mapea a facet.missing
source_url: https://www.php.net/manual/es/solrquery.setfacetmissing.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrquery/setfacetmissing.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_revision: b6e314781
order: 80150
---

SolrQuery::setFacetMissing

Mapea a facet.missing

## Descripción

```php
public SolrQuery::setFacetMissing(bool $flag, [string $field_override]): SolrQuery
```php

Usado para indicar que además de las restricciones basdas en términos de un campo de faceta, debería ser computada una cuenta de todos los resultados coincidentes que no tienen valor para el campo

## Parámetros

`flag`  
`true` activa esta característica. `false` la desactiva.

`field_override`  
El nombre del campo.

## Valores devueltos

Devuelve el objeto SolrQuery actual, si se usó el valor de retorno.
