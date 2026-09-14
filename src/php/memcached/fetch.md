---
title: Memcached::fetch
description: Lee el siguiente resultado
source_url: https://www.php.net/manual/es/memcached.fetch.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/memcached/memcached/fetch.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: memcached
translation_status: ready
translation_reviewed: true
translation_revision: df78bd1d2
order: 46490
---

Memcached::fetch

Lee el siguiente resultado

## Descripción

```php
public Memcached::fetch(): array
```php

`Memcached::fetch` lee el siguiente resultado de la última petición.

## Parámetros

Esta función no contiene ningún parámetro.

## Valores devueltos

Devuelve el siguiente resultado, o bien `false` en caso contrario. El método Memcached::getResultCode va devolver `Memcached::RES_END` si el conjunto de resultados ha finalizado.

## Ejemplos

Ejemplo con `Memcached::fetch`

```
<?php
$m = new Memcached();
$m->addServer('localhost', 11211);

$m->set('int', 99);
$m->set('string', 'a simple string');
$m->set('array', array(11, 12));

$m->getDelayed(array('int', 'array'), true);
while ($result = $m->fetch()) {
    var_dump($result);
}
?>

    
```php

Resultado del ejemplo anterior es similar a:

    array(3) {
      ["key"]=>
      string(3) "int"
      ["value"]=>
      int(99)
      ["cas"]=>
      float(2363)
    }
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

## Véase también

Memcached::fetchAll, Memcached::getDelayed
