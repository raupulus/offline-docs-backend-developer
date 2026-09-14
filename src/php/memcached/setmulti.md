---
title: Memcached::setMulti
description: Almacena varios elementos
source_url: https://www.php.net/manual/es/memcached.setmulti.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/memcached/memcached/setmulti.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: memcached
translation_status: ready
translation_reviewed: true
translation_revision: 1d8068ecb
order: 46790
---

Memcached::setMulti

Almacena varios elementos

## Descripción

```php
public Memcached::setMulti(array $items, [int $expiration]): bool
```php

`Memcached::setMulti` es similar a Memcached::set, y en lugar de almacenar un solo par clave / valor, opera sobre varios elementos mediante `items`. El tiempo de expiración `expiration` se aplica a todos los elementos en su conjunto.

## Parámetros

`items`  
Un array de pares clave/valor para almacenar en el servidor.

`expiration`  
El tiempo de expiración, predeterminado a 0. Véase [Expiration Times](#memcached.expiration) para más información.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error. Utilice Memcached::getResultCode si es necesario.

## Ejemplos

Ejemplo con `Memcached::setMulti`

```
<?php
$m = new Memcached();
$m->addServer('localhost', 11211);

$items = array(
    'key1' => 'value1',
    'key2' => 'value2',
    'key3' => 'value3'
);
$m->setMulti($items, time() + 300);
?>

    
```php

## Véase también

Memcached::setMultiByKey, Memcached::set
