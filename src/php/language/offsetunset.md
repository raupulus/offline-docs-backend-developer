---
title: ArrayAccess::offsetUnset
description: Destruye un offset
source_url: https://www.php.net/manual/es/arrayaccess.offsetunset.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: language/predefined/arrayaccess/offsetunset.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: language
translation_status: ready
translation_reviewed: false
translation_revision: ed312486f
order: 2850
---

ArrayAccess::offsetUnset

Destruye un offset

## Descripción

```php
public ArrayAccess::offsetUnset(mixed $offset): void
```php

Destruye un offset.

> [!NOTE]
> Este método *no* será llamado cuando se fuerza un tipo mediante [(unset)](#language.types.typecasting)

## Parámetros

`offset`  
El offset a destruir.

## Valores devueltos

No se retorna ningún valor.
