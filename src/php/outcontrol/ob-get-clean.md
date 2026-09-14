---
title: ob_get_clean
description: Obtiene el contenido del búfer de salida activo y lo desactiva
source_url: https://www.php.net/manual/es/function.ob-get-clean.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/outcontrol/functions/ob-get-clean.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: outcontrol
translation_status: ready
translation_reviewed: true
translation_revision: 86b976d5a
order: 59780
---

ob_get_clean

Obtiene el contenido del búfer de salida activo y lo desactiva

## Descripción

```php
ob_get_clean(): string
```php

Esta función llama al gestor de salida (con los flags `PHP_OUTPUT_HANDLER_CLEAN` y `PHP_OUTPUT_HANDLER_FINAL`), ignora su valor de retorno, devuelve el contenido del búfer de salida activo y lo desactiva.

`ob_get_clean` fallará sin un búfer de salida activo iniciado con el flag `PHP_OUTPUT_HANDLER_REMOVABLE`.

`ob_get_clean` eliminará el contenido del búfer de salida activo incluso si fue iniciado sin el flag `PHP_OUTPUT_HANDLER_CLEANABLE`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el contenido del búfer de salida activo en caso de éxito o `false` en caso de fallo.

> [!CAUTION]
> `ob_get_clean` devolverá false pero no generará una `E_NOTICE` si no hay un búfer de salida activo.

## Errores/Excepciones

Si la función falla, genera una `E_NOTICE`.

## Ejemplos

Ejemplo con `ob_get_clean`

```
<?php

ob_start();

echo "¡Hola mundo!";

$out = ob_get_clean();
$out = strtolower($out);

var_dump($out);
?>

    
```php

El ejemplo anterior mostrará:

    string(18) "¡hola mundo!"

## Véase también

`ob_start`, `ob_get_contents`, `ob_clean`, `ob_end_clean`, `ob_get_flush`
