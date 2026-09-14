---
title: Memcached::setOption
description: Configura una opción Memcached
source_url: https://www.php.net/manual/es/memcached.setoption.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/memcached/memcached/setoption.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: memcached
translation_status: ready
translation_reviewed: true
translation_revision: 7e6d80ad1
order: 46810
---

Memcached::setOption

Configura una opción Memcached

## Descripción

```php
public Memcached::setOption(int $option, mixed $value): bool
```php

Este método configura un valor de la opción Memcached `option` con el valor `value`. Algunas opciones corresponden a las definidas en libmemcached, y otras son específicas de la extensión.

## Parámetros

`option`  
Una de las constantes `Memcached::OPT_*`. Ver [Memcached Constants](#memcached.constants) para más información.

`value`  
El valor a definir.

> [!NOTE]
> Las opciones a continuación requieren que los valores sean especificados mediante constantes. `Memcached::OPT_HASH` requiere valores `Memcached::HASH_*`., `Memcached::OPT_DISTRIBUTION` requiere valores `Memcached::DISTRIBUTION_*`., `Memcached::OPT_SERIALIZER` requiere valores `Memcached::SERIALIZER_*`., `Memcached::OPT_COMPRESSION_TYPE` requiere valores `Memcached::COMPRESSION_*`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error.

## Ejemplos

Configuración de una opción Memcached

```
<?php
$m = new Memcached();
var_dump($m->getOption(Memcached::OPT_HASH) == Memcached::HASH_DEFAULT);
$m->setOption(Memcached::OPT_HASH, Memcached::HASH_MURMUR);
$m->setOption(Memcached::OPT_PREFIX_KEY, "widgets");
echo "El prefijo de la clave es ahora: ", $m->getOption(Memcached::OPT_PREFIX_KEY), "\n";
?>

    
```php

El ejemplo anterior mostrará:

    bool(true)
    El prefijo de la clave es ahora: widgets

## Véase también

Memcached::getOption, Memcached::setOptions, [Las constantes Memcached](#memcached.constants)
