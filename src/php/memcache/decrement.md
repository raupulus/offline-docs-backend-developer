---
title: Memcache::decrement
description: Disminuye el valor de un elemento
source_url: https://www.php.net/manual/es/memcache.decrement.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/memcache/memcache/decrement.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: memcache
translation_status: ready
translation_reviewed: false
translation_revision: f4098e2ba
order: 46130
---

Memcache::decrement

Disminuye el valor de un elemento

## Descripción

```php
Memcache::decrement(string $key, [int $value]): int
```php

```php
memcache_decrement(Memcache $memcache, string $key, [int $value]): int
```

`Memcache::decrement` disminuye el valor del elemento por `value`. De manera similar a la función `memcache::increment`, el valor actual del elemento se convierte primero en numérico y luego se resta el valor `value`.

> [!NOTE]
> El nuevo valor del elemento no puede ser inferior a cero.

> [!NOTE]
> No se debe utilizar la función `Memcache::decrement` con elementos almacenados comprimidos. En este caso, la llamada a la función `Memcache::get` fallará.

`Memcache::decrement` *no crea* un elemento si no existe.

## Parámetros

`key`  
Clave del elemento a disminuir.

`value`  
Disminuye el elemento por `value`.

## Valores devueltos

Devuelve el valor del nuevo elemento en caso de éxito o `false` si ocurre un error.

## Ejemplos

Ejemplo con `Memcache::decrement`

```php
<?php

/* API procedimental */
$memcache_obj = memcache_connect('memcache_host', 11211);
/* disminución del elemento por 2 */
$new_value = memcache_decrement($memcache_obj, 'test_item', 2);

/* API orientada a objetos */
$memcache_obj = new Memcache;
$memcache_obj->connect('memcache_host', 11211);
/* disminución del elemento por 3 */
$new_value = $memcache_obj->decrement('test_item', 3);
?>

    
```

## Véase también

Memcache::increment

Memcache::replace
