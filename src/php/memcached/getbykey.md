---
title: Memcached::getByKey
description: Lee un elemento en un servidor específico
source_url: https://www.php.net/manual/es/memcached.getbykey.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/memcached/memcached/getbykey.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: memcached
translation_status: ready
translation_reviewed: true
translation_revision: 1d8068ecb
order: 46540
---

Memcached::getByKey

Lee un elemento en un servidor específico

## Descripción

```php
public Memcached::getByKey(string $server_key, string $key, [callable $cache_cb], [int $get_flags]): mixed
```php

`Memcached::getByKey` es funcionalmente equivalente a Memcached::get, excepto que la variable libre `server_key` puede ser utilizada para dirigir la clave `key` a un servidor específico.

## Parámetros

`server_key`  
La clave que identifica el servidor donde almacenar o recuperar el valor. En lugar de calcular el hash sobre la clave real del elemento, se calcula el hash sobre la clave del servidor al decidir con qué servidor memcached comunicarse. Esto permite agrupar elementos relacionados en un solo servidor para mayor eficiencia con operaciones múltiples.

`key`  
La clave del elemento a leer.

`cache_cb`  
Función de retrollamada en caso de ausencia, o `null`

`get_flags`  
Bandera para controlar el resultado devuelto. Cuando `Memcached::GET_EXTENDED` es proporcionada, la función devolverá también el token CAS.

## Valores devueltos

Devuelve el valor almacenado en la caché, o `false` en caso contrario. El método Memcached::getResultCode devuelve `Memcached::RES_NOTFOUND` si la clave no existe.

## Historial de cambios

| Versión | Descripción |
|----|----|
| PECL memcached 3.0.0 | El parámetro `cas_tokens` ha sido eliminado. `Memcached::GET_EXTENDED` ha sido añadida y cuando se pasa como bandera asegura que los tokens CAS sean recuperados. |

## Véase también

Memcached::get, Memcached::getMulti, Memcached::getDelayed
