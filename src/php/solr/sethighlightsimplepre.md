---
title: SolrQuery::setHighlightSimplePre
description: Establece el texto que aparece antes de un término remarcado
source_url: https://www.php.net/manual/es/solrquery.sethighlightsimplepre.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrquery/sethighlightsimplepre.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_revision: b6e314781
order: 80430
---

SolrQuery::setHighlightSimplePre

Establece el texto que aparece antes de un término remarcado

## Descripción

```php
public SolrQuery::setHighlightSimplePre(string $simplePre, [string $field_override]): SolrQuery
```php

Establece el texto que aparece antes de un término remarcado.

El valor por omisión es \<em\>

## Parámetros

`simplePre`  
El texto que aparece antes de un término remarcado

`field_override`  
El nombre del campo.

## Valores devueltos

Devuelve el objeto SolrQuery actual, si se usó el valor de retorno.
