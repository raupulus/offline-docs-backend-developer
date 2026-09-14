---
title: SolrQuery::setHighlightHighlightMultiTerm
description: Usa SpanScorer para remarcar términos de frases
source_url: https://www.php.net/manual/es/solrquery.sethighlighthighlightmultiterm.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrquery/sethighlighthighlightmultiterm.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_revision: b6e314781
order: 80330
---

SolrQuery::setHighlightHighlightMultiTerm

Usa SpanScorer para remarcar términos de frases

## Descripción

```php
public SolrQuery::setHighlightHighlightMultiTerm(bool $flag): SolrQuery
```php

Usa SpanScorer para remarcar términos de frases sólo cuando aparecen dentro de la frase de consulta del documento.

## Parámetros

`flag`  
Si usar o no SpanScorer para remarcar términos de frases sólo cuando aparecen dentro de la frase de consulta del documento.

## Valores devueltos

Devuelve el objeto SolrQuery actual, si se usó el valor de retorno.
