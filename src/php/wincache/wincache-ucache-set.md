---
title: wincache_ucache_set
description: Añade una variable a la caché de usuario y sobrescribe la variable si
  ya existe en la caché
source_url: https://www.php.net/manual/es/function.wincache-ucache-set.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/wincache/functions/wincache-ucache-set.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: wincache
translation_status: ready
translation_reviewed: false
translation_revision: e2f2172bf
order: 101800
---

wincache_ucache_set

Añade una variable a la caché de usuario y sobrescribe la variable si ya existe en la caché

## Descripción

```php
wincache_ucache_set(mixed $key, mixed $value, [int $ttl]): bool
```php

```php
wincache_ucache_set(array $values, [mixed $unused], [int $ttl]): bool
```

Añade una variable a la caché de usuario. Sobrescribe una variable si ya existe en la caché. La variable así creada o actualizada permanecerá en la caché de usuario mientras no se alcance el tiempo de expiración o hasta que no se elimine con la función `wincache_ucache_delete` o la función `wincache_ucache_clear`.

## Parámetros

`key`  
Almacena la variable usando la clave `key`. Si una variable usando la misma clave `key` ya está presente, la función sobrescribirá el valor anterior con el nuevo. El parámetro `key` es sensible a mayúsculas y minúsculas. `key` también puede ser un array de pares nombre =\> valor donde los nombres serán usados como claves. Esto puede ser útil para añadir múltiples valores en la caché en una sola operación, evitando así las condiciones de carrera.

`value`  
Valor de la variable a almacenar. El parámetro `Value` soporta todos los tipos de datos, excepto recursos, como punteros de archivos. Este parámetro es ignorado si el primer argumento es un array. Es convención pasar `null` como `value` cuando se usa un array en el parámetro `key`. Si el parámetro `value` es un objeto, o un array que contiene objetos, entonces todos los objetos serán serializados. Consulte la función [\_\_sleep()](#object.sleep) para más detalles sobre la serialización de objetos.

`values`  
Array asociativo de claves y valores.

`ttl`  
Tiempo de vida de la variable en la caché, en segundos. Después del tiempo especificado por el parámetro `ttl`, la variable almacenada será eliminada de la caché de usuario. Este parámetro toma por defecto el valor cero (`0`), lo que significa que la variable permanecerá en la caché hasta que no sea explícitamente eliminada llamando a la función `wincache_ucache_delete` o la función `wincache_ucache_clear`.

## Valores devueltos

Si `key` es un `string`, la función devolverá `true` en caso de éxito, `false` si ocurre un error.

Si `key` es un array, la función devolverá:

- Si todas las parejas nombre =\> valor del array han podido ser definidas, la función devolverá un array vacío.
- Si ninguna de las parejas nombre =\> valor del array ha podido ser definida, la función devolverá `false`.
- Si algunas parejas han sido definidas, y otras no, la función devolverá un array de parejas nombre =\> valor que no han podido ser definidas en la caché de usuario.

## Ejemplos

Ejemplo con `wincache_ucache_set` y el parámetro `key` en forma de `string`

```php
<?php
$bar = 'BAR';
var_dump(wincache_ucache_set('foo', $bar));
var_dump(wincache_ucache_get('foo'));
$bar1 = 'BAR1';
var_dump(wincache_ucache_set('foo', $bar1));
var_dump(wincache_ucache_get('foo'));
?>

    
```

El ejemplo anterior mostrará:

    bool(true)
    string(3) "BAR"
    bool(true)
    string(3) "BAR1"

Ejemplo con `wincache_ucache_set` y el parámetro `key` en forma de `array`

```php
<?php
$colors_array = array('green' => '5', 'Blue' => '6', 'yellow' => '7', 'cyan' => '8');
var_dump(wincache_ucache_set($colors_array));
var_dump(wincache_ucache_set($colors_array));
var_dump(wincache_ucache_get('Blue'));
?>

    
```

El ejemplo anterior mostrará:

    array(0) {}
    array(0) {}
    string(1) "6"

## Véase también

`wincache_ucache_add`, `wincache_ucache_get`, `wincache_ucache_delete`, `wincache_ucache_clear`, `wincache_ucache_exists`, `wincache_ucache_meminfo`, `wincache_ucache_info`, [\_\_sleep()](#object.sleep)
