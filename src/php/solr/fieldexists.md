---
title: SolrDocument::fieldExists
description: Comprueba si existe un campo en el documento
source_url: https://www.php.net/manual/es/solrdocument.fieldexists.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrdocument/fieldexists.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_revision: 734ddd27a
order: 77880
---

SolrDocument::fieldExists

Comprueba si existe un campo en el documento

## Descripción

```php
public SolrDocument::fieldExists(string $fieldName): bool
```php

Comprueba si el campo solicitado es un nombre de campo válido del documento.

## Parámetros

`fieldName`  
El nombre del campo.

## Valores devueltos

Devuelve `true` si el campo está presente y `false` si no lo está.
