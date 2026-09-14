---
title: SolrQuery::setHighlightMaxAlternateFieldLength
description: Establece el número máximo de caracteres del campo a devolver
source_url: https://www.php.net/manual/es/solrquery.sethighlightmaxalternatefieldlength.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrquery/sethighlightmaxalternatefieldlength.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_revision: b6e314781
order: 80340
---

SolrQuery::setHighlightMaxAlternateFieldLength

Establece el número máximo de caracteres del campo a devolver

## Descripción

```php
public SolrQuery::setHighlightMaxAlternateFieldLength(int $fieldLength, [string $field_override]): SolrQuery
```php

Si SolrQuery::setHighlightAlternateField() se le pasó el valor `true`, este parámetro especifica el número máximo de caracteres del campo a devolver

Cualquier valor menor o igual que 0 significa ilimitado.

## Parámetros

`fieldLength`  
La longitud del campo

`field_override`  
El nombre del campo.

## Valores devueltos

Devuelve el objeto SolrQuery actual, si se usó el valor de retorno.
