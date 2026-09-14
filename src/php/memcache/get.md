---
title: Memcache::get
description: Recupera un elemento del servidor de caché
source_url: https://www.php.net/manual/es/memcache.get.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/memcache/memcache/get.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: memcache
translation_status: ready
translation_reviewed: false
translation_revision: f4098e2ba
order: 46160
---

Memcache::get

memcache_get

Recupera un elemento del servidor de caché

## Descripción

```php
Memcache::get(string $key, [int $flags]): string
```php

```php
Memcache::get(array $keys, [array $flags]): array
```

```php
memcache_get(Memcache $memcache, string $key, [int $flags]): string
```php

```php
memcache_get(Memcache $memcache, array $keys, [array $flags]): array
```

`Memcache::get` devuelve los datos previamente almacenados en el elemento identificado por la clave `key` si existe en el servidor en el momento de la llamada.

Se puede pasar un array de claves a la función `Memcache::get` para obtener un array de valores. El array resultante contendrá solo las parejas clave-valor encontradas.

## Parámetros

`key`  
La clave o el array de claves a recuperar.

`flags`  
Si este argumento está presente, representará los flags de los valores a recuperar. Estos flags son los mismos que los dados en el ejemplo de la función `Memcache::set`. El byte menos significativo del valor está reservado para un uso interno de pecl/memcache (por ejemplo, para indicar el estado de compresión y serialización).

## Valores devueltos

Devuelve el valor asociado con el argumento `key` o un array que contiene las parejas clave/valor encontradas cuando el argumento `key` es un `array`. Devuelve `false` si ocurre un error, si el argumento `key` no es encontrado, o si el argumento `key` es un `array` vacío.

## Ejemplos

Ejemplo con `Memcache::get`

```php
<?php

/* API procedimental */
$memcache_obj = memcache_connect('memcache_host', 11211);
$var = memcache_get($memcache_obj, 'some_key');

/* API orientada a objetos */
$memcache_obj = new Memcache;
$memcache_obj->connect('memcache_host', 11211);
$var = $memcache_obj->get('some_key');

/*
También se puede utilizar un array de claves como argumento.
Si un elemento de este tipo no es encontrado en el servidor, el array
resultado simplemente no incluirá dicha clave.
*/

/* API procedimental */
$memcache_obj = memcache_connect('memcache_host', 11211);
$var = memcache_get($memcache_obj, Array('some_key', 'another_key'));

/* API Orientada a Objetos */
$memcache_obj = new Memcache;
$memcache_obj->connect('memcache_host', 11211);
$var = $memcache_obj->get(Array('some_key', 'second_key'));

?>

   
```
