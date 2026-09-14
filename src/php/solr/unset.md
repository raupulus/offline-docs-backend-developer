---
title: SolrDocument::__unset
description: Elimina un campo del documento
source_url: https://www.php.net/manual/es/solrdocument.unset.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrdocument/unset.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_revision: 734ddd27a
order: 78120
---

SolrDocument::\_\_unset

Elimina un campo del documento

## Descripción

```php
public SolrDocument::__unset(string $fieldName): bool
```php

Elimina un campo del documento cuando al campo se accede como una propiedad del objeto.

## Parámetros

`fieldName`  
El nombre del campo.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.
