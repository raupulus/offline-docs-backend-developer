---
title: SolrQuery::setHighlightFormatter
description: Especifica un formateador para la salida resaltada
source_url: https://www.php.net/manual/es/solrquery.sethighlightformatter.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrquery/sethighlightformatter.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_reviewed: false
translation_revision: d00128a85
order: 80300
---

SolrQuery::setHighlightFormatter

Especifica un formateador para la salida resaltada

## Descripción

```php
public SolrQuery::setHighlightFormatter(string $formatter, [string $field_override]): SolrQuery
```php

Especifica un formateador para la salida resaltada.

## Parámetros

`formatter`  
Actualmente, el único valor es "simple".

`field_override`  
El nombre del campo.

## Valores devueltos

Devuelve una instancia de `SolrQuery`.
