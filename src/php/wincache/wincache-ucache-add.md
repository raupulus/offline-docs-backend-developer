---
title: wincache_ucache_add
description: Añade una nueva variable al caché de usuario solo si la variable todavía
  no existe en el cache
source_url: https://www.php.net/manual/es/function.wincache-ucache-add.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/wincache/functions/wincache-ucache-add.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: wincache
translation_status: ready
translation_reviewed: false
translation_revision: e2f2172bf
order: 101700
---

wincache_ucache_add

Añade una nueva variable al caché de usuario solo si la variable todavía no existe en el cache

## Descripción

```php
wincache_ucache_add(string $key, mixed $value, [int $ttl]): bool
```php

```php
wincache_ucache_add(array $values, [mixed $unused], [int $ttl]): bool
```

Añade una variable al caché de usuario, solo si no existe ya en el caché. La variable permanecerá en el caché mientras no se alcance el tiempo de expiración o hasta que no se elimine con la función `wincache_ucache_delete` o la función `wincache_ucache_clear`.

## Parámetros

`key`  
Almacena la variable usando el nombre `key`. Si una variable correspondiente a la misma clave ya está presente en el caché, la función fallará y devolverá `false`. El parámetro `key` es sensible a mayúsculas y minúsculas. Para sobrescribir este valor, si `key` está presente, use la función `wincache_ucache_set` en su lugar. `key` también puede ser un array de pares nombre =\> valor donde los nombres serán usados como claves. Este formato puede ser usado para añadir múltiples valores en el caché en una sola operación.

`value`  
El valor de la variable a almacenar. El parámetro `Value` soporta todos los tipos de datos, excepto recursos, como punteros de archivos. Este parámetro será ignorado si el primer argumento es un array. Generalmente, se debe pasar el valor `null` al parámetro `value` cuando se usa un array para el parámetro `key`. Si el parámetro `value` es un objeto, o un array que contiene objetos, entonces los objetos serán serializados. Consulte la función [\_\_sleep()](#object.sleep) para más detalles sobre la serialización de objetos.

`values`  
Array asociativo de claves y valores.

`ttl`  
Duración de vida de la variable en el caché, en segundos. Después del tiempo especificado por el parámetro `ttl`, la variable almacenada será eliminada del caché. Este parámetro toma, como valor por defecto, cero (`0`), lo que significa que la variable permanecerá en el caché hasta que no sea explícitamente eliminada usando la función `wincache_ucache_delete` o la función `wincache_ucache_clear`.

## Valores devueltos

Si el parámetro `key` es una `string`, la función devuelve `true` en caso de éxito, `false` si ocurre un error.

Si el parámetro `key` es un array, la función devuelve:

- Si todas las parejas nombre =\> valor del array pueden ser definidas, la función devolverá un array vacío;
- Si ninguna de las parejas nombre =\> valor del array puede ser definida, la función devolverá `false` ;
- Si algunas pueden ser definidas, y otras no, la función devolverá un array de parejas nombre =\> valor que no han podido ser definidas en el caché de usuario.

## Ejemplos

Ejemplo con `wincache_ucache_add` y el parámetro `key` en forma de `string`

```php
<?php
$bar = 'BAR';
var_dump(wincache_ucache_add('foo', $bar));
var_dump(wincache_ucache_add('foo', $bar));
var_dump(wincache_ucache_get('foo'));
?>

    
```

El ejemplo anterior mostrará:

    bool(true)
    bool(false)
    string(3) "BAR"

Ejemplo con `wincache_ucache_add` y el parámetro `key` en forma de `array`

```php
<?php
$colors_array = array('green' => '5', 'Blue' => '6', 'yellow' => '7', 'cyan' => '8');
var_dump(wincache_ucache_add($colors_array));
var_dump(wincache_ucache_add($colors_array));
var_dump(wincache_ucache_get('Blue'));
?>

    
```

El ejemplo anterior mostrará:

    array(0) { }
    array(4) {
      ["green"]=> int(-1)
      ["Blue"]=> int(-1)
      ["yellow"]=> int(-1)
      ["cyan"]=> int(-1)
    }
    string(1) "6"

## Véase también

`wincache_ucache_set`, `wincache_ucache_get`, `wincache_ucache_delete`, `wincache_ucache_clear`, `wincache_ucache_exists`, `wincache_ucache_meminfo`, `wincache_ucache_info`, [\_\_sleep()](#object.sleep)
