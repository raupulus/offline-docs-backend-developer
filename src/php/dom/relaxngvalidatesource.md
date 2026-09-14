---
title: DOMDocument::relaxNGValidateSource
description: Realiza una validación relaxNG del documento
source_url: https://www.php.net/manual/es/domdocument.relaxngvalidatesource.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domdocument/relaxngvalidatesource.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: 4f5e2b225
order: 13220
---

DOMDocument::relaxNGValidateSource

Realiza una validación relaxNG del documento

## Descripción

```php
public DOMDocument::relaxNGValidateSource(string $source): bool
```php

Realiza una validación [relaxNG](http://www.relaxng.org/) del documento basándose en la fuente RNG dada.

## Parámetros

`source`  
Una cadena que contiene el esquema RNG.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

DOMDocument::relaxNGValidate, DOMDocument::schemaValidate, DOMDocument::schemaValidateSource, DOMDocument::validate
