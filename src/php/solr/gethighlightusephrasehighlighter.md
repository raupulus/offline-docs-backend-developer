---
title: SolrQuery::getHighlightUsePhraseHighlighter
description: Devuelve el estado del parámetro hl.usePhraseHighlighter
source_url: https://www.php.net/manual/es/solrquery.gethighlightusephrasehighlighter.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrquery/gethighlightusephrasehighlighter.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_revision: '475439775'
order: 79540
---

SolrQuery::getHighlightUsePhraseHighlighter

Devuelve el estado del parámetro hl.usePhraseHighlighter

## Descripción

```php
public SolrQuery::getHighlightUsePhraseHighlighter(): bool
```php

Devuelve si usar o no SpanScorer para remarcar términos de frases sólo cuando aparezcan dentro de la frase de consulta en el documento.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve un booleano en caso de éxito y `null` si no se estableció.
