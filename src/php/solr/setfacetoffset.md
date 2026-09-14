---
title: SolrQuery::setFacetOffset
description: Establece el índice de la lista de restricciones para tener en cuenta
  la paginación
source_url: https://www.php.net/manual/es/solrquery.setfacetoffset.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrquery/setfacetoffset.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_revision: b6e314781
order: 80160
---

SolrQuery::setFacetOffset

Establece el índice de la lista de restricciones para tener en cuenta la paginación

## Descripción

```php
public SolrQuery::setFacetOffset(int $offset, [string $field_override]): SolrQuery
```php

Establece el índice de la lista de restricciones para tener en cuenta la paginación.

## Parámetros

`offset`  
El índice

`field_override`  
El nombre del campo.

## Valores devueltos

Devuelve el objeto SolrQuery actual, si se usó el valor de retorno.
