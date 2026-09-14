---
title: SolrQuery::setHighlight
description: Habilita o deshabilita la remarcación
source_url: https://www.php.net/manual/es/solrquery.sethighlight.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrquery/sethighlight.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_revision: b6e314781
order: 80280
---

SolrQuery::setHighlight

Habilita o deshabilita la remarcación

## Descripción

```php
public SolrQuery::setHighlight(bool $flag): SolrQuery
```php

Establecerlo a `true` habilita los trozos remarcados para ser generados en la respuesta de consulta.

Establecerlo a `false` deshabilita la remarcación

## Parámetros

`flag`  
Habilita o deshabilita la remarcación

## Valores devueltos

Devuelve el objeto SolrQuery actual, si se usó el valor de retorno.
