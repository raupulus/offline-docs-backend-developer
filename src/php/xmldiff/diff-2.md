---
title: XMLDiff\DOM::diff
description: Diferencia dos objetos DOMDocument
source_url: https://www.php.net/manual/es/xmldiff-dom.diff.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xmldiff/xmldiff-dom/diff.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xmldiff
translation_status: ready
translation_reviewed: false
translation_revision: e9366ee45
order: 102960
---

XMLDiff\DOM::diff

Diferencia dos objetos DOMDocument

## Descripción

```php
public XMLDiff\DOM::diff(DOMDocument $from, DOMDocument $to): DOMDocument
```php

Diferencia dos instancias de DOMDocument y produce la nueva que contiene la información de la diferencia.

## Parámetros

`from`  
Fuente del objeto DOMDocument.

`to`  
Objeto de destino DOMDocument.

## Valores devueltos

DOMDocument con la información de diferencia o NULL.
