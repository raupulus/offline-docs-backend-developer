---
title: SolrQuery::getFacetOffset
description: Devuelve un índice dentro de la lista de restricciones para ser usado
  en paginación
source_url: https://www.php.net/manual/es/solrquery.getfacetoffset.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrquery/getfacetoffset.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_revision: '475439775'
order: 79170
---

SolrQuery::getFacetOffset

Devuelve un índice dentro de la lista de restricciones para ser usado en paginación

## Descripción

```php
public SolrQuery::getFacetOffset([string $field_override]): int
```php

Devuelve un índice dentro de la lista de restricciones para ser usado en paginación. Acepta una sobrescritura opcional de campos

## Parámetros

`field_override`  
El nombre del campo a sobrescribir.

## Valores devueltos

Devuelve un entero en caso de éxito y `null` si no se estableció
