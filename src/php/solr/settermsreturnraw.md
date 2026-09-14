---
title: SolrQuery::setTermsReturnRaw
description: Devuelve los caracteres en bruto del término indexado
source_url: https://www.php.net/manual/es/solrquery.settermsreturnraw.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrquery/settermsreturnraw.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_revision: b6e314781
order: 80700
---

SolrQuery::setTermsReturnRaw

Devuelve los caracteres en bruto del término indexado

## Descripción

```php
public SolrQuery::setTermsReturnRaw(bool $flag): SolrQuery
```php

Si es true, devuelve los caracteres en bruto del término indexado, sin tener en cuenta si es legible por humanos.

## Parámetros

`value`  
`true` o `false`

## Valores devueltos

Devuelve el objeto SolrQuery actual, si se usó el valor de retorno.
