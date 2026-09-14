---
title: wincache_ucache_get
description: Obtiene una variable almacenada en la caché del usuario
source_url: https://www.php.net/manual/es/function.wincache-ucache-get.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/wincache/functions/wincache-ucache-get.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: wincache
translation_status: ready
translation_reviewed: false
translation_revision: fcddfb255
order: 101760
---

wincache_ucache_get

Obtiene una variable almacenada en la caché del usuario

## Descripción

```php
wincache_ucache_get(mixed $key, [bool $success]): mixed
```php

Obtiene una variable almacenada en la caché del usuario.

## Parámetros

`key`  
La `key` que se utiliza para almacenar la variable en la caché. `key` distingue mayúsculas de minúsculas. `key` puede ser un array de claves. En este caso el valor de retorno será un array de valores de cada elemento en el array `key`. Si un objeto, o un array que contiene objetos, es retornado, entonces los objetos serán decodificados. Véase [\_\_wakeup()](#object.wakeup) para más detalles sobre decodificar objetos.

`success`  
Se establecerá en `true` en caso de éxito y `false` en caso de error.

## Valores devueltos

Si `key` es un string, la función devuelve el valor de la variable almacenada con esa clave. El parámetro `success` es establecido a `true` en caso de éxito y a `false` en caso de error.

El parámetro `key` es un array, el parámetro `success` siempre se establece en `true`. El array devuelto (pares nombre =\> valor) contendrá sólo aquellos pares nombre =\> valor en donde la operación de obtención de caché de usuario se ha realizado correctamente. Si ninguna de las claves del array encuentran una coincidencia en la caché del usuario, un array vacío será devuelto.

## Ejemplos

`wincache_ucache_get` con `key` como un string

```
<?php
wincache_ucache_add('color', 'blue');
var_dump(wincache_ucache_get('color', $success));
var_dump($success);
?>

    
```php

El ejemplo anterior mostrará:

    string(4) "blue"
    bool(true)

`wincache_ucache_get` con `key` como un array

```
<?php
$array1 = array('green' => '5', 'Blue' => '6', 'yellow' => '7', 'cyan' => '8');
wincache_ucache_set($array1);
$array2 = array('green', 'Blue', 'yellow', 'cyan');
var_dump(wincache_ucache_get($array2, $success));
var_dump($success);
?>

    
```php

El ejemplo anterior mostrará:

    array(4) { ["green"]=> string(1) "5"
               ["Blue"]=> string(1) "6"
               ["yellow"]=> string(1) "7"
               ["cyan"]=> string(1) "8" }
    bool(true)

## Véase también

`wincache_ucache_add`, `wincache_ucache_set`, `wincache_ucache_delete`, `wincache_ucache_clear`, `wincache_ucache_exists`, `wincache_ucache_meminfo`, `wincache_ucache_info`, [\_\_wakeup()](#object.wakeup)
