---
title: SolrQuery::addSortField
description: Usado para controlar cómo deberían ordenarse los resultados
source_url: https://www.php.net/manual/es/solrquery.addsortfield.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrquery/addsortfield.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_revision: b6e314781
order: 78940
---

SolrQuery::addSortField

Usado para controlar cómo deberían ordenarse los resultados

## Descripción

```php
public SolrQuery::addSortField(string $field, [int $order]): SolrQuery
```php

Usado para controlar cómo deberían ordenarse los resultados.

## Parámetros

`field`  
El nombre del campo

`order`  
La dirección de ordenación. Debería ser SolrQuery::ORDER_ASC o SolrQuery::ORDER_DESC.

## Valores devueltos

Devuelve el objeto SolrQuery actual.
