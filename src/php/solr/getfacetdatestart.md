---
title: SolrQuery::getFacetDateStart
description: Devuelve el límite inferior del primer rango de datos para todas las
  facetas de fecha de este campo
source_url: https://www.php.net/manual/es/solrquery.getfacetdatestart.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrquery/getfacetdatestart.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_revision: '475439775'
order: 79110
---

SolrQuery::getFacetDateStart

Devuelve el límite inferior del primer rango de datos para todas las facetas de fecha de este campo

## Descripción

```php
public SolrQuery::getFacetDateStart([string $field_override]): string
```php

Devuelve el límite inferior del primer rango de datos para todas las facetas de fecha de este campo. Acepta una sobrescritura opcional de campos

## Parámetros

`field_override`  
El nombre del campo

## Valores devueltos

Devuelve una cadena en caso de éxito y `null` si no se estableció
