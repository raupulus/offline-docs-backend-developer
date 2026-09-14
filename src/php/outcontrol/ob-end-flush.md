---
title: ob_end_flush
description: Vacía (envía) el valor de retorno del manejador de salida activo y desactiva
  el búfer de salida activo
source_url: https://www.php.net/manual/es/function.ob-end-flush.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/outcontrol/functions/ob-end-flush.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: outcontrol
translation_status: ready
translation_reviewed: true
translation_revision: 86b976d5a
order: 59760
---

ob_end_flush

Vacía (envía) el valor de retorno del manejador de salida activo y desactiva el búfer de salida activo

## Descripción

```php
ob_end_flush(): bool
```php

Esta función llama al manejador de salida (con el flag `PHP_OUTPUT_HANDLER_FINAL`), vacía (envía) su valor de retorno, ignora el contenido del búfer de salida activo y desactiva este último.

`ob_end_flush` fallará sin un búfer de salida activo iniciado con el flag `PHP_OUTPUT_HANDLER_REMOVABLE`.

`ob_end_flush` vaciará (enviará) el valor de retorno del manejador de salida incluso si el búfer de salida activo ha sido iniciado sin el flag `PHP_OUTPUT_HANDLER_FLUSHABLE`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

Si la función falla, genera una `E_NOTICE`.

## Ejemplos

Ejemplo con `ob_end_flush`

El ejemplo a continuación muestra un método simple para vaciar todos los búferes:

```
<?php
while (@ob_end_flush());
?>

    
```php

## Véase también

`ob_start`, `ob_get_contents`, `ob_flush`, `ob_get_flush`, `ob_end_clean`
