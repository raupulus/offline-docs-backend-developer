---
title: Memcached::set
description: Almacena un elemento
source_url: https://www.php.net/manual/es/memcached.set.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/memcached/memcached/set.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: memcached
translation_status: ready
translation_reviewed: true
translation_revision: 1d8068ecb
order: 46760
---

Memcached::set

Almacena un elemento

## Descripción

```php
public Memcached::set(string $key, mixed $value, [int $expiration]): bool
```php

`Memcached::set` almacena el valor `value` en un servidor memcache, con la clave de identificación `key`. El argumento `expiration` permite controlar el tiempo de expiración automática del valor.

El valor puede ser cualquier tipo de valor PHP, excepto una recurso, ya que estas no pueden ser representadas en forma lineal. Si la opción `Memcached::OPT_COMPRESSION` está activada, el valor serializado será también comprimido antes del almacenamiento.

## Parámetros

`key`  
La clave bajo la cual almacenar el valor.

`value`  
El valor a almacenar.

`expiration`  
El tiempo de expiración, predeterminado a 0. Véase [Expiration Times](#memcached.expiration) para más información.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error. Utilice Memcached::getResultCode si es necesario.

## Ejemplos

Ejemplo con `Memcached::set`

```
<?php
$m = new Memcached();
$m->addServer('localhost', 11211);

$m->set('int', 99);
$m->set('string', 'a simple string');
$m->set('array', array(11, 12));
/* El 'object' será destruido en 5 minutos */
$m->set('object', new stdClass, time() + 300);

var_dump($m->get('int'));
var_dump($m->get('string'));
var_dump($m->get('array'));
var_dump($m->get('object'));
?>

    
```php

Resultado del ejemplo anterior es similar a:

    int(99)
    string(15) "a simple string"
    array(2) {
      [0]=>
      int(11)
      [1]=>
      int(12)
    }
    object(stdClass)#1 (0) {
    }

## Véase también

Memcached::setByKey, Memcached::add, Memcached::replace
