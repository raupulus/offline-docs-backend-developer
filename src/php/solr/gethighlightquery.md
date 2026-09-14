---
title: SolrQuery::getHighlightQuery
description: Devuelve la consulta de resaltado (hl.q)
source_url: https://www.php.net/manual/es/solrquery.gethighlightquery.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrquery/gethighlightquery.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_reviewed: true
translation_revision: 45819f24a
order: 79460
---

SolrQuery::getHighlightQuery

Devuelve la consulta de resaltado (hl.q)

## Descripción

```php
public SolrQuery::getHighlightQuery(): string
```php

Devuelve la consulta de resaltado previamente definida. Este parámetro permite resaltar términos o campos diferentes de los utilizados para recuperar los documentos.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve la cadena de consulta de resaltado actual, o null si no está definida.
