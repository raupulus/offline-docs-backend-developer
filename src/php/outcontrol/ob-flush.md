---
title: ob_flush
description: Vacía (envía) el valor de retorno del manejador de salida activo.
source_url: https://www.php.net/manual/es/function.ob-flush.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/outcontrol/functions/ob-flush.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: outcontrol
translation_status: ready
translation_reviewed: true
translation_revision: a866f72f5
order: 59770
---

ob_flush

Vacía (envía) el valor de retorno del manejador de salida activo.

## Descripción

```php
ob_flush(): bool
```php

Esta función llama al manejador de salida (con el flag `PHP_OUTPUT_HANDLER_FLUSH`), vacía (envía) su valor de retorno e ignora el contenido del búfer de salida activo.

Esta función no desactiva el búfer de salida activo como lo hacen `ob_end_flush` o `ob_get_flush`.

`ob_flush` fallará sin un búfer de salida activo iniciado con el flag `PHP_OUTPUT_HANDLER_FLUSHABLE`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

Si la función falla, genera una `E_NOTICE`.

## Véase también

`ob_start`, `ob_get_contents`, `ob_end_flush`, `ob_get_flush`, `ob_clean`
