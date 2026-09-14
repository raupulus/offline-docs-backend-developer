---
title: ob_end_clean
description: Elimina (limpia) el contenido del búfer de salida activo y lo desactiva.
source_url: https://www.php.net/manual/es/function.ob-end-clean.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/outcontrol/functions/ob-end-clean.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: outcontrol
translation_status: ready
translation_reviewed: true
translation_revision: 5778b6804
order: 59750
---

ob_end_clean

Elimina (limpia) el contenido del búfer de salida activo y lo desactiva.

## Descripción

```php
ob_end_clean(): bool
```php

Esta función invoca al gestor de salida (con los flags `PHP_OUTPUT_HANDLER_CLEAN` y `PHP_OUTPUT_HANDLER_FINAL`), ignora su valor de retorno, ignora el contenido del búfer de salida activo y lo desactiva.

`ob_end_clean` fallará sin un búfer de salida activo iniciado con el flag `PHP_OUTPUT_HANDLER_REMOVABLE`.

`ob_end_clean` eliminará el contenido del búfer de salida activo incluso si fue iniciado sin el flag `PHP_OUTPUT_HANDLER_CLEANABLE`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Errores/Excepciones

Si la función falla, genera una `E_NOTICE`.

## Ejemplos

El siguiente ejemplo muestra una manera sencilla de deshacerse del contenido del búfer de salida activo:

Ejemplo con `ob_end_clean`

```
<?php
ob_start();
echo 'Texto que no será mostrado.';
ob_end_clean();
?>

    
```php

## Véase también

`ob_start`, `ob_get_contents`, `ob_clean`, `ob_get_clean`, `ob_end_flush`
