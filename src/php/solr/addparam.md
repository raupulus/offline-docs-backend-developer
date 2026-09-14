---
title: SolrParams::addParam
description: Añade un parámetro al objeto
source_url: https://www.php.net/manual/es/solrparams.addparam.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrparams/addparam.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_revision: e41806c30
order: 78640
---

SolrParams::addParam

Añade un parámetro al objeto

## Descripción

```php
public SolrParams::addParam(string $name, string $value): SolrParams
```php

Añade un parámetro al objeto. Se usa para parámetros que pueden ser especificados múltiples veces.

## Parámetros

`name`  
Nombre del parámetro

`value`  
alor del parámetro

## Valores devueltos

Devuelve un objeto SolrParam an caso de éxito y `false` en caso de error.
