---
title: readline_callback_handler_remove
description: Elimina un manejador de devolución de llamada readline
source_url: https://www.php.net/manual/es/function.readline-callback-handler-remove.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/readline/functions/readline-callback-handler-remove.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: readline
translation_status: ready
translation_reviewed: true
translation_revision: 53208f9bd
order: 68730
---

readline_callback_handler_remove

Elimina un manejador de devolución de llamada readline

## Descripción

```php
readline_callback_handler_remove(): bool
```php

Elimina un manejador de devolución de llamada instalado previamente y restaura los parámetros del terminal.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve `true` si un manejador de devolución de llamada previamente instalado ha sido eliminado o `false` si no ha sido encontrado.

## Ejemplos

Consulte la función `readline_callback_handler_install` para un ejemplo sobre el uso de la interfaz de devolución de llamada readline.

## Véase también

readline_callback_handler_install

readline_callback_read_char
