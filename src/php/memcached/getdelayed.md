---
title: Memcached::getDelayed
description: Lee varios elementos
source_url: https://www.php.net/manual/es/memcached.getdelayed.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/memcached/memcached/getdelayed.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: memcached
translation_status: ready
translation_reviewed: true
translation_revision: 1d8068ecb
order: 46550
---

Memcached::getDelayed

Lee varios elementos

## Descripción

```php
public Memcached::getDelayed(array $keys, [bool $with_cas], [callable $value_cb]): bool
```php

`Memcached::getDelayed` envía una orden a memcache para leer varias claves que se especifican en el array `keys`. El método no espera la respuesta y devuelve inmediatamente. Cuando se esté listo para leer los elementos, se llaman los métodos Memcached::fetch o Memcached::fetchAll. Si `with_cas` es `true` también se leerá el CAS.

En lugar de leer los resultados explícitamente, se puede especificar una [función de devolución de llamada de resultados](#memcached.callbacks) mediante el argumento `value_cb`.

## Parámetros

`keys`  
Un array de claves a leer.

`with_cas`  
Si se deben leer los CAS.

`value_cb`  
Una función de devolución de llamada de resultados, o `null`.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error. Utilice Memcached::getResultCode si es necesario.

## Ejemplos

Ejemplo con `Memcached::getDelayed`

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

Memcached::getDelayedByKey, Memcached::fetch, Memcached::fetchAll
