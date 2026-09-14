---
title: array_key_first
description: Recupera la primera clave de un array
source_url: https://www.php.net/manual/es/function.array-key-first.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/array/functions/array-key-first.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: array
translation_status: ready
translation_revision: 85c47f89f
order: 5400
---

array_key_first

Recupera la primera clave de un array

## Descripción

```php
array_key_first(array $array): int
```php

Recupera la primera clave del array `array` dado sin afectar el puntero interno del array.

## Parámetros

`array`  
Un array.

## Valores devueltos

Devuelve la primera clave de `array` si el array no está vacío; `null` en caso contrario.

## Ejemplos

Uso simple de `array_key_first`

```
<?php
$array = ['a' => 1, 'b' => 2, 'c' => 3];

$firstKey = array_key_first($array);

var_dump($firstKey);
?>

    
```php

El ejemplo anterior mostrará:

    string(1) "a"

## Notas

> [!TIP]
> Hay varias maneras de proporcionar esta funcionalidad para versiones anteriores a PHP 7.3.0. Es posible utilizar `array_keys`, pero esto es bastante ineficiente. También es posible utilizar `reset` y `key`, pero esto puede cambiar el puntero interno del array. Una solución eficiente, que no modifica el puntero interno del array, escrita como un polyfill:
>
> <div class="informalexample">
>
> ```
> <?php
> if (!function_exists('array_key_first')) {
>     function array_key_first(array $arr) {
>         foreach($arr as $key => $unused) {
>             return $key;
>         }
>         return NULL;
>     }
> }
> ?>
>
>     
> ```
>
> </div>

## Véase también

array_first

array_key_last

reset
