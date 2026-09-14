---
title: SolrQuery::setHighlightQuery
description: Una consulta designada para la resaltación (hl.q)
source_url: https://www.php.net/manual/es/solrquery.sethighlightquery.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrquery/sethighlightquery.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_reviewed: true
translation_revision: 1d92acb7a
order: 80370
---

SolrQuery::setHighlightQuery

Una consulta designada para la resaltación (hl.q)

## Descripción

```php
public SolrQuery::setHighlightQuery(string $q): SolrQuery
```php

Una consulta a utilizar para la resaltación. Este parámetro permite resaltar términos o campos diferentes de los utilizados para recuperar los documentos.

El valor por omisión si no está definido: el valor del parámetro q de la consulta

Referencia del parámetro Solr: hl.q

## Parámetros

`q`  
La consulta de resaltación

## Valores devueltos

Devuelve el objeto `SolrQuery` actual, si el valor devuelto es utilizado.
