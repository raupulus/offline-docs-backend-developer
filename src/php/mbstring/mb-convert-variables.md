---
title: mb_convert_variables
description: Convierte la codificación de variables
source_url: https://www.php.net/manual/es/function.mb-convert-variables.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/mbstring/functions/mb-convert-variables.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: mbstring
translation_status: ready
translation_revision: 92f1b8b17
order: 45010
---

mb_convert_variables

Convierte la codificación de variables

## Descripción

```php
mb_convert_variables(string $to_encoding, array $from_encoding, mixed $var, mixed ...$vars): string
```php

Convierte la codificación de las variables `var` y `vars` desde la codificación `from_encoding` hacia la codificación `to_encoding`

`mb_convert_variables` coloca las strings en un array o un objeto para detectar la codificación, pero la detección tiende a fallar para strings de pequeño tamaño. Por lo tanto, no es posible mezclar codificaciones en un array o un objeto "simple".

## Parámetros

`to_encoding`  
La codificación a la cual la string debe ser convertida.

`from_encoding`  
`from-encoding` es una lista de codificaciones posibles para las variables `vars`, proporcionada en forma de un array o una lista de codificaciones, separadas por comas. Si `from_encoding` es omitido, las codificaciones proporcionadas en `mb_detect_order` son utilizadas.

`var`  
`var` es una referencia a una variable a convertir. Las strings, arrays y objetos también son soportados. `mb_convert_variables` toma todos estos parámetros con la misma codificación.

`vars`  
Variables adicionales.

## Valores devueltos

La codificación antes de la conversión en caso de éxito, o `false` si ocurre un error.

## Ejemplos

Ejemplo con `mb_convert_variables`

```
<?php
/* Convierte las variables $post1, $post2 a la codificación interna */
$interenc = mb_internal_encoding();
$inputenc = mb_convert_variables($interenc, "ASCII,UTF-8,SJIS-win", $post1, $post2);
?>

    
```php
