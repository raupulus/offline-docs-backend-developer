---
title: Memcache::increment
description: Incrementa el valor de un elemento
source_url: https://www.php.net/manual/es/memcache.increment.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/memcache/memcache/increment.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: memcache
translation_status: ready
translation_reviewed: false
translation_revision: f4098e2ba
order: 46210
---

Memcache::increment

memcache_increment

Incrementa el valor de un elemento

## Descripción

```php
Memcache::increment(string $key, [int $value]): int
```php

```php
memcache_increment(Memcache $memcache, string $key, [int $value]): int
```

`Memcache::increment` incrementa el valor de un elemento identificado por la clave `key` por el valor `value`. Si el elemento identificado por la clave `key` no es de tipo numérico y no puede ser convertido a número, el valor de este elemento será definido a `value`. `Memcache::increment` *no crea* un elemento si no existe.

> [!NOTE]
> No se debe utilizar `memcache::increment` con elementos almacenados comprimidos. En este caso, la llamada a la función `Memcache::get` fallará.

## Parámetros

`key`  
Clave del elemento a incrementar.

`value`  
Incrementa el elemento por `value`.

## Valores devueltos

Devuelve el valor del nuevo elemento en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `Memcache::increment`

```php
<?php

/* API procedimental */
$memcache_obj = memcache_connect('memcache_host', 11211);
/* incrementación del contador en 2 */
$current_value = memcache_increment($memcache_obj, 'counter', 2);

/* API orientada a objetos */
$memcache_obj = new Memcache;
$memcache_obj->connect('memcache_host', 11211);
/* incrementación del contador en 3 */
$current_value = $memcache_obj->increment('counter', 3);

?>

   
```

## Véase también

Memcache::decrement

Memcache::replace
