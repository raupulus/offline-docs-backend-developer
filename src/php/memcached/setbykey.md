---
title: Memcached::setByKey
description: Almacena un elemento en un servidor específico
source_url: https://www.php.net/manual/es/memcached.setbykey.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/memcached/memcached/setbykey.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: memcached
translation_status: ready
translation_reviewed: true
translation_revision: 1d8068ecb
order: 46770
---

Memcached::setByKey

Almacena un elemento en un servidor específico

## Descripción

```php
public Memcached::setByKey(string $server_key, string $key, mixed $value, [int $expiration]): bool
```php

`Memcached::setByKey` es funcionalmente equivalente a Memcached::set, excepto que la variable libre `server_key` puede ser utilizada para enviar la clave `key` a un servidor específico. Esto es útil si se desea agrupar ciertas claves en un servidor.

## Parámetros

`server_key`  
La clave que identifica el servidor donde almacenar o recuperar el valor. En lugar de calcular el hash sobre la clave real del elemento, se calcula el hash sobre la clave del servidor al decidir con qué servidor memcached comunicarse. Esto permite agrupar elementos relacionados en un solo servidor para mayor eficiencia con operaciones múltiples.

`key`  
La clave bajo la cual almacenar el valor.

`value`  
El valor a almacenar.

`expiration`  
El tiempo de expiración, predeterminado a 0. Véase [Expiration Times](#memcached.expiration) para más información.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error. Utilice Memcached::getResultCode si es necesario.

## Ejemplos

Ejemplo con `Memcached::setByKey`

```
<?php
$m = new Memcached();
$m->addServer('localhost', 11211);

/* Conserva los bloques de IP en un servidor */
$m->setByKey('api-cache', 'block-ip:169.254.253.252', 1);
$m->setByKey('api-cache', 'block-ip:169.127.127.202', 1);
?>

    
```php

## Véase también

Memcached::set
