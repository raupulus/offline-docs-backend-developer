---
title: Memcache::add
description: Añade un elemento en el servidor
source_url: https://www.php.net/manual/es/memcache.add.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/memcache/memcache/add.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: memcache
translation_status: ready
translation_reviewed: false
translation_revision: f4098e2ba
order: 46090
---

Memcache::add

memcache_add

Añade un elemento en el servidor

## Descripción

```php
Memcache::add(string $key, mixed $var, [int $flag], [int $expire]): bool
```php

```php
memcache_add(Memcache $memcache, string $key, mixed $var, [int $flag], [int $expire]): bool
```

`Memcache::add` almacena la variable `var` con la clave `key` solo si esta clave no existe ya en el servidor.

## Parámetros

`key`  
La clave a asociar al elemento.

`var`  
La variable a almacenar. Los strings y los integers se almacenan tal cual, los otros tipos se serializan.

`flag`  
Utilice `MEMCACHE_COMPRESSED` para comprimir el elemento (utiliza zlib).

`expire`  
Tiempo de expiración del elemento. Si es igual a cero, el elemento nunca expirará. También puede utilizarse un timestamp Unix o un número de segundos a partir del tiempo actual, pero en este caso el número de segundos no debe exceder 2592000 (30 días).

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error. Devuelve `false` si la clave ya existe. Para el resto, el comportamiento de `Memcache::add` es el mismo que `Memcache::set`.

## Ejemplos

Ejemplo con `Memcache::add`

```php
<?php

$memcache_obj = memcache_connect("localhost", 11211);

/* API procedimental */
memcache_add($memcache_obj, 'var_key', 'test variable', false, 30);

/* API orientada a objetos */
$memcache_obj->add('var_key', 'test variable', false, 30);

?>

   
```

## Véase también

Memcache::set

Memcache::replace
