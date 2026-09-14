---
title: SolrQuery::getHighlightMaxAlternateFieldLength
description: Devuelve el número máximo de caracteres del campo a devolver
source_url: https://www.php.net/manual/es/solrquery.gethighlightmaxalternatefieldlength.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrquery/gethighlightmaxalternatefieldlength.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_revision: '475439775'
order: 79430
---

SolrQuery::getHighlightMaxAlternateFieldLength

Devuelve el número máximo de caracteres del campo a devolver

## Descripción

```php
public SolrQuery::getHighlightMaxAlternateFieldLength([string $field_override]): int
```php

Devuelve el número máximo de caracteres del campo a devolver

## Parámetros

`field_override`  
El nombre del campo

## Valores devueltos

Devuelve un entero en caso de éxito y `null` si no se estableció.
