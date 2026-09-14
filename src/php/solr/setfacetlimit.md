---
title: SolrQuery::setFacetLimit
description: Mapea a facet.limit
source_url: https://www.php.net/manual/es/solrquery.setfacetlimit.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrquery/setfacetlimit.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_revision: b6e314781
order: 80120
---

SolrQuery::setFacetLimit

Mapea a facet.limit

## Descripción

```php
public SolrQuery::setFacetLimit(int $limit, [string $field_override]): SolrQuery
```php

Mapea a facet.limit. Establece el número máximo de restricciones que deberían ser devueltas por los campos de facetas.

## Parámetros

`limit`  
El número máximo de restricciones

`field_override`  
El nombre del campo.

## Valores devueltos

Devuelve el objeto SolrQuery actual, si se usó el valor de retorno.
