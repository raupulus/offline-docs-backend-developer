---
title: XMLDiff\DOM::merge
description: Produce DOMDocument unido
source_url: https://www.php.net/manual/es/xmldiff-dom.merge.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xmldiff/xmldiff-dom/merge.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xmldiff
translation_status: ready
translation_reviewed: false
translation_revision: e9366ee45
order: 102970
---

XMLDiff\DOM::merge

Produce DOMDocument unido

## Descripción

```php
public XMLDiff\DOM::merge(DOMDocument $src, DOMDocument $diff): DOMDocument
```php

Crear un nuevo DOMDocument basado en las diferencias.

## Parámetros

`src`  
Objeto fuente DOMDocument.

`diff`  
Objeto DOMDocument que contiene la información de diferencias.

## Valores devueltos

DOMDocument unido o NULL.
