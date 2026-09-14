---
title: ob_get_flush
description: Vacía (envía) el valor de retorno del gestor de salida activo, devuelve
  el contenido del búfer de salida activo y lo desactiva.
source_url: https://www.php.net/manual/es/function.ob-get-flush.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/outcontrol/functions/ob-get-flush.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: outcontrol
translation_status: ready
translation_reviewed: true
translation_revision: 86b976d5a
order: 59800
---

ob_get_flush

Vacía (envía) el valor de retorno del gestor de salida activo, devuelve el contenido del búfer de salida activo y lo desactiva.

## Descripción

```php
ob_get_flush(): string
```php

Esta función llama al gestor de salida (con el flag `PHP_OUTPUT_HANDLER_FINAL`), envía (vacía) su valor de retorno, devuelve el contenido del búfer de salida activo y desactiva el búfer de salida activo.

`ob_get_flush` fallará sin un búfer de salida activo iniciado con el flag `PHP_OUTPUT_HANDLER_REMOVABLE`.

`ob_get_flush` vaciará (enviará) el valor de retorno del gestor de salida incluso si el búfer de salida activo ha sido iniciado sin el flag `PHP_OUTPUT_HANDLER_FLUSHABLE`.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el contenido del búfer de salida activo en caso de éxito o `false` en caso de fallo.

## Errores/Excepciones

En caso de fallo de la función, genera una `E_NOTICE`.

## Ejemplos

Ejemplo con `ob_get_flush`

```
<?php
//Utilización de output_buffering=On
print_r(ob_list_handlers());

//Guardado del búfer en un fichero
$buffer = ob_get_flush();
file_put_contents('buffer.txt', $buffer);

print_r(ob_list_handlers());
?>

    
```php

El ejemplo anterior mostrará:

    Array
    (
        [0] => default output handler
    )
    Array
    (
    )

## Véase también

`ob_start`, `ob_get_contents`, `ob_flush`, `ob_end_flush`, `ob_get_clean`
