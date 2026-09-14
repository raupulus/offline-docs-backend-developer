---
title: wincache_ucache_delete
description: Elimina las variables de la memoria caché del usuario
source_url: https://www.php.net/manual/es/function.wincache-ucache-delete.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/wincache/functions/wincache-ucache-delete.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: wincache
translation_status: ready
translation_reviewed: false
translation_revision: df78bd1d2
order: 101740
---

wincache_ucache_delete

Elimina las variables de la memoria caché del usuario

## Descripción

```php
wincache_ucache_delete(mixed $key): bool
```php

Elimina los elementos de la caché del usuario apuntado por `key`.

## Parámetros

`key`  
El parámetro `key` que se utiliza para almacenar la variable en la caché. `key` distingue mayúsculas de minúsculas. `key` puede ser un array de claves.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

Si `key` es un array, entonces la función devuelve `false` si cada elemento del array no se borra de la memoria caché del usuario, en caso contrario devuelve un array que consta de todas las claves que se eliminan.

## Ejemplos

Usando `wincache_ucache_delete` con `key` como un string

```
<?php
wincache_ucache_set('foo', 'bar');
var_dump(wincache_ucache_delete('foo'));
var_dump(wincache_ucache_exists('foo'));
?>

    
```php

El ejemplo anterior mostrará:

    bool(true)
    bool(false)

Using`wincache_ucache_delete` con `key` como un array

```
<?php
$array1 = array('green' => '5', 'blue' => '6', 'yellow' => '7', 'cyan' => '8');
wincache_ucache_set($array1);
$array2 = array('green', 'blue', 'yellow', 'cyan');
var_dump(wincache_ucache_delete($array2));
?>

    
```php

El ejemplo anterior mostrará:

    array(4) { [0]=> string(5) "green"
               [1]=> string(4) "blue"
               [2]=> string(6) "yellow"
               [3]=> string(4) "cyan" }

Using `wincache_ucache_delete` con `key` como un array donde algunos elementos no se pueden eliminar

```
<?php
$array1 = array('green' => '5', 'blue' => '6', 'yellow' => '7', 'cyan' => '8');
wincache_ucache_set($array1);
$array2 = array('orange', 'red', 'yellow', 'cyan');
var_dump(wincache_ucache_delete($array2));
?>

    
```php

El ejemplo anterior mostrará:

    array(2) { [0]=> string(6) "yellow"
               [1]=> string(4) "cyan" }

## Véase también

`wincache_ucache_set`, `wincache_ucache_add`, `wincache_ucache_get`, `wincache_ucache_clear`, `wincache_ucache_exists`, `wincache_ucache_meminfo`, `wincache_ucache_info`
