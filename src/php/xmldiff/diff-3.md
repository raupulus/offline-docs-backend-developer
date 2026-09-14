---
title: XMLDiff\File::diff
description: Diferencia dos archivos XML
source_url: https://www.php.net/manual/es/xmldiff-file.diff.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xmldiff/xmldiff-file/diff.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xmldiff
translation_status: ready
translation_reviewed: false
translation_revision: e9366ee45
order: 102980
---

XMLDiff\File::diff

Diferencia dos archivos XML

## Descripción

```php
public XMLDiff\File::diff(string $from, string $to): string
```php

Diferencia dos archivos XML locales y produce una cadena con la información de diferenciación.

## Parámetros

`from`  
Ruta al documento fuente.

`to`  
Ruta al documento fuente.

## Valores devueltos

Cadena con el documento XML que contiene la información diferencial o NULL.
