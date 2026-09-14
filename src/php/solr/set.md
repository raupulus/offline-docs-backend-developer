---
title: SolrDocument::__set
description: Añade otro campo al documento
source_url: https://www.php.net/manual/es/solrdocument.set.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/solr/solrdocument/set.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: solr
translation_status: ready
translation_revision: 734ddd27a
order: 78080
---

SolrDocument::\_\_set

Añade otro campo al documento

## Descripción

```php
public SolrDocument::__set(string $fieldName, string $fieldValue): bool
```php

Añade otro campo al documento. Se usa para establecer el campo como propiedades nuevas.

## Parámetros

`fieldName`  
Nombre del campo.

`fieldValue`  
Valor del campo.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.
