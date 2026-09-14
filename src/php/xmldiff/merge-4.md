---
title: XMLDiff\Memory::merge
description: Produce un documento XML unido
source_url: https://www.php.net/manual/es/xmldiff-memory.merge.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xmldiff/xmldiff-memory/merge.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xmldiff
translation_status: ready
translation_reviewed: false
translation_revision: e9366ee45
order: 103010
---

XMLDiff\Memory::merge

Produce un documento XML unido

## Descripción

```php
public XMLDiff\Memory::merge(string $src, string $diff): string
```php

Crear un nuevo documento XML basado en diferencias y documento fuente.

## Parámetros

`src`  
Documento fuente XML.

`diff`  
Documento XML que contiene información de diferencias.

## Valores devueltos

Cadena con el nuevo documento XML o NULL.
