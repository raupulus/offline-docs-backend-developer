---
title: SolrInputDocument::getFieldBoost
description: Recupera el valor boost de un campo en particular
source_url: https://www.php.net/manual/es/solrinputdocument.getfieldboost.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrinputdocument/getfieldboost.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_revision: '475439775'
order: 78400
---

SolrInputDocument::getFieldBoost

Recupera el valor boost de un campo en particular

## Descripción

```php
public SolrInputDocument::getFieldBoost(string $fieldName): float
```php

Recupera el valor boost de un campo en particular.

## Parámetros

`fieldName`  
El nombre del campo.

## Valores devueltos

Devuelve el valor boost del campo o `false` si hubo un error.
