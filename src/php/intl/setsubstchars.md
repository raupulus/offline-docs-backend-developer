---
title: UConverter::setSubstChars
description: Define los caracteres de sustitución
source_url: https://www.php.net/manual/es/uconverter.setsubstchars.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/uconverter/setsubstchars.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: 1976eae0d
order: 42780
---

UConverter::setSubstChars

Define los caracteres de sustitución

## Descripción

```php
public UConverter::setSubstChars(string $chars): bool
```php

Este método permite establecer los caracteres de sustitución que serán utilizados cuando no sea posible representar un carácter en el conjunto de caracteres de destino.

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

`chars`  
El argumento `chars` debe ser un string que contenga los caracteres de sustitución.

## Valores devueltos

Este método devuelve `TRUE` en caso de éxito y `FALSE` en caso de error.
