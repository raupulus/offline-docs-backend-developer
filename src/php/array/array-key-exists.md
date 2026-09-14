---
title: array_key_exists
description: Verifica si una clave existe en un array
source_url: https://www.php.net/manual/es/function.array-key-exists.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/array/functions/array-key-exists.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: array
translation_status: ready
translation_revision: faa17c20a
order: 5390
---

array_key_exists

Verifica si una clave existe en un array

## Descripción

```php
array_key_exists(string $key, array $array): bool
```php

`array_key_exists` devuelve `true` si existe una clave con el nombre `key` en el array `array`. `key` puede ser cualquier valor válido de índice de array.

## Parámetros

`key`  
Valor a verificar.

`array`  
Un array que contiene las claves a verificar.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

> [!NOTE]
> `array_key_exists` buscará, únicamente, en las claves de la primera dimensión. Las claves anidadas en los arrays multidimensionales no serán encontradas

## Historial de cambios

| Versión | Descripción |
|----|----|
| 8.5.0 | Usar `null` en el parámetro `key` está obsoleto, use un string vacío en su lugar. |
| 8.0.0 | El parámetro `key` acepta ahora los argumentos de tipo `bool`, `float`, `int`, `null`, `resource`, y `string`. |
| 8.0.0 | Ya no es posible pasar un `objeto` al parámetro `array`. |
| 7.4.0 | Se desaconseja pasar un `objeto` al parámetro `array`. Utilizar en su lugar `property_exists`. |

## Ejemplos

Ejemplo con `array_key_exists`

```
<?php
$searchArray = ['first' => 1, 'second' => 4];
var_dump(array_key_exists('first', $searchArray));
?>

    
```php

El ejemplo anterior mostrará:

    bool(true)

`array_key_exists` y `isset`

`isset` no devuelve `true` para las claves de arrays que corresponden a un valor `null` mientras que `array_key_exists` sí lo hace.

```
<?php
$searchArray = ['first' => null, 'second' => 4];

var_dump(isset($searchArray['first']));
var_dump(array_key_exists('first', $searchArray));
?>

   
```php

El ejemplo anterior mostrará:

    bool(false)
    bool(true)

## Véase también

`isset`, `array_keys`, `in_array`, `property_exists`
