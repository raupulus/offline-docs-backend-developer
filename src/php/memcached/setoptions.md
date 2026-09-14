---
title: Memcached::setOptions
description: Define opciones Memcache
source_url: https://www.php.net/manual/es/memcached.setoptions.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/memcached/memcached/setoptions.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: memcached
translation_status: ready
translation_reviewed: false
translation_revision: 1d8068ecb
order: 46820
---

Memcached::setOptions

Define opciones Memcache

## Descripción

```php
public Memcached::setOptions(array $options): bool
```php

`Memcached::setOptions` es una variante del método Memcached::setOption que acepta un array de opciones a definir.

## Parámetros

`options`  
Un array asociativo de opciones donde las claves representan la opción a definir, y los valores, el nuevo valor para la opción.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Definir opciones Memcache

```
<?php
$m = new Memcached();
var_dump($m->getOption(Memcached::OPT_HASH) == Memcached::HASH_DEFAULT);

$m->setOptions(array(Memcached::OPT_HASH => Memcached::HASH_MURMUR, Memcached::OPT_PREFIX_KEY => "widgets"));

var_dump($m->getOption(Memcached::OPT_HASH) == Memcached::HASH_DEFAULT);
echo "El prefijo de las claves es ahora: ", $m->getOption(Memcached::OPT_PREFIX_KEY), "\n";
?>

    
```php

El ejemplo anterior mostrará:

    bool(true)
    bool(false)
    El prefijo de las claves es ahora: widgets

## Véase también

Memcached::getOption, Memcached::setOption, Las [constantes Memcache](#memcached.constants)
