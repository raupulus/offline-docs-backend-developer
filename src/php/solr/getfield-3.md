---
title: SolrInputDocument::getField
description: Recupera un campo por su nombre
source_url: https://www.php.net/manual/es/solrinputdocument.getfield.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrinputdocument/getfield.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_revision: e41806c30
order: 78390
---

SolrInputDocument::getField

Recupera un campo por su nombre

## Descripción

```php
public SolrInputDocument::getField(string $fieldName): SolrDocumentField
```php

Recupera un campo del documento.

## Parámetros

`fieldName`  
El nombre del campo.

## Valores devueltos

Devuelve un objeto SolrDocumentField en caso de éxito y `false` en caso de error.
