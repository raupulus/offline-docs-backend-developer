---
title: XMLDiff\Memory::diff
description: Diferenciar dos documentos XML
source_url: https://www.php.net/manual/es/xmldiff-memory.diff.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xmldiff/xmldiff-memory/diff.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xmldiff
translation_status: ready
translation_reviewed: false
translation_revision: e9366ee45
order: 103000
---

XMLDiff\Memory::diff

Diferenciar dos documentos XML

## Descripción

```php
public XMLDiff\Memory::diff(string $from, string $to): string
```php

Diferenciar dos cadenas que contienen documentos XML y producir la información diferencial.

## Parámetros

`from`  
Documento fuente XML.

`to`  
Documento XML de destino.

## Valores devueltos

Cadena con el documento XML que contiene la información del diferencia o NULL.
