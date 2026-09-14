---
title: SolrQuery::setHighlightFragsize
description: El tamaño de los fragmentos a considerara para remarcación
source_url: https://www.php.net/manual/es/solrquery.sethighlightfragsize.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrquery/sethighlightfragsize.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_revision: b6e314781
order: 80320
---

SolrQuery::setHighlightFragsize

El tamaño de los fragmentos a considerara para remarcación

## Descripción

```php
public SolrQuery::setHighlightFragsize(int $size, [string $field_override]): SolrQuery
```php

Establece el tamaño, en caracteres, de los fragmentos a considerara para remarcación. "0" indica que debería usarse el campo completo (sin fragmentación).

## Parámetros

`size`  
El tamaño, en caracteres, de los fragmentos a considerara para remarcación

`field_override`  
El nombre del campo.

## Valores devueltos

Devuelve el objeto SolrQuery actual, si se usó el valor de retorno.
