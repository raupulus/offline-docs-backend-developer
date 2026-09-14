---
title: SolrQuery::setMltMinDocFrequency
description: Establece la frecuencia de mltMinDoc
source_url: https://www.php.net/manual/es/solrquery.setmltmindocfrequency.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrquery/setmltmindocfrequency.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_revision: b6e314781
order: 80520
---

SolrQuery::setMltMinDocFrequency

Establece la frecuencia de mltMinDoc

## Descripción

```php
public SolrQuery::setMltMinDocFrequency(int $minDocFrequency): SolrQuery
```php

La frecuencia en la que las palabras que no ocurran en por lo menos tantos documentos como este serán ignoradas.

## Parámetros

`minDocFrequency`  
Establece la frecuencia en la que las palabras que no ocurran en por lo menos tantos documentos como este serán ignoradas.

## Valores devueltos

Devuelve el objeto SolrQuery actual, si se usó el valor de retorno.
