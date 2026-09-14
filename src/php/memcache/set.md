---
title: Memcache::set
description: Almacena datos en el servidor de caché
source_url: https://www.php.net/manual/es/memcache.set.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/memcache/memcache/set.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: memcache
translation_status: ready
translation_revision: f4098e2ba
order: 46240
---

Memcache::set

memcache_set

Almacena datos en el servidor de caché

## Descripción

```php
Memcache::set(string $key, mixed $var, [int $flag], [int $expire]): bool
```php

```php
memcache_set(Memcache $memcache, string $key, mixed $var, [int $flag], [int $expire]): bool
```

`Memcache::set` almacena el elemento `var` con la clave `key` en el servidor de caché. El parámetro `expire` representa el tiempo de expiración en segundos del elemento. Si vale 0, el elemento no expirará nunca (aunque el servidor de caché no garantiza que este elemento siempre estará almacenado, puede ser eliminado de la caché para hacer espacio para otros elementos). Puede utilizarse la constante `MEMCACHE_COMPRESSED` como valor del parámetro `flag` si se desea utilizar la compresión en tiempo real (utilizando la biblioteca zlib).

> [!NOTE]
> Tenga en cuenta que los recursos (es decir, identificadores de archivos o conexiones) no pueden almacenarse en la caché, ya que no pueden ser representados linealmente.

## Parámetros

`key`  
La clave que se asociará con el elemento.

`var`  
La variable a registrar. Los strings y los integers se registran como tales, los demás tipos se registran de manera serializada.

`flag`  
Utilice `MEMCACHE_COMPRESSED` para registrar el elemento comprimido (utiliza zlib).

`expire`  
Tiempo de expiración para el elemento. Si es igual a `0`, el elemento no expirará. También puede utilizarse un timestamp Unix o un número de segundos a partir de la fecha actual, pero en este último caso, el número de segundos no debe exceder 2592000 (30 días).

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `Memcache::set`

```php
<?php
/* API procedimental */

/* conexión al servidor de caché */
$memcache_obj = memcache_connect('memcache_host', 11211);

/*
define el valor del elemento identificado por la clave 'var_key' ;
utilización del valor 0 para el flag ;
la compresión no se utiliza ;
el tiempo de expiración es de 30 segundos
*/
memcache_set($memcache_obj, 'var_key', 'algunas variables', 0, 30);

echo memcache_get($memcache_obj, 'var_key');

?>

    
```

Ejemplo con `Memcache::set`

```php
<?php
/* API orientada a objetos */

$memcache_obj = new Memcache;

/* conexión al servidor de caché */
$memcache_obj->connect('memcache_host', 11211);

/*
define el valor del elemento identificado por la clave 'var_key' ;
utilización de la compresión en tiempo real ;
el tiempo de expiración es de 50 segundos
*/
$memcache_obj->set('var_key', 'algunas variables grandes', MEMCACHE_COMPRESSED, 50);

echo $memcache_obj->get('var_key');

?>

    
```

## Véase también

Memcache::add

Memcache::replace
