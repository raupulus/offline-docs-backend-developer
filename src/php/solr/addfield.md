---
title: SolrDocument::addField
description: añade un campo al documento
source_url: https://www.php.net/manual/es/solrdocument.addfield.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrdocument/addfield.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_revision: 734ddd27a
order: 77810
---

SolrDocument::addField

añade un campo al documento

## Descripción

```php
public SolrDocument::addField(string $fieldName, string $fieldValue): bool
```php

Este método añade un campo a la instancia de SolrDocument.

## Parámetros

`fieldName`  
El nombre del campo

`fieldValue`  
El valor del campo.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.
