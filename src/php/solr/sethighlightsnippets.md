---
title: SolrQuery::setHighlightSnippets
description: Establece el número máximo de trozos remarcados para generar por campo
source_url: https://www.php.net/manual/es/solrquery.sethighlightsnippets.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrquery/sethighlightsnippets.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_revision: b6e314781
order: 80440
---

SolrQuery::setHighlightSnippets

Establece el número máximo de trozos remarcados para generar por campo

## Descripción

```php
public SolrQuery::setHighlightSnippets(int $value, [string $field_override]): SolrQuery
```php

Establece el número máximo de trozos remarcados para generar por campo

## Parámetros

`value`  
El número máximo de trozos remarcados para generar por campo

`field_override`  
El nombre del campo.

## Valores devueltos

Devuelve el objeto SolrQuery actual, si se usó el valor de retorno.
