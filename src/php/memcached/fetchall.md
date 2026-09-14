---
title: Memcached::fetchAll
description: Lee todos los demás elementos
source_url: https://www.php.net/manual/es/memcached.fetchall.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/memcached/memcached/fetchall.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: memcached
translation_status: ready
translation_reviewed: true
translation_revision: 1d8068ecb
order: 46500
---

Memcached::fetchAll

Lee todos los demás elementos

## Descripción

```php
public Memcached::fetchAll(): array
```php

`Memcached::fetchAll` lee todos los elementos de la última petición.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve los resultados o `false` si ocurre un error. Utilice Memcached::getResultCode si es necesario.

## Ejemplos

Ejemplo con `Memcached::fetchAll`

```
<?php
$m = new Memcached();
$m->addServer('localhost', 11211);

$m->set('int', 99);
$m->set('string', 'a simple string');
$m->set('array', array(11, 12));

$m->getDelayed(array('int', 'array'), true);
var_dump($m->fetchAll());
?>

    
```php

El ejemplo anterior mostrará:

    array(2) {
      [0]=>
      array(3) {
        ["key"]=>
        string(3) "int"
        ["value"]=>
        int(99)
        ["cas"]=>
        float(2363)
      }
      [1]=>
      array(3) {
        ["key"]=>
        string(5) "array"
        ["value"]=>
        array(2) {
          [0]=>
          int(11)
          [1]=>
          int(12)
        }
        ["cas"]=>
        float(2365)
      }
    }

## Véase también

Memcached::fetch, Memcached::getDelayed
