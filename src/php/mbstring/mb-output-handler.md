---
title: mb_output_handler
description: Función de tratamiento de los despliegues
source_url: https://www.php.net/manual/es/function.mb-output-handler.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mbstring/functions/mb-output-handler.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mbstring
translation_status: ready
translation_reviewed: true
translation_revision: 92f1b8b17
order: 45310
---

mb_output_handler

Función de tratamiento de los despliegues

## Descripción

```php
mb_output_handler(string $string, int $status): string
```php

`mb_output_handler` es la función a proporcionar a `ob_start`. `mb_output_handler` convierte los caracteres enviados al cliente en la codificación parametrizada con `mb_http_output`.

## Parámetros

`string`  
El contenido del búfer de salida.

`status`  
El estado del búfer de salida.

## Valores devueltos

La cadena convertida.

## Ejemplos

Ejemplo con `mb_output_handler`

```
<?php
mb_http_output("UTF-8");
ob_start("mb_output_handler");
?>

    
```php

## Notas

> [!NOTE]
> Si se desea enviar datos binarios tales como imágenes, el encabezado `Content-Type: header` debe ser definido utilizando la función `header` antes de enviar los datos binarios al cliente (por ejemplo, `header("Content-Type: image/png")`. Si `Content-Type: header` es enviado, la conversión de la codificación de salida no se realizará.
>
> Tenga en cuenta que si `Content-Type: text/*` es enviado, el contenido del cuerpo es visto como texto; la conversión será realizada.

## Véase también

`ob_start`
