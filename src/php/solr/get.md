---
title: SolrDocument::__get
description: Acceder al campo como una propiedad
source_url: https://www.php.net/manual/es/solrdocument.get.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrdocument/get.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_reviewed: false
translation_revision: 33040b3b1
order: 77890
---

SolrDocument::\_\_get

Acceder al campo como una propiedad

## Descripción

```php
public SolrDocument::__get(string $fieldName): SolrDocumentField
```php

Método mágico para acceder al campo como si fuera una propiedad.

## Parámetros

`fieldName`  
El nombre del campo.

## Valores devueltos

Devuelve una instancia de SolrDocumentField.
