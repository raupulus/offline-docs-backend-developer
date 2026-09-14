---
title: SolrQuery::setStart
description: Especifica el número de filas que se van a saltar
source_url: https://www.php.net/manual/es/solrquery.setstart.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrquery/setstart.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_revision: b6e314781
order: 80590
---

SolrQuery::setStart

Especifica el número de filas que se van a saltar

## Descripción

```php
public SolrQuery::setStart(int $start): SolrQuery
```php

Especifica el número de filas que se van a saltar. Útil en paginación de resultados.

## Parámetros

`start`  
El número de filas a saltar.

## Valores devueltos

Devuelve el objeto SolrQuery actual.
