---
title: XMLDiff\Base::merge
description: Produce un nuevo documento XML basado en diferencias
source_url: https://www.php.net/manual/es/xmldiff-base.merge.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xmldiff/xmldiff-base/merge.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xmldiff
translation_status: ready
translation_reviewed: false
translation_revision: e9366ee45
order: 102950
---

XMLDiff\Base::merge

Produce un nuevo documento XML basado en diferencias

## Descripción

```php
abstract public XMLDiff\Base::merge(mixed $src, mixed $diff): mixed
```php

Método de fusión abstracta para ser implementado por las clases hereditarias.

Básicamente el propósito del método es producir un nuevo documento XML basado en la información diferencial.

## Parámetros

`src`  
Documento fuente XML.

`diff`  
Documento producido por el método diferencial.

## Valores devueltos

Depende de la implementación.
