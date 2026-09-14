---
title: SolrQuery::getHighlightSimplePost
description: Devuelve el texto que aparece después de un término remarcado
source_url: https://www.php.net/manual/es/solrquery.gethighlightsimplepost.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrquery/gethighlightsimplepost.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_revision: '475439775'
order: 79510
---

SolrQuery::getHighlightSimplePost

Devuelve el texto que aparece después de un término remarcado

## Descripción

```php
public SolrQuery::getHighlightSimplePost([string $field_override]): string
```php

Devuelve el texto que aparece después de un término remarcado. Acepta una sobrescritura opcional de campos

## Parámetros

`field_override`  
El nombre del campo

## Valores devueltos

Devuelve una cadena en caso de éxito y `null` si no se estableció.
