---
title: Transliterator::getErrorCode
description: Obtiene el último código de error
source_url: https://www.php.net/manual/es/transliterator.geterrorcode.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/transliterator/geterrorcode.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: f7f861700
order: 42570
---

Transliterator::getErrorCode

transliterator_get_error_code

Obtiene el último código de error

## Descripción

Estilo orientado a objetos

```php
public Transliterator::getErrorCode(): int
```php

Estilo procedimental

```php
transliterator_get_error_code(Transliterator $transliterator): int
```

Obtiene el último código de error desde este transliterador.

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

`transliterator`  

## Valores devueltos

El código de error en caso de éxito, o `false` si no existe o si ocurre un error.

## Véase también

Transliterator::getErrorMessage, Transliterator::listIDs
