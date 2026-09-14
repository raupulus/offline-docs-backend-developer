---
title: SolrQuery::setHighlightFragmenter
description: Establece el generador de trozos de código para texto remarcado
source_url: https://www.php.net/manual/es/solrquery.sethighlightfragmenter.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrquery/sethighlightfragmenter.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_revision: b6e314781
order: 80310
---

SolrQuery::setHighlightFragmenter

Establece el generador de trozos de código para texto remarcado

## Descripción

```php
public SolrQuery::setHighlightFragmenter(string $fragmenter, [string $field_override]): SolrQuery
```php

Especifica un generador de trozos de código para texto remarcado.

## Parámetros

`fragmenter`  
El fragmentador estándar es el hueco. Otra opción son las expresiones regulares, que intentan crear fragmentos que se parecen a ciertas expresiones regulares

`field_override`  
El nombre del campo.

## Valores devueltos

Devuelve el objeto SolrQuery actual, si se usó el valor de retorno.
