---
title: tidy::isXhtml
description: Indica si el documento es XHTML
source_url: https://www.php.net/manual/es/tidy.isxhtml.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/tidy/tidy/isxhtml.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: tidy
translation_status: ready
translation_revision: 2b84fa46e
order: 94110
---

tidy::isXhtml

tidy_is_xhtml

Indica si el documento es XHTML

## Descripción

Estilo orientado a objetos

```php
public tidy::isXhtml(): bool
```php

Estilo procedimental

```php
tidy_is_xhtml(tidy $tidy): bool
```

Dice si el documento es XHTML.

## Parámetros

`tidy`  
El objeto `Tidy`

## Valores devueltos

Esta función devuelve `true` si el objeto `tidy` tidy especificado es XHTML, o `false` de otra forma.

> [!WARNING]
> Esta función no está implementada aún en Tidylib, por lo que siempre devolverá `false`.
