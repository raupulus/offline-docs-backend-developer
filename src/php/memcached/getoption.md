---
title: Memcached::getOption
description: Lee una opción Memcached
source_url: https://www.php.net/manual/es/memcached.getoption.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/memcached/memcached/getoption.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: memcached
translation_status: ready
translation_reviewed: true
translation_revision: 1d8068ecb
order: 46590
---

Memcached::getOption

Lee una opción Memcached

## Descripción

```php
public Memcached::getOption(int $option): mixed
```php

Devuelve el valor de la opción Memcached `option`. Estas opciones están definidas por libmemcached, y otras son específicas de esta extensión. Véase [constantes Memcached](#memcached.constants) para más información.

## Parámetros

`option`  
Una de las constantes `Memcached::OPT_*`.

## Valores devueltos

Devuelve el valor de la opción solicitada, o bien `false` si ocurre un error.

## Ejemplos

Lectura de opciones Memcached

```
<?php
$m = new Memcached();
var_dump($m->getOption(Memcached::OPT_COMPRESSION));
var_dump($m->getOption(Memcached::OPT_POLL_TIMEOUT));
?>

    
```php

Resultado del ejemplo anterior es similar a:

    bool(true)
    int(1000)

## Véase también

Memcached::getOption, Memcached::setOption, [Constantes Memcached](#memcached.constants)
