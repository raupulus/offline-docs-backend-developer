---
title: Memcached::getServerByKey
description: Dirige una clave a un servidor
source_url: https://www.php.net/manual/es/memcached.getserverbykey.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/memcached/memcached/getserverbykey.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: memcached
translation_status: ready
translation_reviewed: true
translation_revision: 1d8068ecb
order: 46620
---

Memcached::getServerByKey

Dirige una clave a un servidor

## Descripción

```php
public Memcached::getServerByKey(string $server_key): array
```php

`Memcached::getServerByKey` devuelve el servidor que debería ser seleccionado por una clave `server_key` en las operaciones de tipo `Memcached::*ByKey`.

## Parámetros

`server_key`  
La clave de identificación del servidor.

## Valores devueltos

Devuelve un array que contiene 3 claves: `host`, `port`, y `weight` en caso de éxito o `false` si ocurre un error. Utilice Memcached::getResultCode si es necesario.

## Ejemplos

Ejemplo con `Memcached::getServerByKey`

```
<?php
$m = new Memcached();
$m->addServers(array(
    array('mem1.domain.com', 11211, 40),
    array('mem2.domain.com', 11211, 40),
    array('mem3.domain.com', 11211, 20),
));

$m->setOption(Memcached::OPT_LIBKETAMA_COMPATIBLE, true);

var_dump($m->getServerByKey('user'));
var_dump($m->getServerByKey('log'));
var_dump($m->getServerByKey('ip'));
?>

    
```php

Resultado del ejemplo anterior es similar a:

    array(3) {
      ["host"]=>
      string(15) "mem3.domain.com"
      ["port"]=>
      int(11211)
      ["weight"]=>
      int(20)
    }
    array(3) {
      ["host"]=>
      string(15) "mem2.domain.com"
      ["port"]=>
      int(11211)
      ["weight"]=>
      int(40)
    }
    array(3) {
      ["host"]=>
      string(15) "mem2.domain.com"
      ["port"]=>
      int(11211)
      ["weight"]=>
      int(40)
    }
