---
title: SolrQuery::setHighlightSimplePost
description: Define el texto que debe aparecer después de un término resaltado
source_url: https://www.php.net/manual/es/solrquery.sethighlightsimplepost.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrquery/sethighlightsimplepost.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_reviewed: false
translation_revision: d00128a85
order: 80420
---

SolrQuery::setHighlightSimplePost

Define el texto que debe aparecer después de un término resaltado

## Descripción

```php
public SolrQuery::setHighlightSimplePost(string $simplePost, [string $field_override]): SolrQuery
```php

Define el texto que debe aparecer después de un término resaltado.

## Parámetros

`simplePost`  
Define el texto que debe aparecer después de un término resaltado.

El valor por omisión es \</em\>

`field_override`  
El nombre del campo.

## Valores devueltos

Devuelve una instancia de `SolrQuery`.
