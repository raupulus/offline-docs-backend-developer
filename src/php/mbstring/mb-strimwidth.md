---
title: mb_strimwidth
description: Trunca una cadena
source_url: https://www.php.net/manual/es/function.mb-strimwidth.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mbstring/functions/mb-strimwidth.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mbstring
translation_status: ready
translation_reviewed: false
translation_revision: ca4b9d11a
order: 45430
---

mb_strimwidth

Trunca una cadena

## Descripción

```php
mb_strimwidth(string $string, int $start, int $width, [string $trim_marker], [string $encoding]): string
```php

Trunca la cadena `string` a la longitud `width` especificada, donde los caracteres de media caja cuentan como `1`, y los caracteres de caja completa cuentan como `2`. Ver <http://www.unicode.org/reports/tr11/> para más detalles sobre las cajas de caracteres asiáticos del este.

## Parámetros

`string`  
La cadena a truncar.

`start`  
`start` es la posición de inicio, en número de caracteres desde el principio de la cadena (el primer carácter es 0), o si la posición es negativa, número de caracteres desde el final de la `string`.

`width`  
La anchura de la truncación deseada. Si se especifica una anchura negativa, debe contarse desde el final de la cadena.

> [!NOTE]
> Proporcionar una anchura negativa está obsoleto a partir de PHP 8.3.0.

`trim_marker`  
`trim_marker` es la cadena añadida al final de la cadena truncada.

`encoding`  
El parámetro `encoding` es la codificación de caracteres. Si se omite o es `null`, se utilizará el valor de la codificación de caracteres interna.

## Valores devueltos

La cadena truncada. Si `trim_marker` está definido, `trim_marker` reemplaza los últimos caracteres para corresponder al tamaño `width`.

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.3.0 | Proporcionar una `width` negativa a `mb_strimwidth` ahora está obsoleto. |
| 8.0.0 | `encoding` ahora acepta `null`. |
| 7.1.0 | Se añadió soporte para `start`s y `width`s negativos. |

## Ejemplos

Ejemplo con `mb_strimwidth`

```
<?php
echo mb_strimwidth("Hello World", 0, 10, "...");
// Muestra: "Hello W..."
?>

    
```php

## Véase también

`mb_strwidth`, `mb_internal_encoding`
