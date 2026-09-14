---
title: SolrQuery::setHighlightRequireFieldMatch
description: Requerir la coincicencia de campos durante el remarcado
source_url: https://www.php.net/manual/es/solrquery.sethighlightrequirefieldmatch.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrquery/sethighlightrequirefieldmatch.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_revision: b6e314781
order: 80410
---

SolrQuery::setHighlightRequireFieldMatch

Requerir la coincicencia de campos durante el remarcado

## Descripción

```php
public SolrQuery::setHighlightRequireFieldMatch(bool $flag): SolrQuery
```php

Si es `true`, un campo sólo será remarcado si la consulta coincide con este campo en particular.

Esto sólo funciona si SolrQuery::setHighlightUsePhraseHighlighter() se estableció a `true`

## Parámetros

`flag`  
`true` o `false`

## Valores devueltos

Devuelve el objeto SolrQuery actual, si se usó el valor de retorno.
