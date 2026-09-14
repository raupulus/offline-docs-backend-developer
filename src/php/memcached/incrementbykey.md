---
title: Memcached::incrementByKey
description: Incrementa un valor numérico de un elemento almacenado en un servidor
  específico
source_url: https://www.php.net/manual/es/memcached.incrementbykey.php
source_repo: https://github.com/php/doc-es.git
source_ref: master
source_commit: 954a0d911
source_path: reference/memcached/memcached/incrementbykey.xml
technology: php
version: master
license: CC-BY-3.0
retrieved_at: '2026-08-02'
section: memcached
translation_status: ready
translation_reviewed: false
translation_revision: 1d8068ecb
order: 46670
---

Memcached::incrementByKey

Incrementa un valor numérico de un elemento almacenado en un servidor específico

## Descripción

```php
public Memcached::incrementByKey(string $server_key, string $key, [int $offset], [int $initial_value], [int $expiry]): int
```php

`Memcached::incrementByKey` incrementa un valor numérico de un elemento especificando el incremento mediante el argumento `offset`. Si el valor del elemento no es numérico, se emitirá un error. `Memcached::incrementByKey` establecerá el elemento al valor del argumento `initial_value` si la clave no existe.

## Parámetros

`server_key`  
La clave que identifica el servidor donde almacenar o recuperar el valor. En lugar de calcular el hash sobre la clave real del elemento, se calcula el hash sobre la clave del servidor al decidir con qué servidor memcached comunicarse. Esto permite agrupar elementos relacionados en un solo servidor para mayor eficiencia con operaciones múltiples.

`key`  
La clave del elemento a incrementar.

`offset`  
El incremento a utilizar sobre el valor del elemento.

`initial_value`  
El valor a establecer si el elemento no existe.

`expiry`  
El tiempo de expiración para la definición del elemento.

## Valores devueltos

Devuelve el nuevo valor del elemento en caso de éxito o `false` si ocurre un error.

## Véase también

Memcached::decrement, Memcached::decrementByKey, Memcached::increment
