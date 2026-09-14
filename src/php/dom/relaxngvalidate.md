---
title: DOMDocument::relaxNGValidate
description: Realiza una validación relaxNG del documento
source_url: https://www.php.net/manual/es/domdocument.relaxngvalidate.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domdocument/relaxngvalidate.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_revision: 4f5e2b225
order: 13210
---

DOMDocument::relaxNGValidate

Realiza una validación relaxNG del documento

## Descripción

```php
public DOMDocument::relaxNGValidate(string $filename): bool
```php

Realiza una validación [relaxNG](http://www.relaxng.org/) del documento basándose en el esquema RNG dado.

## Parámetros

`filename`  
El fichero RNG.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

DOMDocument::relaxNGValidateSource, DOMDocument::schemaValidate, DOMDocument::schemaValidateSource, DOMDocument::validate
