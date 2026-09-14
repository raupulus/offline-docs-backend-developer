---
title: SolrQuery::setHighlightUsePhraseHighlighter
description: Si remarcar o no términos de frases sólo cuando aparecen en la frase
  de consulta
source_url: https://www.php.net/manual/es/solrquery.sethighlightusephrasehighlighter.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrquery/sethighlightusephrasehighlighter.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_revision: b6e314781
order: 80450
---

SolrQuery::setHighlightUsePhraseHighlighter

Si remarcar o no términos de frases sólo cuando aparecen en la frase de consulta

## Descripción

```php
public SolrQuery::setHighlightUsePhraseHighlighter(bool $flag): SolrQuery
```php

Establece si usar o no SpanScorer para remarcar o no términos de frases sólo cuando aparecen en la frase de consulta del documento

## Parámetros

`value`  
Si usar o no SpanScorer para remarcar o no términos de frases sólo cuando aparecen en la frase de consulta del documento

## Valores devueltos

Devuelve el objeto SolrQuery actual, si se usó el valor de retorno.
