---
title: SolrDocument::offsetGet
description: Recupera un campo
source_url: https://www.php.net/manual/es/solrdocument.offsetget.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrdocument/offsetget.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_revision: 734ddd27a
order: 78020
---

SolrDocument::offsetGet

Recupera un campo

## Descripción

```php
public SolrDocument::offsetGet(string $fieldName): SolrDocumentField
```php

Se usa para recuperar un campo cuando el objeto es tratado como una matriz.

## Parámetros

`fieldName`  
El nombre del campo.

## Valores devueltos

Devuelve un objeto SolrDocumentField.
