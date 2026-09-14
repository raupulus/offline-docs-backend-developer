---
title: SolrQuery::setMltMaxNumTokens
description: Especifica el número máximo de tokens a analizar
source_url: https://www.php.net/manual/es/solrquery.setmltmaxnumtokens.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrquery/setmltmaxnumtokens.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_revision: b6e314781
order: 80500
---

SolrQuery::setMltMaxNumTokens

Especifica el número máximo de tokens a analizar

## Descripción

```php
public SolrQuery::setMltMaxNumTokens(int $value): SolrQuery
```php

Especifica el número máximo de tokens a analizar en cada campo de documento de ejemplo que no esté almacenado con soporte TermVector.

## Parámetros

`value`  
El número máximo de tokens a analizar

## Valores devueltos

Devuelve el objeto SolrQuery actual, si se usó el valor de retorno.
