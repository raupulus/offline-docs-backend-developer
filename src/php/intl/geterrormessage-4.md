---
title: Transliterator::getErrorMessage
description: Obtiene el último mensaje de error
source_url: https://www.php.net/manual/es/transliterator.geterrormessage.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/intl/transliterator/geterrormessage.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: intl
translation_status: ready
translation_reviewed: false
translation_revision: f7f861700
order: 42580
---

Transliterator::getErrorMessage

transliterator_get_error_message

Obtiene el último mensaje de error

## Descripción

Estilo orientado a objetos

```php
public Transliterator::getErrorMessage(): string
```php

Estilo procedimental

```php
transliterator_get_error_message(Transliterator $transliterator): string
```

Obtiene el último mensaje de error desde este transliterador.

> [!WARNING]
> Esta función está actualmente no documentada; solo la lista de sus argumentos está disponible.

## Parámetros

`transliterator`  

## Valores devueltos

El mensaje de error en caso de éxito, o `false` si no existe ningún error, o si ocurre un error.

## Véase también

Transliterator::getErrorCode, Transliterator::listIDs
