---
title: ob_clean
description: Limpiar (borrar) el contenido del búfer de salida activo.
source_url: https://www.php.net/manual/es/function.ob-clean.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/outcontrol/functions/ob-clean.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: outcontrol
translation_status: ready
translation_reviewed: true
translation_revision: 86b976d5a
order: 59740
---

ob_clean

Limpiar (borrar) el contenido del búfer de salida activo.

## Descripción

```php
ob_clean(): bool
```php

Esta función llama al gestor de salida (con el flag `PHP_OUTPUT_HANDLER_CLEAN`), ignora su valor de retorno y limpia (borra) el contenido del búfer de salida activo.

Esta función no desactiva el búfer de salida activo como lo hacen `ob_end_clean` o `ob_get_clean`.

`ob_clean` fallará sin un búfer de salida activo iniciado con el flag `PHP_OUTPUT_HANDLER_CLEANABLE`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

Si la función falla, genera una `E_NOTICE`.

## Véase también

`ob_flush`, `ob_end_flush`, `ob_end_clean`
