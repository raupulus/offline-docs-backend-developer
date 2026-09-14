---
title: XMLDiff\File::merge
description: Produce un documento XML unido
source_url: https://www.php.net/manual/es/xmldiff-file.merge.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xmldiff/xmldiff-file/merge.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xmldiff
translation_status: ready
translation_reviewed: false
translation_revision: e9366ee45
order: 102990
---

XMLDiff\File::merge

Produce un documento XML unido

## Descripción

```php
public XMLDiff\File::merge(string $src, string $diff): string
```php

Crea un nuevo documento XML basado en diferencias y documento fuente.

## Parámetros

`src`  
Ruta al documento XML de origen.

`diff`  
Ruta al documento XML con la información de diferencia.

## Valores devueltos

Cadena con el nuevo documento XML o NULL.
