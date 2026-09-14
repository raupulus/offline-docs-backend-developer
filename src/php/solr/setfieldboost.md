---
title: SolrInputDocument::setFieldBoost
description: Establece el valor boost de tiempo del índice de un campo
source_url: https://www.php.net/manual/es/solrinputdocument.setfieldboost.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrinputdocument/setfieldboost.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_revision: d00128a85
order: 78470
---

SolrInputDocument::setFieldBoost

Establece el valor boost de tiempo del índice de un campo

## Descripción

```php
public SolrInputDocument::setFieldBoost(string $fieldName, float $fieldBoostValue): bool
```php

Establece el valor boost de tiempo del índice de un campo. Esto reemplaza el valor boost acutal de este campo.

## Parámetros

`fieldName`  
El nombre del campo.

`fieldBoostValue`  
El valor boost de tiempo del índice.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.
