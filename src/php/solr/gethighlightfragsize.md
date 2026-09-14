---
title: SolrQuery::getHighlightFragsize
description: Devuelve el número de caracteres de fragmentos a considerar para remarcación
source_url: https://www.php.net/manual/es/solrquery.gethighlightfragsize.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrquery/gethighlightfragsize.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_revision: '475439775'
order: 79410
---

SolrQuery::getHighlightFragsize

Devuelve el número de caracteres de fragmentos a considerar para remarcación

## Descripción

```php
public SolrQuery::getHighlightFragsize([string $field_override]): int
```php

Devuelve el número de caracteres de fragmentos a considerar para remarcación. Cero implica que no hay fragmentos. Debería usarse el camplo completo.

## Parámetros

`field_override`  
El nombre del campo

## Valores devueltos

Devuelve un entero en caso de éxito o `null` si no se estableció
