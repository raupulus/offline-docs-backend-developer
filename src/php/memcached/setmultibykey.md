---
title: Memcached::setMultiByKey
description: Almacena varios elementos en un servidor
source_url: https://www.php.net/manual/es/memcached.setmultibykey.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/memcached/memcached/setmultibykey.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: memcached
translation_status: ready
translation_reviewed: true
translation_revision: 1d8068ecb
order: 46800
---

Memcached::setMultiByKey

Almacena varios elementos en un servidor

## Descripción

```php
public Memcached::setMultiByKey(string $server_key, array $items, [int $expiration]): bool
```php

`Memcached::setMultiByKey` es el equivalente funcional de Memcached::setMulti, con la excepción de que el argumento libre `server_key` puede ser utilizado para dirigir las claves de `items` hacia un servidor específico. Esto es útil si se desea mantener ciertas claves agrupadas en un solo servidor.

## Parámetros

`server_key`  
La clave que identifica el servidor donde almacenar o recuperar el valor. En lugar de calcular el hash sobre la clave real del elemento, se calcula el hash sobre la clave del servidor al decidir con qué servidor memcached comunicarse. Esto permite agrupar elementos relacionados en un solo servidor para mayor eficiencia con operaciones múltiples.

`items`  
Un array de pares clave/valor para almacenar en el servidor.

`expiration`  
El tiempo de expiración, predeterminado a 0. Véase [Expiration Times](#memcached.expiration) para más información.

## Valores devueltos

Esta función retorna `true` en caso de éxito o `false` si ocurre un error. Utilice Memcached::getResultCode si es necesario.

## Véase también

Memcached::setMulti, Memcached::set
