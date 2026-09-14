---
title: XMLDiff\Base::diff
description: Produce diferencias de dos documentos XML
source_url: https://www.php.net/manual/es/xmldiff-base.diff.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/xmldiff/xmldiff-base/diff.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: xmldiff
translation_status: ready
translation_reviewed: false
translation_revision: e9366ee45
order: 102940
---

XMLDiff\Base::diff

Produce diferencias de dos documentos XML

## Descripción

```php
abstract public XMLDiff\Base::diff(mixed $from, mixed $to): mixed
```php

Método abstracto diferencial para ser aplicado por las clases hereditarias.

El propósito básico de este método es producir diferencias entre dos documentos. El orden paramétrico importa y producirá diferentes resultados.

## Parámetros

`from`  
Documento fuente XML.

`to`  
Documento XML de destino.

## Valores devueltos

Depende de la implementación.
