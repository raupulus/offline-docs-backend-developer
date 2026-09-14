---
title: SolrQuery::getHighlightMergeContiguous
description: Devuelve si colapsar o no fragmentos contiguos en un único fragmento
source_url: https://www.php.net/manual/es/solrquery.gethighlightmergecontiguous.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrquery/gethighlightmergecontiguous.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_revision: '475439775'
order: 79450
---

SolrQuery::getHighlightMergeContiguous

Devuelve si colapsar o no fragmentos contiguos en un único fragmento

## Descripción

```php
public SolrQuery::getHighlightMergeContiguous([string $field_override]): bool
```php

Devuelve si colapsar o no fragmentos contiguos en un único fragmento. Acepta una sobrescritura opcional de campos.

## Parámetros

`field_override`  
El nombre del campo

## Valores devueltos

Devuelve un booleano en caso de éxito y `null` si no se estableció.
