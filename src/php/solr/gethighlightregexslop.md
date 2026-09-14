---
title: SolrQuery::getHighlightRegexSlop
description: Devuelve el factor de desviación del tamaño de fragmento ideal
source_url: https://www.php.net/manual/es/solrquery.gethighlightregexslop.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrquery/gethighlightregexslop.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_revision: 19e812213
order: 79490
---

SolrQuery::getHighlightRegexSlop

Devuelve el factor de desviación del tamaño de fragmento ideal

## Descripción

```php
public SolrQuery::getHighlightRegexSlop(): float
```php

Devuelve el factor por el que el fragmentador de expresiones regulares puede desviar desde el tamaño de fragmeto ideal para acomodar la expresión regular

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un `float` en caso de éxito y `null` si no se estableció.
