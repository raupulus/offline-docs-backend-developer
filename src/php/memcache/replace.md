---
title: Memcache::replace
description: Remplaza el valor de un elemento existente
source_url: https://www.php.net/manual/es/memcache.replace.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/memcache/memcache/replace.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: memcache
translation_status: ready
translation_revision: f4098e2ba
order: 46230
---

Memcache::replace

memcache_replace

Remplaza el valor de un elemento existente

## Descripción

```php
Memcache::replace(string $key, mixed $var, [int $flag], [int $expire]): bool
```php

```php
memcache_replace(Memcache $memcache, string $key, mixed $var, [int $flag], [int $expire]): bool
```

`Memcache::replace` se utiliza para reemplazar el valor de un elemento identificado por la clave `key`. En el caso de que el elemento identificado por la clave `key` no exista, la función `Memcache::replace` devolverá `false`. Por lo demás, la función `Memcache::replace` funciona de la misma manera que la función `Memcache::set`.

## Parámetros

`key`  
La clave que se asociará con el elemento.

`var`  
La variable a almacenar. Los strings y los integers se almacenan como tales, los demás tipos se almacenan de manera serializada.

`flag`  
Utilice `MEMCACHE_COMPRESSED` para almacenar el elemento comprimido (utiliza zlib).

`expire`  
Tiempo de expiración para el elemento. Si es igual a `0`, el elemento no expirará nunca. También puede utilizarse un timestamp Unix o un número de segundos a partir de la fecha actual, pero en este último caso, el número de segundos no debe exceder 2592000 (30 días).

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `Memcache::replace`

```php
<?php

$memcache_obj = memcache_connect('memcache_host', 11211);

/* API procedimental */
memcache_replace($memcache_obj, "test_key", "some variable", false, 30);

/* API orientada a objetos */
$memcache_obj->replace("test_key", "some variable", false, 30);

?>

   
```

## Véase también

Memcache::set

Memcache::add
