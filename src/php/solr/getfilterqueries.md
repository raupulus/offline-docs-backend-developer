---
title: SolrQuery::getFilterQueries
description: Devuelve una matriz de consultas de filtro
source_url: https://www.php.net/manual/es/solrquery.getfilterqueries.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrquery/getfilterqueries.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_revision: '475439775'
order: 79220
---

SolrQuery::getFilterQueries

Devuelve una matriz de consultas de filtro

## Descripción

```php
public SolrQuery::getFilterQueries(): array
```php

Devuelve una matriz de consultas de filtro. Éstas son consultas que se pueden usar para restringir el superconjunto de documentos que pueden ser devueltos, sin influenciar en el resutlado

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve una matriz en caso de éxito y `null` si no se estableció.
