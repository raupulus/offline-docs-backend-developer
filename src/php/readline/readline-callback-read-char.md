---
title: readline_callback_read_char
description: Lee un carácter e informa a la interfaz de devolución de llamada readline
source_url: https://www.php.net/manual/es/function.readline-callback-read-char.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/readline/functions/readline-callback-read-char.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: readline
translation_status: ready
translation_reviewed: true
translation_revision: 53208f9bd
order: 68740
---

readline_callback_read_char

Lee un carácter e informa a la interfaz de devolución de llamada readline

## Descripción

```php
readline_callback_read_char(): void
```php

Lee un carácter de la entrada del usuario. Cuando se recibe una línea, la función informa a la interfaz de devolución de llamada readline instalada mediante `readline_callback_handler_install` de que una línea está lista para ser ingresada.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

No se retorna ningún valor.

## Ejemplos

Ver la función `readline_callback_handler_install` para un ejemplo sobre el uso de la interfaz de devolución de llamada readline.

## Véase también

readline_callback_handler_install

readline_callback_handler_remove
