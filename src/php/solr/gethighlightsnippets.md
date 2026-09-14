---
title: SolrQuery::getHighlightSnippets
description: Devuelve el número máximo de trozos remarcados a generar por campo
source_url: https://www.php.net/manual/es/solrquery.gethighlightsnippets.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrquery/gethighlightsnippets.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_revision: '475439775'
order: 79530
---

SolrQuery::getHighlightSnippets

Devuelve el número máximo de trozos remarcados a generar por campo

## Descripción

```php
public SolrQuery::getHighlightSnippets([string $field_override]): int
```php

Devuelve el número máximo de trozos remarcados a generar por campo. Acepta una sobrescritura opcional de campos

## Parámetros

`field_override`  
El nombre del campo

## Valores devueltos

Devuelve un entero en caso de éxito y `null` si no se estableció.
