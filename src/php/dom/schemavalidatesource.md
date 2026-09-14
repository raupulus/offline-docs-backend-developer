---
title: DOMDocument::schemaValidateSource
description: Valida un documento basado en un esquema
source_url: https://www.php.net/manual/es/domdocument.schemavalidatesource.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/dom/domdocument/schemavalidatesource.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: dom
translation_status: ready
translation_reviewed: false
translation_revision: 4f5e2b225
order: 13290
---

DOMDocument::schemaValidateSource

Valida un documento basado en un esquema

## Descripción

```php
public DOMDocument::schemaValidateSource(string $source, [int $flags]): bool
```php

Valida un documento basado en un esquema definido en la cadena dada.

## Parámetros

`source`  
Una cadena que contiene el esquema.

`flags`  
Una máscara de bits de banderas de validación de esquemas de Libxml. Actualmente el único valor admitido es [LIBXML_SCHEMA_CREATE](#libxml.constants). Disponible desde Libxml 2.6.14.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Véase también

DOMDocument::schemaValidate, DOMDocument::relaxNGValidate, DOMDocument::relaxNGValidateSource, DOMDocument::validate
