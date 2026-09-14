---
title: SolrDocument::offsetExists
description: Comprueba si existe un campo en particular
source_url: https://www.php.net/manual/es/solrdocument.offsetexists.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrdocument/offsetexists.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_revision: 734ddd27a
order: 78010
---

SolrDocument::offsetExists

Comprueba si existe un campo en particular

## Descripción

```php
public SolrDocument::offsetExists(string $fieldName): bool
```php

Comprueba si existe un campo en particular. Se usa cuando un objeto es tratado como una matriz.

## Parámetros

`fieldName`  
El nombre del campo.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.
