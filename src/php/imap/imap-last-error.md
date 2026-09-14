---
title: imap_last_error
description: Devuelve el último error ocurrido
source_url: https://www.php.net/manual/es/function.imap-last-error.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imap/functions/imap-last-error.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imap
translation_status: ready
translation_reviewed: false
translation_revision: 4a9963bc4
order: 38240
---

imap_last_error

Devuelve el último error ocurrido

## Descripción

```php
imap_last_error(): string
```php

`imap_last_error` devuelve el texto completo del último error IMAP (si existe) que ocurrió durante la última petición. La pila de errores no se ve afectada. Llamar a `imap_last_error` sucesivamente, sin nuevos errores, devolverá el mismo error.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el texto completo del último mensaje de error IMAP ocurrido en la página actual. Devuelve `false` si no hay ningún mensaje disponible.

## Véase también

`imap_errors`
