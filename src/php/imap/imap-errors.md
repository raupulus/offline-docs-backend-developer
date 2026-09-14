---
title: imap_errors
description: Devuelve todos los errores IMAP ocurridos
source_url: https://www.php.net/manual/es/function.imap-errors.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/imap/functions/imap-errors.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: imap
translation_status: ready
translation_reviewed: false
translation_revision: 4a9963bc4
order: 38060
---

imap_errors

Devuelve todos los errores IMAP ocurridos

## Descripción

```php
imap_errors(): array
```php

Esta función devuelve un array de todos los mensajes de error IMAP generados desde la última llamada a `imap_errors` o desde el inicio de la página.

Cuando `imap_errors` es llamada, la pila de errores es vaciada.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Esta función devuelve un array que contiene todos los mensajes de error IMAP generados desde la última llamada a la función `imap_errors` o desde el inicio de la página. Devuelve `false` si no hay mensajes de error disponibles.

## Véase también

`imap_last_error`, `imap_alerts`
