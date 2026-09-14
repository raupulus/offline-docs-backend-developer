---
title: tidy::isXml
description: Indica si el documento es XML (no HTML/XHTML)
source_url: https://www.php.net/manual/es/tidy.isxml.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/tidy/tidy/isxml.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: tidy
translation_status: ready
translation_revision: 2b84fa46e
order: 94120
---

tidy::isXml

tidy_is_xml

Indica si el documento es XML (no HTML/XHTML)

## Descripción

Estilo orientado a objetos

```php
public tidy::isXml(): bool
```php

Estilo procedimental

```php
tidy_is_xml(tidy $tidy): bool
```

Dice si el documento es un XML genérico (no HTML/XHTML).

## Parámetros

`tidy`  
El objeto `Tidy`

## Valores devueltos

Esta función devuelve `true` si el objeto `tidy` tidy especificado es un documento XML (no HTML/XHTML), o `false` de otra forma.

> [!WARNING]
> Esta función no está implementada aún en Tidylib, por lo que siempre devolverá `false`.
