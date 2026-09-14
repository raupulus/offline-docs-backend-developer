---
title: Memcached::getServerList
description: Lista los servidores del pool memcached
source_url: https://www.php.net/manual/es/memcached.getserverlist.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/memcached/memcached/getserverlist.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: memcached
translation_status: ready
translation_reviewed: true
translation_revision: 1d8068ecb
order: 46630
---

Memcached::getServerList

Lista los servidores del pool memcached

## Descripción

```php
public Memcached::getServerList(): array
```php

`Memcached::getServerList` devuelve la lista de todos los servidores que están en su lista.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

La lista de todos los servidores del pool.

## Ejemplos

Ejemplo con `Memcached::getServerList`

```
<?php
$m = new Memcached();
$m->addServers(array(
    array('mem1.domain.com', 11211, 20),
    array('mem2.domain.com', 11311, 80),
));
var_dump($m->getServerList());
?>

    
```php

El ejemplo anterior mostrará:

    array(2) {
      [0]=>
      array(3) {
        ["host"]=>
        string(15) "mem1.domain.com"
        ["port"]=>
        int(11211)
        ["weight"]=>
        int(20)
      }
      [1]=>
      array(3) {
        ["host"]=>
        string(15) "mem2.domain.com"
        ["port"]=>
        int(11311)
        ["weight"]=>
        int(80)
      }
    }
